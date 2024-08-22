# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Ensure the src directory is in the Python path
ENV PYTHONPATH=/app/src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run tests
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
