from numpy.ma.core import append


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
        self.course_average_grade = 0.00
        self.all_course_grades = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            lecturer.average_grade = sum(lecturer.grades[course]) / len(lecturer.grades[course])
            all_grades = []
            for g in lecturer.grades.values():
                all_grades += g
            lecturer.average_grade = sum(all_grades) / len(all_grades)
        else:
            return 'Ошибка'

    # def rate_course_students(self, students = [], course):
    #     for student in students:
    #         if course in self.courses_in_progress:
    #             self.all_course_grades += self.grades[course]
    #     self.course_average_grade = sum(self.all_course_grades) / len(self.all_course_grades)


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_grade = 0

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)




    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade}')




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            all_grades = []
            for g in student.grades.values():
                all_grades += g
            student.average_grade = sum(all_grades) / len(all_grades)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

#Task #3

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Василий', 'Головкин')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Матвей', 'Попович')
student_1 = Student('Ольга', 'Алёхина', 'Ж')
student_2 = Student('Алехандро', 'Аллерандро', 'М')

lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Python', 'Java']
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python', 'Java']
reviewer_1.courses_attached += ['Python', 'Java']
reviewer_2.courses_attached += ['Python', 'Full-stack']

student_1.rate_lecturer(lecturer_1, 'Python', 3)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'C++', 3)
student_1.rate_lecturer(lecturer_2, 'Python', 2)
student_2.rate_lecturer(lecturer_2, 'Python', 9)

reviewer_1.rate_student(student_1, 'Python', 7)
reviewer_2.rate_student(student_1, 'Python', 8)
reviewer_1.rate_student(student_2, 'Python', 9)
reviewer_2.rate_student(student_2, 'Python', 7)

print(lecturer_1)
# print(lecturer_2)
# print(student_1)
# print(student_2)
# print(lecturer_1 == lecturer_2)
# print(lecturer_1 > lecturer_2)
# print(lecturer_1 < lecturer_2)
# print(student_1 == student_2)
# print(student_1 > student_2)
# print(student_1 < student_2)

print(lecturer_1.grades.values())








# lecturer = Lecturer('Пётр', 'Петров', 'Python')
# print(lecturer)
# Task #2
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
#
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
#
# print(student.rate_lecture(lecturer, 'Python', 7))  # None
# print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
#
# print(lecturer.grades)  # {'Python': [7]}

#Task #1
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)    # []

#0
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)