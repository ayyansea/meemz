import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from config import Component

class TestParse(unittest.TestCase):
    """
    Tests:
    * check return type of get_config()
    * check if returned dict's length is non-zero
    """

    def setUp(self):
        self.name = "name"
        self.data = {
            "width": 100,
            "height": 100,
            "font": "Iosevka",
            "align": "right"
        }
        self.component = Component(self.name, self.data)


    def test_name(self):
        name = self.component.get_name()
        print(name)
        self.assertIsInstance(name, str)
        self.assertGreater(len(name), 0)


    def test_width(self):
        width = self.component.get_width()
        print(width)
        self.assertIsInstance(width, int)
        self.assertGreater(len(name), 0)


if __name__ == "__main__":
    unittest.main()