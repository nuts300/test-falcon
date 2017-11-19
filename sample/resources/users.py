import falcon
import json
from bson.objectid import ObjectId
from sample.db_operators.users import UsersOperator

class User(object):
    def on_get(self, req, resp, id):
        result = UsersOperator.getUser(id)
        resp.body = result

class Users(object):
    def on_get(self, req, resp):
        result = UsersOperator.getUsers()
        resp.body = result

    def on_post(self, req, resp):
        user = json.loads(req.stream.read().decode('utf-8'))
        result = UsersOperator.createUser(user)
        resp.body = result
