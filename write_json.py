import json
from readers.reader_json import ReaderJSON
from readers.reader_csv import ReaderCSV

books = ReaderCSV.books
users = ReaderJSON.u
user_index = 0

for book in books:
    user = users[user_index]
    user['books'].append(book)

    user_index += 1
    if user_index >= len(users):
        user_index = 0

with open("result.json", "w") as f:
    s = json.dumps(users, indent=4)
    f.write(s)
