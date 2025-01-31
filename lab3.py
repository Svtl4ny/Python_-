class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f'Number of pages must be an integer, got {value.__class__.__name__}')
        if value <= 0:
            raise ValueError('Number of pages must be a positive integer.')
        self._pages = value

    def __str__(self):
        return f'{super().__str__()}, {self.pages} pages'

    def __repr__(self):
        return f'PaperBook(name={self.name!r}, author={self.author!r}, pages={self.pages!r})'

class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise ValueError(f'Duration must be a float, got {value.__class__.__name__}')
        if value <= 0:
            raise ValueError('Duration must be a positive number.')
        self._duration = float(value)

    def __str__(self):
        return f'{super().__str__()}, duration: {self.duration:.2f} hours'

    def __repr__(self):
        return f'AudioBook(name={self.name!r}, author={self.author!r}, duration={self.duration!r})'
