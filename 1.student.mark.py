#data lists
students = []
courses = []
marks = []
mark_course = []

#function input number of students
def input_students_number():
    numb_students = int(input("Input number of students "))
    return numb_students

#function input student's info
def input_students_info(numb_students):
    for i in range(numb_students):
        student_id = int(input("Enter student's ID "))
        student_name = input("Enter student's name ")
        student_dob = input("Enter student's Date of birth ")
        student_info = {"ID ":student_id, "Name ":student_name, "Date of birth: ":student_dob}
        students.append(student_info)

#function input number of courses
def input_courses_number():
    numb_courses = int(input("Input number of courses "))
    return numb_courses

#function input course's info
def input_course_info(numb_courses):
    for i in range (numb_courses):
        course_id = int(input("Input course's ID "))
        course_name = input("Inpur course's name ")
        course_info = {"ID: ": course_id, "Name: " : course_name}
        courses.append(course_info)

#function input marks
def input_marks_courses(numb_students):
    course_name = input("Enter courses name: ")
    for i in range(numb_students):
        mark = int(input(f'Enter student {students[i]["Name "]} Mark'))
        mark_info = {"ID ": students[i]["ID "], "Name: ": students[i]["Name "],"Course ": course_name, "Mark": mark}
        marks.append(mark_info)
        
#function list students
def students_list():
    for i in range(len(students)):
        print(students[i])
#function list courses
def courses_list():
    for i in range(len(courses)):
        print(courses[i])

#function show courses mark
def show_courses_mark():
    for i in range(len(marks)):
        print(marks[i])
# main program

# student's info input
numb_students = input_students_number()
input_students_info(numb_students)

# course's info input
numb_courses = input_courses_number()
input_course_info(numb_courses)

#input courses marks
input_marks_courses(numb_students)
