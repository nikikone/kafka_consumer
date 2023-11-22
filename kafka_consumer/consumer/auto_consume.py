from kafka import KafkaConsumer
import multiprocessing
import time


class Consumer:

    def run(self):

        process = multiprocessing.Process(target=self.consume, args=())
        process.start()

    @staticmethod
    def consume():
        from kafka_consumer.models import Zone
        print("start consume")
        consumer = KafkaConsumer(
            'cv_prod',
            bootstrap_servers=['127.0.0.1:9092', '127.0.0.1:9093', '127.0.0.1:9094'],
        )
        try:
            for message in consumer:
                msg = message.value.decode("UTF-8")[1:-1].split()
                print(msg)
                direction = msg[msg.index("direction:") + 1]
                zone_id = msg[msg.index("zone_id:") + 1]
                obj = Zone.objects.filter(id_zone=int(zone_id))
                if not len(obj):
                    a = Zone(id_zone=zone_id)
                else:
                    a = obj[0]
                if direction == "in":
                    a.in_zone += 1
                elif direction == "out":
                    a.out_zone += 1
                a.save()
        except KeyboardInterrupt:
            print('\nexit ctrl+c')

