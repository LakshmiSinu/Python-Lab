class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C", "Data Structures"]

    def display_books(self):
        print("Available books:", self.books)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned successfully")


library = Library()

library.display_books()

book = input("Enter book to borrow: ")
library.borrow_book(book)

library.display_books()

book = input("Enter book to return: ")
library.return_book(book)

library.display_books()
