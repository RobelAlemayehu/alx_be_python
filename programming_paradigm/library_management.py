class Book:
    def __init__(self, title, author):
        
        self.title = title                
        self.author = author              
        self._is_checked_out = False      

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f'"{self.title}" has been checked out.'
        return f'"{self.title}" is already checked out.'

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f'"{self.title}" has been returned.'
        return f'"{self.title}" was not checked out.'

    def is_checked_out(self):
        return self._is_checked_out

    def __str__(self):
        status = "Checked out" if self._is_checked_out else "Available"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self._books = []  
        
    def add_book(self, book):
        self._books.append(book)
        return f'Added "{book.title}" to the library.'

    def remove_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                return f'"{title}" has been removed from the library.'
        return f'"{title}" not found in the library.'

    def list_available_books(self):
        available = [book for book in self._books if not book.is_checked_out()]
        if not available:
            return "No available books at the moment."
        return "\n".join(str(book) for book in available)

    def find_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
