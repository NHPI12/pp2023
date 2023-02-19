students = {}
courses = {}
marks = {}
def studentsInput():
    students_numb = int(input("Enter number of students in the class: "))
    for i in range(students_numb):
        id = input("Enter student ID")
        name = input("Enter student name")
        DOB = input("Enter date of birth")
        students[id] = {"name": name, "dob" :DOB}
def coursesInput():
    numb_courses = int(input("Enter number of courses: "))
    for i in range(numb_courses):
        course_id = input("Enter course  ID")
        course_name = input("Enter course name")
        courses[course_id] = {"name": course_name}
def marksInput():
    course_id = input("Enter course ID")
    course_name = input("Enter course name")
    courses[course_id] = {"name": course_name}
def coursesList():
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]('name')}")

def studentsList():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for id in students:
        if id in marks and course_id in marks[id]:
            print(f"{students[id]['name']}: {marks[id][course_id]}")
        else:
            print(f"{students[id]['name']}: ")



