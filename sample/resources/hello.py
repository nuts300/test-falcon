
class Hello(object):

    def on_get(self, req, resp):
        resp.body = "hello sample service"
