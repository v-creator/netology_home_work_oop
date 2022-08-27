

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = float()

    def calculation(students, course):
        for student in students:
            result = float(sum(student.grades.get(course)) / len(student.grades.get(course)))
            student.average_grades = result

    # def

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grades}'
        return result


petrov = Student('Сергей', 'Петров', 'Мужчина')
petrov.courses_in_progress += ['Python']
ivanov = Student('Влад', 'Иванов', 'Мужчина')
ivanov.courses_in_progress += ['Python']


petrov.grades = {'Python': [10,9], 'ООП': [5,4,4,6,7]}
ivanov.grades = {'Python': [8,7], 'ООП': [9,3,3]}


print(petrov.grades)
print(ivanov.grades)
Student.calculation([petrov,ivanov], 'ООП')
print(petrov)
print(ivanov)