"""
Problem 1
Parse fixed width file
Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
Language choices (Python or Scala)
Deliver source via github or bitbucket
Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
Pay attention to encoding
"""

import csv
import os
import json


specs_json = os.path.join(os.path.dirname(os.path.dirname(__file__)),'spec.json')

# Read and load the spec.json parameters
with open(specs_json, 'r') as specs:
    specs_data = json.loads(specs.read())

# Get the column names and offsets from spec
column_names = specs_data.get('ColumnNames')
offsets = [int(offset) for offset in specs_data.get('Offsets')]


def parse_data(line, field_positions):
    """
    Extract fields based on start and end positions
    """
    return [line[start:end].strip() for start, end in field_positions]


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


def parse_fixed_width_to_csv(input_file, output_file):
    """
    This method is used to read the input file, create a list of tuple consisting position and offset,
    then offset position list use string slicing function to parse the input file as row, and write each row into output file
    """
    field_positions = get_field_positions(offsets)

    # Open the fixed-width file and CSV file
    with open(input_file, 'r', encoding='windows-1252') as fixed_file, \
            open(output_file, 'w', newline='', encoding='utf-8') as csv_file:

        writer = csv.writer(csv_file)

        # Write header here
        writer.writerow(column_names)

        # Read each line in the fixed-width file
        for line in fixed_file:
            row = parse_data(line, field_positions)
            writer.writerow(row)


input_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'sample_data.csv')
output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'parsed_data.csv')

# Run the parser function
parse_fixed_width_to_csv(input_file, output_file)

print(f"CSV file '{output_file}' generated successfully.")