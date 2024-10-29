import sqlite3


connect = sqlite3.connect('HomeWork_8.db')
cur = connect.cursor()

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

def cit():
    connect = sqlite3.connect('HomeWork_8.db')
    cur = connect.cursor()
    cur.execute('''SELECT id, title FROM cities''')
    for row in cur.fetchall():
        print(f'{row[0]}: {row[1]}')
    connect.close()


def info_students(CityId):
    connect = sqlite3.connect('HomeWork_8.db')
    cur = connect.cursor()
    cur.execute('''
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area 
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (CityId,))

    students = cur.fetchall()
    if students:
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет учеников в этом городе.")
    connect.close()



cit()


while True:
    try:
        CityId = int(input(
            'Вы можете отобразить список учеников по выбранному id города из перечня городов выше, для выхода из программы введите 0: '))
        if CityId == 0:
            print("Выход из программы.")
            break
        info_students(CityId)
    except ValueError:
        print("Пожалуйста, введите корректное число.")
