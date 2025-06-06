class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def search_by_title(self, keyword):
        return [book for book in self.books.values() if keyword.lower() in book.title.lower()]

    def search_by_author(self, keyword):
        return [book for book in self.books.values() if keyword.lower() in book.author.lower()]

    def checkout(self, isbn):
        if isbn in self.books and self.books[isbn].available:
            self.books[isbn].available = False
            print(f"{self.books[isbn].title} checked out")
        else:
            print("Book not available")

    def return_book(self, isbn):
        if isbn in self.books and not self.books[isbn].available:
            self.books[isbn].available = True
            print(f"{self.books[isbn].title} returned")
        else:
            print("Book is already available")

def main():
    library = Library()
    while True:
        print("\n1. Add Book")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Checkout")
        print("5. Return")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(Book(title, author, isbn))
        elif choice == "2":
            keyword = input("Enter keyword: ")
            books = library.search_by_title(keyword)
            for book in books:
                print(book.title)
        elif choice == "3":
            keyword = input("Enter keyword: ")
            books = library.search_by_author(keyword)
            for book in books:
                print(book.title)
        elif choice == "4":
            isbn = input("Enter ISBN: ")
            library.checkout(isbn)
        elif choice == "5":
            isbn = input("Enter ISBN: ")
            library.return_book(isbn)
        elif choice == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()