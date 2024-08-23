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

    def test_anonymize_data(self):
        actual_output = data_processing.anonymize_data("Rohit Nimmala")
        expected_output = "78ae5dcbbc1c656ffda05fa688f0245f9776231cede8c5930c20dfd43638927c"
        self.assertEqual(actual_output, expected_output)

    def test_anonymize_rows(self):
        row = {
            'first_name': 'John',
            'last_name': 'Doe',
            'address': '19908 Tony View Suite 051 Romeroland, SC 81958',
            'date_of_birth': '1996-07-09'}
        actual_output = data_processing.anonymize_rows(row)
        expected_output = {'first_name': 'a8cfcd74832004951b4408cdb0a5dbcd8c7e52d43f7fe244bf720582e05241da',
                           'last_name': 'fd53ef835b15485572a6e82cf470dcb41fd218ae5751ab7531c956a2a6bcd3c7',
                           'address': '19866a72e28e72a57724b833674f133093e75640548ed4b53c55def5158fe874',
                           'date_of_birth': '1996-07-09'}
        self.assertDictEqual(actual_output, expected_output)

    if __name__ == '__main__':
        unittest.main()
