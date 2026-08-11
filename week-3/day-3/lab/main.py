#EXCERSISES DURING CLASS
students = ["Sara", "Omar", "Lina"]
print(students) #['Sara', 'Omar', 'Lina']
print(students[0]) #Sara
print(type(students)) #<class 'list'>

colors = ["red", "green", "blue"]
print(colors[0]) #red
print(colors[1]) #green
print(colors[-1]) #blue

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) #[20, 30, 40]
print(numbers[:3]) #[10, 20, 30]
print(numbers[::2]) #[10, 30, 50]
print(numbers[::-1]) #[50, 40, 30, 20, 10]

tasks = ["plan", "code"]
tasks[0] = "design"
tasks.append("test")
tasks.insert(1, "review") #******
print(tasks) #['design', 'review', 'code', 'test']

scores = [88, 72, 95, 81]
scores.remove(72) #******
last = scores.pop() #******
scores.sort()
print(scores) #[88, 95]
print(last) #81

students = ["Sara", "Omar", "Lina"]
for student in students:
    print(student) #Sara Omar Lina
for index, student in enumerate(students):
    print(index, student) #0 Sara 1 Omar 2 Lina

matrix = [[1,2,3],[4,5,6]]
print(matrix[0]) #[1, 2, 3]
print(matrix[1][2]) #6 #******

location = (24.7136, 46.6753)
print(location[0]) #24.7136
print(location[-1]) #46.6753

student = ("Sara", 22, "Python")
name, age, course, *other = student #******
print(name) #Sara
print(age) #22
print(course) #Python
print(other) #[]

skills = {"Python", "Git", "Python"}
skills.add("Django") #******
print(skills) #{'Django', 'Python', 'Git'}
print("Git" in skills) #True
print(len(skills)) #3

backend = {"Python", "Django", "SQL"}
frontend = {"HTML", "CSS", "JavaScript", "SQL"}
print(backend | frontend) #union #{'CSS', 'HTML', 'JavaScript', 'Django', 'Python', 'SQL'} #******
print(backend & frontend) #intersection #{'SQL'} #******
print(backend - frontend) #difference #{'Python', 'Django'} #******

student = {"name":"Sara", "age":22, "course":"Python"}
print(student["name"]) #Sara

student = {"name":"Sara", "score":90}
student["score"] = 95
student["grade"] = "A"
email = student.get("email", "Not set") #******
grade = student.pop("grade") #******
print(email) #Not set 
print(student) #{'name': 'Sara', 'score': 95}

student = {"name": "Sara", "score": 95}
for key in student:
    print(key) #name / score
for key, value in student.items(): #******
    print(key, value) #name Sara / score 95
for value in student.values(): #******
    print(value) #Sara / 95

names = ["Sara", "Omar"]
skills = {"Python", "Git"}
student = {"name":"Sara", "score":95}
print(len(names)) #2
print("Python" in skills) #True
print("name" in student) #True

students = [{"name":"Sara", "score":95}, {"name":"Omar", "score":88}]
for student in students:
    print(student["name"], student["score"]) #Sara 95 / Omar 88

#PRACTICE ***
students = [{"name":"Sara", "score":(95,90,99), "skills":{"HR","Operations"}}, 
            {"name":"Omar", "score":(88,85,90), "skills":{"HTML","CSS","CSS"}},
            {"name":"Ghadah", "score":(99,100,94), "skills":{"Java","Python"}}]
for student in students:
    total = 0
    average = 0
    for score in student["score"]:
        total += score
        average = total / len(student["score"])
    print(f"student {student["name"]} has skills {student["skills"]} and average is {average:.2f}")

import math

#LAB 1 ***
students = ["Sara","Dalal","Taif"]
for student in students:
    print(student)
for iterable in enumerate(students):
    print(iterable) #print(next(iterable))
iterable = enumerate(students)
print(next(iterable)) 

#LAB 2
set_col = {"Abdullah", "Nasser", "Dalal", "Sara"}
tuple_col = (11,22,33,44,55,66)
dict_cole = {"name":"Abdullah", "age":22, "has_car":True}
list_col = ["ABC", 333, (33,33)]
for c in dict_cole.values():
    print(type(c))
print(set_col)
print(tuple_col)
print(dict_cole)
print(list_col)
print(type(set_col))
print(type(tuple_col))
print(type(dict_cole))
print(type(list_col))

#LAB 3
cars = ["GMC", "BMW", "Geely", "Porsche", "Merc", "Chevy"]
print(cars[3])
print(cars[-1])
print(cars[-1::])
print(cars[-1::-1])

#LAB 4 ***
tasks = ["Read email", "Open ticket"]
tasks[0] = "Login"
tasks.append("Get Coffee")
tasks.insert(0, "Get breakfast") #******
tasks.pop(3) #******
print(tasks)

#LAB 5 ***
nums = [11,22,33,44,55,66]
print(sum(nums))
print(len(nums))
print(max(nums))
print(min(nums))
print(math.sqrt(max(nums)))
print(math.__doc__)
print(nums.pop(2))
print(sorted(nums, reverse= True)) #******

#LAB 6 ***
skills = {"Python", "Django", "Flask", "FastAPI", "Java"}
skills.add("CSS")
skills.add("HTML")
skills.remove("Java")
skills.discard("CSS") #******
print(skills)