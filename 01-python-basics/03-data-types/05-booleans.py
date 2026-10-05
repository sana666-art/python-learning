"""Topic 5: Booleans

bool holds only two values: True and False. They represent yes or no, true or
false, on or off.

Run with:  python 05-booleans.py
"""

print("=" * 60)
print("THE TWO BOOLEAN VALUES")
print("=" * 60)

is_student = True
has_permission = False

print("is_student    =", is_student)
print("has_permission =", has_permission)
print("type          =", type(is_student).__name__)

print()
print("Important details:")
print("1. Capital T and capital F. True is correct, true is a different name.")
print("2. They must have no quotes. 'True' is a string, not a boolean.")
print("3. They cannot be assigned to.")

print()
print("=" * 60)
print("COMPARISONS RETURN BOOLEANS")
print("=" * 60)

a = 10
b = 20
print(f"a = {a}, b = {b}")
print()
print("a == b  equal to         ->", a == b)
print("a != b  not equal to     ->", a != b)
print("a < b   less than        ->", a < b)
print("a > b   greater than     ->", a > b)
print("a <= b  less or equal    ->", a <= b)
print("a >= b  greater or equal ->", a >= b)

print()
print("String comparisons work too:")
print('"apple" == "apple"  ->', "apple" == "apple")
print('"apple" == "banana" ->', "apple" == "banana")
print('"apple" < "banana"  ->', "apple" < "banana", "(alphabetical order)")

print()
print("Chained comparisons compare in one go:")
print("0 < 5 < 10   ->", 0 < 5 < 10)
print("0 < 15 < 10  ->", 0 < 15 < 10)
print('"a" <= "b" <= "c" ->', "a" <= "b" <= "c")

print()
print("=" * 60)
print("THE bool() FUNCTION")
print("=" * 60)
print("bool() converts any value into True or False.")

print("bool(1)       ->", bool(1))
print("bool(0)       ->", bool(0))
print('bool("hello") ->', bool("hello"))
print('bool("")      ->', bool(""), "  (an empty string is False)")
print("bool([])      ->", bool([]), "  (an empty list is False)")
print("bool(None)    ->", bool(None), "  (None is False)")
print("bool(0.0)     ->", bool(0.0))

print()
print("=" * 60)
print("TRUTHINESS: WHAT IS TRUE AND WHAT IS FALSE")
print("=" * 60)
print("""
Anything is True unless it is one of these:

    False, None, 0, 0.0, 0j, "", [], {}, set(), ()

Everything else is True, including -1, "False" and 0.5.
""")

truthy_values = [1, -1, 0.5, "text", "False", [0], [None], {"a": 1}, 3.14]
falsy_values = [False, None, 0, 0.0, "", [], {}, set()]

print("True values:")
for value in truthy_values:
    print(f"   {value!r:<14} -> {bool(value)}")

print()
print("False values:")
for value in falsy_values:
    print(f"   {value!r:<14} -> {bool(value)}")

print()
print('Note: "False" as text is True, because it is a non-empty string.')

print()
print("=" * 60)
print("USING BOOLEANS IN CONDITIONS")
print("=" * 60)

age = 20
is_adult = age >= 18
print("age          =", age)
print("is_adult     =", is_adult)

if is_adult:
    print("Result       : allowed to vote")

print()
print("A boolean can be used directly, which is clearer than a raw number:")

username = ""
if username:
    print("not reached, an empty string is False")
else:
    print("username is empty, so please enter one")

balance = 15000
if balance:
    print("Account is active with a balance of", balance)

print()
print("=" * 60)
print("BOOLEANS IN LOGIC")
print("=" * 60)
print("and needs both to be True, or needs only one.")

has_account = True
is_verified = False
has_payment = True

print("has_account =", has_account)
print("is_verified =", is_verified)
print("has_payment =", has_payment)
print()
print("has_account and is_verified ->", has_account and is_verified)
print("has_account or is_verified  ->", has_account or is_verified)
print("has_payment and has_account ->", has_payment and has_account)
print("not is_verified             ->", not is_verified)

print()
print("Short circuit in action:")
print("has_payment and is_verified ->", has_payment and is_verified)
print("These print once, because 'and' stops at the first False value.")
print("'not' flips the value: not False becomes True")

print()
print("=" * 60)
print("BOOLEANS AS NUMBERS")
print("=" * 60)
print("bool is a subclass of int, so True behaves like 1 and False like 0.")

print("True + True    =", True + True)
print("False + True   =", False + True)
print("True * 10      =", True * 10)
print("int(True)      =", int(True))
print("int(False)     =", int(False))

print()
print("This is why sum() can count booleans:")
attendance = [True, False, True, True, False]
present = sum(attendance)
print("attendance    =", attendance)
print("present count =", present)

print()
print("=" * 60)
print("BOOLEANS IN ARITHMETIC COMPARISONS CHAINED WITH IF")
print("=" * 60)


def describe_temperature(celsius):
    """Return a description of the temperature as a string."""
    if celsius > 35:
        return "very hot"
    elif celsius > 25:
        return "warm"
    elif celsius > 15:
        return "mild"
    else:
        return "cold"


for reading in [40, 28, 20, 5]:
    print(f"{reading:>3} C is {describe_temperature(reading)}")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Using lowercase true or false. Python needs True and False.
2. Writing 'True' with quotes. That is a string, and it is always truthy.
3. Comparing with a single = inside if. Use if has_permission:
4. Testing if a value is True when a comparison would be better.
   if value:  only checks whether value is falsy, not what it should equal.
""")

print("Correct and incorrect ways to combine a string and a number:")
string_value = "5"
number_value = 5
try:
    print(string_value + number_value)
except TypeError as error:
    print('   "5" + 5 ->', type(error).__name__, ":", error)
print('   str("5") + str(5) =', str(string_value) + str(number_value))

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- bool has exactly two values: True and False, with capital letters.
- Comparisons, membership tests and logical operators return booleans.
- bool() converts a value, and falsy values are False, None, 0 and empty
  collections.
- and, or and not combine booleans, and short circuit to save work.
- True behaves like 1 and False like 0, so sum() can count them.
""")