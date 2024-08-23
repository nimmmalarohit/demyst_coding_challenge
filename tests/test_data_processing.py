import unittest
import os
import sys
import faker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import data_processing


class TestDataParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fake = faker.Faker()

    def test_generate_random_data(self):
        actual_output = data_processing.generate_random_data(self.fake)
        self.assertIsInstance(actual_output, dict)
        self.assertListEqual(['first_name', 'last_name', 'address', 'date_of_birth'], list(actual_output.keys()))

    if __name__ == '__main__':
        unittest.main()
