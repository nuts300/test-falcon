from mongoengine.document import Document
from mongoengine import fields

class User(Document):
    name = fields.StringField()
    age = fields.IntField()

    def __unicode__(self):
        return self.name
