#LAB 1
age = 20
if 18 <= age <= 60:
    print("Welcome")
print("Code completed")

#LAB 2
temprature = 31
if temprature >= 35:
    print("its hot outside")
else:
    print("cool")

#LAB 3
score = 95
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("YOU FAILED")

#LAB 4
is_active = True
is_verified = True
role = "editor"
is_blocked = False
if is_active and is_verified:
    print("Account is ready")
if role == "admin" or role == "editor":
    print("User can edit")
if not is_blocked:
    print("User is not blocked")
else:
    print("User is blocked")

#LAB 5
account_active = True
has_permission = False
if account_active:
    if has_permission:
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Account is not active")

#LAB 6
name = "ghadah"
cart = []
balance = 0
if name:
    print("Name has a value")
if not cart:
    print("Your cart is empty, please shop")
print(bool(balance))

#LAB 7 **
name = input("Please enter your first name: ").strip()
if not name:
    print("Please enter a name")
elif not name.replace(" ", "").isalpha(): #without replace(), will act the same 
    print("Name must contain letters")
else:
    print(f"Valid name {name}")

#LAB 8 
age_text = input("Enter your age: ").strip()
if age_text.isdigit():
    age = int(age_text)
    print(f"You will be {age + 5} in 5 years")
else:
    print("Enter a number")

#LAB 9
is_score_valid = False
score_text = input("Enter a score between 0 and 100: ")
if score_text.isdigit():
    score_x = int(score_text)
    if score_x >= 0 and score_x <= 100:
        print("Valid score")
        is_score_valid = True
    else:
        print("Score invalid")
else:
    print("Please enter a number")

#LAB 10
membership = ["Admin", "Editor", "Visitor"]
current_membership = input("Enter your membership: ").strip().lower().title()
if current_membership in membership:
    print("You are allowed to view the content")
    print(f"Your current membership is {current_membership}")
else:
    print("Please contact admin team")
    print(f"Your current membership is {current_membership}")

#LAB 11 **
commands = input("Please enter a command (start, stop, status): ").strip().lower()
match commands:
    case "start":
        print("....Starting system")
    case "stop":
        print("Stopping system....")
    case "status":
        print("System is up and running ..")
    case _: #like as default
        print("Please enter a proper command")
