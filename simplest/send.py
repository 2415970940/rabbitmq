import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chan = conn.channel()

chan.queue_declare("hello")

chan.basic_publish(exchange='',routing_key='hello',body='hello world,lunarji')
print('send successfully')
conn.close()