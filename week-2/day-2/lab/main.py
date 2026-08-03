Student_name = "Sara"
student_name = "Abdullah"

print(Student_name)
print(student_name)

score = 95
if score >= 90:
    print("Excellent")
else:
    print("Thank you")

student_name = "Mada"
student_age = 20
course = "Web development bootcamp"
registered = True

MAX_CLASS_SIZE = 25
MIN_CLASS_SIZE = 15

print(f"""
Welcome {student_name} to {course}
You are {student_age}
Registeration status: {registered}
""")

student_name, student_age, student_is_registered = "Nasser", 24, True

print(type(student_name))
print(type(student_age))
print(type(student_is_registered))

print(isinstance(student_age, int))

age = input("Enter your age: ")
if (isinstance(age, int)):
    print("You are", age + 5, "after 5 years")
else:
    print("You are", int(age) + 5, "AFTER 5 years")

teacher_name = "Faisal"
print(teacher_name)

index = int(input("Select an index: "))
if (index < len(teacher_name)):
    print(teacher_name[index])
else:
    print("Out of range")

print(type(len(teacher_name)))