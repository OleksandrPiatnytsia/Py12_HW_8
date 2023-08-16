from datetime import datetime

import sys

from mongoengine import connect, DoesNotExist

from db import URI, db_name, rabbitMQ_queue

from rabbit import connection
from models import Contact

connect(db=db_name, host=URI)


def main():
    channel = connection.channel()

    # queue = channel.queue_declare(queue=rabbitMQ_queue)
    channel.queue_bind(exchange='Events APP', queue=rabbitMQ_queue)

    channel.basic_consume(queue=rabbitMQ_queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = find_contact(contact_id)
    if contact:
        contact.got_email = True
        contact.email_date_got = datetime.now()
        contact.save()

    print(f" [x] Email sent to {contact.email}: {contact_id}: {contact.fullname}")


def find_contact(contact_id):
    try:
        author = Contact.objects.get(id=contact_id)
        return author
    except DoesNotExist:
        return None


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
