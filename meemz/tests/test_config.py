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


if __name__ == "__main__":
    unittest.main()