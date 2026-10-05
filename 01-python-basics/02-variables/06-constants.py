"""Topic 6: Constants

A constant is a value that should not change after you set it. Python has no
real constant keyword, so it uses naming conventions.

Run with:  python 06-constants.py
"""

print("=" * 60)
print("WHAT IS A CONSTANT?")
print("=" * 60)
print("""
A constant holds a value that stays the same for the whole program.

Examples:
- Pi = 3.14159
- MAX_MARKS = 100
- GRAVITY = 9.81

Writing them in ALL CAPS tells the reader that the value is fixed.
""")

print("=" * 60)
print("THE UPPERCASE CONVENTION")
print("=" * 60)
print("PEP 8: constants are written in upper case with underscores.")

MAX_MARKS = 100
PASS_MARKS = 40
PI = 3.14159
DEFAULT_TAX_RATE = 0.17
COURSE_NAME = "Introduction to Python"

print("MAX_MARKS        =", MAX_MARKS)
print("PASS_MARKS       =", PASS_MARKS)
print("PI               =", PI)
print("DEFAULT_TAX_RATE =", DEFAULT_TAX_RATE)
print("COURSE_NAME      =", COURSE_NAME)

print()
print("Notice the difference between the two styles:")
tax_rate = 0.17        # a value that may change
INTEREST_RATE = 0.05   # a fixed rate
print("lower case is for changing values, UPPER CASE is for fixed values")

print()
print("=" * 60)
print("USING CONSTANTS IN A CALCULATION")
print("=" * 60)

radius = 5
area = PI * radius ** 2
print("radius =", radius)
print("area = PI * radius ** 2 ->", round(area, 2))
print("If PI changes, every calculation updates. One place to edit.")

total_marks = 450
obtained = 387
percentage = obtained / total_marks * 100
is_pass = obtained >= PASS_MARKS
print()
print("total_marks =", total_marks, "| obtained =", obtained)
print("percentage  =", round(percentage, 2))
print("PASS_MARKS  =", PASS_MARKS, "| is_pass =", is_pass)

price = 2000
tax = price * DEFAULT_TAX_RATE
print("price =", price, "| tax =", round(tax, 2), "| total =", round(price + tax, 2))

print()
print("=" * 60)
print("IMPORTANT: UPPER CASE IS A CONVENTION, NOT A RULE")
print("=" * 60)
print("Python will not stop you from changing a constant.")
print("Uncomment the lines below to see it happen:")
print()
print("#   MAX_MARKS = 200")
print("#   print(MAX_MARKS)   # runs fine, no warning from Python")

print("Two extra tools exist, but are advanced for now:")
print("  enum.Enum     used when you want a set of named fixed values")
print("  typing.Final  used by type checkers to flag changes")
print("For beginner code, UPPER CASE naming is enough.")

print()
print("=" * 60)
print("CONSTANTS INSIDE A CLASS")
print("=" * 60)
print("Class-level constants are written in upper case too.")


class Rectangle:
    """Uses two constants to describe the unit square."""

    UNITS_IN_WIDTH = 1.0
    UNITS_IN_HEIGHT = 1.0

    def area(self):
        return self.UNITS_IN_WIDTH * self.UNITS_IN_HEIGHT


rect = Rectangle()
print("UNITS_IN_WIDTH  =", Rectangle.UNITS_IN_WIDTH)
print("UNITS_IN_HEIGHT =", Rectangle.UNITS_IN_HEIGHT)
print("rect.area()     =", rect.area())
print("Read the code and you can tell these values are meant to stay fixed.")

print()
print("=" * 60)
print("NAMING RULES FOR CONSTANTS")
print("=" * 60)
print("""
- All upper case: MAX_ATTEMPTS, not MaxAttempts
- Separate words with underscores: MAX_LOGIN_ATTEMPTS
- Short and descriptive: TAX_RATE is better than RATE_OF_TAX_APPLICATION
- Put constants near the top of the file so they are easy to find
""")

print("=" * 60)
print("CONSTANT vs VARIABLE: SIDE BY SIDE")
print("=" * 60)

MAX_RETRIES = 3          # constant, should not change
attempts = 0              # variable, increases each try

while attempts < MAX_RETRIES:
    attempts += 1
    print(f"attempt {attempts} of {MAX_RETRIES}")

print()
print("MAX_RETRIES is the limit, attempts is the running count.")
print("The code reads clearly because the naming shows the difference.")