print("Hello Dictionaries")

# Dictionaries are Python's most powerful data collection
# They allow fast, database-like operations

# Creating and updating dictionaries
purse = dict()
purse['Candy'] = 20
purse['Money'] = 30
purse['tissues'] = 50
print(purse)

name = dict()
name['Owais Iqbal'] = 10
name['Umair Iqbal'] = 20
name['Hamza Jaffar'] = 30
name['Junaid Saeed'] = 50
print(name)

students = dict()
students['Ali Murtaza'] = 10
students['Mesam'] = 88
students['Muzamil'] = 100
students['Hammad Shah'] = 500
print(students)

# Accessing values
print(students['Ali Murtaza'])
print(students['Hammad Shah'])
print(purse['Candy'])
print(purse['Money'])

# Updating values
purse['Money'] += 4
print(purse)

students['Hammad Shah'] += 100
print(students)

name['Junaid Saeed'] += 700
print(name)

# Working with lists
lst = list()
lst.append("Owais_iqbal")
lst.append("Umair Iqbal")
lst.append(44)
lst.append(100)
print(lst)

# Dictionary constants
name = {'Owais': 100, 'hamza': 55}
print(name)

name = {'Name': 100, 'brother': 200, 'sister': 1}
print(name)

ooo = {}
print(ooo)

total_frnd = {'school_frnd': 20, 'Collage_frnd': 4, 'Uni_frnd': 10}
print(total_frnd)

# Counting with dictionaries
counts = dict()
names = ['Owais', 'umair', 'owais', 'bilal', 'owais', 'umair']
for person in names:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] += 1
print(counts)

counts = dict()
names = ['bilal', 'Umair', 'bilal', 'owais', 'umair']
for person in names:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] += 1
print(counts)

# Incorrect usage fixed: counts must be a dictionary, not an integer
counts = dict()
names = ['owais', 'umair', 'owais', 'owais']
for person in names:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] += 1
print(counts)

counts = dict()
names = ['jim', 'bill', 'bill']
for person in names:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] += 1
print(counts)

counts = dict()
names = ['owais', 'jim', 'jim', 'jim']
for person in names:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] += 1
print(counts)

counts = dict()
names = ['Owais', 'umair', 'jim', 'jim', 'Owais']
for person in names:
    if person not in counts:
        counts[person] = 1
    else:
        counts[person] += 1
print(counts)

# Definite loops and dictionaries
counts = {'Owais': 10, 'Umair': 20, 'Hamza': 55}
for key in counts:
    print(key, counts[key])