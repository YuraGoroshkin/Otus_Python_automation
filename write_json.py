import math
import json
from readers.reader_json import ReaderJSON
from readers.reader_csv import ReaderCSV

# n нужно получать от деления длины найденныйх книг с длинны найденных пользователей
number = math.ceil(ReaderCSV().number_of_books() / ReaderJSON().number_of_user())

books = ReaderCSV.books
# parts_book = lambda books, n=number: [books[i:i + n] for i in range(0, len(books), n)]
# parts_book(books)
# print(parts_book(books))
# print(number)


parts_book = (books[i:i + number] for i in range(0, len(books), number))

c = list(parts_book)[0]

data = [
    {
        "name": ReaderJSON.user['name'],
        "gender": ReaderJSON.user['gender'],
        "address": ReaderJSON.user['address'],
        "age": ReaderJSON.user['age'],
        "books": c
    },
]

with open("result.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)
