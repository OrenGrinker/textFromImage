# tests/test_core.py

import unittest
from textfromimage import get_description

class TestTextFromImage(unittest.TestCase):

    def test_get_description_invalid_url(self):
        with self.assertRaises(ValueError):
            get_description('invalid_url')

    def test_get_description_no_api_key(self):
        # Temporarily unset the API key
        import os
        original_api_key = os.environ.get('OPENAI_API_KEY')
        os.environ['OPENAI_API_KEY'] = ''

        with self.assertRaises(ValueError):
            get_description('https://example.com/image.jpg')

        # Reset the API key
        if original_api_key is not None:
            os.environ['OPENAI_API_KEY'] = original_api_key

if __name__ == '__main__':
    unittest.main()
