import os

import falcon

# import images
from sample.resources.hello import Hello

def create_app():
    api = falcon.API()
    api.add_route('/hello', Hello())
    return api

def get_app():
    return create_app()