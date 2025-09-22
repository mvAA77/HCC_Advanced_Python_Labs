### Tanya Kadiyala
### CMSY-257-300
### Lab 2
### Problem 4: Library

from datetime import datetime

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.checked_out = False
        self.due_date = None

    def is_available(self):
        return not self.checked_out

    def checkout(self, due_date):
        if self.checked_out:
            raise Exception(f"Book '{self.title}' is already checked out.")
        self.checked_out = True
        self.due_date = due_date

    def checkin(self):
        if not self.checked_out:
            raise Exception(f"Book '{self.title}' is not checked out.")
        self.checked_out = False
        self.due_date = None

    def __str__(self):
        status = "Available" if not self.checked_out else f"Checked out (Due: {self.due_date})"
        return f"{self.title} by {self.author} ({self.year}) [ISBN: {self.isbn}] — {status}"


# ----------------- Member Class -----------------
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __str__(self):
        return f"{self.member_id} — {self.name}"



class Library:
    def __init__(self):
        self.__catalog = {}

    def add_book(self, book):
        if book.isbn in self.__catalog:
            raise Exception(f"Book with ISBN {book.isbn} already exists in catalog.")
        self.__catalog[book.isbn] = book

    def remove_book(self, isbn):
        if isbn not in self.__catalog:
            raise Exception(f"No book with ISBN {isbn} found.")
        if self.__catalog[isbn].checked_out:
            raise Exception(f"Cannot remove book {isbn}, it is currently checked out.")
        del self.__catalog[isbn]

    def checkout(self, isbn, member, due_date):
        if isbn not in self.__catalog:
            raise Exception(f"No book with ISBN {isbn} found.")
        book = self.__catalog[isbn]
        book.checkout(due_date)
        print(f"{member.name} successfully checked out '{book.title}' (Due: {due_date})")

    def checkin(self, isbn):
        if isbn not in self.__catalog:
            raise Exception(f"No book with ISBN {isbn} found.")
        self.__catalog[isbn].checkin()
        print(f"Book {isbn} has been checked in.")

    def search_title(self, substr):
        results = [str(book) for book in self.__catalog.values() if substr.lower() in book.title.lower()]
        return results if results else ["No matching books found."]

    def available_books(self):
        return [str(book) for book in self.__catalog.values() if book.is_available()]



if __name__ == "__main__":
    lib = Library()

    # Create books
    b1 = Book("Book A", "Author1", 2020, "111")
    b2 = Book("Book B", "Author2", 2021, "222")
    b3 = Book("Python Basics", "Guido", 2019, "333")
    b4 = Book("Advanced Python", "Rossum", 2022, "444")

    # Add books to library
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)
    lib.add_book(b4)

    # Create members
    m1 = Member("M01", "Alice")
    m2 = Member("M02", "Bob")

    # Checkout books
    lib.checkout("111", m1, "2025-09-15")
    lib.checkout("222", m2, "2025-09-20")

    print("\nAvailable books after checkout:")
    for b in lib.available_books():
        print(b)

    # Attempt invalid checkout
    try:
        lib.checkout("111", m2, "2025-09-25")
    except Exception as e:
        print("\nError:", e)

    # Check in a book
    lib.checkin("111")

    print("\nAvailable books after checkin:")
    for b in lib.available_books():
        print(b)

    # Search by title
    print("\nSearch results for 'Python':")
    for result in lib.search_title("Python"):
        print(result)
