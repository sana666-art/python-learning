"""Topic 1: Introduction to Data Types

A data type tells you what kind of value something holds and what you can do
with it. Python decides the type from the value you write.

This folder covers the basic types:

    int     whole numbers          42, -7, 0
    float   decimal numbers        3.14, -0.5
    str     text                   "hello", 'Ali'
    bool    True or False          True, False
    None    the absence of a value None

list, tuple, set and dict are also data types, but they have so many
operations that they get their own sections later.

Run with:  python 01-introduction-to-data-types.py
"""

print("=" * 60)
print("WHAT IS A DATA TYPE?")
print("=" * 60)
print("""
A data type answers two questions:

1. What kind of value is this?
2. What can I do with it?

For example, 5 is an int, so you can add it. "5" is a str, so you can join it
with other text. Same looking characters, different behaviour.
""")

print("=" * 60)
print("PYTHON IS DYNAMICALLY TYPED")
print("=" * 60)
print("You never write the type in the code. Python infers it at runtime.")

count = 42
price = 3.14
name = "Ali"
is_open = True
missing = None

print("count   =", count, "  Python decides: int")
print("price   =", price, "  Python decides: float")
print("name    =", name, "  Python decides: str")
print("is_open =", is_open, "  Python decides: bool")
print("missing =", missing, "  Python decides: NoneType")
print()
print("The same name can point to different types at different moments.")

status = 1
print("status  =", status)
status = "waiting"
print("status  =", status)

print()
print("=" * 60)
print("THE TYPES COVERED IN THIS FOLDER")
print("=" * 60)
print("""
Type      Example      Purpose
------    ---------    ---------------------------
int       42, -7       whole numbers, counting
float     3.14, -0.5   decimals, measurements
str       "hello"      text, names, sentences
bool      True, False  yes or no, on or off
NoneType  None         nothing, no value yet

Later folders cover the collection types:
list, tuple, set, dict
""")

print("=" * 60)
print("MEETING THE TYPES IN CODE")
print("=" * 60)

whole = 42
decimal = 3.14
negative = -17
text = "Python"
answer = True
empty = None

print("whole   =", repr(whole), "type:", type(whole).__name__)
print("decimal =", repr(decimal), "type:", type(decimal).__name__)
print("negative=", repr(negative), "type:", type(negative).__name__)
print("text    =", repr(text), "type:", type(text).__name__)
print("answer  =", repr(answer), "type:", type(answer).__name__)
print("empty   =", repr(empty), "type:", type(empty).__name__)

print()
print("repr() shows the value the way Python stores it, so you can see the")
print("quotes around a string.")

print()
print("=" * 60)
print("WHY TYPES MATTER")
print("=" * 60)
print("1. Operations depend on the type.")
print("   5 + 5        gives 10")
print('   "5" + "5"    gives "55"')
print("   Mixing them raises TypeError. See the line below:")
try:
    print(5 + "5")
except TypeError as error:
    print("   5 + '5' ->", type(error).__name__, ":", error)

print()
print("2. Comparisons depend on the type.")
print('   5 == "5"  is', 5 == "5", "because the types differ")
print("   5 == 5    is", 5 == 5)

print()
print("3. Conversion problems appear when reading user input.")
print("   input() always returns text, so numbers must be converted.")

print()
print("=" * 60)
print("HOW PYTHON CHOOSES THE TYPE")
print("=" * 60)
print("Look at how you write the value:")

print("42            no dot, no quotes     -> int")
print("4.2           has a dot            -> float")
print('"42"          quotes               -> str')
print("True          no quotes, T capital -> bool")
print("None          no quotes            -> NoneType")
print()

print("=" * 60)
print("THE COMMON BUILTIN TYPES")
print("=" * 60)

values = [42, 3.14, "Python", True, False, None, 1_000_000, 7, -3, 0.5]
print("Value            repr()            type()")
print("-" * 50)
for value in values:
    print(f"{str(value):<16} {repr(value):<18} {type(value).__name__}")

print()
print("=" * 60)
print("CHECKING A TYPE AT ANY TIME")
print("=" * 60)
print("Use type() to ask, and isinstance() to test safely:")

value = 42
print("type(value)              :", type(value))
print("type(value).__name__     :", type(value).__name__)
print("isinstance(value, int)   :", isinstance(value, int))
print("isinstance(value, str)   :", isinstance(value, str))

print()
print("=" * 60)
print("A QUICK LOOK AT THE COLLECTION TYPES")
print("=" * 60)
print("""
These are mentioned only so you recognise them. They get their own sections
because they have many operations.

list     [1, 2, 3]      ordered, changeable, allows duplicates
tuple    (1, 2, 3)      ordered, unchangeable, allows duplicates
set      {1, 2, 3}      unordered, changeable, no duplicates
dict     {"a": 1}       key and value pairs

In this folder we use a list and a dict only to display tables of examples.
""")

numbers = [1, 2, 3]
letters = {"a": 1, "b": 2}
print("list example :", numbers, "->", type(numbers).__name__)
print("dict example :", letters, "->", type(letters).__name__)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- A data type tells you what a value is and what you can do with it.
- Python is dynamically typed, so it infers the type from the value.
- Basic types: int, float, str, bool, None.
- type() tells you the type, isinstance() checks it.
- The same characters can be different types, and that changes what works.
- list, tuple, set and dict come later.
""")