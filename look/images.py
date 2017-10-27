# import json

import io
import os
import uuid
import mimetypes

import falcon
import msgpack


class Resource(object):
    _CHUNK_SIZE_BYTES = 4096

    def __init__(self, storage_path):
        self._storage_path = storage_path

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/kuma.png'
                }
            ]
        }

        # Create a JSON representation of the resource
        # resp.body = json.dumps(doc, ensure_ascii=False)
        resp.data = msgpack.packb(doc, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK


        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        ext = mimetypes.guess_extension(req.content_type)
        name = '{uuid}{ext}'.format(uuid=uuid.uuid4(), ext=ext)
        image_path = os.path.join(self._storage_path, name)

        with io.open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break

                image_file.write(chunk)

        resp.status = falcon.HTTP_201
        resp.location = '/images/' + name
