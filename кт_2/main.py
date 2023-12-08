import csv
import json


class User:
    def __init__(self, name, gender, address, age):
        """
        Инициализация объекта пользователя.

        Параметры:
        - name (str): Имя пользователя.
        - gender (str): Пол пользователя.
        - address (str): Адрес пользователя.
        - age (int): Возраст пользователя.
        """
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = []

    def add_book(self, title, author, pages, genre):
        """
        Добавляет информацию о книге в список книг пользователя.

        Параметры:
        - title (str): Название книги.
        - author (str): Автор книги.
        - pages (int): Количество страниц книги.
        - genre (str): Жанр книги.
        """
        self.books.append({
            'title': title,
            'author': author,
            'pages': pages,
            'genre': genre
        })


def read_json_users(file_path):
    """
    Читает данные о пользователях из JSON-файла.

    Параметры:
    - file_path (str): Путь к JSON-файлу.

    Возвращает:
    - list: Список объектов User.
    """
    users = []
    with open(file_path, "r") as file:
        extracted_users = json.load(file)
        for user_data in extracted_users:
            user = User(
                name=user_data['name'],
                gender=user_data['gender'],
                address=user_data['address'],
                age=user_data['age']
            )
            users.append(user)
    return users


def read_csv_books(file_path, users):
    """
    Читает данные о книгах из CSV-файла и обновляет информацию в объектах User.

    Параметры:
    - file_path (str): Путь к CSV-файлу.
    - users (list): Список объектов User.

    Возвращает:
    - None
    """
    with open(file_path, "r") as file:
        books = csv.DictReader(file)
        for i, book_data in enumerate(books):
            user_index = i % len(users)
            users[user_index].add_book(
                title=book_data['Title'],
                author=book_data['Author'],
                pages=book_data['Pages'],
                genre=book_data['Genre']
            )


def save_users_to_json(users):
    """
        Сохраняет данные о пользователях в JSON-файл.

        Параметры:
        - users (list): Список объектов User. Каждый объект User будет преобразован в словарь.
        - output_file (str): Имя выходного JSON-файла. По умолчанию используется 'result.json'.

        Возвращает:
        - None
        """
    with open('result.json', 'w') as file:
        # Преобразование каждого объекта User в словарь и сохранение в JSON-файл
        json.dump([vars(user) for user in users], file, indent=4)


def main():
    """
    Основная функция, выполняющая чтение данных и вывод результата.

    Параметры:
    - None

    Возвращает:
    - None
    """
    users = read_json_users("data/users.json")
    read_csv_books("data/books.csv", users)

    save_users_to_json(users)
    # pprint([vars(user) for user in users])  # Выводим атрибуты объектов User


if __name__ == "__main__":
    main()
