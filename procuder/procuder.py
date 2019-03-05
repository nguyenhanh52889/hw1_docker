import pika
from random import *
 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='number')

message = randint(1, 100)

while True:
    try:
        message = input('> ')
    except EOFError:
        break

    channel.basic_publish(exchange='', routing_key='number', body=message)

connection.close()
