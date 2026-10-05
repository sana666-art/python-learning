"""Topic 7: The type() Function and Type Checking

type() tells you the type of a value. This file covers type(), isinstance()
and the related checking tools.

Run with:  python 07-type-function.py
"""

print("=" * 60)
print("type() RETURNS THE TYPE OF A VALUE")
print("=" * 60)

value = 42
print("value          =", value)
print("type(value)    =", type(value))
print("type(value).__name__ =", type(value).__name__)

print()
print("Print the name instead when you only want to read it, because")
print("type() returns the class itself rather than a readable name.")

print()
print("=" * 60)
print("type() ON EACH BASIC TYPE")
print("=" * 60)

samples = [42, -7, 0, 3.14, "Python", True, False, None]
print(f"{'value':<12}{'repr':<12}{'type()':<28}{'__name__'}")
print("-" * 64)
for value in samples:
    print(f"{str(value):<12}{repr(value):<12}{str(type(value)):<28}{type(value).__name__}")

print()
print("=" * 60)
print("COMPARING TYPES")
print("=" * 60)
print("Use == to compare two type objects.")

number = 42
print("type(number) == int   ->", type(number) == int)
print("type(number) == str   ->", type(number) == str)
print("type(number) == type(42) ->", type(number) == type(42))

print()
print("=" * 60)
print("THE EXACT TYPE PROBLEM")
print("=" * 60)
print("""
type(x) == int is an exact check. It says nothing about a subclass.

bool is a subclass of int in Python, and True is an instance of int:

    type(True) == int      -> False, because type(True) is bool
    isinstance(True, int)  -> True, because bool inherits from int
""")

value = True
print("type(True)              =", type(True).__name__)
print("type(True) == int       ->", type(True) == int)
print("isinstance(True, int)   ->", isinstance(True, int))
print("isinstance(True, bool)  ->", isinstance(True, bool))
print("So an exact type check can surprise you with booleans.")

print()
print("=" * 60)
print("isinstance(): THE SAFER CHECK")
print("=" * 60)
print("isinstance(value, type_or_tuple) returns True or False.")

value = 42
print('isinstance(value, int)                ->', isinstance(value, int))
print('isinstance(value, (int, float))       ->', isinstance(value, (int, float)), " (a tuple means any of)")
print('isinstance(value, str)                ->', isinstance(value, str))
print('isinstance(3.14, int)                 ->', isinstance(3.14, int))

print()
print("A tuple of types is useful for values that could be one of several:")
mixed = [42, 3.14, "text", True, None]
for value in mixed:
    print(f"   {repr(value):<10} -> {type(value).__name__}")

print()
print("=" * 60)
print("WRITING A CHECK THAT ACCEPTS SEVERAL TYPES")
print("=" * 60)


def describe(value):
    """Describe a value using isinstance checks."""
    if value is None:
        return "None, nothing here"
    if isinstance(value, bool):
        return "a boolean"
    if isinstance(value, (int, float)):
        return "a number"
    if isinstance(value, str):
        return "text"
    return "something else"


for value in [42, 3.14, "Python", True, None, [1, 2]]:
    print(f"   {value!r:<12} is {describe(value)}")

print()
print("Note the order: bool is checked before int, because bool is an int.")
print("If you checked int first, True would be reported as a number.")

print()
print("=" * 60)
print("ID(): IS THIS THE SAME OBJECT?")
print("=" * 60)
print("id() returns the memory address of an object.")

a = 42
b = 42
print("a = 42, b = 42")
print("id(a)          =", id(a))
print("id(b)          =", id(b))
print("a == b         ->", a == b, " (same value)")
print("a is b         ->", a is b, " (may be the same object or not)")
print("Small integers are often interned, so identity can be True.")
print("id() is useful for debugging, not for normal comparisons.")

print()
print("=" * 60)
print("THE is OPERATOR FOR None, True and False")
print("=" * 60)
print("""
None, True and False are singletons, so is always works and is the correct
check:

    if value is None:
    if flag is True:
    if other is False:
""")

value = None
print("value is None    ->", value is None)
print("value == None    ->", value == None, "(works, but is less clear)")

print()
print("=" * 60)
print("type() WITH A VARIABLE THAT HAS NO VALUE YET")
print("=" * 60)

value = None
print("value        =", repr(value))
print("type(value)  =", type(value).__name__, "(the type exists even though the value is None)")

print()
print("=" * 60)
print("CHECKING MANY VALUES AT ONCE")
print("=" * 60)
print("You can compare types in a loop, which is handy for validation.")

values = [10, 20.5, "hello", True, None, [1], (1,), {1, 2}, {"a": 1}]
print(f"{'value':<14}{'type':<12}{'is int?':<10}{'is str?':<10}{'is None?'}")
print("-" * 56)
for value in values:
    print(
        f"{str(value):<14}"
        f"{type(value).__name__:<12}"
        f"{str(isinstance(value, int)):<10}"
        f"{str(isinstance(value, str)):<10}"
        f"{value is None}"
    )

print()
print("=" * 60)
print("TYPE ERRORS YOU WILL MEET")
print("=" * 60)

print("1. Mixing incompatible types in an operation:")
try:
    print(42 + " years")
except TypeError as error:
    print("   42 + ' years' ->", type(error).__name__, ":", error)

print()
print("2. Calling something that is not a function:")
try:
    print("text"())
except TypeError as error:
    print("   'text'() ->", type(error).__name__, ":", error)

print()
print("3. Using None in arithmetic:")
try:
    print(None + 1)
except TypeError as error:
    print("   None + 1 ->", type(error).__name__, ":", error)

print()
print("4. Indexing a type that does not support it:")
try:
    print(42[0])
except TypeError as error:
    print("   42[0] ->", type(error).__name__, ":", error)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- type(value) returns the type, and type(value).__name__ gives a readable name.
- Comparing types with == is an exact check: type(True) == int is False.
- isinstance(value, int) checks the type and any parent types, which is safer.
- isinstance(value, (int, float)) accepts several types at once.
- id() shows the memory address, useful for debugging only.
- Use  is None  for None, True and False.
""")