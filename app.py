from mongoengine import DoesNotExist

from models import Author


def find_author(author_name):
    try:
        author = Author.objects.get(fullname=author_name)
        return author
    except DoesNotExist:
        return None
