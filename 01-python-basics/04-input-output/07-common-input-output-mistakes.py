"""Topic 7: Common Input/Output Mistakes

The errors beginners hit most often with print() and input(), with a working
version of each fix.

Run with:  python 07-common-input-output-mistakes.py
"""

import builtins

real_input = builtins.input


def scripted_input(prompt="", answers=None):
    """Stand-in for input() with a scripted answer so this file runs alone."""
    print(prompt, end="", flush=True)
    answer = answers.pop(0) if answers else real_input()
    print(answer)
    return answer


print("=" * 60)
print("MISTAKE 1: FORGETTING THE PARENTHESES")
print("=" * 60)
print("Without () you mention the function instead of calling it.")

print("print('hello')   -> calls the function, prints hello")
print("print             -> prints the function address, not your text")
print()
print("The address looks like this:")
print(print)

print()
print("=" * 60)
print("MISTAKE 2: MISMATCHED QUOTES OR BRACKETS")
print("=" * 60)
print("Every quote and bracket must be closed, and quotes must match.")

print('Correct: print("Hello")')
print("Correct: print('Hello')")
print('Broken : print("Hello)       SyntaxError')
print("Broken : print('Hello')  ... second quote style wrong")
print()
print("VS Code underlines the problem, so read the message carefully:")

try:
    compile('print("hello', '<string>', 'exec')
except SyntaxError as error:
    print("   compile ->", type(error).__name__, ":", error.msg)

print()
print("=" * 60)
print("MISTAKE 3: ADDING STRINGS AND NUMBERS")
print("=" * 60)
print("You cannot join text and a number with + without converting first.")

age = 20
try:
    print("Age: " + age)  # pyright: ignore[reportOperatorIssue]
except TypeError as error:
    print('   "Age: " + age ->', type(error).__name__, ":", error)

print()
print("Three correct fixes:")
print('1. f-string      ->', f"Age: {age}")
print('2. str(age)      ->', "Age: " + str(age))
print('3. separate args ->', "Age:", age)

print()
print("=" * 60)
print("MISTAKE 4: FORGETTING input() RETURNS TEXT")
print("=" * 60)
print("Arithmetic fails, or worse, does the wrong thing quietly.")

answers = ["25"]
# builtins.input = lambda prompt="": scripted_input(prompt, answers)
age_text = input("Age: ")
builtins.input = real_input

print("value :", repr(age_text))
try:
    print(age_text + 1)  # pyright: ignore[reportOperatorIssue]
except TypeError as error:
    print("   age_text + 1 ->", type(error).__name__, ":", error)
print('age_text * 2 ->', age_text * 2, "  (no error, but the result is wrong)")
print("Convert first:", int(age_text) + 1)

print()
print("=" * 60)
print("MISTAKE 5: CONVERTING BEFORE VALIDATING")
print("=" * 60)
print("int(input(...)) crashes the program on the first bad character.")

answers = ["abc"]
# builtins.input = lambda prompt="": scripted_input(prompt, answers)
try:
    value = int(input("Enter a whole number: "))
    print("value =", value)
except ValueError as error:
    print("   int('abc') ->", type(error).__name__, ":", error)
builtins.input = real_input

print()
print("The safe version catches the error and asks again:")


def read_int(prompt):
    """Loop until the user types a whole number."""
    while True:
        try:
            return int(real_input(prompt))
        except ValueError:
            print("  Whole numbers only, for example 42.")


print("Uncomment to try it:")
print()
print("#   marks = read_int('Marks: ')")
print("#   print(marks)")

print()
print("=" * 60)
print("MISTAKE 6: NOT STRIPPING WHITESPACE")
print("=" * 60)
print("Users type extra spaces, and Enter does not remove them.")

answers = [" yes "]
# builtins.input = lambda prompt="": scripted_input(prompt, answers)
reply = input("Continue? ")
builtins.input = real_input

print("as typed   :", repr(reply))
print('reply == "yes" ->', reply == "yes", "  (fails)")
print("strip() removes them:", repr(reply.strip()))
print('"yes" in reply.strip().lower() ->', "yes" in reply.strip().lower())

print()
print("=" * 60)
print("MISTAKE 7: EMPTY PROMPT AND A PROGRAM THAT LOOKS STUCK")
print("=" * 60)
print("If input() has no prompt, the user sees nothing and cannot tell the")
print("program is waiting. Always describe what is expected.")

print("Bad : input()")
print("Good: input('Enter the price in rupees: ')")

print()
print("=" * 60)
print("MISTAKE 8: DIVIDING BY A VALUE THE USER TYPED")
print("=" * 60)
print("Zero from input() is still zero, and division by it stops the program.")

answers = ["0"]
# builtins.input = lambda prompt="": scripted_input(prompt, answers)
divisor = float(input("Divisor: "))
builtins.input = real_input

if divisor == 0:
    print("Cannot divide by zero. The program keeps running.")
else:
    print("Result:", 100 / divisor)

print()
print("=" * 60)
print("MISTAKE 9: STORING THE RESULT OF print()")
print("=" * 60)
print("print() returns None, so storing it gives you None.")

message = print("hello")
print("message =", repr(message))
print("if message: is False, so a check like that silently fails.")

print()
print("=" * 60)
print("MISTAKE 10: WRONG SEPARATOR OR END")
print("=" * 60)
print("sep and end must be strings. Any other type raises TypeError.")
print("None is also allowed: it means use the default, so end=None prints")
print("the normal newline instead of raising an error.")

# try:
#     print("a", "b", sep=1)
# except TypeError as error:
#     print("   sep=1 ->", type(error).__name__, ":", error)

# try:
#     # print("a", end=1)
# except TypeError as error:
#     print("   end=1 ->", type(error).__name__, ":", error)

print()
print("end=None is legal and quiet:")
print("   print('a', end=None)  ->  a  (followed by the usual newline)")

print()
print("Correct uses:")
print("   print('a', 'b', sep=', ')")
print("   print('done', end='\\n\\n')")

print()
print("=" * 60)
print("MISTAKE 11: FORGETTING THE F PREFIX")
print("=" * 60)
name = "Ali"
print('Without f: "{name}"')
print(f"With f   : {name}")
print()
print("Braces without f are just characters, which is the usual cause of")
print("output that literally shows {value}.")

print()
print("=" * 60)
print("MISTAKE 12: SPLITTING WITH THE WRONG ARGUMENT")
print("=" * 60)
messy = "  one   two  three  "
print("text          :", repr(messy))
print("split(' ')    :", messy.split(" "), " (empty strings from extra spaces)")
print("split()       :", messy.split(), " (handles any run of spaces)")
print("split(',')    :", messy.split(","), " (no commas, so one whole piece)")

print()
print("=" * 60)
print("DEBUG CHECKLIST")
print("=" * 60)
print("""
When output looks wrong, ask in this order:

1. Is the value the type I expect?     print(type(value).__name__)
2. Is it the value I expect?           print(repr(value))
3. Did I store the result?             check the assignment on the left
4. Did I strip and lower the answer?   apply them before comparing
5. Did I convert before arithmetic?    int() or float() after input()
6. Is the format spec correct?         {value:>10} not {value:10>}
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Call print() and input() with parentheses and matching brackets.
- Never add text and numbers with + without str() or an f-string.
- input() returns text: validate first, then convert.
- strip() and lower() before comparing user answers.
- Check for zero before dividing by user input.
- print() returns None, so never store its result.
""")