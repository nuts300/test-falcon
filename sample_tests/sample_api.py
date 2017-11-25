from falcon import testing
from sample.app import get_app

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        # Assume the hypothetical `myapp` package has a
        # function called `create()` to initialize and
        # return a `falcon.API` instance.

        self.app = get_app()


class TestMyApp(MyTestCase):
    def test_hello(self):
        result = self.simulate_get('/hello')
        self.assertEqual(result._content, b"hello sample service")
