'''
1. Create a program that simulates a university course registration system. Consider the following requirements:
2. Courses: Define a Course class with attributes like course code, title, maximum capacity, current number of students enrolled, etc.
3. Students: Create a Student class with attributes such as student ID, name, courses enrolled, etc.
4. Registration Process: Implement methods to enroll students in courses, check available slots, display course details, display student information, etc.
5. Data Handling: Use file handling to read/write course information and student data. Courses and student data should be stored in separate files.
6. Validation: Ensure that the system prevents enrolling a student in a course that has reached its maximum capacity.
7. Driver file/main file: Test that your classes, methods, and data handling work successfully.
8. Extra things you can do: visualize the number of students in each course, GUI for the system, and many more.

'''


import json

class Course: # course class 
    def __init__(self, code, title, max_capacity, current_enrollment, students_enrolled):
        self.code = code
        self.title = title
        self.max_capacity = max_capacity
        self.current_enrollment = current_enrollment
        self.students_enrolled = students_enrolled

    def display_course_details(self):
        print(f"Course Code: {self.code}")
        print(f"Title: {self.title}")
        print(f"Max Capacity: {self.max_capacity}")
        print(f"Current Enrollment: {self.current_enrollment}")


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses_enrolled = []

    def display_student_info(self, courses):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Courses Enrolled:")
        for course_code in self.courses_enrolled:
            course = next((c for c in courses if c['code'] == course_code), None)
            if course:
                print(f"- {course['title']} ({course['code']})")
            else:
                print(f"- {course_code} (Course not found)")


class UniversitySystem:
    def __init__(self):
        self.courses = []
        self.students = []

    def load_data(self):
        try:
            with open('courses.json', 'r') as f:
                self.courses = json.load(f)
                # Convert loaded data to Course instances
                self.courses = [Course(**course) for course in self.courses]
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('courses.json', 'w') as f:
            json.dump(self.courses, f, indent=2)

        with open('students.json', 'w') as f:
            json.dump(self.students, f, indent=2)

    def enroll_student(self, student_id, course_code):
        student = next((s for s in self.students if s['student_id'] == student_id), None)
        course = next((c for c in self.courses if c['code'] == course_code), None)

        if student and course:
            if len(course['students_enrolled']) < course['max_capacity']:
                course['students_enrolled'].append(student_id)
                student['courses_enrolled'].append(course_code)
                course['current_enrollment'] += 1
                print(f"Enrollment successful for {student['name']} in {course['title']}.")
            else:
                print(f"Sorry, {course['title']} is full. Cannot enroll {student['name']}.")
        else:
            print("Student or course not found.")

    def display_courses(self):
        for course in self.courses:
            course.display_course_details()

    def display_students(self):
        for student in self.students:
            Student(**student).display_student_info(self.courses)



# Sample data
initial_courses = [
    {"code": "COMP88", "title": "Introduction to Computer Science", "max_capacity": 30, "current_enrollment": 0, "students_enrolled": []},
    {"code": "METH707", "title": "Calculus", "max_capacity": 25, "current_enrollment": 0, "students_enrolled": []},
    {"code": "PHYS101", "title": "Physics", "max_capacity": 20, "current_enrollment": 0, "students_enrolled": []},
]

initial_students = [
    {"student_id": "1001", "name": "Michelle", "courses_enrolled": []},
    {"student_id": "1002", "name": "Billie", "courses_enrolled": []},
    {"student_id": "1003", "name": "Dan", "courses_enrolled": []},
]

# Create UniversitySystem instance
university_system = UniversitySystem()

# Load initial data
university_system.courses = initial_courses
university_system.students = initial_students

# Driver code
university_system.load_data()

while True:
    print("\nUniversity Course Registration System")
    print("1. Display Courses")
    print("2. Display Students")
    print("3. Enroll Student")
    print("4. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        university_system.display_courses()
    elif choice == "2":
        university_system.display_students()
    elif choice == "3":
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        university_system.enroll_student(student_id, course_code)
    elif choice == "4":
        university_system.save_data()
        print("Data saved. Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")