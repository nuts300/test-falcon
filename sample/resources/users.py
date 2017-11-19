import falcon
from bson.objectid import ObjectId
from sample.db_operator.main import DbOperator
from sample.extentions.parse_json import parseJson

class User(object):
    def on_get(self, req, resp, id):
        result = DbOperator.getUser(id)
        resp.body = result

class Users(object):
    def on_get(self, req, resp):
        result = DbOperator.getUsers()
        resp.body = result

    @falcon.before(parseJson)
    def on_post(self, req, resp):
        user = req.body
        result = DbOperator.createUser(user)
        resp.body = result
