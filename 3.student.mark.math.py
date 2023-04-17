import math
import numpy as np
import curses
from curses import wrapper
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
            print(f"Name: {Students[a].name}- ID: {Students[a].id} - Mark: {math.floor(self.marks[a])}")

#Function input number of students
def InputNumbStudent(stdscr):
    stdscr.clear()
    stdscr.addstr("Input number of students")
    stdscr.refresh()
    numb_students = stdscr.getstr(4)
    numb_students = int(numb_students)
    return numb_students

#Function input students info
def InputStudents(numb_students,stdscr):
    stdscr.clear()
    for i in range(numb_students):
        stdscr.addstr("Enter a name")
        stdscr.refresh()
        name = stdscr.getstr(20)
        stdscr.addstr("Enter an ID")
        stdscr.refresh()
        id = stdscr.getstr(5)
        stdscr.addstr("Enter a date of birth")
        stdscr.refresh()
        dob = stdscr.getstr(20)
        Students.append(Student(name,id,dob))

#Function input number of courses
def InputNumbCourse(stdscr):
    stdscr.clear()
    stdscr.addstr("Input number of courses")
    stdscr.refresh()
    numb_courses = stdscr.getstr(4)
    numb_courses = int(numb_courses)
    return numb_courses

#Function input course info
def InputCourses(numb_course,stdscr):
    stdscr.clear()
    for i in range(numb_course):
        stdscr.addstr("Enter a course name")
        stdscr.refresh()
        name = stdscr.getstr(20)
        stdscr.addstr("Enter an ID")
        stdscr.refresh()
        id = stdscr.getstr(5)
        Courses.append(Course(name,id))

#Function input students' marks of a course
def InputMarks(numb_students,stdscr):
    stdscr.clear()
    stdscr.addstr("Enter a course's name: ")
    stdscr.refresh()
    course_name = stdscr.getstr(20)
    for k in range(len(Courses)):
        if Courses[k].name == course_name :
            for i in range(numb_students):
                stdscr.addstr(f"Enter student {Students[i].name}'s mark: ")
                stdscr.refresh()
                mark = stdscr.getstr(3)
                mark = float(mark)
                Courses[k].marks.append(mark)

#Function list students' info
def ListStudents(stdscr):
    stdscr.clear()
    for i in range(len(Students)):
        stdscr.addstr(Students[i])
        stdscr.refresh()

#Function list courses' info
def ListCourses(stdscr):
    stdscr.clear()
    for i in range(len(Courses)):
        stdscr.addstr(Courses[i])
        stdscr.refresh()

#Function list marks of a course
def ListMarks(numb_student,stdscr):
    stdscr.clear()
    stdscr.addstr("Enter Courses's name: ")
    stdscr.refresh()
    course_name = stdscr.getstr(20)
    for k in range(len(Courses)):
        if Courses[k].name == course_name:
            for a in range(numb_student):
                Courses[k].show_mark(a)

#Function calculate GPA
GPAs = []
def CalGPA(numb_student):
    
    for i in range(numb_student):
        Gpa = 0
        for k in range(len(Courses)):
            Gpa = Gpa + Courses[k].marks[i]
        Gpa = Gpa/len(Courses)
        GPAs.append(Gpa) 

#Function show GPA
def ShowGPA():
    for i in range(len(GPAs)):
        print(GPAs[i])


def main(stdscr):
    n = InputNumbStudent(stdscr)
    InputStudents(n,stdscr)
    ListStudents(stdscr)
    a = InputNumbCourse(stdscr)
    InputCourses(a,stdscr)
    ListCourses(stdscr)
    InputMarks(n,stdscr)
    ListMarks(n,stdscr)
    #CalGPA(n)
    #ShowGPA()
#main program
wrapper(main)




