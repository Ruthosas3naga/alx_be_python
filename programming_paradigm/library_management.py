class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def _is_checked_out(self):
        pass
class Library(Book):
    def __init__(self, title, author,_books=[]):
        super().__init__(title, author)
        add.book = 