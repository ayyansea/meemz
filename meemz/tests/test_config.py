import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from config import Config

class TestParse(unittest.TestCase):
    """
    Tests:
    * check return type of get_config()
    * check if returned dict's length is non-zero
    """

    def test_type(self):
        conf = Config("twitter").get_config()
        print(conf)
        self.assertIsInstance(conf, dict)


    def test_length(self):
        conf = Config("twitter").get_config()
        print(conf)
        self.assertGreater(len(conf), 0)


    def test_colors(self):
        color = Config("twitter").get_colors()
        print(color)
        self.assertGreater(len(color), 0)


    def test_global_font(self):
        font = Config("twitter").get_global_font()
        print(font)
        self.assertGreater(len(font), 0)


    def test_components(self):
        components = Config("twitter").get_components()
        print(components)
        self.assertGreater(len(components), 0)

if __name__ == "__main__":
    unittest.main()