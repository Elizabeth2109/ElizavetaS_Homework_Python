from book import Book

library = [
    Book("Евгений Онегин", "Александр Пушкин"),
    Book("Отцы и дети", "Иван Тургенев"),
    Book("Мертвые души", "Николай Гоголь"),
]

for book in library:
    print(f"{book.title} - {book.author}")
