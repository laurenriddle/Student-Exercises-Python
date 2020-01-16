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
Joe.slack_handle = "JoeShep"
Joe.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Joe.specialty = "Python"
Cohort_36.add_instructor(Joe)

Jisie = Instructor()
Jisie.first_name = "Jisie"
Jisie.last_name = "David"
Jisie.slack_handle = "JisieD"
Jisie.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Jisie.specialty = "Javascript"
Cohort_36.add_instructor(Jisie)


Rose = Instructor()
Rose.first_name = "Rose"
Rose.last_name = "W"
Rose.slack_handle = "RoseW"
Rose.cohort = "C36 - The most awesome cohort in the history of cohorts!"
Rose.specialty = "Javascript"
Cohort_36.add_instructor(Rose)

# Have each instructor assign 2 exercises to each of the students.
Rose.assign_student_exercise(Cori, MonkeyChicken)
Rose.assign_student_exercise(Cori, Cash_to_Coins)
Rose.assign_student_exercise(Christian, MonkeyChicken)
Rose.assign_student_exercise(Christian, Cash_to_Coins)
Rose.assign_student_exercise(Michelle, Cash_to_Coins)
Rose.assign_student_exercise(Michelle, MonkeyChicken)
Rose.assign_student_exercise(Matthew, Cash_to_Coins)
Rose.assign_student_exercise(Matthew, MonkeyChicken)
Rose.assign_student_exercise(Brant, Cash_to_Coins)
Rose.assign_student_exercise(Brant, MonkeyChicken)


Jisie.assign_student_exercise(Cori, Urban_Planner)
Jisie.assign_student_exercise(Cori, Coins_to_Cash)
Jisie.assign_student_exercise(Christian, Urban_Planner)
Jisie.assign_student_exercise(Christian, Coins_to_Cash)
Jisie.assign_student_exercise(Michelle, Coins_to_Cash)
Jisie.assign_student_exercise(Michelle, Urban_Planner)
Jisie.assign_student_exercise(Matthew, Coins_to_Cash)
Jisie.assign_student_exercise(Matthew, Urban_Planner)
Jisie.assign_student_exercise(Brant, Coins_to_Cash)
Jisie.assign_student_exercise(Brant, Urban_Planner)

Joe.assign_student_exercise(Cori, Urban_Planner)
Joe.assign_student_exercise(Cori, MonkeyChicken)
Joe.assign_student_exercise(Christian, Urban_Planner)
Joe.assign_student_exercise(Christian, MonkeyChicken)
Joe.assign_student_exercise(Michelle, MonkeyChicken)
Joe.assign_student_exercise(Michelle, Urban_Planner)
Joe.assign_student_exercise(Matthew, MonkeyChicken)
Joe.assign_student_exercise(Matthew, Urban_Planner)
Joe.assign_student_exercise(Brant, MonkeyChicken)
Joe.assign_student_exercise(Brant, Urban_Planner)

exercises = [Cash_to_Coins, MonkeyChicken, Coins_to_Cash, Urban_Planner]
students = [Cori, Christian, Matthew, Michelle, Brant]


for student in students:
    exercise_string = ""
   
    student_exercise = list(dict.fromkeys(student.exercise)) # removes duplicates from list
    for exercise in student_exercise[:-1]:
                # loops over the exercises list and puts all of them into a sentence except for the last one which will be accessed with student_exercise[-1].exercise_name

        exercise_string += f"{exercise.exercise_name}, "
    print(f"{student.first_name} is working on {exercise_string}and {student_exercise[-1].exercise_name}.")