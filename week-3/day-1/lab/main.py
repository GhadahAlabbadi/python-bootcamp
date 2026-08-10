#LAB 11
password = input("Please Enter your password: ")
while password != "python123":
    password = input("Incorrect password, try again: ")
print("Access Granted!")

#LAB 12
for score in [80, 55, 45, 90]:
    if score < 50:
        pass
    print(f"If passed the {score}")
for record in [80, 55, 45, 90]:
    if record < 50:
        continue
    print(f"If did not skip {record}")
for badscore in [80, 55, 45, 90]:
    if badscore < 50:
        break
    print(f"We saw: {badscore}")

#LAB 13
for row in range(1,4):
    for column in range(1,4):
        print(f"{row} X {column} = {row * column}")

#PRACTICE
def calculate_grade(score):
    grade = ""
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"
    return grade
print(calculate_grade(80))

#LAB 1
def greet():
    print("Welcome to Python")
greet()

#LAB 2
def show_menu():
    print("1- Coffee")
    print("2- Tea")
    print("3- Ginger")
show_menu()
print("Outside the call")
show_menu()

#LAB 3
print("Line one")
def gotoFunc():
    print("From within the GoTo")
print("Where is line 2?")
gotoFunc()
print("I'm up here")

#LAB 4
def greet_student(name):
    print(f"Welcome {name}")
greet_student("Sara")

#LAB 5
def show_booking(destination, nights):
    print(f"You are travelling to {destination}, and will stay for {nights} nights")
show_booking("Jeddah", 3)
show_booking("Doha", 5)

#LAB 6
def getVAT(total, rate = 0.15):
    """This function will get the total with VAT added to it, and return"""
    not_subtotal = total + (total * rate)
    return not_subtotal
print(getVAT(154))
print(getVAT(154, 0.05))
print(getVAT.__doc__)
help(getVAT)