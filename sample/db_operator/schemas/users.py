from mongoengine.document import Document
from mongoengine import fields

class Users(Document):
    name = fields.StringField()
    age = fields.IntField()
    meta = {'collection': 'users'}
