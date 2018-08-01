#!/usr/bin/env python
# -*- coding: utf_8 -*-


import pika
import sys

username='user'
pwd='123'

user_pwd = pika.PlainCredentials(username, pwd)
#创建连接connection到localhost
# con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# s_conn = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',port=15627,virtual_host="/",credentials=user_pwd))
s_conn = pika.BlockingConnection(pika.ConnectionParameters('localhost',virtual_host='/vhost_mmr',credentials=user_pwd))
#创建虚拟连接channel
# cha = con.channel()
chan = s_conn.channel()
#创建队列anheng,durable参数为真时，队列将持久化；exclusive为真时，建立临时队列
# result=cha.queue_declare(queue='anheng',durable=True,exclusive=False)
chan.queue_declare(queue='hello')
# #创建名为yanfa,类型为fanout的exchange，其他类型还有direct和topic，如果指定durable为真，exchange将持久化
# cha.exchange_declare(durable=False,
#                      exchange='yanfa',
#                      type='direct',)
# #绑定exchange和queue,result.method.queue获取的是队列名称
# cha.queue_bind(exchange='yanfa',
#                queue=result.method.queue,
#                routing_key='',)
# #公平分发，使每个consumer在同一时间最多处理一个message，收到ack前，不会分配新的message
# cha.basic_qos(prefetch_count=1)
# #发送信息到队列‘anheng’
# message = ' '.join(sys.argv[1:])
# #消息持久化指定delivery_mode=2；
# cha.basic_publish(exchange='',
#                   routing_key='anheng',
#                   body=message,
#                   properties=pika.BasicProperties(
#                      delivery_mode = 2,
#                  ))

chan.basic_publish(exchange='',  #交换机
                   routing_key='hello',#路由键，写明将消息发往哪个队列，本例是将消息发往队列hello
                   body='hello world')#生产者要发送的消息
print("[生产者] send 'hello world")
s_conn.close()#当生产者发送完消息后，可选择关闭连接
# print('[x] Sent %r' % (message,))
# #关闭连接
# con.close()