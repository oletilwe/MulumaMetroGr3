class Book:
    #This is to initialize. 
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Library:
    #This is to initialize.
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        # function to add a book using the book that is initialized in the init method. 
        self.books[book.isbn] = book

    def search_by_title(self, keyword):
        return [book for book in self.books.values() if keyword.lower() in book.title.lower()]
    # this returns a list comprehension that looks for books by title using the key word. The keyword and the title are
   # are converted to lowercase. 

    def search_by_author(self, keyword):
        # search for books by the author
        return [book for book in self.books.values() if keyword.lower() in book.author.lower()]
# list comprehension to again check the name of the author and the authors name is convereted to lowercase 

    def checkout(self, isbn):
        # this checks if the book is available as well as the book number is there 
        if isbn in self.books and self.books[isbn].available:
            # if the book and the book number is there the book will be checked out and it wont be available until 
            # it is returned. 
            self.books[isbn].available = False
            # will print book title checked out
            print(f"{self.books[isbn].title} checked out")
        else:
            print("Book not available")

    def return_book(self, isbn):
        # this method will only work when the book is returned 
        if isbn in self.books and not self.books[isbn].available:
            # it will check if the book was taken out and if so it will
            # mark it as returned 
            self.books[isbn].available = True
            print(f"{self.books[isbn].title} returned")
        else:
            print("Book is already available")

def main():
    library = Library()
    while True:
        # this where the user will be asked to choose wich option they want. 
        print("\n1. Add Book")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Checkout")
        print("5. Return")
        print("6. Exit")
        choice = input("Choose an option: ")

# all the options above will have an if statement of their own to follow
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            # adds the book's title, author name and the isbn 
            library.add_book(Book(title, author, isbn))
        elif choice == "2":
            keyword = input("Enter keyword: ")
            # it asks the user what book they want to search and stores it in the variable 'keyword' it is 
            # then checked. 
            books = library.search_by_title(keyword)
            for book in books:
                print(book.title)
        elif choice == "3":
            keyword = input("Enter keyword: ")
            # it doesnt search the book by its name but by the the author 
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