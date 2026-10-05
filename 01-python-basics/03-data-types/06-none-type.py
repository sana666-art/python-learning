"""Topic 6: The None Type

None is the single value of the NoneType. It means no value, nothing, not set
yet, or not applicable.

Run with:  python 06-none-type.py
"""

print("=" * 60)
print("WHAT IS None?")
print("=" * 60)
print("""
None is Python's way of saying there is no value here.

Common meanings:
- a variable has not been given a value yet
- a function returns nothing
- a result was not found
- a value is deliberately not applicable

It is not the same as 0, False or an empty string. It is its own type.
""")

value = None
print("value        =", repr(value))
print("print shows  :", value)
print("type         =", type(value).__name__)

print()
print("None is also written as NoneType when you print the type.")

print()
print("=" * 60)
print("None IS NOT ZERO, False OR EMPTY")
print("=" * 60)
print("""
None == 0    -> False
None == False -> False
None == ""    -> False

None is falsy, so it behaves like False in a condition, but it is a
different type and a different value.
""")

print("None == 0     ->", None == 0)
print("None == False ->", None == False)
print('None == ""    ->', None == "")
print("bool(None)    ->", bool(None))

print()
print("=" * 60)
print("CHECKING FOR None")
print("=" * 60)
print("""
Use the is keyword:

    if value is None:

Never write  if value == None:  even though it works for None, == can be
overridden by custom objects and None is a singleton, so is is correct and
faster.
""")

result = None
if result is None:
    print("result is None, so there is nothing to show yet")

print()
print("More examples:")

for value in [None, 0, False, "", [], "text", 1]:
    if value is None:
        print(f"   {value!r:<8} -> is None")
    else:
        print(f"   {value!r:<8} -> not None")

print()
print("=" * 60)
print("WHERE None APPEARS")
print("=" * 60)

print("1. A variable declared but not yet given a value.")
result = None
print("   result = None")
result = 42
print("   later   =", result)

print()
print("2. A function that returns nothing.")


def greet_silently():
    """Does some work and returns nothing."""


value = greet_silently()
print("   greet_silently() returned:", repr(value))

print()
print("3. A search that found nothing.")


def find_index(items, target):
    """Return the position of target, or None when it is not present."""
    for position, item in enumerate(items):
        if item == target:
            return position
    return None


fruits = ["apple", "banana", "mango"]
print("   find_index(fruits, 'banana') ->", find_index(fruits, "banana"))
print("   find_index(fruits, 'grape')  ->", find_index(fruits, "grape"))
print("   The second call returned None, which is how you signal not found.")

print()
print("=" * 60)
print("THE NoneType TYPE")
print("=" * 60)
print("None is the only value that has the type NoneType.")

print("type(None)          ->", type(None))
print("type(None).__name__ ->", type(None).__name__)
print("isinstance(None, type(None)) ->", isinstance(None, type(None)))

print()
print("=" * 60)
print("PATTERN: DEFAULT IS None, THEN FILL IT LATER")
print("=" * 60)


def calculate_discount(total, is_member):
    """Return the final amount after any discount."""
    discount = None
    if is_member:
        discount = total * 0.10
    if discount is not None:
        return total - discount
    return total


print("calculate_discount(1000, True)  ->", calculate_discount(1000, True))
print("calculate_discount(1000, False) ->", calculate_discount(1000, False))
print("None as a marker lets the function say no discount was applied.")

print()
print("=" * 60)
print("NONE IN A DICTIONARY")
print("=" * 60)
print("A missing value is often stored as None rather than left out.")

student = {"name": "Ali", "result": None}
print("student            =", student)
print('student["result"]  =', repr(student["result"]))
print('"result" in student:', "result" in student)
print("The key exists, so the value is known to be missing.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Comparing with == instead of is.
   Use  if value is None:   not  if value == None:
2. Writing None with quotes.
   'None'  is the four character string, not the None value.
3. Testing None with if value:  works, because None is falsy, but is None
   states the intent more clearly.
4. Trying to use None in arithmetic.
   None + 1  raises TypeError, so check for None first.
""")

nothing = None
try:
    print(nothing + 1)
except TypeError as error:
    print("   None + 1 ->", type(error).__name__, ":", error)

print()
print('"None" == None ->', "None" == None)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- None is the single value of NoneType and means no value.
- It is not 0, not False and not an empty string.
- Check it with  is None,  never with == None.
- It appears as a default, as a return value for not found, and as a
  placeholder before a value is known.
- None is falsy, so it works in conditions, but tests with is read better.
""")