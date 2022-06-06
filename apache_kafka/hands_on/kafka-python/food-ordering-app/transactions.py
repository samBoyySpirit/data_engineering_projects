import json
from kafka import KafkaConsumer
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
        ORDER_KAFKA_TOPIC,
        bootstrap_servers="localhost:9092",
        auto_offset_reset='earliest',
        group_id="consumer-group-a"   
    )

producer = KafkaProducer(
        bootstrap_servers="localhost:9092"
    )

if __name__ == "__main__":
    while True:
        for msg in consumer:
            consumed_msg = json.loads(msg.value.decode())
            print(consumed_msg)
            print("Successful consumption of message!")
            print('\n')
            print("...To broadcast it to the consumed topic")

            order_id = consumed_msg["order_id"]
            user_name = consumed_msg["username"]
            user_email = consumed_msg["user_email"]
            total_cost = consumed_msg["total_cost"]

            data = {
                "confirmed_order_id": order_id,
                "confirmed_customer_name": user_name,
                "confirmed_customer_email": user_email,
                "confirmed_total_cost": total_cost
            }

            producer.send(
                ORDER_CONFIRMED_KAFKA_TOPIC,
                json.dumps(data).encode('utf-8')
            )
            print("Published to the confirmed kafka topic!")
            print('\n')
