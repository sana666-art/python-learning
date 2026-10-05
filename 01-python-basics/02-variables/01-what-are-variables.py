"""Topic 1: What Are Variables?

A variable is a name that refers to a value stored in memory. You use the
name to read or change that value later.

Run with:  python 01-what-are-variables.py
"""

print("=" * 60)
print("WHAT IS A VARIABLE?")
print("=" * 60)
print("""
Think of a variable as a labelled box:

    variable name  ->  box with a label on it
    value          ->  what is inside the box

When you write  price = 100

- price  is the name of the variable
- =      is the assignment operator
- 100   is the value being stored
""")

price = 100
print("price holds the value", price)

print()
print("=" * 60)
print("VARIABLES LET YOU REUSE A VALUE")
print("=" * 60)
print("Without variables you would repeat the number everywhere.")
print("With one variable you change it in a single place.")

tax = 0.10
total_before_tax = 500
total_after_tax = total_before_tax + (total_before_tax * tax)

print("Price            :", total_before_tax)
print("Tax rate         :", tax)
print("Total after tax  :", total_after_tax)

print()
print("Change the tax rate to 0.20 and everything updates automatically.")

print()
print("=" * 60)
print("HOW PYTHON STORES VALUES")
print("=" * 60)
print("When you assign a value, Python:")
print("1. Creates an object in memory holding the value.")
print("2. Points the name at that object.")
print("3. Sends the reference to the object to the variable.")
print()
print("So a variable is really a name pointing to an object.")

a = 10
b = a
print("a =", a, "| b =", b)
print("a and b point to the same value, so changing a does not change b:")
a = 99
print("a =", a, "| b =", b, "(b kept the old value)")
print("This shows two names, two separate boxes.")

print()
print("=" * 60)
print("VARIABLES CAN HOLD ANYTHING")
print("=" * 60)
print("A variable can hold a number, text, a list, a dictionary, or even")
print("another variable. Types are covered in 03-data-types, so here we")
print("only show what a variable can point to.")

number = 42
text = "Python"
items = [1, 2, 3]
person = {"name": "Ali", "age": 20}

print("number ->", number)
print("text   ->", text)
print("items  ->", items)
print("person ->", person)

print()
print("You can ask what a variable holds with type():")
print("type(number):", type(number).__name__)
print("type(text)  :", type(text).__name__)
print("type(items) :", type(items).__name__)
print("type(person):", type(person).__name__)

print()
print("=" * 60)
print("A VARIABLE MUST EXIST BEFORE YOU USE IT")
print("=" * 60)
print("Reading a variable before assigning it raises NameError.")
print("These two lines are commented out because they would stop the script:")
print()
print("#   print(greeting)      # NameError, not defined yet")
print("#   greeting = 'Hello'")
print("#   print(greeting)      # works, now it exists")

print()
print("=" * 60)
print("VARIABLES ARE CASE SENSITIVE")
print("=" * 60)
print("name and Name are two different variables.")
name = "lower case"
Name = "capital N"
print("name =", name)
print("Name =", Name)