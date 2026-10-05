"""Topic 8: Type Conversion

Type conversion turns a value from one type into another. It is also called
casting. This happens most often with input(), which always returns text.

Run with:  python 08-type-conversion.py
"""

print("=" * 60)
print("WHAT IS TYPE CONVERSION?")
print("=" * 60)
print("""
Convert a value by calling the target type as a function:

    int(value)
    float(value)
    str(value)
    bool(value)

The original value is untouched. The function returns a new value, so store
it:

    age = int(input("Enter your age: "))
""")

print("=" * 60)
print("CONVERTING TO int")
print("=" * 60)

print("int('42')      =", repr(int("42")))
print('int("42")      =', repr(int("42")))
print("int(42.9)      =", repr(int(42.9)), "  (truncates toward zero)")
print("int(-42.9)     =", repr(int(-42.9)), "  (also truncates toward zero)")
print('int("  42  ")  =', repr(int("  42  ")), "  (spaces are ignored)")
print("int(7 // 2)    =", repr(int(7 // 2)))

print()
print("int() truncates, it does not round. For rounding use round():")

number = 42.7
print("number         =", number)
print("int(number)    =", int(number), "  (down to 42)")
print("round(number)  =", round(number), "  (nearest, so 43)")

print()
print("=" * 60)
print("CONVERTING TO float")
print("=" * 60)

print('float("42")      =', repr(float("42")))
print('float("42.5")    =', repr(float("42.5")))
print("float(42)        =", repr(float(42)), "  (int becomes float)")
print('float("3.14")    =', repr(float("3.14")))
print('float("  2.5  ") =', repr(float("  2.5  ")))

print()
print("=" * 60)
print("CONVERTING TO str")
print("=" * 60)
print("str() turns any value into readable text.")

print("str(42)        =", repr(str(42)))
print("str(3.14)      =", repr(str(3.14)))
print("str(True)      =", repr(str(True)))
print("str(None)      =", repr(str(None)))
print('str(3.0)       =', repr(str(3.0)), "  (note the .0 is kept)")

print()
print("Numbers join with text only after str():")

number = 42
print('Correct: "Age: " + str(number)')
print("         ", "Age: " + str(number))
print('Correct: f"Age: {number}"')
print("         ", f"Age: {number}")
print()
try:
    print("Wrong:   " + "Age: " + number)
except TypeError as error:
    print('         "Age: " + number ->', type(error).__name__, ":", error)

print()
print("=" * 60)
print("CONVERTING TO bool")
print("=" * 60)
print("bool() applies the truthiness rules.")

print("bool(1)       =", bool(1))
print("bool(0)       =", bool(0))
print('bool("text")  =', bool("text"))
print('bool("")      =', bool(""))
print("bool(None)    =", bool(None))
print("bool([])      =", bool([]))

print()
print("=" * 60)
print("INVALID CONVERSIONS")
print("=" * 60)
print("""
Conversion can fail. The usual errors are:

    ValueError   the text is not a number at all
    TypeError    the value cannot be converted in any way

ValueError examples:
""")

for text in ["abc", "42abc", "", "3.5.7", "one two"]:
    try:
        result = int(text)
        print(f'   int({text!r:<10}) -> {result}')
    except ValueError as error:
        print(f'   int({text!r:<10}) -> {type(error).__name__}: {error}')

print()
print("TypeError examples:")

for value in [[1, 2], {"a": 1}, None]:
    try:
        result = int(value)
        print(f"   int({value!r:<10}) -> {result}")
    except TypeError as error:
        print(f"   int({value!r:<10}) -> {type(error).__name__}: {error}")

print()
print("=" * 60)
print("SAFER CONVERSION")
print("=" * 60)
print("""
Before converting user input, check it looks right, or catch the error.

isdigit() checks digits only.
isnumeric() and isdecimal() are close relatives worth knowing.
""")

text = "42"
print(f"text = {text!r}")
print("isdigit() ->", text.isdigit(), " (only digits, no sign or decimal point)")
print('int(text) ->', int(text))

print()
text = "42.5"
print(f"text = {text!r}")
print("isdigit() ->", text.isdigit(), " (the dot makes it False)")
print("float(text) ->", float(text))

print()
text = "-42"
print(f"text = {text!r}")
print("isdigit() ->", text.isdigit(), " (a minus sign is not a digit)")
print("int(text) ->", int(text), " (the conversion still works)")

print()
text = "  42  "
print(f"text = {text!r}")
print("isdigit() ->", text.isdigit(), " (spaces make it False)")
print("int(text) ->", int(text), " (the conversion still works)")

print()
print("Using try and except to handle bad input:")


def read_number(prompt):
    """Ask for a number until valid text is given."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That was not a whole number. Try again.")


print("Uncomment the call below to try it. Type letters to see the retry.")
print()
#   age = read_number("Enter your age: ")
#   print("You entered", age)

print()
print("A function with safe conversion and a default:")


def to_int(text, default=0):
    """Return text as an int, or default when it is not a valid integer."""
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


print("to_int('50')      =", to_int("50"))
print("to_int('abc')     =", to_int("abc"))
print("to_int('abc', -1) =", to_int("abc", -1))
print("to_int(None)      =", to_int(None))

print()
print("=" * 60)
print("THE MOST COMMON CASE: input() RETURNS TEXT")
print("=" * 60)
print("""
input() always gives a str, even when you type digits.

    age = input("Age: ")      # you type 20
    print(age + 1)            # TypeError

Fix it by converting first:

    age = int(input("Age: "))
    print(age + 1)            # 21

For calculations use float():

    price = float(input("Price: "))
    print(price * 2)          # works
""")

print("Demonstrating the problem and the fix without waiting for input:")
typed_text = "20"  # this is what input() would return

print('typed_text =', repr(typed_text))
try:
    print(typed_text + 1)
except TypeError as error:
    print("typed_text + 1 ->", type(error).__name__, ":", error)

converted = int(typed_text)
print("int(typed_text) + 1 =", converted + 1)

converted_float = float("19.99")
print('float("19.99") * 2 =', converted_float * 2)

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Forgetting to store the result.
   int("42")       does nothing on its own
   age = int("42") is the correct form
2. Converting too early and losing information.
   int("42.9") becomes 42, so keep the decimal until you really need an int.
3. Assuming int() rounds. It truncates toward zero. Use round() to round.
4. Converting a value that may be None. int(None) raises TypeError, so check
   for None first.
5. Comparing values of different types.
   "5" == 5 is False. Convert one side before comparing.
""")

print("String numbers compare as text, which gives a different order:")
print('"10" < "9"  ->', "10" < "9", " (text compares digit by digit)")
print("10 < 9      ->", 10 < 9, " (numbers compare by value)")
print('int("10") < int("9") ->', int("10") < int("9"))

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Convert by calling the target type: int(), float(), str(), bool().
- int() truncates toward zero, round() rounds to the nearest value.
- Convert user input, because input() always returns text.
- Bad text raises ValueError, and an unsuitable value raises TypeError.
- Guard with try and except, or check with isdigit(), before converting.
""")