#LAB 1 ***
course = "Web Development Bootcamp"
duration = 12

def type(course):
    print("Opss")

print(course)
print(duration)
print(type(course))
print(globals()) #***

#LAB 2 ***
building = "Tuwaiq Academy"
cohort_size = 20
print(f"Welcome to {building}, class limit is {cohort_size}")
print("Tuwaiq" in building)
print("cohort_size" in globals())
print(globals()["cohort_size"]) #***

#LAB 3
location = "Global"
def outter():
    location = "Outter"
    print(f"From {location}")
    def inner():
        location = "Inner"
        print(f"From {location}")
    inner()
outter()

#LAB 4 ***
location = 0
def outter():
    location = 1
    print(f"From {location}")
    def inner():
        nonlocal location #*** 
        location += 2
        print(f"From {location}")
    inner()
    print(location)
outter()

#LAB 5
def printer():
    print("Wecome")
def desk():
    printer()
def room():
    desk()
def house():
    room()
def city():
    house()
def country():
    city()
country()

#LAB 6
language = "Python"
def show_lang(language):
    print(language)
show_lang("Dart")
print(language)

#LAB 7 ***
rate = 0.15
def getTotal(amount):
    total = amount * rate + amount
    return total
print(f"{getTotal(199.99):.2f}")
print(round(getTotal(199.99))) #***
print(round(getTotal(199.99), 2)) #***

#LAB 8 ***
def inspect_order(item, qty):
    subtotal = 25 * qty
    print(locals())
    print(locals()["subtotal"]) #***
inspect_order("Pen", 10)