import falcon

from .images import Resource, ImageStore


def create_app(image_store):
    image_resource = Resource(image_store)
    api = falcon.API()
    api.add_route('/images', image_resource)
    return api


def get_app():
    image_store = ImageStore('./images/')
    return create_app(image_store)

# api = application = falcon.API()

# image_store = ImageStore('./images/')
# images = Resource(image_store)
# api.add_route('/images', images)