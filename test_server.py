import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_root_status_code(self):
        r =requests.get("http://localhost:8000")
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()