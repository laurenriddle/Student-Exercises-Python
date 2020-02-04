'''
You must define a type for representing an exercise in code. An exercise can be assigned to many students.

Name of exercise
Language of exercise (JavaScript, Python, CSharp, etc.)

'''
class Exercise: 
    def __init__(self, name, language):
        self.exercise_name = name
        self.language = language
    def __repr__(self):
        return f'This exercise is called {self.exercise_name}. It is written in {self.language}.'