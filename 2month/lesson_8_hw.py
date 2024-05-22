import sqlite3


def create_database():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Создание таблицы countries
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
    ''')

    # Вставка записей в таблицу countries
    countries = [('Киргизия',), ('Германия',), ('Китай',)]
    cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)

    # Создание таблицы cities
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    )
    ''')

    # Вставка записей в таблицу cities
    cities = [
        ('Бишкек', 127, 1),
        ('Ош', 182, 1),
        ('Берлин', 891, 2),
        ('Гамбург', 755, 2),
        ('Пекин', 16410, 3),
        ('Шанхай', 6340, 3),
        ('Гуанчжоу', 7434, 3)
    ]
    cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)

    # Создание таблицы students
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities (id)
    )
    ''')

    # Вставка записей в таблицу students
    students = [
        ('Айбек', 'Иманов', 1),
        ('Салтанат', 'Жунусова', 1),
        ('Эрлан', 'Беков', 2),
        ('Зарина', 'Калыкова', 2),
        ('Ганс', 'Мюллер', 3),
        ('Анна', 'Шмитт', 3),
        ('Юлия', 'Браун', 4),
        ('Филипп', 'Шульц', 4),
        ('Ли', 'Вэй', 5),
        ('Чжан', 'Вэй', 5),
        ('Ван', 'Ли', 6),
        ('Чен', 'Ли', 6),
        ('Лю', 'Мин', 7),
        ('Фэн', 'Чжао', 7),
        ('Лин', 'Чен', 7)
    ]
    cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', students)

    conn.commit()
    conn.close()


def display_students(city_id):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (city_id,))

    students = cursor.fetchall()

    if students:
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет учеников в выбранном городе.")

    conn.close()


def main():
    create_database()

    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    for city in cities:
        print(f"{city[0]}: {city[1]}")

    while True:
        city_id = int(input("\nВведите id города: "))

        if city_id == 0:
            break

        display_students(city_id)


if __name__ == '__main__':
    main()
