import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chan = conn.channel()

chan.queue_declare("hello")

# message = ' '.join(sys.argv[1:]) or 'hello world,lunarji'
for i in range(100):
    # a="."*i
    # message = "message %s - %d"%(a,i)
    message = "message - %d"%i
    chan.basic_publish(exchange='',routing_key='hello',body=message)
    print('send successfully,%r'%message)
conn.close()