from datetime import datetime

from mongoengine import connect
from mongoengine import Document, StringField, BooleanField, DateTimeField

from db import URI, db_name

connect(db=db_name, host=URI)


class Contact(Document):
    fullname = StringField(max_length=120, required=True)
    email = StringField(max_length=60, required=True)
    got_email = BooleanField(default=False)
    email_date_got = DateTimeField(default=datetime(1970, 1, 1, 0, 0, 0))
    meta = {'collection': 'contacts'}
