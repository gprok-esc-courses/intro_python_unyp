
from library_classes import Library, Book, Menu

lib = Library()
lib.load_books()

menu = Menu()

while True:
    menu.display()
    choice = menu.get_user_choice()

    match choice:
        case 1:
            isbn = input("ISBN: ")
            print("Available" if lib.is_available(isbn) else "Not Available")
        case 2:
            isbn = input("ISBN: ")
            lib.borrow(isbn)
        case 3:
            isbn = input("ISBN: ")
            lib.return_book(isbn)
        case 0:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice")