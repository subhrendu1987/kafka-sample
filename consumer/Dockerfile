# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install the confluent-kafka-python library
RUN pip install confluent-kafka

# Install the ping utility (iputils-ping package)
RUN apt-get update && apt-get install -y iputils-ping

# Copy the consumer Python script into the container
COPY consumer.py .

CMD ["/bin/bash"]
# Run the consumer script
#CMD ["python", "consumer.py"]
