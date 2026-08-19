#LAB 5
class Student:

    def __init__(self, name):
        self.name = name
        self.score = []
        self.__enrolled = True #! double underscore to make it private (name mangling)
    
    @property
    def enrolled(self):
        return self.__enrolled
    @enrolled.setter
    def enrolled(self, _):
        self.__enrolled = not self.__enrolled

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score.append(score)
    @property #!!!!!!!!!!!!!!!!!!!!!!!
    def average(self):
        if not self.score:
            return 0
        else:
            return sum(self.score) / len(self.score)
student = Student("Sara")
student.add_score(80)
student.add_score(90)
student.add_score(100)
print(student.score)
print(student.average)
#print(student.__enrolled) #! this will raise an error because __enrolled is private
#print(student._Student__enrolled) #! this will print the value of __enrolled
student.enrolled = ""
print(student.enrolled)

#LAB 6
class Food:
    def __init__(self, name):
        self.name = name
    def ShowName(self):
        return self.name
class Fruits(Food):
    def __init__(self, name, cal):
        super().__init__(name)
        self.cal = cal
    @staticmethod
    def stripName(newname):
        return newname.strip()
myFruite = Fruits("Apple", 200)
print(myFruite.ShowName())
print(myFruite.stripName("   fa   "))
