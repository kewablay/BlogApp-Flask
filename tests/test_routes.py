from flask import Flask
import unittest

from app import app


class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_index_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertFalse(b'Blog post Loaded' in response.data)


if __name__ == '__main__':
    unittest.main()