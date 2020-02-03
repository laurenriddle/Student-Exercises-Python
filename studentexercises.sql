-- DROP TABLE IF EXISTS Cohort;
-- DROP TABLE IF EXISTS Exercise;
-- DROP TABLE IF EXISTS Assignments;
-- DROP TABLE IF EXISTS Instructor;
-- DROP TABLE IF EXISTS Student;

-- Creating all tables

CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL
);

CREATE TABLE Instructor (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First_Name   TEXT NOT NULL,
    Last_Name   TEXT NOT NULL,
    Slack_Handle   TEXT NOT NULL,
    Specialty	TEXT NOT NULL, 
    Cohort_Id	INTEGER,
    FOREIGN KEY('Cohort_Id') REFERENCES 'Cohort'('Id')
    
);


CREATE TABLE Student (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First_Name   TEXT NOT NULL,
    Last_Name   TEXT NOT NULL,
    Slack_Handle   TEXT NOT NULL, 
    Cohort_Id	INTEGER,
    FOREIGN KEY('Cohort_Id') REFERENCES 'Cohort'('Id')
    
);

CREATE TABLE Exercise (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL,
    Language   TEXT NOT NULL
    
);

CREATE TABLE Assignments (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Exercise_Id	INTEGER,
    Student_Id	INTEGER,
    FOREIGN KEY('Exercise_Id') REFERENCES 'Exercise'('Id'),
    FOREIGN KEY('Student_Id') REFERENCES 'Student'('Id')
    
);


-- Creating 3 cohorts

INSERT INTO Cohort (Name)
VALUES ('Day Cohort 36');

INSERT INTO Cohort (Name)
VALUES ('Day Cohort 37');

INSERT INTO Cohort (Name)
VALUES ('Day Cohort 39');


-- Creating 5 exercises
INSERT INTO Exercise (Name, Language)
VALUES ('Monkey Chicken', 'Python');

INSERT INTO Exercise (Name, Language)
VALUES ('Cash to Coins', 'Python');

INSERT INTO Exercise (Name, Language)
VALUES ('Coins to Cash', 'Python');

INSERT INTO Exercise (Name, Language)
VALUES ('Chicken Monkey', 'JavaScript');

INSERT INTO Exercise (Name, Language)
VALUES ('Car Sales', 'JavaScript');

-- Creating 3 Instructors
INSERT INTO Instructor (First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
VALUES ('Joe', 'Shepherd', 'JoeShep', 'Python', 1);

INSERT INTO Instructor (First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
VALUES ('Kristen', 'Norris', 'KristenN', 'JavaScript', 2);

INSERT INTO Instructor (First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
VALUES ('Jenna', 'Solis', 'JennaS', 'JavaScript', 3);


-- Create 7 Students
INSERT INTO Student (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Michelle', 'Johnson', 'Stitchell', 1);

INSERT INTO Student (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Christian', 'Pippin', 'Ian', 1);

INSERT INTO Student (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Brant', 'Pippin', 'BPippin', 3);

INSERT INTO Student (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Bito', 'Mann', 'BMan', 2);


INSERT INTO Student (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Ryan', 'Crowley', 'RC', 1);

INSERT INTO Student (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Julian', 'Garcia', 'JGarcia', 2);

INSERT INTO Student (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Corri', 'Golden', 'Silence', 3);


-- Creating 2 exercises for each student

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (1, 1);

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (1, 2);


INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (2, 3);

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (2, 4);


INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (3, 4);

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (3, 5);


INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (4, 1);

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (4, 3);


INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (5, 5);

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (5, 2);


INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (6, 4);

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (6, 5);


INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (7, 1);

INSERT INTO Assignments (Student_Id, Exercise_Id)
VALUES (7, 3);



