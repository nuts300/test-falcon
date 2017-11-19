import falcon
from bson.objectid import ObjectId
from sample.db_operators.users import UsersOperator
from sample.extentions.parse_json import parseJson

class User(object):
    def on_get(self, req, resp, id):
        result = UsersOperator.getUser(id)
        resp.body = result

class Users(object):
    def on_get(self, req, resp):
        result = UsersOperator.getUsers()
        resp.body = result

    @falcon.before(parseJson)
    def on_post(self, req, resp):
        user = req.body
        result = UsersOperator.createUser(user)
        resp.body = result
