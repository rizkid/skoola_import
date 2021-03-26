import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../../src/service"))

from string_transfomer import StringTransformer

class StringTransformerTest(unittest.TestCase):
    def setUp(self):
        self.transformer = StringTransformer()

    def test_default_transformer(self):
        actual_output = self.transformer.transform("datatest")
        print(actual_output)
        expected_output = "default_prefix_datatest_default_suffix"

        self.assertEqual(actual_output, expected_output)
