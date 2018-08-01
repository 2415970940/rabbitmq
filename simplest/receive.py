import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chan = conn.channel()
chan.queue_declare('hello')

def callback(ch,method,properties,body):
    print("Received %r"%body)
# no_ack   message acknowledgment
chan.basic_consume(callback,queue='hello',no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
chan.start_consuming()