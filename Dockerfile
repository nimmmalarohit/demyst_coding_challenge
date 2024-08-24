# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Spark
ENV SPARK_VERSION=3.4.3
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip

# Install dependencies
RUN apt-get update && apt-get install -y wget curl gnupg2 dos2unix && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install OpenJDK 11
RUN wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz && \
    tar xvf openjdk-11+28_linux-x64_bin.tar.gz && \
    mv jdk-11 /usr/local/ && \
    ln -s /usr/local/jdk-11/bin/java /usr/bin/java && \
    rm openjdk-11+28_linux-x64_bin.tar.gz

# Install Spark
RUN curl -L "https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -o /tmp/spark.tgz && \
    tar -xvzf /tmp/spark.tgz -C /opt/ && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} $SPARK_HOME && \
    rm /tmp/spark.tgz

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

# Ensure all scripts have Unix-style line endings
RUN dos2unix /app/entrypoint.sh

# Ensure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Run the entrypoint script
CMD ["/app/entrypoint.sh"]
