"""Topic 3: Variable Naming Rules

Names are not free. Python enforces a few rules and expects good habits.

Run with:  python 03-variable-naming-rules.py
"""

print("=" * 60)
print("RULE 1: LETTERS, DIGITS AND UNDERSCORE ONLY")
print("=" * 60)
print("A name may contain a-z, A-Z, 0-9 and _ and nothing else.")

user_name = "Ali"
name2 = "Ahmed"
_name = "leading underscore is allowed"
print("user_name, name2, _name all work.")

print()
print("=" * 60)
print("RULE 2: CANNOT START WITH A DIGIT")
print("=" * 60)
print("Valid:   student1, course2, mark_total")
print("Invalid: 2student, 1st_place   SyntaxError")
print("Workaround: start with a letter or underscore")

year2026 = 2026
print("year2026 =", year2026)

print()
print("=" * 60)
print("RULE 3: NO SPACES")
print("=" * 60)
print('Valid:   full_name, my_var, total_marks')
print('Invalid: full name, my var   SyntaxError')
print("Use an underscore instead of a space.")

print()
print("=" * 60)
print("RULE 4: CANNOT USE RESERVED KEYWORDS")
print("=" * 60)
print("These words have a fixed meaning in Python.")
print("Using one as a variable name causes a SyntaxError.")

reserved = [
    "False", "None", "True", "and", "as", "assert", "async", "await",
    "break", "class", "continue", "def", "del", "elif", "else",
    "except", "finally", "for", "from", "global", "if", "import", "in",
    "is", "lambda", "match", "nonlocal", "not", "or", "pass", "raise",
    "return", "try", "while", "with", "yield",
]
for row in range(0, len(reserved), 7):
    print("  " + ", ".join(reserved[row:row + 7]))

print()
print("=" * 60)
print("RULE 5: CASE SENSITIVE")
print("=" * 60)
print("These are four separate variables:")
Age = 20
age = 21
AGE = 22
aGe = 23
print("Age =", Age, "| age =", age, "| AGE =", AGE, "| aGe =", aGe)

print()
print("=" * 60)
print("RULE 6: AVOID NAMES THAT SHADOW BUILTINS")
print("=" * 60)
print("A variable can overwrite a built-in function such as print or list.")
print("Python allows it, but your code then breaks.")

# Uncomment to see the damage:
# list = [1, 2, 3]
# print(list([4, 5]))   # TypeError: 'list' object is not callable

# Bad variable names to avoid:
print("Avoid: list, dict, str, int, type, sum, max, min, print, id, input")

print()
print("=" * 60)
print("GOOD NAMING PRACTICE (PEP 8)")
print("=" * 60)
print("""
- Use lower_case_with_underscores for normal variables
- No capital letters in the middle of a name
- Keep names short but meaningful: n is poor, total_marks is good
- Do not use single letters except for a loop counter or a maths symbol
- Use is_ or has_ for booleans: is_student, has_permission
""")

# A name for a whole calculation
total_marks = 450
obtained_marks = 387
percentage = obtained_marks / total_marks * 100
print("percentage =", round(percentage, 2))

# A name for a description
book_title = "Python Basics"
is_available = True
print("book_title   =", book_title)
print("is_available =", is_available)

print()
print("=" * 60)
print("VALID NAMES YOU CAN USE")
print("=" * 60)

name = "Ali"
_name = "allowed"
user_id_2 = "allowed"
itemPrice = "valid syntax, but not Python style"
very_long_variable_name_that_is_still_legal = 1

print("name, _name, user_id_2 all follow the rules")
print("itemPrice is valid but should be written item_price in Python style")
print("very long names are legal:", very_long_variable_name_that_is_still_legal)

print()
print("=" * 60)
print("NAMES THAT FAIL")
print("=" * 60)
print("These lines are commented out so the script can run.")
print("Each one raises a SyntaxError when uncommented:")
print()
print("   2nd_place = 1        # starts with a digit")
print("   my name = 'Ali'      # contains a space")
print("   my-name = 'Ali'      # contains a hyphen")
print("   user@name = 'Ali'    # contains a symbol")
print("   class = 10           # reserved keyword")
print("   $total = 10          # starts with a symbol")