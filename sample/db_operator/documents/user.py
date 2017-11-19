from mongoengine.document import Document
from mongoengine import fields

class UserDocument(Document):
    name = fields.StringField()
    age = fields.IntField()

