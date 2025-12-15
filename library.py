import json
import os
from datetime import datetime

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self):
        book_id = len(self.books) + 1
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        added_on = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "added_on": added_on
        })

        self.save_books()
        print("Book added successfully")

    def search_book(self):
        title = input("Enter book title to search: ")
        for book in self.books:
            if book["title"].lower() == title.lower():
                print("📘 Book Found:")
                print(book)
                return
        print(" Book not found")

    def remove_book(self):
        book_id = int(input("Enter book ID to remove: "))
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                self.save_books()
                print(" Book removed successfully")
                return
        print("Book not found")

    def show_all_books(self):
        if not self.books:
            print("📂 No books in library")
            return

        print("\n📚 All Books in Library:")
        for book in self.books:
            print(
                f"ID: {book.get('id', 'N/A')} | "
                f"Title: {book['title']} | "
                f"Author: {book['author']} | "
                f"Added On: {book.get('added_on', 'N/A')}"
            )

    def menu(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Add Book")
            print("2. Search Book")
            print("3. Remove Book")
            print("4. Show All Books")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.search_book()
            elif choice == "3":
                self.remove_book()
            elif choice == "4":
                self.show_all_books()
            elif choice == "5":
                print(" Exiting Library System")
                break
            else:
                print(" Invalid choice")

library = Library()
library.menu()
