import re
from mongoengine import connect, Q

from db import URI, db_name
from models import Quot, Author
from app import find_author

connect(db=db_name, host=URI)


def find_quotes_by_author(author_name):
    author = find_author(author_name)
    if author:
        quotes = Quot.objects(author=author)
        for quote in quotes:
            quote_dict = quote.to_mongo().to_dict()
            print(f"Author: {author.fullname}\nQuote: {quote_dict['quote']}\n")

def find_quotes_by_tags(tags):
    # quotes = Quot.objects(tags=tags)
    quotes = Quot.objects(Q(tags__all=tags.split(",")))
    for quote in quotes:
        quote_dict = quote.to_mongo().to_dict()
        author = Author.objects(id=quote_dict['author']).first()
        print(f"Author: {author.fullname}\nQuote: {quote_dict['quote']}\n")

def find_quotes_by_author_tag(author_name, tags):
    author = find_author(author_name)
    if author:
        quotes = Quot.objects(author=author, tags=tags)
        for quote in quotes:
            quote_dict = quote.to_mongo().to_dict()
            print(f"Author: {author.fullname}\nQuote: {quote_dict['quote']}\n")


def parse_data(inputted_data):

    pattern = r'(\w+)\s*:\s*([^:]+)(?=\s+\w+:|$)'
    matches = re.findall(pattern, inputted_data)

    result_dict = dict(matches)
    return result_dict

def main():

    while True:
        inputted_data = input("Input search data or type 'exit' to close app:").strip()

        if inputted_data == "exit":
            break

        parsed_to_dict = parse_data(inputted_data)
        authors_name = parsed_to_dict.get("name")
        tags = parsed_to_dict.get("tag")
        if authors_name and tags:
            find_quotes_by_author_tag(authors_name,tags)
        elif authors_name:
            find_quotes_by_author(authors_name)
        elif tags:
            find_quotes_by_tags(tags)
        else:
            print(f"No search result by inputted data: {inputted_data}")


if __name__ == '__main__':
    main()
