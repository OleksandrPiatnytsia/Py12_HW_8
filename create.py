import argparse
import json

from mongoengine import connect

from db import URI, db_name
from app import find_author

from models import Author, Quot

connect(db=db_name, host=URI)

parser = argparse.ArgumentParser(description='Authors quotes APP')
parser.add_argument('--database')
parser.add_argument('--path')

arguments = parser.parse_args()
my_arg = vars(arguments)

database = my_arg.get('database')
path = my_arg.get('path')

def create_authors(fullname="", born_date="", born_location="", description="", filepath=""):
    if filepath:

        authors_list = []
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
            for author_dict in data:
                author = Author(fullname=author_dict["fullname"], born_date=author_dict["born_date"],
                                born_location=author_dict["born_location"],
                                description=author_dict["description"])
                author.save()
                authors_list.append(author)

        result = authors_list

    else:
        author = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
        author.save()
        result = author
    return result


def create_quotes(author="", quote="", tags="", filepath=""):
    if filepath:

        qoutes_list = []

        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
            for quotes_dict in data:

                author = find_author(quotes_dict["author"])

                if author:
                    quot = Quot(author=author, quote=quotes_dict["quote"], tags=quotes_dict["tags"]).save()
                    qoutes_list.append(quot)

        result = qoutes_list

    else:
        quot = Quot(author=author, quote=quote, tags=tags)
        quot.save()
        result = quot

    return result

def main():

    match database:
        case 'authors':
            print("start authors creation...")
            create_authors(filepath=path)
            print("creation successfully done")
        case 'quotes':
            print("start quotes creation...")
            create_quotes(filepath=path)
            print("creation successfully done")
        case _:
            print("Unknown command")


if __name__ == '__main__':
    main()
