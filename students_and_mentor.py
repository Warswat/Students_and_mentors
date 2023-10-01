class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        Student.all_students.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def rate_lecture(self,lecturer,course,grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    def avg_grade(self):
        grade_sum = 0
        avg = 0
        grade_count = 0
        for course,grade in self.grades.items():
            grade_sum += sum(grade)
            grade_count += len(grade)
        avg = grade_sum/grade_count
        return round(avg,1)

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self,name, surname):
        super().__init__(name, surname)
        Lecturer.all_lecturers.append(self)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}"

    def avg_grade(self):
        grade_sum = 0
        avg = 0
        grade_count = 0
        for course,grade in self.grades.items():
            grade_sum += sum(grade)
            grade_count += len(grade)
        avg = grade_sum/grade_count
        return round(avg,1)

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def avg_hw_grade(course):
    grade_sum = 0
    avg = 0
    grade_count = 0

    for student in Student.all_students:
        if course in student.grades:
            grade_sum += sum(student.grades[course])
            grade_count += len(student.grades[course])
            avg = grade_sum/grade_count
    if avg == 0:
        print("По данному курсу нет оценок")
    else:
        print(f'Средняя оценка по курсу: {round(avg,1)}')


def avg_lecturer_grade(course):
    grade_sum = 0
    avg = 0
    grade_count = 0

    for lecturer in Lecturer.all_lecturers:
        if course in lecturer.grades:
            grade_sum += sum(lecturer.grades[course])
            grade_count += len(lecturer.grades[course])
            avg = grade_sum / grade_count
    if avg == 0:
        print("По данному курсу нет оценок")
    else:
        print(f'Средняя оценка по курсу: {round(avg,1)}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
worst_student = Student('Beorn', 'German', 'your_gender')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Java']

best_lecturer = Lecturer('Ry', 'Emen')
best_lecturer.courses_attached += ['Python']
some_lecturer = Lecturer('Bob','Alen')
some_lecturer.courses_attached += ['Java']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
bad_mentor = Reviewer('Dave','Joe')
bad_mentor.courses_attached += ['Java']

best_student.rate_lecture(best_lecturer,'Python',9)
best_student.rate_lecture(best_lecturer,'Python',10)
best_student.rate_lecture(best_lecturer,'Python',6)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(worst_student, 'Python', 9)
cool_mentor.rate_hw(worst_student, 'Python', 4)
cool_mentor.rate_hw(worst_student, 'Python', 7)
cool_mentor.rate_hw(worst_student, 'Python', 5)

print(best_lecturer)
print(best_student)
print(best_student<worst_student)
avg_hw_grade('Java')
avg_hw_grade('Python')
avg_lecturer_grade('Python')