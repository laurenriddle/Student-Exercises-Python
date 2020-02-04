import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/laurenriddle/workspace/python/book-one/student-exercises/studentexercises.db"

    # def create_student(self, cursor, row):
        # return Student(row[1], row[2], row[3], row[5])

        

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
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
                print(student)

    # def create_instructor(self, cursor, row):
        
        # Change row 4!!!!
        # return Instructor(row[4], row[1], row[2], row[3], row[5])


    def all_instructors(self):
        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[4], row[1], row[2], row[3], row[5])
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
                    print(instructor)


    # def create_cohort(self, cursor, row):
        # return Cohort(row[1])


    def all_cohorts(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_Cohorts = db_cursor.fetchall()

            for cohort in all_Cohorts:
                print(cohort)

    # def create_exercise(self, cursor, row):
        # return Exercise(row[1], row[2])


    def all_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.language
            from Exercise e
            """)

            all_Exercises = db_cursor.fetchall()

            for exercise in all_Exercises:
                    print(exercise)

    # def create_exercise(self, cursor, row):
        # print(f'{row[1]}, {row[2]}')

    def all_assignments(self):
        """Retrieve all exercises"""
        assignments = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Exercise_Id, 
            e.Name, 
            e.Language, 
            s.Id Student_Id, 
            s.First_Name, 
            s.Last_Name , 
            i.First_Name, 
            i.Last_Name from 
            Assignments a 
            JOIN Exercise e 
            ON a.Exercise_Id = e.Id 
            JOIN Student s
            ON a.Student_Id = s.Id
            JOIN Instructor i 
            ON a.Instructor_Id = i.Id
            """)

            all_Assigments = db_cursor.fetchall()

            for row in all_Assigments:
                # exercise_Id = row[0]
                exercise_name = row[1]
                # exercise_language = row[2]
                student_Id = row[3]
                student_name = f'{row[4]} {row[5]}'
                # instructor_name = f'{row[6]} {row[7]}

                if student_Id not in assignments:
                    assignments[student_Id] = {"name": student_name,
                    "exercises": [exercise_name] }
                else: 
                    assignments[student_Id]["exercises"].append(exercise_name)
            
            for student_Id, objects in assignments.items():
                print(f'{objects["name"]} is working on:')
                for object in objects["exercises"]:
                    print(f'\t* {object}')

    def all_instructor_assignments(self):
        """Retrieve all exercises"""
        assignments = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Exercise_Id, e.Name, i.First_Name, i.Last_Name, i.id
            FROM 
            Assignments a 
            JOIN Exercise e 
            ON a.Exercise_Id = e.Id 
            JOIN Instructor i 
            ON a.Instructor_Id = i.Id;
            """)

            all_Assigments = db_cursor.fetchall()

            for row in all_Assigments:
                # exercise_Id = row[0]
                exercise_name = row[1]
                # exercise_language = row[2]
                instructor_Id = row[4]
                instructor_name = f'{row[2]} {row[3]}'
                # instructor_name = f'{row[6]} {row[7]}

                if instructor_Id not in assignments:
                    assignments[instructor_Id] = {"name": instructor_name,
                    "exercises": {exercise_name} }
                else: 
                    assignments[instructor_Id]["exercises"].add(exercise_name)
            
            for instructor_Id, objects in assignments.items():
                print(f'{objects["name"]} has assigned:')
                for object in objects["exercises"]:
                    print(f'\t* {object}')

reports = StudentExerciseReports()
# reports.all_students()
# reports.all_instructors()
# reports.all_cohorts()
# reports.all_exercises()
# reports.all_assignments()
reports.all_instructor_assignments()