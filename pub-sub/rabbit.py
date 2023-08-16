import pika
from db import rabbitMQ_user, rabbitMQ_password

credentials = pika.PlainCredentials(rabbitMQ_user, rabbitMQ_password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))

