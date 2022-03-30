from kafka import KafkaConsumer
import json

def create_consumer(topic, groupId):
    return KafkaConsumer(
        topic,
        bootstrap_servers='127.0.0.1:9092',
        auto_offset_reset='earliest',
        group_id=groupId)

if __name__ == "__main__":
    consumer = create_consumer("test_topic_8","consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))