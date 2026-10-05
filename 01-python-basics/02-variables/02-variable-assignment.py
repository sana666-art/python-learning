"""Topic 2: Variable Assignment

Assignment means storing a value in a variable using =.

Run with:  python 02-variable-assignment.py
"""

print("=" * 60)
print("THE ASSIGNMENT OPERATOR")
print("=" * 60)
print("Syntax:  variable_name = value")
print("Read it as: store value IN variable_name")

country = "Pakistan"
print("country =", country)

print()
print("=" * 60)
print("BASIC ASSIGNMENTS")
print("=" * 60)

name = "Ahmed"
age = 20
height = 5.8
is_student = True
city = "Lahore"

print("name       =", name)
print("age        =", age)
print("height     =", height)
print("is_student =", is_student)
print("city       =", city)

print()
print("=" * 60)
print("NO SPACE BEFORE THE EQUALS SIGN")
print("=" * 60)
print("PEP 8 style writes the equals sign with one space on each side.")
print("Both of these work, but use the spaced form:")
x = 5
print("x = 5   is correct style")
print("x=5   also runs, but avoid it")

print()
print("=" * 60)
print("ASSIGNING FROM EXPRESSIONS")
print("=" * 60)
print("The right side can be any expression. Python evaluates it first,")
print("then stores the result.")

a = 10
b = 4
print("a =", a, "| b =", b)
print("sum    = a + b   ->", a + b)
print("diff   = a - b   ->", a - b)
print("prod   = a * b   ->", a * b)
print("quot   = a / b   ->", a / b)
print("floor  = a // b  ->", a // b)
print("mod    = a % b   ->", a % b)
print("power  = a ** b  ->", a ** b)

print()
print("=" * 60)
print("ASSIGNING TO AN EXPRESSION USING OTHER VARIABLES")
print("=" * 60)

first_name = "Ali"
last_name = "Khan"
full_name = first_name + " " + last_name
doubled = 21 * 2
upper_city = "karachi".upper()

print("first_name =", first_name)
print("last_name  =", last_name)
print("full_name  =", full_name)
print("doubled    =", doubled)
print("upper_city =", upper_city)

print()
print("=" * 60)
print("CHAINED ASSIGNMENT")
print("=" * 60)
print("Several variables can share one value with = = =")
x = y = z = 100
print("x =", x)
print("y =", y)
print("z =", z)
print("All three point to the same object, so changing one changes it for all:")
x = 200
print("after x = 200  ->  x =", x, "y =", y, "z =", z)
print("This is why chain assignment is risky for values you want separate.")

print()
print("=" * 60)
print("AUGMENTED ASSIGNMENT")
print("=" * 60)
print("Combine an operation with assignment using one symbol.")

count = 10
count += 5
print("count = 10, then count += 5  ->", count)
count -= 3
print("count -= 3                   ->", count)
count *= 2
print("count *= 2                   ->", count)
count /= 4
print("count /= 4                   ->", count)

score = 10
score += 5
score *= 3
print("score: 10 + 5, then * 3      ->", score)

text = "Py"
text += "thon"
print('text = "Py", then text += "thon" ->', text)

print()
print("=" * 60)
print("THE VALUE CAN CHANGE TYPE AFTER ASSIGNMENT")
print("=" * 60)
print("Python has no fixed type for a variable, so a name can point to")
print("different kinds of values over time. Types are studied in")
print("03-data-types.")

value = 10
print("value =", value)
value = "now a string"
print("value =", value)
value = [1, 2, 3]
print("value =", value)
print("Same name, different values at different moments.")

print()
print("=" * 60)
print("COMMON ASSIGNMENT MISTAKES")
print("=" * 60)
print("1. Using a variable before assigning it  -> NameError")
print("2. Writing = and == interchangeably     -> = assigns, == compares")
print("3. Forgetting quotes around text        -> NameError")
print('   name = Ali      fails, because Ali is not a value Python knows')
print('   name = "Ali"    correct')
print("4. Typing a variable name wrong         -> NameError, check spelling")
print("5. Assigning to a reserved word          -> SyntaxError, e.g. class = 5")