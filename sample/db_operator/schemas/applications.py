from mongoengine.document import Document
from mongoengine import fields

class Applications(Document):
    application_id = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)
    admin = fields.BooleanField(required=True)
    meta = {'collection': 'applications'}
