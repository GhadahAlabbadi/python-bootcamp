#PRACTICE DURING CLASS
numbers = [1, 2, 3, 4, 5] #EXPRESSION
#COMPREHENSION
squares = [number ** 2 #EXPRESSION #******
           for number in numbers #CLOSE #******
           if number % 2 == 1 ] #FILTER #******
print(squares) #[1, 9, 25]

prices = [10, 25, 40]
prices_with_vat = [round(price * 1.15, 2)
                   for price in prices] #CLOSE
print(prices_with_vat) #[11.5, 28.75, 46.0]

scores = [42, 67, 91, 58, 75]
passing_scores = [score
                  for score in scores
                  if score >= 60]
print(passing_scores) #[67, 91, 75]

raw_names = [" sara ", " ", "OMAR", " lina"]
clean_names = [name.strip().title()
               for name in raw_names
               if name.strip()]
print(clean_names) #['Sara', 'Omar', 'Lina']

numbers = [1,2]
letters = ["A", "B"]
pairs = [(number, letter)
         for number in numbers
         for letter in letters]
print(pairs) #[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

scores = [42, 67, 91]
labels = ["pass" if score >= 60 else "retry" #******
          for score in scores]
print(labels) #['retry', 'pass', 'pass']

emails = ["SARA@EXAMPLE.COM", "omar@example.com", "lina@school.sa"]
domains = {email.split("@")[1].lower()
           for email in emails}
print(domains) #{'school.sa', 'example.com'}

numbers = range(1,6)
squares = {number: number ** 2
           for number in numbers}
print(squares) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Research: can we make tuple and add items which is list or dict then update the values of list or dict?