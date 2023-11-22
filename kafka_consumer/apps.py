from django.apps import AppConfig
import sys
from .consumer.auto_consume import Consumer


class KafkaConsumerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kafka_consumer'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        Consumer().run()
