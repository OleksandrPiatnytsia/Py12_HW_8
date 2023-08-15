import re
from mongoengine import connect, DoesNotExist

from db import URI, db_name
from models import Quot, Author
from app import find_author

connect(db=db_name, host=URI)


def find_quotes_by_author():
    author = find_author("Albert Einstein")
    if author:
        quotes = Quot.objects(author=author)
        for quote in quotes:
            quote_dict = quote.to_mongo().to_dict()
            print(f"Author: {author.fullname}\nQuote: {quote_dict['quote']}\n")

def find_quotes_by_tag():
    quotes = Quot.objects(tags='my tag')
    for quote in quotes:
        quote_dict = quote.to_mongo().to_dict()
        author = Author.objects(id=quote_dict['author']).first()
        print(f"Author: {author.fullname}\nQuote: {quote_dict['quote']}\n")

def find_quotes_by_author_tag():
    author = find_author("Albert Einstein")
    if author:
        quotes = Quot.objects(author=author, tags='my tag')
        for quote in quotes:
            quote_dict = quote.to_mongo().to_dict()
            print(f"Author: {author.fullname}\nQuote: {quote_dict['quote']}\n")


def parse_data(inputted_data):

    pattern = r'(\w+)\s*:\s*([^:]+)(?=\s+\w+:|$)'
    matches = re.findall(pattern, inputted_data)

    result_dict = dict(matches)
    return result_dict


def main():
    find_quotes_by_author_tag()

    # inputted_data = "name: Albert tag: man,bla"
    # rarsed_to_dict = parse_data(inputted_data)
    # if


    # find_quotes_by_author()
    # find_quotes_by_tag()
    # inputted_data = input("Input search data:").strip()

    while True:
        inputted_data = input("Input search data:").strip()


if __name__ == '__main__':
    main()
