import pika
import time

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chan = conn.channel()
chan.exchange_declare(exchange='logs',exchange_type='fanout')
result = chan.queue_declare(exclusive=True)
queuename = result.method.queue
chan.queue_bind(exchange='logs',queue=queuename)

def callback(ch,method,properties,body):
    print("Received %r"%body)
    time.sleep(body.count(b'.'))
    print('Done')

chan.basic_consume(callback,queue=queuename,no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
chan.start_consuming()