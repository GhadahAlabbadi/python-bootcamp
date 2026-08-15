# numbers = range(1_000_000)
# total = sum(number ** 2
#             for number in numbers)
# print(total) #333332833333500000

# items = ["Python", "Git"]
# items.append("Django")
# name = "sara"
# name = name.title()
# print(items) #['Python', 'Git', 'Django']
# print(name) #Sara

# original = ["Python", "Git"]
# alias = original
# alias.append("Django")
# print(original) #['Python', 'Git', 'Django']
# print(alias) #['Python', 'Git', 'Django']
# print(original is alias) #True

# original = ["Python", "Git"]
# clone = original.copy()
# clone.append("Django")
# print(original) #['Python', 'Git']
# print(clone) #['Python', 'Git', 'Django']
# print(original is clone) #False

# original = [["Sara",90], ["omar", 85]]
# clone = original.copy()
# clone[0][1] = 95
# print(original) #[['Sara', 95], ['omar', 85]]
# print(clone) #[['Sara', 95], ['omar', 85]]
# print(original[0] is clone[0]) #True

# from copy import deepcopy
# original = [["Sara",90], ["omar", 85]]
# clone = deepcopy(original)
# clone[0][1] = 95
# print(original) #[['Sara', 90], ['omar', 85]]
# print(clone) #[['Sara', 95], ['omar', 85]]
# print(original[0] is clone[0]) #False

# names = ["Sara", "Omar", "Lina"]
# # Search items one by one : O(n)
# print("Lina" in names)
# name_set = set(names)
# # Average membership lookup: O(1)
# print("Lina" in name_set)

# students = [{"id":101, "name":"Sara"}, {"id":102, "name":"Omar"}]
# students_by_id = {student["id"]: student
#                   for student in students}
# print(students_by_id[102]["name"])

# #!IMPORTANT PRACTICE !!!
# students = [{"name":"ghadah", "scores":[99,98,100]}, 
#             {"name":"majd", "scores":[100,98,100]},
#             {"name":"omar", "scores":[20,30,40]}]
# list_of_scores = [sum(student["scores"])/len(student["scores"])
#                  for student in students]
# print(list_of_scores)
# record = {student["name"]: avg
#           for student in students
#           for avg in list_of_scores
#           if avg >= 60}
# print(record)
# from copy import deepcopy
# deepCopy_dict = deepcopy(record)
# deepCopy_dict["shahad"] = 99
# print(deepCopy_dict)

#LAB 1
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)
print(squared_numbers)
comp_numbers = [number ** 2
                for number in numbers]
print(comp_numbers)

#LAB 2
prices = [10, 25, 40]
prices_with_vat = [round(price * 1.15, 2)
                   for price in prices]
print(prices_with_vat)

#LAB 3
names = ["SaRa", "ArEej", "Mashael", "nasser"]
lower = [name.lower()
         for name in names]
upper = [name.upper()
         for name in names]
titled = [name.title()
          for name in names]
print(lower, upper, titled)

#LAB 4
c_temp = [20, 33, 15, 1]
f_temp = [(temp * 1.8 + 32)
          for temp in c_temp
          if temp > 0]
print(f_temp)

#LAB 5
nested_list = [[1,2],[3,4],[5,6]]
flattened_list = []
for row in nested_list:
    for column in row:
        flattened_list.append(column)
print(flattened_list)
comp_flattened_list = [column
                       for row in nested_list
                       for column in row]
print(comp_flattened_list)

#LAB 6
scores = [45, 55, 65, 75, 86, 95]
passing_score = ["Pass" if score >= 60 else "Failed"
                 for score in scores]
print(passing_score)

#LAB 7
skills = ["PYTHON", "Git", "python", "Javascript", "SQL", "git"]
skills_set = {skill.lower()
              for skill in skills}
print(skills_set)

#LAB 8
list_name = ["Sara", "Dalal", "Nouf", "Taif"]
counted_chars = [{"name":name, "count":len(name)}
                 for name in list_name]
print(counted_chars)

#LAB 9 ***
new_names = ["Mada", "Khadija", "Yamam", "Mashael"]
upp = (name.upper()
       for name in new_names)
print(next(upp))
print(next(upp))
#print(list(upp)) #consume
print("-"*5)
for x in upp:
    print(x)
