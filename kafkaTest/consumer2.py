

from consumer import create_consumer
import json


if __name__ == "__main__":
    consumer = create_consumer("test_topic_8","consumer-group-b")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))