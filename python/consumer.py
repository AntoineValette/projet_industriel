from kfk.consumer.consumer import consummer
from waiting.wait_for_postgres import wait_for_postgres
from waiting.wait_for_kafka import wait_for_service

if __name__ == "__main__":
    wait_for_postgres()
    wait_for_service("kafka", 9092)
    consummer()
