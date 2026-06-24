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


# TODO Импортируйте и скопируйте ранее написанный класс Book
import importlib.util
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
target_file_path = os.path.join(project_root, "Класс Book", "main.py")

spec = importlib.util.spec_from_file_location("books_module", target_file_path)
books_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(books_main)

Book = books_main.Book

class Library:
    def __init__(self, books=None):
        """
        Не забудьте про 'Конструктор должен принимать необязательный аргумент со значением по умолчанию. Если пользователь
        его не передал, то библиотека инициализируется с пустым списком книг.'
        :param books:
        """
        # TODO дописать метод
        self.books = books if books is not None else []

    def get_next_book_id(self) -> str:
        """
        Необходимо узнать последнюю книгу в библиотеке, посмотреть атрибут 'id' этой книги и вернуть следующее
        значение после этого `id`
        :return:
        """
        # TODO дописать метод
        if not self.books:
            return "1"
        all_id = []
        for book in self.books:
            all_id.append(book.id_)
        all_id = sorted(all_id)

        return str(all_id[-1] + 1)

    def get_index_by_book_id(self, id_) -> int:
        """
        Так как в библиотеке книги хранятся в списке, то данная функция возвращает индекс где книга с определенным
        `id` хранится в списке книг. Для примера. [Book(id=1, ...), Book(id=2, ...)] книга с id=2 хранится
        на индексе 1 списка книг
        :param id_: id книги
        :return: индекс, где лежит книга в списке книг
        """
        # TODO дописать метод
        inx_ = 0
        for book in self.books:
            if book.id_ == id_:
               return inx_
            inx_ += 1

        raise ValueError ("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    try:
        print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    except ValueError as e:
        print(e)
