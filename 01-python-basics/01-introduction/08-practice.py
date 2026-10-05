"""Topic 8: Practice

Tasks for Topic 1 to Topic 7. Try each task on your own first, then compare
with the answer section at the bottom of this file.

How to practise:
  1. Run this file once to see the expected output.
  2. Comment out the answer section.
  3. Write your own code for each task under the task heading.
  4. Run again and compare your output with the expected output.
"""

print("=" * 60)
print("TASK 1: PRINT YOUR NAME")
print("=" * 60)
print("Use print() to show your full name.")
print("Expected output: your name on one line")

print()
print("=" * 60)
print("TASK 2: PRINT YOUR UNIVERSITY")
print("=" * 60)
print("Store your university in a variable, then print it with a label.")
print('Expected output: University: <your university>')

print()
print("=" * 60)
print("TASK 3: PRINT YOUR FAVOURITE PROGRAMMING LANGUAGE")
print("=" * 60)
print("Store the language in a variable and print it.")
print("Expected output: My favourite programming language is <language>")

print()
print("=" * 60)
print("TASK 4: PRINT A SHORT INTRODUCTION ABOUT YOURSELF")
print("=" * 60)
print("Print 3 to 4 lines about yourself: name, city, what you study or do,")
print("and one hobby. Use several print() calls, or one multi-line f-string.")

print()
print("=" * 60)
print("BONUS TASK A: INTERPRET YOUR YEAR OF BIRTH")
print("=" * 60)
print("Use input() to read your birth year, subtract it from 2026 with f-strings,")
print("then print your age.")

print()
print("=" * 60)
print("BONUS TASK B: RECEIVE A VALUE FROM THE TERMINAL")
print("=" * 60)
print("Run the file with a value: python 08-practice.py YourName")
print("Read sys.argv[1] and greet that name.")

print()
print("=" * 60)
print("=" * 60)
print("ANSWER SECTION - READ AFTER YOU FINISH THE TASKS")
print("=" * 60)
print("=" * 60)

print()
print("--- ANSWER 1: PRINT YOUR NAME ---")
name = "Ahmed Khan"
print(name)

print()
print("--- ANSWER 2: PRINT YOUR UNIVERSITY ---")
university = "University of Karachi"
print("University:", university)

print()
print("--- ANSWER 3: FAVOURITE PROGRAMMING LANGUAGE ---")
language = "Python"
print("My favourite programming language is", language)
print(f"My favourite programming language is {language}")

print()
print("--- ANSWER 4: SHORT INTRODUCTION ---")
name = "Ahmed Khan"
city = "Karachi"
occupation = "Computer Science student"
hobby = "playing cricket"

print(f"Hello, my name is {name}.")
print(f"I live in {city} and I am a {occupation}.")
print("I am learning Python because I want to build useful software.")
print(f"In my free time I enjoy {hobby}.")

print()
print("--- BONUS ANSWER A: AGE FROM INPUT ---")
# Uncomment the lines below and run the file to try it.
# birth_year = int(input("Enter your year of birth: "))
# current_year = 2026
# print(f"You are {current_year - birth_year} years old in {current_year}.")

print("Commented out so the script runs without waiting for input.")

print()
print("--- BONUS ANSWER B: GREETING FROM sys.argv ---")
import sys

if len(sys.argv) > 1:
    user = sys.argv[1]
    print(f"Hello, {user}! Welcome to the Python course.")
else:
    print("No name given.")
    print("Run it like this: python 08-practice.py Sara")