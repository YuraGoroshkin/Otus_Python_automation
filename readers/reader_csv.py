from csv import DictReader

from files import CSV_FILE_PATH


class ReaderCSV:
    with open(CSV_FILE_PATH, newline='') as f:
        reader = DictReader(f)
        books = []
        # Итерируемся по данным делая из них словари
        for row in reader:
            books.append(row)

    def number_of_books(self):
        return len(self.books)
