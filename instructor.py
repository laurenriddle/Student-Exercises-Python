'''
You must define a type for representing an instructor in code.

First name
Last name
Slack handle
The instructor's cohort
The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
A method to assign an exercise to a student
'''
class Instructor:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.slack_handle = ""
        self.cohort = ""
        self.specialty = ""
    
    def assign_student_exercise(self, student, exercise):
        student.exercise.append(exercise)