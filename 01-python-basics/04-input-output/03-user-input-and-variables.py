"""Topic 3: User Input and Variables

input() only becomes useful when you store the result. This file shows how to
capture input, keep it, and use it in later statements.

Run with:  python 03-user-input-and-variables.py
"""

import builtins

print("=" * 60)
print("WHY STORE THE INPUT?")
print("=" * 60)

print("input() returns a value. If you do not store it, it disappears after")
print("that line. Assign it to a variable so you can reuse it.")

print()
print("=" * 60)
print("STORE INPUT IN A VARIABLE")
print("=" * 60)

real_input = builtins.input


def scripted_input(prompt: object = "", answers=None):
    """Stand-in for input() with a scripted answer so this file runs alone."""
    print(prompt, end="", flush=True)
    if answers:
        answer = answers.pop(0)
    else:
        answer = real_input()
    print(answer)
    return answer


answers = ["Ahmed"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
name = input("Enter your name: ")
builtins.input = real_input

print("The variable name now holds:", repr(name))
print("You can use it as many times as you like:")
print("Hello,", name)
print("Welcome,", name)
print("Goodbye,", name)

print()
print("=" * 60)
print("ONE INPUT, MANY USES")
print("=" * 60)

answers = ["Sara"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
student = input("Student name: ")
builtins.input = real_input

print("Report for:", student)
print("Student    :", student)
print("Length of name:", len(student))
print("Upper case :", student.upper())

print()
print("=" * 60)
print("SEVERAL VARIABLES FROM ONE INPUT")
print("=" * 60)
print("split() divides the typed line into pieces.")

answers = ["Ahmed Khan"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
full_name = input("Full name: ")
builtins.input = real_input

first_name, last_name = full_name.split(" ", 1)
print("full_name   :", repr(full_name))
print("first_name  :", repr(first_name))
print("last_name   :", repr(last_name))

print()
print("split() with no argument uses any space and ignores extras:")

answers = ["  one   two  three  "]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
line = input("Words: ")
builtins.input = real_input

words = line.split()
print("as typed :", repr(line))
print("split()  :", words)
print("count    :", len(words))

print()
print("=" * 60)
print("INPUT USED IN CALCULATIONS")
print("=" * 60)
print("Store the input, convert it, then compute.")

answers = ["500", "3"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
price = float(input("Price per item: "))
quantity = int(input("Quantity       : "))
builtins.input = real_input

subtotal = price * quantity
print("price      =", price)
print("quantity   =", quantity)
print("subtotal   =", subtotal)

print()
print("=" * 60)
print("INPUT IN CONDITIONS")
print("=" * 60)

answers = ["yes"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
reply = input("Continue? (yes/no): ").strip().lower()
builtins.input = real_input

print("reply =", repr(reply))
if reply == "yes":
    print("Decision: continuing")
elif reply == "no":
    print("Decision: stopping")
else:
    print("Decision: unclear answer, treated as stopping")

print()
print("strip() and lower() make the comparison reliable, because the user")
print("might type 'Yes', 'YES ' or ' yes'.")

print()
print("=" * 60)
print("PROMPTING UNTIL YOU GET WHAT YOU NEED")
print("=" * 60)


def read_positive_number(prompt):
    """Keep asking until the user gives a number greater than zero."""
    while True:
        text = real_input(prompt)
        try:
            value = float(text)
        except ValueError:
            print("  That is not a number. Try again.")
            continue
        if value <= 0:
            print("  It must be greater than zero. Try again.")
            continue
        return value


print("The function below loops until the value is valid.")
print("Uncomment to try it interactively:")
print()
print("#   amount = read_positive_number('Amount: ')")
print("#   print('Amount:', amount)")

print()
print("A second example, reading a choice from a list:")


def read_choice(prompt, options):
    """Ask until the user types one of the allowed options."""
    while True:
        text = real_input(prompt).strip().lower()
        if text in options:
            return text
        print("  Please choose one of:", ", ".join(options))


print()
print("#   size = read_choice('Size (S/M/L): ', ['s', 'm', 'l'])")

print()
print("=" * 60)
print("COMBINING INPUT WITH OUTPUT")
print("=" * 60)
print("Use an f-string to build a message from stored input.")

answers = ["Hina", "22"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
person_name = input("Name: ")
person_age = input("Age : ")
builtins.input = real_input

print(f"Name: {person_name}")
print(f"Age : {person_age}")
print(f"Welcome, {person_name}! You are {person_age} years old.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Forgetting to store the result.
   input('Name: ')        the value is thrown away
   name = input('Name: ')  the value is kept
2. Storing the same name for different values, which hides the meaning.
3. Not stripping whitespace before comparing an answer.
4. Assuming the user typed what the prompt asked for. Validate it.
5. Converting too early with int(input(...)) when the text may be invalid.
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Assign input() to a variable, otherwise the value is lost.
- split() turns one line into several values.
- Convert the stored text before doing arithmetic with it.
- strip() and lower() make comparisons with the user's answer reliable.
- Loop while the input is invalid instead of accepting bad data.
""")