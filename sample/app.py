import os

import falcon
from mongoengine import connect
from sample.resources.hello import Hello
from sample.resources.users import User, Users
from sample.extentions.print_log_middleware import PrintLogMiddleware
from sample.error.sample_error import SampleError
from sample.error.final_error_handler import final_error_handler
from sample.env import get_db_host, get_db_port

# connect db
DB_HOST = get_db_host()
DB_PORT = get_db_port()
connect('mongotest', host=DB_HOST, port=DB_PORT)

def get_app():
    api = falcon.API(middleware=[PrintLogMiddleware()])
    api.add_error_handler(Exception, final_error_handler)
    api.add_route('/hello', Hello())
    api.add_route('/users/{user_id}', User())
    api.add_route('/users', Users())
    return api
