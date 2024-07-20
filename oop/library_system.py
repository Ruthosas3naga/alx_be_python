class Book:
    def __init__(self,title:str, author:str):
     self.title = title
     self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


class EBook(Book):
   def __init__(self,title:str, author:str,file_size:int):
    super().__init__(title,author)
    self.file_size = file_size

   def __str__(self):
        return f"{self.title} by {self.author} {self.file_size}"
    
   def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.file_size}')"

    
class PrintBook(Book):
    def __init__(self,title:str, author:str,page_count:int):
        super().__init__(title,author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} {self.page_count}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.page_count}')"
    

class Library:
   def __init__(self):
      self.books = []

   def add_book(self, book):
      self.books.append(book)

   def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added {book}")
        else:
            raise ValueError("Can only add instances of Book, EBook, or PrintBook")

   def __str__(self):
        return f"Library with {len(self.books)} books"