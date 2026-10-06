"""Topic 4: Input Type Conversion

input() returns text. To do maths with it, convert it to the right type.
This file covers the conversions you need and how to avoid the errors.

Run with:  python 04-input-type-conversion.py
"""

import builtins

print("=" * 60)
print("THE CORE PROBLEM")
print("=" * 60)
print("input() always gives a str, even when the user types digits.")

answers = ["25"]
real_input = builtins.input


def scripted_input(prompt="", answers=None):
    """Stand-in for input() with a scripted answer so this file runs alone."""
    print(prompt, end="", flush=True)
    answer = answers.pop(0) if answers else real_input()
    print(answer)
    return answer


builtins.input = lambda prompt="": scripted_input(prompt, answers)
age_text = input("Enter your age: ")
builtins.input = real_input

print("value :", repr(age_text))
print("type  :", type(age_text).__name__)
print()
print("Arithmetic with it fails:")
try:
    print(age_text + 1)
except TypeError as error:
    print("   age_text + 1 ->", type(error).__name__, ":", error)
print()
print("Multiplication silently does the wrong thing instead of failing:")
print('age_text * 2 ->', age_text * 2, " (doubles the text, not the number)")

print()
print("=" * 60)
print("THE FIX: CONVERT RIGHT AFTER READING")
print("=" * 60)

answers = ["25"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
age = int(input("Enter your age: "))
builtins.input = real_input

print("value :", repr(age))
print("type  :", type(age).__name__)
print("age + 1      =", age + 1)
print("age * 2      =", age * 2)
print("age >= 18    =", age >= 18)

print()
print("Which conversion you choose depends on what you need:")
print("  int()    counts, marks, quantities, years")
print("  float()  prices, measurements, percentages")
print("  str()    only when joining text, which input already gives you")

print()
print("=" * 60)
print("WHEN THE TEXT IS NOT A NUMBER")
print("=" * 60)
print("int() and float() raise ValueError on text they cannot read.")

bad_inputs = ["abc", "", "25a", "3.5.1", "one"]
for text in bad_inputs:
    try:
        result = int(text)
        print(f"   int({text!r:<8}) -> {result}")
    except ValueError as error:
        print(f"   int({text!r:<8}) -> ValueError: {error}")

print()
print("float() accepts a decimal point, so it accepts more input:")
for text in ["3.5", "25", "", "-7"]:
    try:
        result = float(text)
        print(f"   float({text!r:<8}) -> {result}")
    except ValueError as error:
        print(f"   float({text!r:<8}) -> ValueError: {error}")

print()
print("=" * 60)
print("SAFER: CHECK BEFORE CONVERTING")
print("=" * 60)
print("isdigit() rejects signs and decimal points, which is a limitation.")
print("It is still worth knowing for simple whole numbers.")

tests = ["25", "3.5", "-7", "", "abc", "25a"]
for text in tests:
    print(f"   {text!r:<8} isdigit() -> {text.isdigit()}")

print()
print("A check that accepts signs and decimals:")


def is_number(text):
    """Return True when text can be converted to a float."""
    try:
        float(text)
    except ValueError:
        return False
    return True


for text in ["25", "3.5", "-7", "", "abc", "1e5"]:
    print(f"   {text!r:<8} is_number -> {is_number(text)}")

print()
print("=" * 60)
print("SAFER: CATCH THE ERROR AND TRY AGAIN")
print("=" * 60)


def read_int(prompt):
    """Loop until the user types a whole number."""
    while True:
        text = real_input(prompt)
        try:
            return int(text)
        except ValueError:
            print("  Please enter a whole number, for example 42.")


def read_float(prompt):
    """Loop until the user types a number."""
    while True:
        text = real_input(prompt)
        try:
            return float(text)
        except ValueError:
            print("  Please enter a number, for example 42 or 3.5.")


print("read_int and read_float keep asking until valid text arrives.")
print("Uncomment to try them:")
print()
print("#   marks  = read_int('Marks: ')")
print("#   price  = read_float('Price: ')")
print("#   print(marks, price)")

print()
print("=" * 60)
print("ROUNDING THE RESULT OF CALCULATIONS")
print("=" * 60)
print("floats keep many decimal places. round() tidies the output.")

answers = ["19.99"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
price = float(input("Price: "))
builtins.input = real_input

quantity = 3
subtotal = price * quantity
tax = subtotal * 0.17
total = subtotal + tax

print("price     =", price)
print("subtotal  =", subtotal)
print("tax       =", tax)
print("total     =", total)
print()
print("Rounded for display:")
print(f"subtotal  : {subtotal:.2f}")
print(f"tax       : {tax:.2f}")
print(f"total     : {total:.2f}")
print("round(total, 2) =", round(total, 2))

print()
print("=" * 60)
print("COMPARING A CONVERTED VALUE")
print("=" * 60)
print("Convert both sides to the same type before comparing.")

answers = ["5"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
typed = input("Enter a number: ")
builtins.input = real_input

print("typed            :", repr(typed))
print('typed == 5       :', typed == 5, " (text vs number)")
print("int(typed) == 5  :", int(typed) == 5, " (numbers compared)")
print('typed == "5"     :', typed == "5", " (text vs text)")
print()
print("Order matters when the text may be invalid:")
print("Check first, then convert, so a bad value cannot crash the program.")

print()
print("=" * 60)
print("WHOLE PROGRAM: A SIMPLE CALCULATOR")
print("=" * 60)


def calculator():
    """Read two numbers and an operator, then show the result."""
    first = read_float("First number : ")
    second = read_float("Second number: ")
    operator = real_input("Operator (+ - * /): ").strip()

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Unknown operator:", operator)
        return

    print(f"{first} {operator} {second} = {result}")


print("Reads two numbers, checks the operator, then prints the result.")
print("Uncomment to run it interactively:")
print()
print("#   calculator()")

print()
print("What it does, step by step:")
print("  1. Convert both inputs to float, retrying until valid.")
print("  2. Read the operator as text.")
print("  3. Choose the calculation with if, elif, else.")
print("  4. Guard the division against a zero divisor.")
print("  5. Print the result with an f-string.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. int('3.5')  raises ValueError. Use float('3.5') or int(float('3.5')).
2. Multiplying text instead of failing: '5' * 2 gives '55'.
3. Converting in the condition instead of the assignment, so the value is
   converted again every time it is used.
4. Forgetting that a negative sign or a decimal point fails isdigit().
5. Dividing by a zero the user typed without checking first.
""")

print("int('3.5') fails, so here is the correct route:")
try:
    int("3.5")
except ValueError as error:
    print("   int('3.5') ->", type(error).__name__, ":", error)
print("   float('3.5')      =", float("3.5"))
print("   int(float('3.5')) =", int(float("3.5")), " (truncates to 3)")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- input() gives text, so convert it before any arithmetic.
- int() for whole numbers, float() for decimals.
- Invalid text raises ValueError, which you catch or check for first.
- Loop until the input is valid instead of accepting bad data.
- Round or format the result before displaying money-like values.
""")