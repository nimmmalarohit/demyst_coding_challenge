# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install dependencies
RUN apt-get update && apt-get install -y wget gnupg2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install OpenJDK 11
RUN wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz && \
    tar xvf openjdk-11+28_linux-x64_bin.tar.gz && \
    mv jdk-11 /usr/local/ && \
    ln -s /usr/local/jdk-11/bin/java /usr/bin/java && \
    rm openjdk-11+28_linux-x64_bin.tar.gz

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/local/jdk-11
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run tests
RUN echo "Running the unit tests"
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]

# Run Problem 1
CMD ["python", "src/data_parser.py"]

# Run Problem 2
CMD ["python", "src/data_processing.py"]
