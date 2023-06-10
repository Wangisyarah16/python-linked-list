class Book:
    def __init__(self, title):
        self.title = title
        self.next = None

class Visitor:
    def __init__(self, name):
        self.name = name
        self.books = None
        self.next = None

class Library:
    def __init__(self):
        self.head = None

    def add_visitor(self, name):
        new_visitor = Visitor(name)
        if self.head is None:
            self.head = new_visitor
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_visitor

    def borrow_book(self, visitor_name, book_title):
        visitor = self.find_visitor(visitor_name)
        if visitor is None:
            print(f"{visitor_name} is not a registered visitor.")
            return

        new_book = Book(book_title)
        if visitor.books is None:
            visitor.books = new_book
        else:
            current = visitor.books
            while current.next is not None:
                current = current.next
            current.next = new_book

    def find_visitor(self, name):
        current = self.head
        while current is not None:
            if current.name == name:
                return current
            current = current.next
        return None

    def print_borrowed_books(self, visitor_name):
        visitor = self.find_visitor(visitor_name)
        if visitor is None:
            print(f"{visitor_name} is not a registered visitor.")
        elif visitor.books is None:
            print(f"{visitor_name} has not borrowed any books.")
        else:
            print(f"{visitor_name}'s borrowed books:")
            current = visitor.books
            while current is not None:
                print(current.title)
                current = current.next

library = Library()

library.add_visitor("popi pertiwi")
library.add_visitor("luluk hf")
library.add_visitor("pinca")

library.borrow_book("popi pertiwi", "septihan")
library.borrow_book("popi pertiwi", "galaksi")
library.borrow_book("luluk hf", "mariposa")
library.borrow_book("pinca", "strawberry cloud")

library.print_borrowed_books("popi pertiwi")
print("---")
library.print_borrowed_books("luluk hf")
print("---")
library.print_borrowed_books("pinca")
print("---")
library.print_borrowed_books("firda")
