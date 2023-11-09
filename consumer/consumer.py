from confluent_kafka import Consumer, KafkaError

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'kafka:9092',  # Use the hostname 'kafka' for the broker
    'client.id': 'python-consumer'
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to the Kafka topic
topic = 'test-topic'
consumer.subscribe([topic])

# Consume and print messages
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error: {msg.error()}' )
    else:
        print(f'Received message: {msg.value().decode("utf-8")}')

# Close the consumer
consumer.close()
