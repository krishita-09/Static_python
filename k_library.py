def dec(func):
    def process():
        print("Welcome user!")
        func()
        print("Goodbye user")
    return process

@dec
def lib():
    def add_book(title, author, genre):
        book = (title,author,genre)

    library = []
    library_set = set()
    def add_to_library(book): 
        if book not in library_set:
            library.append(book)
            library_set.add(book)
            print("Book added to library.")
        else:
            print("Book already presnet in library.")

    def remove_from_library(title): 
        for book in library:
            if book[0] == title:
                library.remove(book)
                library_set.remove(book)
                print("Book removed from library.")
                return
        else:
            print("Book not present in library.")

    def search_books(s): 
        for book in library:
            if book[0] == s or book[1] == s:
                print(f"Name: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
                return
        else:
            print("No such books found in library with given name/author.")

    def list_books():
        if not library:
            print("The library is empty. Add books.")
        else:
            print("Books in library include:")
            for book in library:
                print(f"Name: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

    def categorize_books():
        global dict
        dict = {}

        for book in library:
            title, author, genre = book
            if genre not in dict:
                dict[genre] = []
            dict[genre].append(book)

    def  print_by_genre(inp_genre): 
        if inp_genre in dict:
            print(f"Books in {inp_genre} genre :")
            for book in dict[inp_genre]:
                print(f"Name: {book[0]}, Author: {book[1]}")
        else:
            print("No books of that genre.")

    x = 0

    while x != 6:
        print("1. Add a book. \n2. Remove a book. \n3. Search for a book. \n4. List all books in library. \n5. List books by category \n6. Exit")
        x = int(input("Enter choice : "))

        if x == 1:
            title = input("Enter book title : ")
            author = input("Enter book author : ")
            genre = input("Enter book genre : ")
            new_book = (title, author, genre)
            add_to_library(new_book)
            categorize_books()
        
        elif x == 2:
            title = input("Enter title of the book to be removed : ")
            remove_from_library(title)

        elif x == 3:
            s = input("Enter name or author of the book to be searched : ")
            search_books(s)
        
        elif x == 4:
            list_books()
        
        elif x == 5:
            inp_genre = input("Enter genre to be searched : ")
            print_by_genre(inp_genre)

        elif x != 6:
            print("Invalid choice. Please enter a number between 1-6.")
            
        else:
            break
    exit

lib()