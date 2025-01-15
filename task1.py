BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name="{self.name}", pages={self.pages})'

# Пример использования
#book = Book(1, 'Программирование на Python', 300)
#print(str(book))  # Вывод: Книга "Программирование на Python"
#print(repr(book)) # Вывод: Book(id_=1, name="Программирование на Python", pages=300)


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book.__str__())  # проверяем метод __str__

    print(list_books.__repr__())  # проверяем метод __repr__
