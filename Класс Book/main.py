# База данных книг для проверки
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


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        # TODO дописать метод
        """
        Инициализирует объект книга с атрибутами

        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге
        """

        if not isinstance(id_, int) or id_ == 0:
            raise TypeError(f"[!!!] ОШИБКА. Идентификатор книги должен быть целым числом!")

        if not isinstance(pages, int):
            raise TypeError(f"[!!!] ОШИБКА. Количество страниц книги должено быть целым числом!")

        self.id_ = id_
        self.name_ = name
        self.pages_ = pages

    def __str__(self) -> str:
        # TODO дописать метод
        """Возвращает строку заданного формата."""

        return f'Книга "{self.name_}"'

    def __repr__(self) -> str:
        # TODO дописать метод
        """Возвращает валидную python строку."""

        return f"Book(id_='{self.id_}', name='{self.name_}', pages='{self.pages_}')"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__