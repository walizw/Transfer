from .object import Object

class Collection (Object):
    type = "Collection"
    totalItems = 0
    current = None
    first = None
    last = None
    items = []
    items_to_dict = True # If true, "items" will be added to the dictionary

    def __init__ (self):
        super ().__init__ ()
        self.items.clear ()

    def add_item (self, item):
        self.items.append (item)

    def to_dict (self):
        dict = super ().to_dict ()

        dict ["totalItems"] = int (self.totalItems)

        if self.items != None and self.items_to_dict:
            dict ["items"] = self.items

        if self.current != None:
            dict ["current"] = self.current

        if self.first != None:
            dict ["first"] = self.first

        if self.last != None:
            dict ["last"] = self.last

        return dict

class OrderedCollection (Collection):
    type = "OrderedCollection"
    items_to_dict = False

    def to_dict (self):
        dict = super ().to_dict ()
        dict ["orderedItems"] = self.items

        return dict

class CollectionPage (Collection):
    type = "CollectionPage"
    partOf = ""
    next = None
    prev = None

    def to_dict (self):
        dict = super ().to_dict ()
        dict ["partOf"] = self.partOf

        if self.next != None:
            dict ["next"] = self.next

        if self.prev != None:
            dict ["prev"] = self.prev

        return dict

class OrderedCollectionPage (CollectionPage):
    type = "OrderedCollectionPage"
    startIndex = None

    def to_dict (self):
        dict = super ().to_dict ()

        if self.startIndex != None:
            dict ["startIndex"] = self.startIndex

        return dict
