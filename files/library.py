"""
Section 6: Library Management System
Covers: Structure Code with OOP Principles (classes, encapsulation, inheritance)
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_issued = False  # encapsulated flag

    def issue(self):
        if self._is_issued:
            print(f"'{self.title}' is already issued.")
            return False
        self._is_issued = True
        print(f"Issued '{self.title}'.")
        return True

    def return_book(self):
        if not self._is_issued:
            print(f"'{self.title}' was not issued.")
            return
        self._is_issued = False
        print(f"Returned '{self.title}'.")

    def status(self):
        return "Issued" if self._is_issued else "Available"

    def __str__(self):
        return f"{self.title} by {self.author} [{self.status()}]"


class EBook(Book):
    """Inherits from Book; e-books can be issued to multiple people at once."""

    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)
        self.file_size_mb = file_size_mb
        self._is_issued = True  # ebooks are never "unavailable"

    def issue(self):
        print(f"'{self.title}' (e-book, {self.file_size_mb}MB) sent to your device.")
        return True

    def return_book(self):
        print(f"E-books don't need to be returned: '{self.title}'.")


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []


class Library:
    def __init__(self):
        self.catalog = []
        self.members = {}

    def add_book(self, book):
        self.catalog.append(book)

    def register_member(self, name):
        self.members[name] = Member(name)
        print(f"Registered member: {name}")

    def issue_to_member(self, title, member_name):
        member = self.members.get(member_name)
        if not member:
            print("Member not found.")
            return
        for book in self.catalog:
            if book.title == title:
                if book.issue():
                    member.borrowed.append(book)
                return
        print("Book not found in catalog.")

    def return_from_member(self, title, member_name):
        member = self.members.get(member_name)
        if not member:
            print("Member not found.")
            return
        for book in member.borrowed:
            if book.title == title:
                book.return_book()
                member.borrowed.remove(book)
                return
        print(f"{member_name} hasn't borrowed '{title}'.")

    def show_catalog(self):
        if not self.catalog:
            print("Catalog is empty.")
            return
        for book in self.catalog:
            print(f"  {book}")


def run_library_menu():
    print("\n--- Library Management System ---")
    lib = Library()
    # seed a couple of demo books
    lib.add_book(Book("Automate the Boring Stuff", "Al Sweigart"))
    lib.add_book(EBook("Python Crash Course", "Eric Matthes", 12))

    while True:
        print("\n1. Add book  2. Register member  3. Issue book  4. Return book  "
              "5. Show catalog  6. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            is_ebook = input("Is it an e-book? (y/n): ").lower() == "y"
            if is_ebook:
                size = input("File size (MB): ")
                lib.add_book(EBook(title, author, size))
            else:
                lib.add_book(Book(title, author))
        elif choice == "2":
            lib.register_member(input("Member name: "))
        elif choice == "3":
            lib.issue_to_member(input("Book title: "), input("Member name: "))
        elif choice == "4":
            lib.return_from_member(input("Book title: "), input("Member name: "))
        elif choice == "5":
            lib.show_catalog()
        elif choice == "6":
            break
        else:
            print("Unknown option.")
