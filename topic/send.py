#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()

# python35 send.py "kern.critical" "A critical kernel error"  all receive
# python35 send.py "kern" "A kernel error"                    1   receive
# python35 send.py "kern.*" "A kernel error"                  1,2,4 receive
# python35 send.py "kern.#" "A kernel error"                  1,2,4 receive
# python35 send.py "kern123" "A kernel123 error"              1   receive
# python35 send.py "kern.123" "A kernel123 error"              1,2,4   receive
# python35 send.py "123213" "unknown"                          1  receive
