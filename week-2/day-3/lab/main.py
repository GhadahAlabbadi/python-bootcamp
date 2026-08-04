#LAB 1
results = 10 + 5 * 2 - 4 / 2
print(results)

#LAB 2
total_items = 17
box_capacity = 5
full_box = total_items // box_capacity
remaining_items = total_items % box_capacity
print(f"You can fill up to: {full_box}")
print(f"And you will have {remaining_items} remaining")

#LAB 3
base_calc = 2 + 3 * 3 **2
gcalc = (2 + 3) * 3 **2
print(base_calc)
print(gcalc)

#LAB 4
user_age = 25
has_permission = True
is_eligible = (True if (user_age >= 18 and has_permission) else False)
print(f"Eligibility status: {is_eligible}")

#LAB 5
score = 10
score += 5 #score = score + 5
score *= 5 #score = score * 5
print(f"your score is {score}")

#LAB 6
memberships = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
if current_membership in memberships:
    print("Welcome")
else: 
    print("Go to sign up page")

#LAB 7
sentence = "Python Web Development"
new_sentence = sentence.find("Web")
print(new_sentence) #-> 7 (find Web in index 7)

#LAB 8
message = "Python Programming"
first_char = message[0]
last_char = message[-1]
print(f"First character is {first_char} and last character is {last_char}")
sliced_message = message[:6]
print(sliced_message)
reversed_message = message[::-1] #reverse the message
print(f"""Your message was {message}, 
if we take the first 6 chars it will be {sliced_message}
if we reversed it, it will be {reversed_message}""")

#LAB 9
my_email = "      ghadah.au4@gmail.com      "
cleaned_email = my_email.strip().lower()
message = "Python web development"
titled_message = message.title()
print(f"Your email is {cleaned_email}, and your course is {titled_message}")

#LAB 10
csv_text = "apple,orange,banana,cherry,dates"
splitted_text = csv_text.split(",")
joined_text = " - ".join(splitted_text)
print(f"""Your list is {csv_text}
Splitted like this {splitted_text}
Rejoined like this {joined_text}""")

#LAB 11
name = "Khalid"
try:
    name[0] = "A"
except TypeError as e:
    print(e)

x = 5
y = 5
if x == y: # -> True but x is y -> else
    print("They are the same value")
else:
    print("They are not the same value")
print(id(x)) # print place of x in memory
print(id(y))

#LAB 12
message = "Python Web Development"
new_message = message.replace("Development","Programming")
print(new_message)

is_online = None
if is_online == True:
    print("True")
elif is_online == False:
    print("False")
else:
    print("None")
