import os

import falcon
from mongoengine import connect
from sample.resources.hello import Hello
from sample.resources.users import User, UserList

# connect db
connect('mongotest', host='127.0.0.1', port=3001)

# import images
from sample.resources.hello import Hello

def create_app():
    api = falcon.API()
    api.add_route('/hello', Hello())
    api.add_route('/users/{id}', User())
    api.add_route('/users', UserList())
    return api

def get_app():
    return create_app()