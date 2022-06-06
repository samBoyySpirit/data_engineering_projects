from kafka import KafkaProducer
import json
from data_gen import get_registered_user
import time

def json_serializer(data):\
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer,
)

if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        producer.send('kafka.learning.messages', registered_user)
        print(registered_user)
        time.sleep(5)