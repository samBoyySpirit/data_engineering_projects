import json
from kafka import KafkaConsumer

ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"


if __name__ == "__main__":
    consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    group_id="consumer-group-a"
    )

    email_sent_so_far = set()
    print("Email is listening...")

    while True:
        for msg in consumer:
            consumed_msg = json.loads(msg.value.decode())
            customer_email = consumed_msg["confirmed_customer_email"]

            print(f"Sending email to {customer_email}")

            email_sent_so_far.add(customer_email)
            print(f"So far emails sent to {len(email_sent_so_far)} unique emails")
            print('\n')
