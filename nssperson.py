# Find any common properties and/or behaviors on students and instructors and create a new parent class for both of them to inherit from.
class NSSPerson():
    def __init__(self, first, last, handle, cohort):
    # What common properties will go here?
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort