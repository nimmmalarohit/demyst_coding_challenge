"""
Generating the CSV file with first_name, last_name, address, date_of_birth and Anonymizing the data.

Problem 2: Data Processing
 - Generate a CSV file containing first_name, last_name, address, and date_of_birth.
 - Process the CSV file to anonymize the data.
 - Columns to anonymize are first_name, last_name, and address.
 - Ensure the solution can efficiently handle a 2GB CSV file on a typical laptop.
 - Demonstrate that the same solution can scale to process even larger datasets.
 - Hint: Achieve scalability and efficiency using a distributed computing platform like Apache Spark.
"""

import csv
import os
import faker
import hashlib
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def generate_random_data(fake):
    """
    Generate a dictionary containing fake data for first_name, last_name, address, and date_of_birth.
    :param fake: A Faker instance for generating realistic fake data.
    :return: dict: A dictionary with keys 'first_name', 'last_name', 'address', and 'date_of_birth'.
    """
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address().replace("\n", " "),
        'date_of_birth': fake.date_of_birth()
    }


# Initialize Faker library to generate fake data
fake = faker.Faker()

# Filepath for the generated CSV
csv_output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'large_sample_data.csv')

# This specifies where the generated and anonymized CSV files will be saved.
anonymize_data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'anonymize_data.csv')

# Number of records to generate
num_records = 1000
chunk_size = 1000

# Generate the CSV file
# The data is generated and written in chunks to minimize memory usage.
with open(csv_output_file, 'w', newline='', buffering=chunk_size) as csvfile:
    fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Write the header row with column names
    writer.writeheader()
    for _ in range(num_records):
        writer.writerow(generate_random_data(fake))
        # print(f"records written: {_+1}")

print(f'{csv_output_file} generated with {num_records} records.')

# Initialize Spark session for processing the CSV file
# Spark is used here to leverage its distributed computing capabilities, which allows
# processing of large datasets that may exceed the memory limits of a single machine.
spark = SparkSession.builder.master("local[*]").getOrCreate()

# Read the generated CSV file into a Spark DataFrame
# The DataFrame API in Spark is leveraged for efficient distributed processing.
generated_data_df = spark.read.option("header", "true").option("delimiter", ",").csv(csv_output_file)

# Anonymize the specified columns using SHA-256 hashing
df_anonymized = generated_data_df.withColumn("first_name", F.sha2("first_name", 256)) \
                  .withColumn("last_name", F.sha2("last_name", 256)) \
                  .withColumn("address", F.sha2("address", 256))

# Write the anonymized data to a new CSV file
# The processed data is written out in a distributed manner, ensuring that the entire
df_anonymized.write.csv(anonymize_data_file, header=True, mode="overwrite")
spark.stop()

print(f'{anonymize_data_file} generated.')
