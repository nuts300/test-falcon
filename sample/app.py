import os

import falcon
from mongoengine import connect
from sample.resources.hello import Hello
from sample.resources.users import User, Users

# connect db
connect('mongotest', host='127.0.0.1', port=3001)

def create_app():
    api = falcon.API()
    api.add_route('/hello', Hello())
    api.add_route('/users/{id}', User())
    api.add_route('/users', Users())
    return api

def get_app():
    return create_app()