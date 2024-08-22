import unittest
import os
import sys
import json
from io import StringIO
import csv


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import data_parser


class TestDataParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        specs_json = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'spec.json')
        with open(specs_json, 'r') as specs:
            specs_data = json.loads(specs.read())
        cls.column_names = specs_data.get('ColumnNames')
        cls.offsets = [int(offset) for offset in specs_data.get('Offsets')]

    def test_get_field_positions(self):
        sample_offsets = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
        expected_field_positions = [(0, 5), (5, 17), (17, 20), (20, 22), (22, 35), (35, 42), (42, 52), (52, 65), (65, 85), (85, 98)]
        actual_field_positions = data_parser.get_field_positions(sample_offsets)
        self.assertEqual(actual_field_positions, expected_field_positions)

    def test_parse_data(self):
        self.sample_data1 = "67890test string2456CDanother test2value22data part2longer data 2more data  see here1final text223"
        self.expected_csv_data1 = ['67890','test string2','456','CD','another test2','value22','data part2','longer data 2','more data  see here1','final text223']
        self.field_positions = data_parser.get_field_positions(self.offsets)

        actual_data1 = data_parser.parse_data(self.sample_data1, self.field_positions)
        self.assertEqual(actual_data1, self.expected_csv_data1)

    if __name__ == '__main__':
        unittest.main()