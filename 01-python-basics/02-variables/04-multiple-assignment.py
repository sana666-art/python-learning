"""Topic 4: Multiple Assignment

Assign several variables in one line. Useful for swapping values and for
short two-variable setups.

Run with:  python 04-multiple-assignment.py
"""

print("=" * 60)
print("ASSIGN MANY AT ONCE")
print("=" * 60)
print("Use commas between the names and the values.")

a, b, c = 10, 20, 30
print("a, b, c = 10, 20, 30")
print("a =", a, "| b =", b, "| c =", c)

x, y, z = 1, 2, 3
print("x, y, z = 1, 2, 3")
print("x =", x, "| y =", y, "| z =", z)

print()
print("=" * 60)
print("SWAPPING VARIABLES")
print("=" * 60)
print("Without a temporary variable, swapping looks wrong:")

first = "Ali"
second = "Sara"
print("before swap: first =", first, "| second =", second)
first, second = second, first
print("after  swap: first =", first, "| second =", second)
print("This is the clean Python way to swap.")

print()
print("=" * 60)
print("USING A TEMPORARY VARIABLE")
print("=" * 60)
print("You can also do it in three steps:")

p = 10
q = 20
print("before: p =", p, "| q =", q)
temp = p
p = q
q = temp
print("after : p =", p, "| q =", q)
print("Both give the same result. The tuple swap is shorter.")

print()
print("=" * 60)
print("MIXING DIFFERENT KINDS OF VALUES")
print("=" * 60)

name = "Ali"
age = 20
height = 5.8
is_student = True

name, age, height, is_student = "Bilal", 22, 6.1, False
print("name        =", name)
print("age         =", age)
print("height      =", height)
print("is_student  =", is_student)
print("Each name receives the value in the matching position.")

print()
print("=" * 60)
print("UNPACKING FROM A LIST OR TUPLE")
print("=" * 60)
print("A list or tuple with the right number of items can be spread out.")

marks = [88, 92, 79]
english, maths, physics = marks
print("marks =", marks)
print("english =", english, "| maths =", maths, "| physics =", physics)

coordinates = (3, 7)
x_coord, y_coord = coordinates
print("coordinates =", coordinates)
print("x_coord =", x_coord, "| y_coord =", y_coord)

print()
print("The number of names must match the number of values.")
print("Too few or too many names raises ValueError. Uncomment to test:")
print()
print("#   a, b = 1, 2, 3      # ValueError: too many values")
print("#   a, b, c = 1, 2      # ValueError: not enough values")

print()
print("=" * 60)
print("IGNORING VALUES YOU DO NOT NEED")
print("=" * 60)
print("Use an underscore for names you want to skip.")

student_name, _, student_city = ("Fatima", 21, "Islamabad")
print("Using _ to skip the age:")
print("student_name =", student_name)
print("student_city =", student_city)
print("Underscore means I do not need this value. It is conventional, not")
print("enforced, so do not rely on it in important code.")

print()
print("=" * 60)
print("MULTIPLE ASSIGNMENT WITH EXPRESSIONS")
print("=" * 60)
print("The right side is evaluated fully before anything is assigned, so the")
print("new values never affect each other.")

width = 10
height = 20
area, perimeter = width * height, 2 * (width + height)
print("width =", width, "| height =", height)
print("area =", area, "| perimeter =", perimeter)

a = 5
b = a * 2
a, b = b, a
print("a = 5, b = a * 2, then swap  ->  a =", a, "| b =", b)
print("The swap saw b as 10, so a became 10 and b became 5.")

print()
print("=" * 60)
print("WHEN TO USE MULTIPLE ASSIGNMENT")
print("=" * 60)
print("""
- Swapping two values
- Grouping related values on one line for readability
- Unpacking a small list or tuple
- Setting a few related defaults quickly

Avoid it when the values are unrelated, because the code becomes harder to
follow.
""")