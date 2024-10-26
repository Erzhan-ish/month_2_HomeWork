import sqlite3


# connect = sqlite3.connect('HomeWork_8.db')
# cur = connect.cursor()

# cur.execute('''
#     create table if not exists countries(
#     id integer primary key autoincrement,
#     title text not null
#     )
# ''')

# cur.execute('''
#     create table if not exists cities(
#     id integer primary key autoincrement,
#     title text not null,
#     area float default 0,
#     country_id references countries(id)
#     )
# ''')

# cur.execute('''
#     create table if not exists students(
#     id integer primary key autoincrement,
#     first_name varchar(50) not null,
#     last_name varchar(50) not null,
#     sity_id references sities(id)
#     )
# ''')

def display_students(city_id):
    conn = sqlite3.connect('HomeWork_8.db')
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
            print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет учеников в выбранном городе.")

    conn.close()


def main():
    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    conn = sqlite3.connect('HomeWork_8.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()

    for city in cities:
        print(f"{city[0]}: {city[1]}")

    while True:
        city_id = int(input("Введите id города: "))
        display_students(city_id)
        if city_id == 0:
            break

    conn.close()


if __name__ == "__main__":
    main()