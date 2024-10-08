class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        return (f'name: {self.full_name}\nage: {self.age}\nis_married: {self.is_married}')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks
    def average_rating(self):
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, age, is_married, experience,):
        super().__init__(full_name,age,is_married)
        self.experience = experience

    def salary_counter(self, base_salary):
        if self.experience > 3:
            bonus_experience = self.experience - 3
            bonus = self.base_salary * 0.05 * bonus_experience
            return base_salary + bonus
        else:
            return self.base_salary
teacher = Teacher('Нина Васильевна', 47, 'Да', 7)
print(f'ФИО: {teacher.full_name}\nВозраст: {teacher.age}\n'
      f'в браке/нет: {teacher.is_married}\nОпыт: {teacher.experience}'
      f' лет\nЗарплата: {teacher.salary_counter(teacher.base_salary)}')
def greate_students():
    student0 = Student('Ишенбеков Эржан', 16,'Нет',
                        {'Математика': 3, 'Биология': 5,'Физ-ра': 5,'Физика': 4})
    student1 = Student('Джээнбаев Алибек', 17, 'Нет',
                        {'Математика': 5,'Биология': 5,'Физ-ра': 5,'Физика': 5})
    student2 = Student('Тологонов Рамазан', 17, 'Нет',
                        {'Математика': 5,'Биология': 4,'Физ-ра': 3,'Физика': 3})
    student3 = Student('Туратбеков Гулмырза', 17, 'Нет',
                        {'Математика': 4, 'Биология': 5, 'Физ-ра': 3, 'Физика': 5})
    return [student0, student1,student2,student3]

students = greate_students()
for student in students:
    print(student.introduce_myself())
    for i ,j in student.marks.items():
        print(f'{i}: {j}')
    print(f'Средняя оценка: {student.average_rating()}')



