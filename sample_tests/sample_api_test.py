import json
import unittest
from falcon import testing
from sample.app import get_app

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        # Assume the hypothetical `myapp` package has a
        # function called `create()` to initialize and
        # return a `falcon.API` instance.

        self.app = get_app()


# pylint: disable=W0212,W0201,C0301,W0703
class TestMyApp(MyTestCase):

    def test_01_hello(self):
        response = self.simulate_get('/hello')
        self.assertEqual(response._content, b"hello sample service")

    def test_02_create_user(self):
        body = json.dumps({"name": "aaaaaa", "age":20})
        response = self.simulate_post(
            '/users',
            body=body,
            headers={'content-type': 'application/json'}
        )
        TestMyApp._created_user_id = response.json.get("_id").get("$oid")
        self.assertEqual(response._status_code, 200)

    def test_03_get_user(self):
        response = self.simulate_get('/users/' + TestMyApp._created_user_id)
        self.assertEqual(response._status_code, 200)
        self.assertEqual(response.json.get("_id").get("$oid"), TestMyApp._created_user_id)

    def test_04_get_users(self):
        response = self.simulate_get('/users')
        self.assertTrue(len(response.json) > 0)
        finded = [user for user in response.json if user.get("_id").get("$oid") == TestMyApp._created_user_id]
        self.assertTrue(len(finded) == 1)

    def test_05_update_user(self):
        response = self.simulate_put(
            '/users/' + TestMyApp._created_user_id,
            body=json.dumps({"name": "changed"}),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response._status_code, 204)

        get_res = self.simulate_get('/users/' + TestMyApp._created_user_id)
        self.assertEqual(get_res.json.get("name"), "changed")

    def test_06_delete_user(self):
        response = self.simulate_delete('/users/' + TestMyApp._created_user_id)
        self.assertEqual(response._status_code, 204)

        get_res = self.simulate_get('/users/' + TestMyApp._created_user_id)
        self.assertEqual(get_res._status_code, 404)

    if __name__ == '__main__':
        unittest.main(failfast=True, exit=False)
