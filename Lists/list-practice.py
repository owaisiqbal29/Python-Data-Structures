# Algorithms
# A set of rules or steps used to solve a problem

# Data Structures
# A specific way to organize and store data in a computer

# List Constants
print([1, 50, 100])
print(['Red', 'Yellow', 'Blue'])
print(['Red', 29, 98.6, 'watch'])
print([4.5, 'Python', 45.7])
print([3, 5.5, 9.1, 'Pythonistas', 9.8])
print([2.3, 45, 'Amazing', [4 + 10], 10])
print([1, [5, 6], 20])
print(['Owais_Iqbal', [20 + 20], 12])
print([])

# Using Lists in Loops
for number in [3, 5, 6, 7, 80, 90]:
    print(number)

for j in [45, 78, 90, 12, 34]:
    print(j)

for t in ['Awais', 'Umair', 'Joule']:
    print(t)

# Accessing List Elements
friends = ['Awais', 'Hamza', 'Junaid']
for friend in friends:
    print("Happy to see you again:", friend)

print(friends[1])
print(friends[0])
print(friends[-1])

# Mutability
fruit = "Banana"
# fruit[0] = 'b'  # This will raise an error
x = fruit.lower()
print(x)

lotto = [40, 12, 80, 50, 100]
lotto[0] = 30
lotto[-1] = 70
lotto[3] = 20
lotto[4] = 85
print(lotto)

# Range Function
print(range(4))
print(range(8))
print(range(10))
print(range(3))
print(range(100))
print(range(30))
print(range(12))

# Building Lists from Scratch
stuff = list()
stuff.append('book')
stuff.append('owais')
stuff.append(99)
print(stuff)

Books = list()
Books.append("python")
Books.append("Excel")
Books.append("SQL")
print(Books)

names = list()
names.extend(["Owais Iqbal", "Umair Iqbal", "Maqbool Ahmed", "Hamza Jaffer", "Junaid Saeed", "Wasiq Jatt"])
print(names)

programming_languages = ["python", "SQL", "Java", "Ruby", "c++", "Cobol"]
print(programming_languages)

task = ["Create a file", "learning a new tech"]
print(task)

# Sorting Lists
friends = ["owais", "Hamza", "junaid", "jaffar"]
friends.sort()
print(friends)

friends[0] = "Owais"
print(friends)

# Splitting Strings
sentence = "I am learning list data structure in python:"
var = sentence.split()
print(var)

Fav = "Python is my favorite language"
x = Fav.split()
print(x)

# Working with Files
# Uncomment and ensure 'mbox.txt' exists before running
# file = open('mbox.txt')
# for line in file:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     words = line.split()
#     print(words[2])

# Lists
# A linear collection of values that maintains order

# Dictionaries
# A bag of labeled values where each item is accessed by its key