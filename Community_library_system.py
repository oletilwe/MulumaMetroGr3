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
        


