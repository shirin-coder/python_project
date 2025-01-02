class Library:
    _book_list = []

    @classmethod
    def entry_book(cls, book):
        cls._book_list.append(book)


class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def ViewTheBooks(self):
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Availability: {'Yes' if self.__availability else 'No'}")

    def BorrowAnyBook(self):
        if self.__availability:
            self.__availability = False
            print(f"You have successfully borrowed '{self.__title}'. Enjoy reading!")
        else:
            print(f"Sorry, '{self.__title}' is currently not available.")

    def ReturnBook(self):
        if not self.__availability:
            self.__availability = True
            print(f"Thank you for returning '{self.__title}'.")
        else:
            print(f"'{self.__title}' does not belong to our library.")

    def getBookId(self):
        return self.__book_id


lib1 = Library()
book1 = Book(1, "Coding is Fun", "Shirin")
book2 = Book(2, "Learn Database", "Fatema")
book3 = Book(3, "C++ Programming", "Rabeya")


def menu_system():
    while True:
        print("\nLibrary Menu:")
        print("1. View all books")
        print("2. Borrow book")
        print("3. Return book")
        print("4. Exit")

        choice = input("Enter your choice : 1 or 2 or 3 or 4-> ")

 
        if choice ==  "1":

            print("\nHere are all the books in the library:")
            for book in Library._book_list:
                book.ViewTheBooks()
                print()

        elif choice == "2":
            book_id = int(input("Enter the Book ID to borrow: "))
            for book in Library._book_list:
                if book.getBookId() == book_id:
                    book.BorrowAnyBook()
                    break
            else:
                print(" Book not found.  Please try again.")

        elif choice ==  "3":
            book_id = int(input ("Enter the Book ID to return: "))
            for book in Library._book_list:
                if book.getBookId() == book_id:
                    book.ReturnBook()

                    break
            else:
                print("Invalid Book ID.")

        elif choice ==  "4":
            print("Exiting the library system")

            break

        else:
            print("Invalid choice. ")

menu_system()


