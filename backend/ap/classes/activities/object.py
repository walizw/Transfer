class Object ():
    context = "https://www.w3.org/ns/activitystreams"
    type = "Object"
    id = None
    name = None
    attachment = None
    attributedTo = None
    audience = None
    content = None
    endTime = None
    generator = None
    icon = None
    image = None
    inReplyTo = None
    location = None
    preview = None
    published = None
    replies = None
    startTime = None
    summary = None
    tag = None
    updated = None
    url = None
    to = None
    bto = None
    cc = None
    bcc = None
    mediaType = None
    duration = None

    def to_dict (self):
        dict = {}
        dict ["context"] = self.context
        dict ["type"] = self.type

        if self.id != None:
            dict ["id"] = self.id

        if self.name != None:
            dict ["name"] = self.name

        if self.attachment != None:
            dict ["attachment"] = self.attachment

        if self.attributedTo != None:
            dict ["attributedTo"] = self.attributedTo

        if self.audience != None:
            dict ["audience"] = self.audience

        if self.content != None:
            dict ["content"] = self.content

        if self.endTime != None:
            dict ["endTime"] = self.endTime

        if self.generator != None:
            dict ["generator"] = self.generator

        if self.icon != None:
            dict ["icon"] = self.icon

        if self.image != None:
            dict ["image"] = self.image

        if self.inReplyTo != None:
            dict ["inReplyTo"] = self.inReplyTo

        if self.location != None:
            dict ["location"] = self.location

        if self.preview != None:
            dict ["preview"] = self.preview

        if self.published != None:
            dict ["published"] = self.published

        if self.replies != None:
            dict ["replies"] = self.replies

        if self.startTime != None:
            dict ["startTime"] = self.startTime

        if self.summary != None:
            dict ["summary"] = self.summary

        if self.tag != None:
            dict ["tag"] = self.tag

        if self.updated != None:
            dict ["updated"] = self.tag

        if self.url != None:
            dict ["url"] = self.url

        if self.to != None:
            dict ["to"] = self.to

        if self.bto != None:
            dict ["bto"] = self.bto

        if self.cc != None:
            dict ["cc"] = self.cc

        if self.bcc != None:
            dict ["bcc"] = self.bcc

        if self.mediaType != None:
            dict ["mediaType"] = self.mediaType

        if self.duration != None:
            dict ["duration"] = self.duration

        return dict
