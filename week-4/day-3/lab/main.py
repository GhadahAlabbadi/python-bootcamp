import csv
with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "course"])
    writer.writerow(["Sara", "Python"])
    writer.writerow(["Ali", "Django"])

import json
students = [{"name": "Sara", "score": 92},{"name": "Ali", "score": 85}]
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)
with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
print(loaded[0]["name"])

try:
    score = int(input("Score: "))
except ValueError as e:
    print("Enter a whole number")
    print(e)
print("Program continues")

from pathlib import Path
try:
    text = Path("students.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    print("Student file not found")
except PermissionError:
    print("Student file cannot be read")

path = Path("students.txt")
try:
    text = path.read_text(encoding="utf-8")
except OSError as e:
    print("Load failed:", e)
else:
    print(text)
finally:
    print("Load attempt finished")

def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be 0 to 100")
    return score
try:
    score = validate_score(120)
except ValueError as e:
    print(e)

#! IMPORTANT: Custom Exception
class StudentNotFoundError(Exception):
    pass
def find_student(name, students):
    for student in students:
        if student["name"] == name:
            return student
    raise StudentNotFoundError(name)
students = [{"name":"Sara"}]
try:
    print(find_student("Ali", students))
except StudentNotFoundError as e:
    print("Missing student:",e)

#!GUIDED PRACTICE
from pathlib import Path
import json
from json import JSONDecodeError
class InvalidStudentError(Exception):
    pass
path = Path("students.json")
file_dir = Path("data")
file_dir.mkdir(exist_ok=True)
new_path = file_dir / path
students = [{"name":"ghadah", "score":99},{"name":"sara", "score":98}]
try:
    with open(new_path, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)

    with open(new_path, "r", encoding="utf-8") as file:
        loaded = json.load(file)

    for student in loaded:
        if not student["name"] or not student["score"]:
            raise InvalidStudentError("Missing value")
except FileNotFoundError as e:
    print(e)
except JSONDecodeError as e:
    print(e)
else:
    print(loaded)

#LAB 1
from os import name


class Ticket:
    def __init__(self, name, status = "open"):
        self.name = name
        self.status = status
    def newStatus(self, status):
        self.status = status
    
myTicket1 = Ticket("1000", "In-Progress")
myTicket2 = Ticket("1001", "Pending")
print(myTicket1.status)
print(f"Ticket ID: {myTicket2.name} is {myTicket2.status}")

#LAB 2
class Greeter:
    def __init__(self, message):
        self.message = message
    def greet(self, user):
        self.user = user
        print(f"Hello {self.user}, {self.message}")
mygreet = Greeter("Welcome to Tuwaiq")
mygreet.greet("Ghadah")

#LAB 3
class Welcome:
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f"Welcome {self.name}")
students = [Welcome("Sara"), Welcome("Ghadah"), Welcome("Omar")]
for student in students:
    student.welcome()

#LAB 4
from pathlib import Path
path = Path("home") / "students"
path.mkdir(parents=True, exist_ok=True)
new_path = path / "students.txt"
# print(path.is_dir())
# print(path.suffix)
# print(path.name)
# print(path.is_file())
new_path.write_text("Welcome to class", encoding="utf-8")  