from kfk.producer.producer import main
import asyncio

from waiting.wait_for_postgres import wait_for_postgres
from waiting.wait_for_kafka import wait_for_service

wait_for_postgres()
wait_for_service("kafka", 9092)

# Démarrer le programme
asyncio.run(main())