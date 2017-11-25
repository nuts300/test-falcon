import falcon

class Hello(object):

    def on_get(self, req, resp) -> None:
        resp.content_type = "text/html"
        resp.body = "hello sample service"
        resp.status = falcon.HTTP_200
