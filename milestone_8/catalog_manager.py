from shelf import Shelf

def organize(books):
    shelves = {}
    for book in books:
        if book.category not in shelves:
            shelves[book.category] = Shelf(book.category)
        shelves[book.category].add_book(book)

    return list(shelves.values())

def sort(shelves):
    for shelf in shelves:
        shelf.sort_books()
