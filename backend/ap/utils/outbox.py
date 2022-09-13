from api.models import User

from ..models import Activity
from ..utils.federation import Federation

from django.conf import settings

class Outbox ():
    actor = None
    data = {}
    message = {
        "@context": "https://www.w3.org/ns/activitystreams"
    }
    activities = len (Activity.objects.all ())
    activity = None
    object = ""
    
    def __init__ (self, actor, data, object):
        self.actor = actor
        self.data = data
        self.object = object

        if self.data ['type'] == "Follow":
            self.process_follow ()
        elif self.data ['type'] == "Unfollow":
            self.process_unfollow ()
        elif self.data ['type'] == "Accept":
            self.process_accept ()
        else:
            return # No hacer nada?

        self.fedi = Federation (self.actor)
        response = self.fedi.send_one (self.object, self.message)

        if self.activity != None:
            self.activity.save ()

    def process_follow (self):
        self.message ["id"] = f"{self.data ['actor']}/follows/{self.activities}"
        self.message ["type"] = "Follow"
        self.message ["actor"] = self.data ["actor"]
        self.message ["object"] = self.data ['object']

        self.activity = Activity (
            activity_id = self.message["id"],
            type = "Follow",
            actor = self.message ["actor"],
            object = self.message ["object"]
        )

    def process_unfollow (self):
        follow_activity = Activity.objects.filter (actor=self.data ["actor"], object=self.object)
        if len (follow_activity) < 1:
            return
        follow_activity = follow_activity.get ()

        self.message ["id"] = f"{self.data ['actor']}/follows/{self.activities}/undo"
        self.message ["type"] = "Undo"
        self.message ["actor"] = self.data ["actor"]
        self.message ["object"] = {
            "id": follow_activity.activity_id,
            "type": "Follow",
            "actor": follow_activity.actor,
            "object": follow_activity.object
        }

        follow_activity.delete ()

    def process_accept (self):
        pass
