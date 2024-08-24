"""
Problem 1: Parse fixed width file
 - Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
 - Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
 - DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
 - Language choices (Python or Scala)
 - Deliver source via github or bitbucket
  -Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
 - Pay attention to encoding
"""

import csv
import os
import json


class DataParser:
    def __init__(self):
        self.specs_json = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'spec.json')
        # Read and load the spec.json parameters
        with open(self.specs_json, 'r') as specs:
            self.specs_data = json.loads(specs.read())

        # Get the column names and offsets from spec
        self.column_names = self.specs_data.get('ColumnNames')
        self.offsets = [int(offset) for offset in self.specs_data.get('Offsets')]

    @staticmethod
    def parse_data(line, field_positions):
        """
        Extract fields based on start and end positions
        """
        return [line[start:end].strip() for start, end in field_positions]

    @staticmethod
    def get_field_positions(offsets):
        """
        create a list of tuple consisting position and offset of column
        """
        field_positions = []
        start_pos = 0
        for offset in offsets:
            field_positions.append((start_pos, start_pos + offset))
            start_pos += offset
        return field_positions

    def write_parsed_data_to_csv(self, input_file, output_file):
        """
        This method is used to read the input file, create a list of tuple consisting position and offset,
        then offset position list use string slicing function to parse the input file as row, and write each row into output file
        """
        field_positions = self.get_field_positions(self.offsets)

        # Open the fixed-width file and CSV file
        with open(input_file, 'r', encoding='windows-1252') as fixed_file, \
                open(output_file, 'w', newline='', encoding='utf-8') as csv_file:

            writer = csv.writer(csv_file)

            # Write header here
            writer.writerow(self.column_names)

            # Read each line in the fixed-width file
            for line in fixed_file:
                row = self.parse_data(line, field_positions)
                writer.writerow(row)


if __name__ == '__main__':
    data_parser = DataParser()
    input_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'sample_data.csv')
    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'parsed_data.csv')

    # Run the parser function
    data_parser.write_parsed_data_to_csv(input_file, output_file)
    print(f"CSV file '{output_file}' generated successfully.")