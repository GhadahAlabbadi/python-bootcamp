class Student:
    pass
print(Student) #<class '__main__.Student'>
print(type(Student)) #<class 'type'>

class Student:
    def __init__(self, name, score): #***
        self.name = name
        self.score = score
    def display_result(self):
        print(self.name, self.score)
sara = Student("Sara", 92)
omar = Student("Omar", 81)
sara.score = 95
print(sara.score)
print(omar.score)
print(isinstance(omar, Student)) #True
sara.display_result() #Sara 95
omar.display_result() #Omar 81

class Student:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"I am {self.name}")
student = Student("Omar")
student.introduce() # I am Omar

class Student:
    academy = "Tuwaiq Academy" # class attribute
    def __init__(self, name):
        self.name = name
sara = Student("Sara")
print(Student.academy)
print(sara.academy) 
print(sara) #<__main__.Student object at 0x000001DAC97A4980>

class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
counter = Counter()
counter.increment()
counter.increment()
print(counter.value) #2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rectangle = Rectangle(5, 3)
print(rectangle.area()) #15

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True
account = BankAccount(500)
print(account.withdraw(200)) #True
print(account.balance) 

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}: {self.score}"
student = Student("Sara", 95)
print(student) #Sara: 95

class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
first = Counter()
second = Counter()
first.increment()
print(first.value) #1
print(second.value) #0

class Student:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}"
students = [Student("Sara"), Student("Omar"), Student("Lina")]
print(students[0]) #<__main__.Student object at 0x00000238F5894EC0>
for student in students:
    print(student.greet())

class Student:
    pass
student = Student()
print(type(student)) #<class '__main__.Student'>
print(type(student) is Student) #True
print(isinstance(student, Student)) #True

class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score #_ say that this attribute is private and should not be accessed directly
student = Student("Sara", 95)
print(student.name)
print(student._score)

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores 
    def average(self):
        return sum(self.scores) / len(self.scores)
    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
student = Student("Sara", [80,90])
student.add_score(100)
print(student.scores) # [80, 90, 100]
print(student.name, student.average()) #Sara 90.0

#!GUIDED PRACTICE
class Student:
    def __init__(self, name, scores=[]):
        self.name = name
        self.scores = scores
    def add_score(self, score):
            if 0 <= score <= 100:
                self.scores.append(score)
    def average(self):
            if self.scores:
                return sum(self.scores) / len(self.scores)
            else:
                return 0
    def __str__(self):
        return f"{self.name}, with scores: {self.scores}, average: {self.average()}"

class Course:
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students
    def add_student(self, student):
         self.students.append(student)
    def display_students(self):
        for student in self.students:
            print(student)
         
course = Course("Python", [])
course.add_student(Student("Sara", [80, 90]))
course.add_student(Student("Omar", [70, 85]))
course.display_students()