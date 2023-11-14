# Download and Launch kafka Broker, Producer and Client as a single docker
1. Download and build `docker`



1. Launch kafka broker
    ```
    cd kafka; sudo docker-compose up -d
    ```
1. Open *two* interactive terminal in the container and use them for producer and consumer respectively:
    ```
    sudo docker exec -it kafka-kafka-1 bash
    ```
    1. Navigate to the following directory `/opt/bitnami/kafka/bin` inside the kafka broker
        ```
        cd opt/bitnami/kafka/bin
        ```
    1. Now, let’s create our first topic. Execute the following command:
        ```
        kafka-topics.sh --create --bootstrap-server 127.0.0.1:9092 --replication-factor 1 --partitions 1 --topic room_1
        ```
    1. Test with inbuilt producer / consumer script
        1.
            ```
            kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092 --producer.config /opt/bitnami/kafka/config/producer.properties --topic room_1
            ```
        1. 
            ``` kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --consumer.config /opt/bitnami/kafka/config/consumer.properties --topic room_1 --from-beginning 
            ```

