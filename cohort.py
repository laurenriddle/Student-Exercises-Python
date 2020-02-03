'''
You must define a type for representing a cohort in code.

The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
The collection of students in the cohort.
The collection of instructors in the cohort.
'''
class Cohort: 
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []

    def add_student(self, name):
        self.students.append(name)
    def add_instructor(self, name):
        self.instructors.append(name)
