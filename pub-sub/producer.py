import logging
from faker import Faker
from models import Contact

from mongoengine import connect

from db import URI, db_name, rabbitMQ_queue

from rabbit import connection

connect(db=db_name, host=URI)

fake = Faker("uk_UA")

CONTACT_COUNT = 5

if __name__ == '__main__':

    channel = connection.channel()
    # channel.exchange_declare(exchange='HW8', exchange_type='fanout')
    channel.queue_declare(queue=rabbitMQ_queue)

    for _ in range(0, CONTACT_COUNT):
        contact = Contact()
        contact.fullname = fake.name()
        contact.email = fake.email()
        contact.save()

        channel.basic_publish(exchange='Events APP', routing_key=rabbitMQ_queue, body=str(contact.id).encode())

        print(f"publish in queue: {contact.id}")

    connection.close()

