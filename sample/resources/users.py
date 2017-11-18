import json
from bson.objectid import ObjectId
from bson import json_util
from sample.models.user import User

class Users(object):

    def on_get(self, req, resp):
        users = User.objects.all()
        resp.body = json_util.dumps(users)

    # def on_get(self, req, resp, id):
    #     user = json.find({"_id": ObjectId(id)})
    #     resp.body = json_util(user)
    
    def on_post(self, req, resp):
        data = req.body 
        user = User(data)
        user.save()