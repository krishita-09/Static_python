class Library:
    def __init__(self):
        self.books = set()
        self.library_list = []
        self.genre_dict = {}

    def add_book(self, title, author, genre):
        return (title, author, genre)

    def add_to_library(self, book):
        if book not in self.books:
            self.books.add(book)
            self.library_list.append(book)
            self._update_genre_dict(book)

    def _update_genre_dict(self, book):
        title, author, genre = book
        if genre in self.genre_dict:
            self.genre_dict[genre].append((title, author))
        else:
            self.genre_dict[genre] = [(title, author)]

    def remove_from_library(self, title):
        for book in self.library_list:
            if book[0] == title:
                self.library_list.remove(book)
                self.books.remove(book)
                self._update_genre_dict(book)
                break

    def search_books(self, search_term):
        matching_books = []
        for book in self.library_list:
            if search_term.lower() in book[0].lower() or search_term.lower() in book[1].lower():
                matching_books.append(book)
        return matching_books

    def list_books(self):
        for book in self.library_list:
            print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

    def categorize_books(self):
        for genre, books in self.genre_dict.items():
            print(f"Genre: {genre}")
            for book in books:
                print(f"Title: {book[0]}, Author: {book[1]}")
            print()


def main():
    library = Library()

    while True:
        print("\n1. Add a book")
        print("2. Remove a book")
        print("3. Search for books")
        print("4. List all books")
        print("5. Categorize books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            book = library.add_book(title, author, genre)
            library.add_to_library(book)
            print("Book added to library.")

        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_from_library(title)
            print("Book removed from library.")

        elif choice == '3':
            search_term = input("Enter the title or author to search: ")
            search_results = library.search_books(search_term)
            print("Search Results:")
            for book in search_results:
                print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

        elif choice == '4':
            print("\nAll Books in the Library:")
            library.list_books()

        elif choice == '5':
            print("\nCategorized Books:")
            library.categorize_books()

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
