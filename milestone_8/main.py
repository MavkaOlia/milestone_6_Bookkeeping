from book import Book
from catalog_manager import organize, sort

def main():
    book1 = Book("The Great Gatsby", "Fiction", "F. Scott Fitzgerald", 1925)
    book2 = Book("To Kill a Mockingbird", "Fiction", "Harper Lee", 1960)
    book3 = Book("The Art of Computer Programming", "Computer Science", "Donald Knuth", 1968)
    book4 = Book("Introduction to Algorithms", "Computer Science", "Thomas H. Cormen", 1990)

    books = [book1, book2, book3, book4]
    shelves = organize(books)

    sort(shelves)

    for shelf in shelves:
        print(f"{shelf.name} Shelf:")
        for book in shelf.books:
            print(f"  - {book}")

if __name__ == "__main__":
    main()
