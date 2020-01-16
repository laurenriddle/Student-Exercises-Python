from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

'''
Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

Create 4, or more, exercises.
Create 3, or more, cohorts.
Create 4, or more, students and assign them to one of the cohorts.
Create 3, or more, instructors and assign them to one of the cohorts.
Have each instructor assign 2 exercises to each of the students.

'''


# Create 4, or more, exercises.
MonkeyChicken = Exercise()
MonkeyChicken.exercise_name = "MonkeyChicken"
MonkeyChicken.language = "Python"

Coins_to_Cash = Exercise()
Coins_to_Cash.exercise_name = "Coins to Cash"
Coins_to_Cash.language = "Python"

Cash_to_Coins = Exercise()
Cash_to_Coins.exercise_name = "Cash to Coins"
Cash_to_Coins.language = "Python"

Urban_Planner = Exercise()
Urban_Planner.exercise_name = "Urban Planner"
Urban_Planner.language = "Python"

Pizza_Joint = Exercise()
Pizza_Joint.exercise_name = "Pizza Joint"
Pizza_Joint.language = "Python"


# Create 3, or more, cohorts.
Cohort_36 = Cohort()
Cohort_36.name = "C36 - The most awesome cohort in the history of cohorts!"

Cohort_35 = Cohort()
Cohort_35.name = "C35"

Cohort_39 = Cohort()
Cohort_39.name = "C39 - The second most awesome cohort in the history of cohorts!"

# Create 4, or more, students and assign them to one of the cohorts.

Cori = Student()
Cori.first_name = "Cori"
Cori.last_name = "Golden"
Cori.slack_handle = "Cori G."
Cori.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Cohort_36.add_student(Cori)

Christian = Student()
Christian.first_name = "Christian"
Christian.last_name = "Pippin"
Christian.slack_handle = "Christian P."
Christian.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Cohort_36.add_student(Christian)

Michelle = Student()
Michelle.first_name = "Michelle"
Michelle.last_name = "Johnson"
Michelle.slack_handle = "Michelle J."
Michelle.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Cohort_36.add_student(Michelle)

Matthew = Student()
Matthew.first_name = "Matthew"
Matthew.last_name = "Blagg"
Matthew.slack_handle = "Matthew B."
Matthew.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Cohort_36.add_student(Matthew)

Brant = Student()
Brant.first_name = "Brant"
Brant.last_name = "Pippin"
Brant.slack_handle = "Brant P."
Brant.cohort = "C39 - The second most awesome cohort in the history of cohorts!"
Cohort_39.add_student(Brant)



# Create 3, or more, instructors and assign them to one of the cohorts.

Joe = Instructor()
Joe.first_name = "Joe"
Joe.last_name = "Shepherd"
Joe.slack_handle "JoeShep"
Joe.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Joe.specialty = "Python"
Cohort_36.add_instructor(Joe)

Jisie = Instructor()
Jisie.first_name = "Jisie"
Jisie.last_name = "David"
Jisie.slack_handle "JisieD"
Jisie.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Jisie.specialty = "Javascript"
Cohort_36.add_instructor(Jisie)


Rose = Instructor()
Rose.first_name = "Rose"
Rose.last_name = "W"
Rose.slack_handle "RoseW"
Rose.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Rose.specialty = "Javascript"
Cohort_36.add_instructor(Rose)

# Have each instructor assign 2 exercises to each of the students.


