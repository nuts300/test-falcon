import json
from bson.objectid import ObjectId
from sample.models.user import User

class Users(object):

    def on_get(self, req, resp):
        users = User.objects.all()
        resp.body = json.dumps(users.tojson())

    def on_get(self, req, resp, id):
        user = json.find({"_id": ObjectId(obj_id_to_find)})
        resp.body = json.dumps(user.tojson())
        