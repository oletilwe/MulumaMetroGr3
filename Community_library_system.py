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
     def __init__(self, author, title, book_list):
         self.author = author
         self.title = title
         self.book_list = book_list
         
book_list = {
        "nothing but the truth" : "Pro",
        "Le gae" : " charmaine",
        "48 Laws of power" : "Tsitso",
        "Think like a man" : "ntsako",
        "The psychology of money" : "titi",
     }
         
    # def find_book_by_author(self, keyword):
    #     for book in book_list:
    #         if book in book_list:
    #             keyword.lower 
    #         return book