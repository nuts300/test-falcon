import os

import falcon
from mongoengine import connect
from sample.resources.hello import Hello
from sample.resources.users import User, Users
from sample.extentions.print_log_middleware import PrintLogMiddleware
from sample.error.sample_error import SampleError
from sample.error.final_error_handler import FinalErrorHandler

# connect db
connect('mongotest', host='127.0.0.1', port=3001)

def create_app():
    api = falcon.API(middleware=[PrintLogMiddleware()])
    api.add_error_handler(Exception, FinalErrorHandler.handle)
    api.add_error_handler(SampleError, SampleError.handle)
    api.add_route('/hello', Hello())
    api.add_route('/users/{id}', User())
    api.add_route('/users', Users())
    return api

def get_app():
    return create_app()