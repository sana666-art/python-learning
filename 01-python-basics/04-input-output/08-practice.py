"""Topic 8: Practice

Exercises for the whole input and output folder. Try each task yourself first,
then compare with the answers at the bottom.

How to practise:
  1. Run the file once to see the expected output.
  2. Write your own solution under each task.
  3. Run again and compare.
  4. For the interactive tasks, rewrite them with input() and run the file
     from a terminal so you can type the values yourself.
"""

print("=" * 60)
print("TASK 1: PRINT BASICS")
print("=" * 60)
print("Print 'Hello, World!' on one line.")
print("Print two more lines in a single print() call using \\n.")
print("Print the values 1, 2, 3 on one line separated by a dash.")

print()
print("=" * 60)
print("TASK 2: sep AND end")
print("=" * 60)
print("Print the date 2026 10 05 as 2026-10-05 using sep.")
print("Print 'Loading' and 'complete' on the same line using end.")
print("Print three star characters on one line with no spaces between them.")

print()
print("=" * 60)
print("TASK 3: STORE AND REUSE INPUT")
print("=" * 60)
print("Ask the user for their name with input() and print three different")
print("sentences that each include the name.")
print("Print the length of the name and the name in upper case.")

print()
print("=" * 60)
print("TASK 4: CONVERT INPUT AND CALCULATE")
print("=" * 60)
print("Ask for a price and a quantity, convert them, then print:")
print("  subtotal  price * quantity")
print("  tax       subtotal * 0.17")
print("  total     subtotal + tax")
print("Format each money value to two decimal places.")

print()
print("=" * 60)
print("TASK 5: FORMAT A TABLE")
print("=" * 60)
print("Print this table with aligned columns using f-strings:")
print()
print("Name        Age  Score")
print("----------------------")
print("Ahmed        20  88.50")
print("Sara         21  92.25")
print("Bilal        19  75.00")
print()
print("Use a name width of 10, age width of 5, score width of 7 with .2f.")

print()
print("=" * 60)
print("TASK 6: NUMBER FORMATTING")
print("=" * 60)
print("Print 1234567 with a thousands separator.")
print("Print 3.14159 with exactly 3 decimal places.")
print("Print the ratio 45 / 55 as a percentage with 1 decimal place.")
print("Print 42 zero padded to 5 digits.")

print()
print("=" * 60)
print("TASK 7: READ SEVERAL VALUES")
print("=" * 60)
print("Ask for a full name on one line and split it into first and last.")
print("Then ask for three marks separated by spaces, convert them with a")
print("list comprehension, and print the total and the average.")

print()
print("=" * 60)
print("TASK 8: VALIDATE INPUT")
print("=" * 60)
print("Write a loop that keeps asking for a whole number until the user")
print("types digits only. Use isdigit() to check before converting.")
print("Uncomment your test call so you can try it interactively.")

print()
print("=" * 60)
print("TASK 9: SAFE CONVERSION")
print("=" * 60)
print("Write to_int(text, default=0) that returns int(text) when it works and")
print("default when it does not.")
print("Print to_int('42'), to_int('abc'), to_int('') and to_int('3.5').")

print()
print("=" * 60)
print("TASK 10: A GREETING PROGRAM")
print("=" * 60)
print("Read a name and an age, then print:")
print("  Hello, <name>. You are <age> years old.")
print("  Next year you will be <age + 1>.")
print("  Your name has <length> characters.")
print("Format the age right aligned in 5 spaces.")

print()
print("=" * 60)
print("TASK 11: A RECEIPT")
print("=" * 60)
print("Ask for an item name, a unit price and a quantity.")
print("Print a receipt with a heading, the item line, a divider of dashes,")
print("the subtotal, the tax at 17 percent and the total.")
print("Align the numbers to the right in a column of width 12.")

print()
print("=" * 60)
print("TASK 12: MULTIPLYING TEXT BY MISTAKE")
print("=" * 60)
print("Show that '5' * 2 gives '55' rather than 10, and that '5' + 1 fails.")
print("Then show the correct way with int('5').")

print()
print("=" * 60)
print("BONUS TASK A: INTERACTIVE QUIZ")
print("=" * 60)
print("Ask five questions, read each answer, and count the correct ones.")
print("Print the score and a pass or fail message at the end.")
print("Strip and lower every answer before comparing it.")

print()
print("=" * 60)
print("BONUS TASK B: PRACTICE TIMER SETUP")
print("=" * 60)
print("Ask for a student name, a subject and three test scores on one line")
print("each. Print a report with the name, the subject, each score, the")
print("total, the average and the highest score, all aligned in columns.")

print()
print("=" * 60)
print("=" * 60)
print("ANSWER SECTION - READ AFTER YOU FINISH THE TASKS")
print("=" * 60)
print("=" * 60)

print()
print("--- ANSWER 1: PRINT BASICS ---")
print("Hello, World!")
print("Line one\nLine two\nLine three")
print("1 - 2 - 3")

print()
print("--- ANSWER 2: sep AND end ---")
print("2026", "10", "05", sep="-")
print("Loading ...", end=" ")
print("complete")
print("*", "*", "*", sep="")

print()
print("--- ANSWER 3: STORE AND REUSE INPUT ---")
print("Real form, uncomment to run interactively:")
print()
print("#   name = input('Enter your name: ')")
print("#   print(f'Hello, {name}!')")
print("#   print(f'Welcome to Python, {name}.')")
print("#   print(f'Good luck, {name}.')")
print("#   print(f'Your name has {len(name)} characters.')")
print("#   print(f'Upper case: {name.upper()}')")
print()
print("Demonstration with a scripted value:")

name = "Ahmed"
print(f"Hello, {name}!")
print(f"Welcome to Python, {name}.")
print(f"Good luck, {name}.")
print(f"Your name has {len(name)} characters.")
print(f"Upper case: {name.upper()}")

print()
print("--- ANSWER 4: CONVERT INPUT AND CALCULATE ---")
print()
print("#   price = float(input('Price: '))")
print("#   quantity = int(input('Quantity: '))")
print("#   subtotal = price * quantity")
print("#   tax = subtotal * 0.17")
print("#   total = subtotal + tax")
print("#   print(f'Subtotal: {subtotal:.2f}')")
print("#   print(f'Tax      : {tax:.2f}')")
print("#   print(f'Total    : {total:.2f}')")

price = 120.5
quantity = 3
subtotal = price * quantity
tax = subtotal * 0.17
total = subtotal + tax
print()
print("Sample run with price 120.5 and quantity 3:")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax      : {tax:.2f}")
print(f"Total    : {total:.2f}")

print()
print("--- ANSWER 5: FORMAT A TABLE ---")
records = [("Ahmed", 20, 88.5), ("Sara", 21, 92.25), ("Bilal", 19, 75.0)]

print(f"{'Name':<10}{'Age':>5}{'Score':>7}")
print("-" * 22)
for record_name, record_age, record_score in records:
    print(f"{record_name:<10}{record_age:>5}{record_score:>7.2f}")

print()
print("--- ANSWER 6: NUMBER FORMATTING ---")
print(f"{1234567:,}")
print(f"{3.14159:.3f}")
print(f"{45 / 55:.1%}")
print(f"{42:05d}")

print()
print("--- ANSWER 7: READ SEVERAL VALUES ---")
print()
print("#   full_name = input('Full name: ')")
print("#   first, last = full_name.split(' ', 1)")
print("#   print(first, last)")
print("#   marks = [int(x) for x in input('Three marks: ').split()]")
print("#   print('Total :', sum(marks))")
print("#   print('Average:', sum(marks) / len(marks))")

full_name = "Ahmed Khan"
first_name, last_name = full_name.split(" ", 1)
marks = [int(piece) for piece in "88 92 79".split()]
print()
print("Demonstration with 'Ahmed Khan' and marks 88 92 79:")
print(first_name, last_name)
print("Total  :", sum(marks))
print("Average:", sum(marks) / len(marks))

print()
print("--- ANSWER 8: VALIDATE INPUT ---")
print()
print("#   while True:")
print("#       text = input('Enter a whole number: ').strip()")
print("#       if text.isdigit():")
print("#           number = int(text)")
print("#           break")
print("#       print('Digits only, please.')")
print("#   print('You entered', number)")

print("Demonstration of the check:")
for text in ["42", "-5", "3.5", "abc"]:
    print(f"   {text!r:<8} isdigit() -> {text.isdigit()}")

print()
print("--- ANSWER 9: SAFE CONVERSION ---")


def to_int(text, default=0):
    """Return text as an int, or default when it is not a valid integer."""
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


print("to_int('42')  =", to_int("42"))
print("to_int('abc') =", to_int("abc"))
print("to_int('')    =", to_int(""))
print("to_int('3.5') =", to_int("3.5"), " (a decimal is not a whole number)")

print()
print("--- ANSWER 10: A GREETING PROGRAM ---")
print()
print("#   name = input('Name: ')")
print("#   age = int(input('Age : '))")
print("#   print(f'Hello, {name}. You are {age:>5} years old.')")
print("#   print(f'Next year you will be {age + 1}.')")
print("#   print(f'Your name has {len(name)} characters.')")

name = "Sara"
age = 21
print()
print("Demonstration with Sara and 21:")
print(f"Hello, {name}. You are {age:>5} years old.")
print(f"Next year you will be {age + 1}.")
print(f"Your name has {len(name)} characters.")

print()
print("--- ANSWER 11: A RECEIPT ---")
print()
print("#   item = input('Item name   : ')")
print("#   price = float(input('Unit price : '))")
print("#   quantity = int(input('Quantity   : '))")
print("#   subtotal = price * quantity")
print("#   tax = subtotal * 0.17")
print("#   total = subtotal + tax")
print("#   print(f'{item}')")
print("#   print('-' * 34)")
print("#   print(f'{quantity:>4} x {price:>10.2f} {subtotal:>12.2f}')")
print("#   print('-' * 34)")
print("#   print(f'{\"Tax (17%)\":<22}{tax:>12.2f}')")
print("#   print(f'{\"Total\":<22}{total:>12.2f}')")

item = "Rice"
price = 450.5
quantity = 3
subtotal = price * quantity
tax = subtotal * 0.17
total = subtotal + tax

print()
print("Sample run with Rice, 450.5 and quantity 3:")
print(f"{item}")
print("-" * 34)
print(f"{quantity:>4} x {price:>10.2f} {subtotal:>12.2f}")
print("-" * 34)
print(f"{'Tax (17%)':<22}{tax:>12.2f}")
print(f"{'Total':<22}{total:>12.2f}")

print()
print("--- ANSWER 12: MULTIPLYING TEXT BY MISTAKE ---")
print("'5' * 2 ->", "5" * 2, " (text doubled, not multiplied)")
try:
    print("5 + 1 ->", "5" + 1)  # type: ignore[operator]
except TypeError as error:
    print("'5' + 1 ->", type(error).__name__, ":", error)
print("int('5') + 1 =", int("5") + 1, " (converted, so it adds correctly)")
print('f-string     ->', f"{int('5') + 1}", " (the cleanest fix)")

print()
print("--- BONUS ANSWER A: INTERACTIVE QUIZ ---")
print()
quiz = [
    ("What is 2 + 3?", "5"),
    ("Capital of France?", "paris"),
    ("Is Python case sensitive? (yes/no)", "yes"),
    ("Largest planet?", "jupiter"),
    ("How many days in a week?", "7"),
]
print("#   answers = []")
print("#   for question, correct in quiz:")
print("#       given = input(question + ' ').strip().lower()")
print("#       answers.append(given == correct)")
print("#   score = sum(answers)")
print("#   print(f'You scored {score} of {len(quiz)}')")
print("#   print('Pass' if score >= 3 else 'Fail')")

score = sum([True, True, False, True, True])
print()
print("Demonstration with 4 correct out of 5:")
print(f"You scored {score} of 5")
print("Pass" if score >= 3 else "Fail")

print()
print("--- BONUS ANSWER B: PRACTICE REPORT ---")
print()
print("#   student = input('Student name: ')")
print("#   subject = input('Subject     : ')")
print("#   scores = [int(x) for x in input('Three scores: ').split()]")
print("#   print(f\"{'Name':<12}{student}\")")
print("#   print(f\"{'Subject':<12}{subject}\")")
print("#   print('-' * 30)")
print("#   for index, score in enumerate(scores, start=1):")
print("#       print(f\"{'Score ' + str(index):<12}{score:>8}\")")
print("#   print('-' * 30)")
print("#   print(f\"{'Total':<12}{sum(scores):>8}\")")
print("#   print(f\"{'Average':<12}{sum(scores) / len(scores):>8.2f}\")")
print("#   print(f\"{'Highest':<12}{max(scores):>8}\")")

student = "Ahmed"
subject = "Physics"
scores = [88, 92, 79]
print()
print("Demonstration with Ahmed, Physics and scores 88 92 79:")
print(f"{'Name':<12}{student}")
print(f"{'Subject':<12}{subject}")
print("-" * 30)
for index, score in enumerate(scores, start=1):
    print(f"{'Score ' + str(index):<12}{score:>8}")
print("-" * 30)
print(f"{'Total':<12}{sum(scores):>8}")
print(f"{'Average':<12}{sum(scores) / len(scores):>8.2f}")
print(f"{'Highest':<12}{max(scores):>8}")