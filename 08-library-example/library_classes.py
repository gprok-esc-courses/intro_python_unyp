
class Book:
    def __init__(self, isbn, title, n_copies, n_borrowed):
        self.isbn = isbn
        self.title = title 
        self.n_copies = n_copies 
        self.n_borrowed = n_borrowed

    def is_available(self):
        return self.n_copies - self.n_borrowed > 0
    
    def is_borrowed(self):
        return self.n_borrowed > 0
    
    def __str__(self):
        return self.isbn + " " + self.title



class Library:
    def __init__(self):
        self.books = {}

    def load_books(self):
        self.books['1111'] = Book('1111', 'Python', 7, 2)
        self.books['2222'] = Book('2222', 'Java', 3, 1)
        self.books['3333'] = Book('3333', 'Web Systems', 10, 0)
        self.books['4444'] = Book('4444', 'Networks', 6, 6)

    def is_available(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.is_available(): 
                return True 
            else: 
                return False
        else:
            print("ISBN not found")
            return False 
        
    def borrow(self, isbn):
        if self.is_available(isbn):
            book = self.books[isbn]
            book.n_borrowed += 1
        else: 
            print("Book is not available")

    def return_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.is_borrowed():
                book.n_borrowed -= 1
            else:
                print("Book is not borrowed to anyone")
        else:
            print("ISBN not bound")



class Menu:
    def display(self):
        print("1. Is Available?")
        print("2. Borrow")
        print("3. Return")
        print("0. Exit")

    def get_user_choice(self):
        choice = int(input("Choose: "))
        return choice