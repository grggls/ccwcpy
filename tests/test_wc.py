# ./tests/test_wc.py
from ccwc import ccwc_library as ccwc
import sys
import unittest

sys.path.append("../")


class TestWC(unittest.TestCase):
    def setUp(self):
        with open("./tests/lorem.txt", "r") as file:
            self.lorem = file.read()

    def test_count_bytes(self):
        self.assertEqual(ccwc.count_bytes(self.lorem), "446")

    def test_count_characters(self):
        self.assertEqual(ccwc.count_characters(self.lorem), "446")

    def test_count_lines(self):
        self.assertEqual(ccwc.count_lines(self.lorem), "1")

    def test_count_words(self):
        self.assertEqual(ccwc.count_words(self.lorem), "69")
