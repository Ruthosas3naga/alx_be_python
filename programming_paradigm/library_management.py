class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"Book '{self.title}' checked out.")
        else:
            print(f"Book '{self.title}' is already checked out.")
    
    def check_in(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"Book '{self.title}' checked in.")
        else:
            print(f"Book '{self.title}' is not checked out.")

    def is_checked_out(self):
        return self._is_checked_out
    
    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
class Library:
    def __init__(self):
        self._books=[]
    
    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Book '{book.title}' by {book.author} added to the library.")
        else:
            print("Error: Only instances of Book can be added to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.check_out()
                    return
                else:
                    print(f"Book '{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self):
        for book in self._books:
        
                if book.is_checked_out():
                    book.check_in()
                    return
                else:
                    print(f"Book  was not checked out.")
                    return
        print(f"Book  not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books available in the library.")
