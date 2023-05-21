import math
import json
from readers.reader_json import ReaderJSON
from readers.reader_csv import ReaderCSV

# n нужно получать от деления длины найденныйх книг с длинны найденных пользователей
number = math.ceil(ReaderCSV().number_of_books() / ReaderJSON().number_of_user())

books = ReaderCSV.books


parts_book = (books[i:i + number] for i in range(0, len(books), number))
f = ReaderJSON().number_of_user()
c = list(parts_book)[2]
data = []
name = ReaderJSON.u
i = 0
for element in name:
    if i < f:
        # c = list(parts_book)[i]
        element['books'] = c
        data.append(element)
        i = i+1

with open("result.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)