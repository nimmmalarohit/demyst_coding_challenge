"""
Generating the csv file with first_name, last_name, address, date_of_birth and Anonymize the data

                Problem 2
                Data processing
Generate a csv file containing first_name, last_name, address, date_of_birth
Process the csv file to anonymise the data
Columns to anonymise are first_name, last_name and address
You might be thinking that is silly
Now make this work on 2GB csv file (should be doable on a laptop)
Demonstrate that the same can work on bigger dataset
Hint - You would need some distributed computing platform
"""

import csv
import os
import faker
import hashlib


def generate_random_data(fake):
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address().replace("\n", " "),
        'date_of_birth': fake.date_of_birth()
    }


def anonymize_data(data):
    """Anonymize the data by hashing."""
    return hashlib.sha256(data.encode()).hexdigest()


def anonymize_rows(row):
    row['first_name'] = anonymize_data(row['first_name'])
    row['last_name'] = anonymize_data(row['last_name'])
    row['address'] = anonymize_data(row['address'])
    return row


# Initialize Faker library to generate fake data
fake = faker.Faker()

# Filepath for the generated CSV
csv_output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'large_sample_data.csv')
anonymize_data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'anonymize_data.csv')

# Number of records to generate
num_records = 1000
chunk_size = 1000

# Generate the CSV file
with open(csv_output_file, 'w', newline='', buffering=chunk_size) as csvfile:
    fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(num_records):
        writer.writerow(generate_random_data(fake))
        print(f"records written: {_+1}")

print(f'{csv_output_file} generated with {num_records} records.')


# Process and anonymize a CSV file in chunks.
with open(csv_output_file, 'r') as infile, open(anonymize_data_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    while True:
        rows = []
        try:
            for _ in range(chunk_size):
                rows.append(next(reader))
        except StopIteration:
            break

        if not rows:
            break
        for row in rows:
            row = anonymize_rows(row)
            writer.writerow(row)

        print(f'Processed {len(rows)} rows...')

print(f'{anonymize_data_file} generated with anonymized data.')