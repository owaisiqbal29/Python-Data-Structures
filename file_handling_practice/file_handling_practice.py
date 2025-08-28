"""
File Handling Practice in Python
--------------------------------
This script contains examples of basic file handling operations in Python,
combined with my personal learning journey and achievements.

I have added clear explanations in comments so that anyone reading this
on GitHub can easily understand each concept.
"""

# --------------------------------------------------------
# Opening a file in read mode
# --------------------------------------------------------
file = open('mbox.txt', 'r')
print(file)  # This shows the file object
# Output: <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>


# --------------------------------------------------------
# Newline character example
# --------------------------------------------------------
var_book = "Python\nFor\nEveryBody"
print(var_book)
# Output:
# Python
# For
# EveryBody


# --------------------------------------------------------
# File as a sequence: Iterating line by line
# --------------------------------------------------------
file = open('mbox.txt')
for read in file:
    print(read)


# --------------------------------------------------------
# Counting lines in a file
# --------------------------------------------------------
file = open('mbox.txt')
count = 0
for line in file:
    count += 1
    print("Lines Count:", count)


# --------------------------------------------------------
# Reading the whole file at once
# --------------------------------------------------------
file = open('mbox.txt')
content = file.read()
print("Length of file content:", len(content))
print("First 50 characters:\n", content[:50])


# --------------------------------------------------------
# Searching through a file: lines starting with specific letters
# --------------------------------------------------------
file = open('mbox.txt')
for line in file:
    if line.startswith('A'):
        print(line.rstrip())  # Lines starting with A

file = open('mbox.txt')
for line in file:
    if line.startswith('B'):
        print(line.rstrip())  # Lines starting with B


# --------------------------------------------------------
# Searching through a file (fixed with rstrip to clean whitespace)
# --------------------------------------------------------
file = open('mbox.txt')
for line in file:
    line = line.rstrip()
    if line.startswith('IELTS'):
        print(line)


# --------------------------------------------------------
# Skipping lines using "continue"
# --------------------------------------------------------
file = open("mbox.txt")
for line in file:
    line = line.rstrip()
    if not line.startswith('state'):
        continue
    print(line)


# --------------------------------------------------------
# Personal Achievements (stored inside mbox.txt for practice)
# --------------------------------------------------------
"""
A technically skilled software engineer with hands-on experience 
building websites in JavaScript and Python.

Key Highlights:
- Advent of Code 2024: Achieved 17th position on day 20 among 198,321 participants internationally.
- Google Code Jam 2023: Ranked as the 3rd highest female coder nationwide and 1798th globally.
- Advent of Code 2023: Secured 45th position on day 19 among 311,017 coders.
- CS50x Puzzle Day 2023, 2024: Winner of the puzzle day organized by Harvard University.
- IELTS: Achieved a band score of 7.0.
- Ministry of Economy, Trade and Industry Japan Internship: Selected as the only candidate 
  from Pakistan among 90 awardees globally from 20,000 participants.
- ASCE NUST Thesis Competition: 2nd position at a top-ranked university in Pakistan.

Scholarships:
- Awarded laptops based on merit by the Prime Minister and the Chief Minister.
- HEC scholarship holder for Master of Science.
- Benevolent fund scholarship holder during Bachelor of Science.
- Fully funded scholarship holder throughout high school.

Other Achievements:
- Kufic Calligraphy: 1st position in a national competition.
- Girl Representative: Certificate of appreciation from University of Gujrat.

Currently:
- Solving Leetcode problems.
- Can be reached at: mznb03@gmail.com
- Fun fact: Other than coding, I am a big fan of chocolates.
"""
