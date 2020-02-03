import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/laurenriddle/workspace/python/book-one/student-exercises/studentexercises.db"

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[5])

        

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_student
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Name
            from Student s
            join Cohort c on s.Cohort_Id = c.Id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(f'{student.first_name} {student.last_name} is a student in {student.cohort}. Their Slack handle is {student.slack_handle}.')

    def create_instructor(self, cursor, row):
        
        # Change row 4!!!!
        return Instructor(row[4], row[1], row[2], row[3], row[5])


    def all_instructors(self):
        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_instructor
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.First_Name,
                i.Last_Name,
                i.Slack_Handle,
                i.Cohort_Id,
                c.Name
            from Instructor i
            join Cohort c on i.Cohort_Id = c.Id
            order by i.Cohort_Id
            """)

            all_Instructors = db_cursor.fetchall()

            for instructor in all_Instructors:
                    print(f'{instructor.first_name} {instructor.last_name} is an instructor in {instructor.cohort}. Their slack handle is {instructor.slack_handle}.')


    def create_cohort(self, cursor, row):
        return Cohort(row[1])


    def all_cohorts(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_cohort
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_Cohorts = db_cursor.fetchall()

            for cohort in all_Cohorts:
                print(f'This is {cohort.name}. We are awesome!')

    def create_exercise(self, cursor, row):
        return Exercise(row[1], row[2])


    def all_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_exercise 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.language
            from Exercise e
            """)

            all_Exercises = db_cursor.fetchall()

            for exercise in all_Exercises:
                    print(f'This exercise is called {exercise.exercise_name}. It is written in {exercise.language}.')

reports = StudentExerciseReports()
reports.all_students()
reports.all_instructors()
reports.all_cohorts()
reports.all_exercises()