from kfk.producer.producer import main
import asyncio

from waiting.wait_for_postgres import wait_for_postgres
from waiting.wait_for_kafka import wait_for_service
from core.settings import settings

wait_for_postgres()
wait_for_service(settings.KAFKA_HOST, int(settings.KAFKA_PORT))

# Démarrer le programme
asyncio.run(main())