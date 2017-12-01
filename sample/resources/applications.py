import sys
from bson.json_util import dumps
import falcon
from mongoengine.errors import ValidationError, OperationError

from sample.extentions.parse_json import parse_json
from sample.db_operator.main import DbOperator
from sample.error.sample_error import SampleError
from sample.error.code import ErrorCode

class Applications(object):

    @falcon.before(parse_json)
    def on_post(self, req, resp) -> None:
        application = req.context.get('body')
        application_id = application.get('application_id')
        password = application.get('password')
        admin = application.get('admin')
        created = DbOperator.register_application(application_id=application_id, password=password, admin=admin)
        resp.body = dumps(created)
