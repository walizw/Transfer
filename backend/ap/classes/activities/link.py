from .object import Object

class Link (Object):
    href = ""
    rel = None
    hreflang = None
    height = None
    width = None

    def to_dict (self):
        dict = super ().to_dict ()
        dict ["href"] = self.href

        if self.rel != None:
            dict ["rel"]= self.rel

        if self.hreflang != None:
            dict ["hreflang"] = self.hreflang

        if self.width != None:
            dict ["width"] = self.width

        if self.height != None:
            dict ["height"] = self.height

        return dict
