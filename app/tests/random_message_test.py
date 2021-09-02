"""
Random Message endpoint test
"""

import unittest
from api import app, prefix
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

class RandomMessageTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_response(self):
        response = self.client.get(prefix + '/message')
        logger.info(f'Response: {response.get_json()}')
        self.assertEqual(response.status_code, 200)

        #validate json attributes
        self.assertTrue(response.get_json()['id'])
        self.assertTrue(response.get_json()['punchline'])
        self.assertTrue(response.get_json()['setup'])
        self.assertTrue(response.get_json()['type'])

if __name__ == '__main__':
    unittest.main()