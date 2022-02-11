class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_cources = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lectuer, course, grade):
        if isinstance(lectuer, Lectuer) and course in self.courses_in_progress and course in lectuer.courses_attached:
            if course in lectuer.grades:
                lectuer.grades[course] += [grade]
            else:
                lectuer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        avg_rate = 0
        count = 0
        for key, values in self.grades.items():
            avg_rate += float(sum(values)) / len(values)
            count += 1
        rate = avg_rate / count
        return rate

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Неверное сопоставление')
            return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредний балл за домашки: {round(self.average_rate(), 1)}\n"
                f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {','.join(self.finished_cources)}"
                )


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


class Lectuer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        avg_rate = 0
        count = 0
        for key, values in self.grades.items():
            avg_rate += float(sum(values)) / len(values)
            count += 1
        rate = avg_rate / count
        return rate

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредний балл за лекции {round(self.average_rate(), 1)}'

    def __lt__(self, other):
        if not isinstance(other, Lectuer):
            print('Неверное сопоставление')
            return
        return self.average_rate() < other.average_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def avg_rate_students(students, course):
    avg_rate = 0
    count = 0
    for student in students:
        if course == student.courses_in_progress:
            avg_rate += student.average_rate()
            count += 1
    if count == 0:
        print('Курс не найден')
    else:
        print(f'Средний балл всех студентов на курсе {" ".join(course)}: {round(avg_rate / count, 1)}')


def avg_rate_lectuers(lectuers, course):
    avg_rate = 0
    count = 0
    for lectuer in lectuers:
        if course == lectuer.courses_attached:
            avg_rate += lectuer.average_rate()
            count += 1
    if count == 0:
        print('Курс не найден')
    else:
        print(f'Средний балл всех лекторов на курсе {" ".join(course)}: {round(avg_rate / count, 1)}')


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

cool_student = Student('Biba', 'Boba', 'female')
cool_student.courses_in_progress += ['SQL']

cool_lectuer = Lectuer('Dude', 'Mark')
cool_lectuer.courses_attached += ['Python']

just_lectuer = Lectuer('Little', 'Pony')
just_lectuer.courses_attached += ['SQL']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

just_reviever = Reviewer('Bobba', 'Fet')
just_reviever.courses_attached += ['SQL']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

just_reviever.rate_hw(cool_student, 'SQL', 9)
just_reviever.rate_hw(cool_student, 'SQL', 8)
just_reviever.rate_hw(cool_student, 'SQL', 8)

best_student.rate_lecture(cool_lectuer, 'Python', 8)
best_student.rate_lecture(cool_lectuer, 'Python', 9)
best_student.rate_lecture(cool_lectuer, 'Python', 10)

cool_student.rate_lecture(just_lectuer, 'SQL', 8)
cool_student.rate_lecture(just_lectuer, 'SQL', 8)
cool_student.rate_lecture(just_lectuer, 'SQL', 7)

print(cool_lectuer)
print(just_lectuer)

print(cool_reviewer)
print(just_reviever)

print(best_student)
print(cool_student)

print(cool_lectuer.grades)
print(just_lectuer.grades)

print(best_student.grades)
print(cool_student.grades)

print(cool_lectuer > just_lectuer)
print(best_student > cool_student) 

students_list = [best_student, cool_student]
lectuers_list = [cool_lectuer, just_lectuer]
course_list = ['SQL']  # Мои списки для функций и название курса

avg_rate_students(students_list, course_list)

avg_rate_lectuers(lectuers_list, course_list)
