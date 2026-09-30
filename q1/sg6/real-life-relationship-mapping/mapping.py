class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = [] 

    def add_student(self, student):
        self.students.append(student)
        print(student.name + " has been added to " + self.course_name)

    def show_students(self):
        print("\nStudents in " + self.course_name + ":")
        for student in self.students:
            print("- " + student.name + " (ID: " + student.student_id + ")")


my_course = Course("Intro to Python")

student_list = [
    Student("Reign Canen", "2024-16-021"),
    Student("Hillari Legaspi", "2024-16-022"),
    Student("Natalie Yuag", "2024-16-023"),
    Student("Epple Zamoras", "2024-16-024"),
    Student("Jhane Gimolatan", "2024-16-025"),
]

for student in student_list:
    my_course.add_student(student)


my_course.show_students()