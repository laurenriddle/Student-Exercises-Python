import sqlite3

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/laurenriddle/workspace/python/book-one/student-exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
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
                print(f'{student[1]} {student[2]} is a student in {student[5]}')


    def all_instructors(self):
        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
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

            for instuctor in all_Instructors:
                    print(f'{instuctor[1]} {instuctor[2]} is an instructor in {instuctor[5]}')

    def all_cohorts(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_Cohorts = db_cursor.fetchall()

            for cohort in all_Cohorts:
                    print(f'This is {cohort[1]}. We are awesome!')

    def all_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.language
            from Exercise e
            """)

            all_Exercises = db_cursor.fetchall()

            for exercise in all_Exercises:
                    print(f'This exercise is called {exercise[1]}. It is written in {exercise[2]}.')

reports = StudentExerciseReports()
reports.all_students()
reports.all_instructors()
reports.all_cohorts()
reports.all_exercises()