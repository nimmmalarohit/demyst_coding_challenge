import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import data_processing


class TestDataParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d_processing = data_processing.DataProcessing()

    def test_generate_random_data(self):
        actual_output = self.d_processing.generate_random_data()
        self.assertIsInstance(actual_output, dict)
        self.assertListEqual(['first_name', 'last_name', 'address', 'date_of_birth'], list(actual_output.keys()))

    if __name__ == '__main__':
        unittest.main()
