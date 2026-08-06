maximum_number = int(input("Enter a maximum number: "))

count_even = 0
total = 0
for number in range(1,maximum_number + 1):
    total += number
    if number % 2 == 0:
        count_even += 1
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")

print(f"Total is {total}")
print(f"Number of even numbers is {count_even}")

#LAB 1
for attempts in range(3):
    print(f"Attempts: {attempts + 1}")

#LAB 2
for num in range(2, 11, 2):
    print(num)

#LAB 3
for secondsToLaunch in range(10, 0, -1):
    print(f"T-: {secondsToLaunch}")

#LAB 4
course = "Python"
for letter in course:
    print(letter)

#LAB 5
students = ["Shahad", "Khadija", "Yamam", "Sara", "Abdullah"]
for student in students:
    print(f"Progressing student is: {student}")

#LAB 6
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    print("-------------")

#LAB 7
numbers = [4, 7, 10, 13, 16, 21]
even_counter = 0
for num in numbers:
    if num % 2 == 0:
        even_counter += 1
print(f"Total even numbers is: {even_counter}")

#LAB 8
prices = [25, 30, 55, 115]
total = 0
for price in prices:
    total += price
print(f"Your total is {total} VAT: {total * (15/100)}")

#LAB 9
count = 0
while count < 5:
    count += 1
    print(f"Count...{count}")
print("Loop completed")

#LAB 10
message = "Please enter your age: "
age_text = input(message).strip() #TRUE FALSE Q

while not age_text.isdigit():
    age_text = input(message).strip()
age = int(age_text)
print(f"You are: {age}")

#LAB 11
password = "python123"
print("Please Enter your password")
while password != "":
    password = input("Enter your password: ")