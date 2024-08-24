#!/bin/sh

# Run Problem 1
python src/data_parser.py

# Run Problem 2
spark-submit --master local[*] src/data_processing.py

# Run tests
python -m unittest discover -s tests
