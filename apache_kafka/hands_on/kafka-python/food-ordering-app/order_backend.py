from random import random
from kafka import KafkaProducer
from faker import Faker
import json
import time
import random

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 100_000
price_list = [30,45,69,88,99]
food_list = ["pizza", "burger", "masala dosa", "aloo paratha", "croissant"]
fake = Faker()

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=json_serializer
)

if __name__ == "__main__":
    print("Producer generating data!")
    for i in range(1, ORDER_LIMIT):
        data={
            "order_id": i,
            "username": fake.name(),
            "user_address": fake.address(),
            "user_email": fake.email(),
            "total_cost": random.choice(price_list),
            "order_item": random.choice(food_list)
        }

        producer.send(
        ORDER_KAFKA_TOPIC,
        data
        )
        print(data)
        # time.sleep(2)