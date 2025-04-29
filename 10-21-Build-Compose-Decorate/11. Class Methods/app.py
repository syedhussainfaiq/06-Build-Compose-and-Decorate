class Book:
    # Class variable to keep track of total book
    total_books = 0


    def __init__(self, title, author):
        """Initialize the books's title and author """
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
            """Class method to increment the total book count."""
            cls.total_books += 1

    @classmethod
    def get_total_books(cls):
            """Class method to get the current total book count."""
            return cls.total_books
        
 # Example usage
if __name__ == "__main__":
    book1 = Book ("1984", "Georg Orwell")
    book2 = Book ("To Kill a Mockingbard", "Harper Lee")

    print(f"Total books: {Book.get_total_books()}")

        