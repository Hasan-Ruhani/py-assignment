import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
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
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'No courses enrolled'}")
        print(f"Grades: {self.grades if self.grades else 'No grades assigned'}")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join([student.name for student in self.students]) if self.students else 'No students enrolled'}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid Student ID or Course Code.")

    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        if student_id in self.students and course_code in self.courses:
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

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            student.display_student_info()
        else:
            print("Student not found.")

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        if course_code in self.courses:
            course = self.courses[course_code]
            course.display_course_info()
        else:
            print("Course not found.")

    def save_data(self):
        data = {
            "students": {student_id: student.__dict__ for student_id, student in self.students.items()},
            "courses": {course_code: course.__dict__ for course_code, course in self.courses.items()}
        }
        with open("data.json", "w") as f:
            json.dump(data, f)
        print("All student and course data saved successfully.")

    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
            self.students = {
                student_id: Student(**student_data)
                for student_id, student_data in data["students"].items()
            }
            self.courses = {
                course_code: Course(**course_data)
                for course_code, course_data in data["courses"].items()
            }
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No data file found.")

    def main_menu(self):
        while True:
            print("\n==== Student Management System ====")
            print("1. Add New Student")
            print("2. Add New Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade for Student")
            print("5. Display Student Details")
            print("6. Display Course Details")
            print("7. Save Data to File")
            print("8. Load Data from File")
            print("0. Exit")
            option = input("Select Option: ")

            if option == '1':
                self.add_student()
            elif option == '2':
                self.add_course()
            elif option == '3':
                self.enroll_student_in_course()
            elif option == '4':
                self.add_grade_for_student()
            elif option == '5':
                self.display_student_details()
            elif option == '6':
                self.display_course_details()
            elif option == '7':
                self.save_data()
            elif option == '8':
                self.load_data()
            elif option == '0':
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")



if __name__ == "__main__":
    system = StudentManagementSystem()
    system.main_menu()
