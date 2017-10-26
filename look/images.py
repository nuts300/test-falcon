# import json

import falcon

import msgpack


class Resource(object):

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