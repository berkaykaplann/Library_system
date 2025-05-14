from models.book import Book
from utils.helpers import load_data, save_data

class BookService:
    @staticmethod
    def add_book(title, author, total_copies):
        data = load_data()
        new_book = Book(title, author, total_copies)
        data["books"].append(new_book.to_dict())
        save_data(data)
        return new_book

    @staticmethod
    def get_book_by_id(book_id):
        data = load_data()
        for book in data["books"]:
            if book["id"] == book_id:
                return Book.from_dict(book)
        return None

    @staticmethod
    def list_books():
        data = load_data()
        books = data["books"]
        print("\n--- Kitap Listesi ---")
        for book in books:
            print(f"ID: {book['id']} | {book['title']} - {book['author']} "
                  f"({book['available_copies']}/{book['total_copies']} mevcut)")
        return books  # <-- DÖNDÜR!


