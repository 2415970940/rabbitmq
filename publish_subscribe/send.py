import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
chan = conn.channel()

chan.exchange_declare(exchange='logs',exchange_type='fanout')
# chan.queue_declare("hello")

# message = ' '.join(sys.argv[1:]) or 'hello world,lunarji'
for i in range(10):
    a="."*i
    message = "message %s - %d"%(a,i)
    # message = "message - %d"%i
    chan.basic_publish(exchange='logs',routing_key='',body=message)
    print('send successfully,%r'%message)
conn.close()