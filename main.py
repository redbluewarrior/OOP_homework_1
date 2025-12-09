class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}

#Task #1
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)    # []

#0
#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)