# ./tests/test_wc.py
from ccwc import ccwc_library as ccwc
import sys
import subprocess
import unittest

sys.path.append("../")


class TestWC(unittest.TestCase):
    def setUp(self):
        with open("./tests/lorem.txt", "r") as file:
            self.lorem = file.read()

    def test_lorem_count_bytes(self):
        self.assertEqual(ccwc.count_bytes(self.lorem), "446")

    def test_lorem_count_characters(self):
        self.assertEqual(ccwc.count_characters(self.lorem), "446")

    def test_lorem_count_lines(self):
        self.assertEqual(ccwc.count_lines(self.lorem), "1")

    def test_lorem_count_words(self):
        self.assertEqual(ccwc.count_words(self.lorem), "69")

    def test_wc_counts(self):
        # Read the contents of the test file (To Be Alive by Gregory Orr)
        file = "./tests/alive.txt"
        with open(file, "r") as f:
            input_string = f.read()

        # Get the expected counts using the wc command
        wc_output = subprocess.check_output(["wc", "-c", "-l", "-w", file])
        wc_counts = wc_output.decode("utf-8").split()

        # Get the computed counts using the ccwc library
        computed_counts = [
            ccwc.count_lines(input_string),
            ccwc.count_words(input_string),
            ccwc.count_bytes(input_string),
            file,
        ]

        # Compare the expected and actual counts
        assert computed_counts == wc_counts

    def test_wc_long(self):
        # Read the test file (Metamorphosis by Franz Kafka via Gutenberg)
        file = "./tests/metamorphosis.txt"
        with open(file, "r") as f:
            input_string = f.read()

        # Get the expected counts using the wc command
        wc_output = subprocess.check_output(["wc", "-c", "-l", "-w", file])
        wc_counts = wc_output.decode("utf-8").split()

        # Get the computed counts using the ccwc library
        computed_counts = [
            ccwc.count_lines(input_string),
            ccwc.count_words(input_string),
            ccwc.count_bytes(input_string),
            file,
        ]

        # Compare the expected and actual counts
        assert computed_counts == wc_counts
