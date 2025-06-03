class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrow_by = None

    def lend(self, out_to_user):
        if self.is_available:
            self.is_available = False
            self.borrow_by = out_to_user
            return f"'{self.title}' has been lent to {out_to_user}."
        else:
            return f"'{self.title}' is currently not available."
        
My_book = Book("surrounded by idiots", "Le Hao", "1254-95478")

hello = My_book.lend("Oletilwe")
print(hello)


class Library:
     def __init__(self, book_list):
         self.book_list = book_list

     def find_book_by_author(self, keyword):
         keyword = keyword.lower()
         results = []
         for title, author in self.book_list.items():
             if author.lower() == keyword:
                 results.append(title)
         return results
    

book_list = {
        "nothing but the truth" : "Pro",
        "Le gae" : " charmaine",
        "48 Laws of power" : "Tsitso",
        "Think like a man" : "ntsako",
        "The psychology of money" : "titi",
     }

if __name__ == "__main__":
    library = Library()

    library.add_book("Le gae", "Charmaine")
    library.add_book("nothing but the truth", "Pro")
    library.add_book("48 laws of power", "Tsitso" )
    library.add_book("think like a man", "ntsako")
    library.add_book("The psychology of money", "Titi")

    print("Le gae':")
    for book in library.find_books_by_title("Le gae"):
        print(book)

    print("\nBooks by author 'Charmaine':")
    for book in library.find_books_by_author("Charmaine"):
        print(book)


Library = Library(book_list)
found_books = Library.find_book_by_author("Pro")
print(found_books)
