"""Topic 6: Multiple Inputs

Reading several values at once. You can use one input() per value, a single
line split into pieces, or a packed result.

Run with:  python 06-multiple-inputs.py
"""

import builtins

print("=" * 60)
print("APPROACH 1: ONE input() PER VALUE")
print("=" * 60)
print("Simple and clear. Each value gets its own prompt.")

real_input = builtins.input


def scripted_input(prompt: object = "", answers=None):
    """Stand-in for input() with a scripted answer so this file runs alone."""
    print(prompt, end="", flush=True)
    answer = answers.pop(0) if answers else real_input()
    print(answer)
    return answer


answers = ["Ahmed", "20"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
name = input("Name: ")
age_text = input("Age : ")
builtins.input = real_input

print("name =", repr(name))
print("age  =", repr(age_text))
print()
print("Good when each value needs its own prompt.")
print("Downside: the user must press Enter several times.")

print()
print("=" * 60)
print("APPROACH 2: ONE LINE, SPLIT INTO PIECES")
print("=" * 60)
print("Ask for everything on one line and split it.")

answers = ["Ahmed 20 Karachi"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
line = input("Name, age, city separated by spaces: ")
builtins.input = real_input

parts = line.split()
print("line  :", repr(line))
print("parts :", parts)

if len(parts) == 3:
    person_name, person_age, person_city = parts
    print("name  :", person_name)
    print("age   :", person_age)
    print("city  :", person_city)
else:
    print("The user did not give exactly three values.")

print()
print("Use split(',') when values may contain spaces:")

answers = ["Ahmed, 20, Karachi"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
line = input("Enter name, age, city (comma separated): ")
builtins.input = real_input

person_name, person_age, person_city = [piece.strip() for piece in line.split(",")]
print("name  :", person_name)
print("age   :", person_age)
print("city  :", person_city)
print("strip() removes any spaces the user typed around the commas.")

print()
print("=" * 60)
print("APPROACH 3: SEVERAL input() CALLS ON ONE LINE")
print("=" * 60)
print("Python lets you write two calls in one statement.")

answers = ["Ali", "21"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
first, second = input("First : "), input("Second: ")
builtins.input = real_input

print("first  =", repr(first))
print("second =", repr(second))
print("Works, but the prompts appear together, which can look confusing.")

print()
print("=" * 60)
print("UNPACKING MUST MATCH THE NUMBER OF VALUES")
print("=" * 60)
print("Too many or too few values raises ValueError.")

good = "Ahmed 20 Karachi".split()
print("three names, three values:", good)
name, age, city = good
print("   name =", name, "| age =", age, "| city =", city)

try:
    name, age = good
except ValueError as error:
    print("   two names, three values ->", type(error).__name__, ":", error)

try:
    name, age, city, country = good
except ValueError as error:
    print("   four names, three values ->", type(error).__name__, ":", error)

print()
print("=" * 60)
print("SAFELY HANDLING THE WRONG COUNT")
print("=" * 60)
print("Check the length before unpacking, or catch the error.")


def parse_student(line):
    """Return a tuple of name, age and city, or None when the input is wrong."""
    parts = [piece.strip() for piece in line.split(",")]
    if len(parts) != 3:
        return None
    return parts[0], int(parts[1]), parts[2]


for sample in ["Ahmed, 20, Karachi", "Sara,21,Lahore", "Bilal, 19"]:
    parsed = parse_student(sample)
    print(f"   {sample:<24} -> {parsed}")

print()
print("With an unknown count, unpack the rest with an asterisk:")

answers = ["Ali 1 2 3 4"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
line = input("First and any extra values: ")
builtins.input = real_input

parts = line.split()
first_value, *rest = parts
print("first value :", first_value)
print("the rest    :", rest)
print("That works no matter how many values follow.")

print()
print("=" * 60)
print("COUNTING AND VALIDATING THE INPUT")
print("=" * 60)


def read_pair(prompt, expected=2):
    """Read one line and split it into exactly expected values."""
    while True:
        text = real_input(prompt).strip()
        parts = text.split()
        if len(parts) == expected:
            return parts
        print(f"  Enter exactly {expected} values separated by spaces.")


print("read_pair keeps asking until the count is right.")
print("Uncomment to try it:")
print()
print("#   name, age = read_pair('Name and age: ')")
print("#   print(name, age)")

print()
print("=" * 60)
print("READING A LIST OF NUMBERS")
print("=" * 60)
print("One line, split, then convert each piece.")


def read_numbers(prompt):
    """Read a line of numbers separated by spaces and return a list."""
    text = real_input(prompt).strip()
    return [int(piece) for piece in text.split()]


print("read_numbers('Marks: ') would return [88, 92, 79]")
print()
print("Demonstrating the conversion without waiting for input:")

sample = "88 92 79 35"
marks = [int(piece) for piece in sample.split()]
print("input text :", repr(sample))
print("marks      :", marks)
print("count      :", len(marks))
print("total      :", sum(marks))
print("highest    :", max(marks))
print("average    :", sum(marks) / len(marks))

print()
print("=" * 60)
print("PRACTICAL EXAMPLE: A MINI RESULT FORM")
print("=" * 60)

answers = ["Ahmed Khan", "88 92 79 35 56", "yes"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
student_name = input("Student name      : ")
marks_line = input("Five marks (spaces): ")
attended_text = input("Attended class? (yes/no): ")
builtins.input = real_input

student_marks = [int(piece) for piece in marks_line.split()]
attended = attended_text.strip().lower() == "yes"
average = sum(student_marks) / len(student_marks)
result = "pass" if average >= 40 else "fail"

print()
print(f"Student    : {student_name}")
print(f"Marks      : {student_marks}")
print(f"Total      : {sum(student_marks)}")
print(f"Average    : {average:.2f}")
print(f"Result     : {result}")
print(f"Attended   : {attended}")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Forgetting to strip() after split, so a stray space changes a value.
2. Unpacking without checking the count, which crashes on short input.
3. Splitting on the wrong character, for example split(' ') when the user
   typed tabs or double spaces. split() with no argument handles all of it.
4. Converting inside the loop and letting one bad value stop everything.
5. Putting two input() calls on one line, where the prompts appear together.
""")

print("split(' ') keeps empty strings, split() does not:")
messy = "  one   two  three  "
print("   split(' ') ->", messy.split(" "))
print("   split()    ->", messy.split())

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- One input() per value is clearest for a form with separate prompts.
- One line plus split() is faster when the values are related.
- Check the count before unpacking, or use an asterisk for the rest.
- strip() after splitting removes spaces the user typed by mistake.
- Convert each piece to the type you need before doing anything with it.
""")