#Define lists
Students =[]
Courses= []

#Define class Student
class Student:
    def __init__(self, n,i,dob):
        self.name = n
        self.id = i
        self.DOB = dob
    def __str__(self):
        return f"Name: {self.name} - ID: {self.id} - Date of birth: {self.DOB}"

#Define class Course
class Course:
    def __init__(self, n,i):
        self.name = n
        self.id = i
        self.marks = []             #List to store marks
    def __str__(self):
        return f"{self.id} - {self.name}"
    def show_mark(self,a):
            print(f"Name: {Students[a].name}- ID: {Students[a].id} - Mark: {self.marks[a]}")

#Function input number of students
def InputNumbStudent():
    numb_students = int(input("Input number of students: "))
    return numb_students

#Function input students info
def InputStudents(numb_students):
    for i in range(numb_students):
        name = input("Enter a name ")
        id = input("Enter an ID ")
        dob = input("Enter a date of birth ")
        Students.append(Student(name,id,dob))

#Function input number of courses
def InputNumbCourse():
    numb_courses = int(input("Input number of courses"))
    return numb_courses

#Function input course info
def InputCourses(numb_course):
    for i in range(numb_course):
        name = input("Enter course name: ")
        id = input("Enter course ID ")
        Courses.append(Course(name,id))

#Function input students' marks of a course
def InputMarks(numb_students):
    course_name = input("Enter courses name: ")
    for k in range(len(Courses)):
        if Courses[k].name == course_name :
            for i in range(numb_students):
                mark = int(input(f"Enter student {Students[i].name}'s mark: "))
                Courses[k].marks.append(mark)

#Function list students' info
def ListStudents():
    for i in range(len(Students)):
        print(Students[i])

#Function list courses' info
def ListCourses():
    for i in range(len(Courses)):
        print(Courses[i])

#Function list marks of a course
def ListMarks(numb_student):
    course_name = input("Enter Course's name: ")
    for k in range(len(Courses)):
        if Courses[k].name == course_name:
            for a in range(numb_student):
                Courses[k].show_mark(a)


#main program
n = InputNumbStudent()
InputStudents(n)
ListStudents()
a = InputNumbCourse()
InputCourses(a)
ListCourses()
InputMarks(n)
ListMarks(n)



