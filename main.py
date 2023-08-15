import argparse
import json

from mongoengine import *

from db import URI, db_name

from models import Author, Quot

connect(db=db_name, host=URI)

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
age = my_arg.get('age')
_id = my_arg.get('id')
features = my_arg.get('features')


def create(fullname="", born_date="", born_location="", description="", filepath=""):
    result = None
    if filepath:

        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
            print(data)

    else:
        author = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
        author.save()
        result = author
    return result


# def find():
#     # cats = Cat.objects.as_pymongo()
#     cats = Cat.objects.all()
#     return cats
#
#
# def find_by_id(pk):
#     try:
#         cat = Cat.objects.get(id=pk)
#         return cat
#     except DoesNotExist:
#         return "Немає такого кота"
#
#
# def update(pk, name, age, features):
#     cat = Cat.objects(id=pk).first()  # None якщо не існує
#     if cat:
#         cat.update(name=name, age=age, features=features)
#         cat.reload()
#     return cat
#
#
# def remove(pk):
#     cat = Cat.objects.get(id=pk)
#     cat.delete()
#     return cat


def main():
    match action:
        case 'create':
            result = create(name, age, features)
            print(result.to_mongo().to_dict())
        case 'find':
            result = find()
            # print(result)
            [print(r.to_mongo().to_dict()) for r in result]
        case 'update':
            result = update(_id, name, age, features)
            print(result.to_mongo().to_dict())
        case 'remove':
            result = remove(_id)
            print(result.to_mongo().to_dict())
        case _:
            print("Unknown command")


if __name__ == '__main__':
    main()
    # print(find_by_id("649b1a8bc48b832dfb7146f8"))
