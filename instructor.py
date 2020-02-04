'''
You must define a type for representing an instructor in code.

First name
Last name
Slack handle
The instructor's cohort
The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
A method to assign an exercise to a student
'''
from nssperson import NSSPerson
class Instructor(NSSPerson):
    def __init__(self, specialty, first, last, handle, cohort):
        super().__init__(first, last, handle, cohort)        
        self.specialty = ""
    
    def assign_student_exercise(self, student, exercise):
        student.exercise.append(exercise)
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is an instructor in {self.cohort}. Their Slack Handle is {self.slack_handle}.'