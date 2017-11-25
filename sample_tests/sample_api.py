import json
from falcon import testing
from sample.app import get_app

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        # Assume the hypothetical `myapp` package has a
        # function called `create()` to initialize and
        # return a `falcon.API` instance.

        self.app = get_app()


# pylint: disable=W0212,W0201
class TestMyApp(MyTestCase):

    def test_hello(self):
        response = self.simulate_get('/hello')
        self.assertEqual(response._content, b"hello sample service")

    def test_create_user(self):
        body = json.dumps({"name": "aaaaaa", "age":20})
        response = self.simulate_post(
            '/users',
            body=body,
            headers={'content-type': 'application/json'}
        )
        content = json.loads(response._content)
        created_user_id = content.get("_id").get("$oid")
        self.assertEqual(response._status_code, 200)

        print('/users/' + created_user_id)
        get_resp = self.simulate_get('/users/' + created_user_id)
        self.assertEqual(get_resp._status_code, 200)
        print(get_resp.json)
        self.assertEqual(get_resp.json.get("_id").get("$oid"), created_user_id)

    # def test_get_user(self):
    #     response = self.simulate_get('/users/' + self._created_user_id)
    #     print(response._content)

    # def test_get_users(self):
    #     result = self.simulate_get('/users')
    #     print(vars(result))
