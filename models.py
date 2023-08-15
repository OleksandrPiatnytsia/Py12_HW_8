from mongoengine import connect
from mongoengine import Document, StringField, ListField, ReferenceField

from db import URI, db_name

connect(db=db_name, host=URI)


class Author(Document):
    fullname = StringField(max_length=120, required=True)
    born_date = StringField(max_length=60, required=True)
    born_location = StringField(max_length=120, required=True)
    description = StringField(max_length=240, required=True)
    meta = {'collection': 'authors'}


class Quot(Document):
    author = ReferenceField(Author)
    quote = StringField(max_length=240, required=True)
    tags = ListField(StringField(max_length=30))
    meta = {'collection': 'quotes'}
