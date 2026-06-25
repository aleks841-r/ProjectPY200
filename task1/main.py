class Book:
    """ Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """ Атрибут name. Только для чтения."""
        return self._name

    @property
    def author(self) -> str:
        """ Атрибут author. Только для чтения."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """Атрибут pages, ограничения по типу и допустимым значениям."""
        if not isinstance(pages, int) or isinstance(pages, bool) :
            raise TypeError(f"\n[!!!] Ошибка. Количество страниц должно быть целым числом!\n")

        if pages <= 0:
            raise ValueError(f"\n[!!!] Ошибка. Количество страниц должно быть больше нуля!\n")

        super().__init__(name, author)

        self._name = name
        self._author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return self.__str__()


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """Атрибут duration, ограничения по типу и допустимым значениям."""
        if not isinstance(duration, float):
            raise TypeError(f"\n[!!!] Ошибка. Продолжительность аудиокниги должна быть числом с плавающей запятой!\n")

        if duration <= 0:
            raise ValueError(f"\n[!!!] Ошибка. Продолжительность аудиокниги должна быть больше нуля!\n")

        super().__init__(name, author)

        self._name = name
        self._author = author
        self.duration = duration

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return self.__str__()


def main():
    # Базы данных книг для проверки
    AUDIOBOOKS_DATABASE = [
        {
            "name": "book1",
            "author": "author1",
            "duration": 20.0,
        },
        {
            "name": "book2",
            "author": "author1",
            "duration": 40.5,
        },
        {
            "name": "book3",
            "author": "author2",
            "duration": 30.8,
        }
    ]

    BOOKS_DATABASE = [
        {
            "name": "book1",
            "author": "author1",
            "pages": 200,
        },
        {
            "name": "book4",
            "author": "author3",
            "pages": 400,
        }
    ]

    try:
        paper_books = [
            PaperBook(name=book_dict["name"], author=book_dict["author"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
        ]
        audio_books = [
            AudioBook(name=book_dict["name"], author=book_dict["author"], duration=book_dict["duration"]) for book_dict in AUDIOBOOKS_DATABASE
        ]
        print(paper_books)
        print(audio_books)
        print(PaperBook(name="Незнайка", author="Н.Носов", pages=700.0))
        #print(PaperBook(name="Незнайка", author="Н.Носов", pages=-700))
        #print(AudioBook(name="Незнайка", author="Н.Носов", duration=-700.0))
        #print(AudioBook(name="Незнайка", author="Н.Носов", duration=700))
    except (TypeError, ValueError) as error:
        print(error)

if __name__ == "__main__":
    main()