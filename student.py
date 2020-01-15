'''
You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

Properties
First name
Last name
Slack handle
The student's cohort
The collection of exercises that the student is currently working on

'''
class Student: 
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.slack_handle = ""
        self.cohort = ""
        self.exercises = []
