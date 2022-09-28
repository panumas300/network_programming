import json

with open("week5/books.json","rt") as file:
    books = json.load(file)

print(books)

print(type(books))