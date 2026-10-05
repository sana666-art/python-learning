"""Topic 2: Features of Python

This script shows, with runnable examples, the features that make Python
beginner friendly: simplicity, high-level design, interpretation, dynamic
typing, object-orientation, and a large standard library.

Run with:  python 02-features-of-python.py
"""

print("=" * 60)
print("1. EASY TO LEARN")
print("=" * 60)
print('Python syntax is close to plain English.')
print("You write one instruction per line and no semicolons are needed.")

greeting = "Hello"
name = "Ali"
print(greeting + ", " + name + "!")

print()
print("=" * 60)
print("2. HIGH-LEVEL LANGUAGE")
print("=" * 60)
print("You focus on WHAT to do; Python handles the low-level details,")
print("such as memory management, for you.")
print("Adding two numbers requires no type declaration and no manual memory work.")
a = 10
b = 32
print(f"{a} + {b} = {a + b}")

print()
print("=" * 60)
print("3. INTERPRETED")
print("=" * 60)
print("Python runs the code line by line, so you get results immediately")
print("and errors point to the exact line that failed.")
print("No separate build or compile step is required.")

print()
print("=" * 60)
print("4. DYNAMICALLY TYPED")
print("=" * 60)
print("A variable can hold any value. The type is decided at runtime.")
value = 10
print("value is", value, "->", type(value).__name__)
value = "ten"
print("value is", value, "->", type(value).__name__)
value = 10.5
print("value is", value, "->", type(value).__name__)
print("You can check a type any time with type() and isinstance().")
print("isinstance(value, float):", isinstance(value, float))

print()
print("=" * 60)
print("5. OBJECT-ORIENTED")
print("=" * 60)
print("Everything in Python is an object, and classes bundle data with actions.")


class Student:
    """A simple class showing objects, attributes and methods."""

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 50:
            return "Pass"
        return "Fail"


student = Student("Sara", 78)
print("Student  :", student.name)
print("Marks    :", student.marks)
print("Result   :", student.result())
print("Student is an object of type:", type(student).__name__)

print()
print("=" * 60)
print("6. LARGE STANDARD LIBRARY")
print("=" * 60)
print("Batteries are included: modules for maths, dates, files and more")
print("come with Python, so you do not install extra packages for them.")
import math
import datetime

print("Square root of 144:", math.sqrt(144))
print("Value of pi       :", round(math.pi, 4))
print("Today's date      :", datetime.date.today())
print("Number of days in the standard library: hundreds of modules.")

print()
print("=" * 60)
print("BONUS: PORTABLE AND CROSS-PLATFORM")
print("=" * 60)
print("The same Python code runs on Windows, macOS and Linux.")
print("Cross-platform means you write the code once and it works everywhere.")