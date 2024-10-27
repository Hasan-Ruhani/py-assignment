
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        self.display_person_info()
        print(f"Studnet ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'No courses enrolled'}")
        print(f"Grades: {self.grades if self.grades else 'No grades assigned'}")


class Course: 
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.student = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print(f"Enrolled Student: {', '.join([student.name for student in self.students]) if self.students else 'No students enrolled'}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        name: input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student{name} (ID: {student_id} added successfully...")

    def add_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code) {course_code} created witth instructor {instructor}.")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID")
        course_code = input("Enter Course Code")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: j{course_code}).")
        else:
            print("Invalid Student ID or Course Code.")

    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        if(student_id in self.students and course_code in self.courses):
            student = self.students[student_id]
            course = self.courses[course_code]
            if course.course_name in student.courses:
                grade = input(f"Enter Grade for {course.course_name}: ")
                student.add_grade(course.course_name, grade)
                print(f"Grade {grade} added for {student.name} in {course.course_name}.")
            else:
                print(f"Student {student.name} is not enrolled in {course.course_name}.")
        else:
            print("Invalid Student ID or Course Code.")

        
