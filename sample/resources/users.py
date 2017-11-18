import falcon
import json
from bson.objectid import ObjectId
from bson import json_util
from sample.documents.user import UserDocument

class User(object):
    def on_get(self, req, resp, id):
        user = UserDocument.objects(id=ObjectId(id))
        resp.body = user.to_json()

class UserList(object):
    def on_get(self, req, resp):
        users = UserDocument.objects.all()
        resp.body = users.to_json()
    def on_post(self, req, resp):
        data = json.loads(req.stream.read().decode('utf-8'))
        user = UserDocument(**data)
        user.save()
        resp.body = user.to_json()