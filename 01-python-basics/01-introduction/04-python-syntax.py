"""Topic 4: Python Syntax

Syntax means the rules you must follow when writing Python code. Python has
very few rules, but the ones it has must be followed exactly.

Run with:  python 04-python-syntax.py
"""

print("=" * 60)
print("RULE 1: INDENTATION MATTERS")
print("=" * 60)
print("Python uses indentation (spaces at the start of a line) to define blocks")
print("of code. Four spaces is the standard. Indenting wrongly causes errors.")


# Correct structure: the body of the if is indented one level (4 spaces)
age = 20
if age >= 18:
    print("You are allowed to vote.")
    print("You are an adult.")
else:
    print("You are not an adult.")

print("Notice both lines under 'if' are indented by exactly 4 spaces.")

print()
print("=" * 60)
print("RULE 2: STATEMENTS")
print("=" * 60)
print("A statement is one complete instruction. It usually ends on its own line,")
print("and semicolons are optional, so you almost never need them.")

name = "Bilal"          # assignment statement
print("My name is Bilal")  # function call statement
print("2 + 3 =", 2 + 3)    # expression statement

print()
print("=" * 60)
print("RULE 3: CASE SENSITIVITY")
print("=" * 60)
print("Python distinguishes between uppercase and lowercase letters.")
print("name, Name and NAME are three different variables.")

name = "Ali"
Name = "Ahmed"
NAME = "Usman"
print("name =", name)
print("Name =", Name)
print("NAME =", NAME)
print("print and Print are also different. Using Print raises NameError.")

print()
print("=" * 60)
print("RULE 4: OTHER BASIC RULES")
print("=" * 60)
print("1. Variable names cannot start with a number or a special character.")
print("   Good: user_name, total2, _count")
print("   Bad : 2total, user-name, $total")
print("2. Variable names cannot use spaces.")
print("   Use user_name instead of 'user name'.")
print("3. Strings must be written in matching quotes.")
print("   'single', \"double\", and triple quotes '''for multiple lines''' all work.")
print("4. Comments start with # and are ignored by Python.")
print("   This whole line is a comment.")
print("5. Python is whitespace sensitive: extra blank lines are allowed,")
print("   but extra spaces in the middle of an expression are not.")

print()
print("=" * 60)
print("PRACTICE: VALID VS INVALID NAMES")
print("=" * 60)

user_name = "valid"
total2 = "valid"
_private = "valid"
print(user_name, "|", total2, "|", _private)

print()
print("These would cause SyntaxError or NameError:")
print("  2nd_total  = 10   # cannot start with a digit")
print("  user-name  = 10   # minus sign is subtraction")
print("  class      = 10   # reserved keyword")

print()
print("=" * 60)
print("KEYWORDS YOU CANNOT USE AS VARIABLE NAMES")
print("=" * 60)
print("False, None, True, and, as, assert, async, await, break, class,")
print("continue, def, del, elif, else, except, finally, for, from, global,")
print("if, import, in, is, lambda, nonlocal, not, or, pass, raise, return,")
print("try, while, with, yield, match, case")