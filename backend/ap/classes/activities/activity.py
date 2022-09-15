from .object import Object

class Activity (Object):
    type = "Activity"
    actor = ""
    object = ""
    target = None
    result = None
    origin = None
    instrument = None

    def to_dict (self):
        dict = super ().to_dict ()
        dict ["actor"] = self.actor
        dict ["object"] = self.object

        if self.target != None:
            dict ["target"] = self.target

        if self.result != None:
            dict ["result"] = self.result

        if self.origin != None:
            dict ["origin"] = self.origin

        if self.instrument != None:
            dict ["instrument"] = self.instrument
            
        return dict
