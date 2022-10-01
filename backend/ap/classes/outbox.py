from api.models import User

from ..models import Activity as ActivityModel
from ..classes import Federation
from ..classes.activities import Activity

from django.conf import settings

class Outbox ():
    actor = None
    data = {}
    activity = Activity ()
    activities = len (ActivityModel.objects.all ())
    activity_model = None
    object = ""

    def __init__ (self, data):
        self.activities = len (ActivityModel.objects.all ())
        self.data = data

        if self.data ['type'] == "Follow":
            self.actor = User.objects.filter (name=self.data ["actor"].split ("/")[-1]).get ()
            self.process_follow ()
        elif self.data ['type'] == "Unfollow":
            self.actor = User.objects.filter (name=self.data ["actor"].split ("/")[-1]).get ()
            self.process_unfollow ()
        elif self.data ['type'] == "Accept":
            self.actor = User.objects.filter (name=self.data ["actor"].split ("/")[-1]).get ()
            self.process_accept ()
        else:
            return # No hacer nada?

        self.fedi = Federation (self.actor)
        response = self.fedi.send_one (self.object, self.activity.to_dict ())

        if self.activity_model != None:
            self.activity_model.save ()

    def process_follow (self):
        self.object = self.data ["object"]

        self.activity.id = f"{self.data ['actor']}/follows/{self.activities}"
        self.activity.type = "Follow"
        self.activity.actor = self.data ["actor"]
        self.activity.object = self.data ['object']

        self.activity_model = ActivityModel (
            activity_id = self.activity.id,
            type = "Follow",
            actor = self.activity.actor,
            object = self.activity.object
        )

    def process_unfollow (self):
        self.object = self.data ["object"]

        follow_activity = ActivityModel.objects.filter (actor=self.data ["actor"], object=self.object)
        if len (follow_activity) < 1:
            return
        follow_activity = follow_activity.get ()

        self.activity.id = f"{self.data ['actor']}/follows/{self.activities}/undo"
        self.activity.type = "Undo"
        self.activity.actor = self.data ["actor"]
        self.activity.object = {
            "id": follow_activity.activity_id,
            "type": "Follow",
            "actor": follow_activity.actor,
            "object": follow_activity.object
        }

        follow_activity.delete ()

    def process_accept (self):
        # TODO: Hasta ahora solo se aceptan peticiones de Follow
        activity = ActivityModel.objects.filter (activity_id=self.data ["act_id"])
        if len (activity) < 1:
            return
        activity = activity.get ()

        self.activity.id = f"{self.data ['actor']}#accepts/follows/{self.activities}"
        self.activity.type = "Accept"
        self.activity.actor = self.data ["actor"]
        self.activity.object = {
            "id": activity.activity_id,
            "type": activity.type,
            "actor": activity.actor,
            "object": activity.object
        }

        self.object = activity.actor
