import requests
import unittest

class TestAGTWorld(unittest.TestCase):
    def test_website_status_code(self):
        url = 'https://agt.world'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
