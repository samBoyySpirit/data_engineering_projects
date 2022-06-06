import json
from kafka import KafkaConsumer

ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    group_id="consumer-group-a"
)
total_order_count=0
total_revenue=0
print("Analytics listening...")

if __name__ == "__main__":
    while True:
        for msg in consumer:
            consumed_msg = json.loads(msg.value.decode())
            total_cost = consumed_msg["confirmed_total_cost"]

            total_revenue +=total_cost
            total_order_count +=1

            print(f"Total Revenue is {total_revenue} and order count is {total_order_count}")
