# Python Practice – Strings
# This script walks through basic string operations step by step.

# What is a string?
# A string is a sequence of characters, created using single or double quotes.

# Basic string creation and printing
print("Hello")  # Output: Hello

string1 = "Hello "
string2 = "world"
concat = string1 + string2
print(concat)  # Output: Hello world

# Type conversion: converting string to integer
x = '123'
print("Type of x:", type(x))  # Output: <class 'str'>

y = int(x)
print("Type of y:", type(y))  # Output: <class 'int'>
print("Converted value:", y)  # Output: 123

# User input and basic arithmetic
name = input("Please enter your name: ")
print("You entered:", name)

apple = input("Enter a number: ")
y = int(apple) - 10
print("Result after subtracting 10:", y)

# Accessing characters using index
fruit = "banana"
letter = fruit[1]  # Index starts from 0
print("Second letter in 'banana':", letter)

string = "I am learning python"
print("Fourth character:", string[3])  # Output: m

book = "this book is amazing"
print("Length of string:", len(book))  # Output: 20

# Looping through strings using while loop
name = "Owais Iqbal"
index = 0
while index < len(name):
    letter = name[index]
    print("Index", index, ":", letter)
    index += 1

# Looping through strings using for loop
fruit = "Banana"
for letter in fruit:
    print("Letter:", letter)

# Counting specific characters
word = "banana"
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print("Number of 'a's:", count)  # Output: 3

# Slicing strings
s = "Monty Python"
print("First 4 characters:", s[0:4])   # Output: Mont
print("Characters from index 6 onward:", s[6:20])  # Output: Python
print("First 2 characters:", s[:2])    # Output: Mo
print("From index 2 to end:", s[2:])   # Output: nty Python
print("Full string:", s[:])            # Output: Monty Python

# String manipulation
a = "owais "
b = "iqbal"
print("Full name:", a + b)  # Output: owais iqbal

# String operations
fruit = "Banana"
print("'B' in fruit:", "B" in fruit)     # Output: True
print("'na' in fruit:", "na" in fruit)   # Output: True

# String methods: lower and upper
greet = "HELLO WORLD"
print("Lowercase:", greet.lower())   # Output: hello world
print("Uppercase:", greet.upper())   # Output: HELLO WORLD

# Searching strings with find()
fruit = "Banana"
print("Index of 'na':", fruit.find("na"))  # Output: 2
print("Index of 'z':", fruit.find("z"))    # Output: -1

# Replacing substrings
name = "Hello World"
print("After replacement:", name.replace("Hello", "Happy"))  # Output: Happy World

# Stripping whitespace
name = "   this   "
print("Stripped string:", name.strip())   # Output: "this"

# Checking string prefix
x = "I am ok with using python"
print("Starts with 'I':", x.startswith("I"))       # Output: True
print("Starts with 'Python':", x.startswith("Python"))  # Output: False