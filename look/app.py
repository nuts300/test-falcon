import falcon

from .images import Resource, ImageStore


def create_app(image_store):
    image_resource = Resource(image_store)
    api = falcon.API()
    api.add_route('/images', image_resource)
    return api


def get_app():
    storage_path = os.environ.get('LOOK_STORAGE_PATH', './images/')
    image_store = ImageStore(storage_path)
    return create_app(image_store)

# api = application = falcon.API()

# image_store = ImageStore('./images/')
# images = Resource(image_store)
# api.add_route('/images', images)