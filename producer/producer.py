from confluent_kafka import Producer

conf = {
    'bootstrap.servers': '127.0.0.1:9092',  # Use the hostname 'kafka' for the broker
    'client.id': 'python-producer'
}

# Create a Kafka producer instance
producer = Producer(conf)

# Define the Kafka topic to produce to
topic = 'test-topic'

# Produce messages to the Kafka topic
for i in range(10):
    message = f"Message {i}"
    producer.produce(topic, key=str(i), value=message)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()
