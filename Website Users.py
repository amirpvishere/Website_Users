courses = [
    {
        'title': 'Python',
        'teacher': 'Smith'
    },
    {
        'title': 'HTML',
        'Teacher': 'Dykes'
    }
]

class User:

    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname

    def fullname(self):
        print(f'Your name is {self.fname} {self.lname}')

class Student(User):

    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname)
        self.email = email
        self.courses = []

    def fullname(self):
        print(f'Hi {self.fname} {self.lname}')
        super().fullname()

    def printcourses(self):
        if self.courses:
            for courses in self.courses:
                print(courses['title'])
        else:
            print('You Have no course')

class Teacher(Student):

    def __init__(self, firstname, lastname, email, age):
        super().__init__(firstname, lastname, email)
        self.age = age

    def text(self):
        x = input('Enter your text: ')
        print(x)

