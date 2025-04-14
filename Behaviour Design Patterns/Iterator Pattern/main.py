class Books:
    def __init__(self, books):
        self.books = books

    def create_iterator(self):
        return BooksIterator(self.books)
    def create_reverse_iterator(self):
        return ReverseBookIterator(self.books)


class BooksIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


class ReverseBookIterator:
    def __init__(self, books):
        self.books = books
        self.index = len(books) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            book = self.books[self.index]
            self.index -= 1
            return book
        else:
            raise StopIteration


my_playlist = Books(["Bohemian Rhapsody", "Billie Jean", "Thriller"])
iterator = my_playlist.create_iterator()
rev_iterator = my_playlist.create_reverse_iterator()

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(rev_iterator))
print(next(rev_iterator))
print(next(rev_iterator))
