"""
Hello Word endpoint test
"""

import unittest
from api import app, prefix
 
class HelloWorldTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_response(self):
        response = self.client.get(prefix + '/hello-world')
        expected_resp = {'message': 'Hello World!'}
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_resp)

if __name__ == '__main__':
    unittest.main()