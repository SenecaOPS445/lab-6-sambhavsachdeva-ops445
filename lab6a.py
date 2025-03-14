#!/usr/bin/env python3
# Author ID: ssachdeva25


class Student:

    # Define the name and number when a student object is created, ex. student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)
        self.courses = {}

 
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if not self.courses or all(self.courses[course] == 0.0 for course in self.courses):  
            return 'GPA of student ' + self.name + ' is 0.0'
        
        Grades_Total = 0.0
        i = 0
        for course in self.courses:
            Grades_Total += self.courses[course]
            i += 1
        
        return 'GPA of student ' + self.name + ' is ' + str(Grades_Total / i)
       

   
    def displayCourses(self):
        listOfCourses = []
        for course, grade in self.courses.items():
            if grade > 0.0:
                listOfCourses.append(course)
        
        return listOfCourses  
if __name__ == '__main__':

    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)


    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())