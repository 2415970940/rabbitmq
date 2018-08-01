import pika
import time

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chan = conn.channel()
chan.queue_declare('hello')

def callback(ch,method,properties,body):
    print("Received %r"%body)
    time.sleep(body.count(b'.'))
    print('Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

chan.basic_qos(prefetch_count=1)
chan.basic_consume(callback,queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')
chan.start_consuming()