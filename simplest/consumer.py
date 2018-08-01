#!/usr/bin/env python
# -*- coding: utf_8 -*-

# import pika
#
# #建立连接connection到localhost
# con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# #创建虚拟连接channel
# cha = con.channel()
# #创建队列anheng
# result=cha.queue_declare(queue='anheng',durable=True)
# #创建名为yanfa,类型为fanout的交换机，其他类型还有direct和topic
# cha.exchange_declare(durable=False,
#                      exchange='yanfa',
#                      type='direct',)
# #绑定exchange和queue,result.method.queue获取的是队列名称
# cha.queue_bind(exchange='yanfa',
#                queue=result.method.queue,
#                routing_key='',)
# #公平分发，使每个consumer在同一时间最多处理一个message，收到ack前，不会分配新的message
# cha.basic_qos(prefetch_count=1)
# print(' [*] Waiting for messages. To exit press CTRL+C')
# #定义回调函数
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % (body,))
#     ch.basic_ack(delivery_tag = method.delivery_tag)
#
# cha.basic_consume(callback,
#                   queue='anheng',
#                   no_ack=False,)
#
# cha.start_consuming()

import pika

username="user"
pwd="123"
user_pwd = pika.PlainCredentials(username, pwd)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('localhost',virtual_host="/vhost_mmr",credentials=user_pwd))#创建连接
chan = s_conn.channel()#在连接上创建一个频道

chan.queue_declare(queue='hello')#声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行


def callback(ch,method,properties,body): #定义一个回调函数，用来接收生产者发送的消息
    print("[消费者] recv %s" % body)

chan.basic_consume(callback,  #调用回调函数，从队列里取消息
                   queue='hello',#指定取消息的队列名
                   no_ack=True) #取完一条消息后，不给生产者发送确认消息，默认是False的，即  默认给rabbitmq发送一个收到消息的确认，一般默认即可
print('[消费者] waiting for msg .')
chan.start_consuming()#开始循环取消息
