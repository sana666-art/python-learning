"""Topic 10: Practice

Exercises covering every topic in this folder. Try each task yourself first,
then compare with the answers at the bottom.

How to practise:
  1. Run the file once to see the expected output.
  2. Write your own solution under each task.
  3. Run again and compare your output.
"""

print("=" * 60)
print("TASK 1: IDENTIFY THE TYPE")
print("=" * 60)
print("For each value below, print the value and its type name.")
print("Use type(value).__name__")
print("Values: 42, 3.14, 'Python', True, None, -7")
print()
print("=" * 60)
print("TASK 2: INTEGER ARITHMETIC")
print("=" * 60)
print("With a = 17 and b = 5, print the result of:")
print("  a + b, a - b, a * b, a / b, a // b, a % b, a ** b")
print("Then explain in a comment why a / b and a // b give different results.")

print()
print("=" * 60)
print("TASK 3: SPLIT A BILL")
print("=" * 60)
print("Set total_bill = 1000 and friends = 3.")
print("Print how much each friend pays using // and what is left over using %.")
print("Expected: each pays 333, leftover 1")

print()
print("=" * 60)
print("TASK 4: FLOAT PRECISION")
print("=" * 60)
print("Print 0.1 + 0.2 and show that it is not exactly 0.3.")
print("Then write a function nearly_equal(a, b, tolerance=1e-9) that uses")
print("abs(a - b) < tolerance and returns True for 0.1 + 0.2 against 0.3.")

print()
print("=" * 60)
print("TASK 5: STRING INDEXING AND SLICING")
print("=" * 60)
print("With word = 'Introduction to Python', print:")
print("  word[0], word[-1], word[:12], word[15:], word[-6:], word[::-1]")
print("Also print len(word) and word.count('o').")

print()
print("=" * 60)
print("TASK 6: STRING OPERATIONS")
print("=" * 60)
print("With name = 'ahmed khan', print the upper case, title case and length.")
print("Split 'Ali,Sara,Ahmed' on the comma and print the resulting list.")
print("Replace every 'o' with '0' in 'Python is fun' and print the result.")

print()
print("=" * 60)
print("TASK 7: F-STRINGS")
print("=" * 60)
print("Create name = 'Ali', age = 20, price = 1234.5.")
print("Print one line with an f-string that shows:")
print("  name left aligned in 10 spaces")
print("  price with exactly two decimal places")
print("  age right aligned in 5 spaces")
print("Expected: Name: Ali        | Price: 1234.50 | Age:    20")

print()
print("=" * 60)
print("TASK 8: BOOLEANS AND TRUTHINESS")
print("=" * 60)
print("Print the result of each comparison:")
print("  10 == 10, 10 != 10, 10 > 5, 'apple' < 'banana', 1 < 2 < 3")
print("Then print bool() for: 0, 1, '', 'text', [], [0], None")
print("Expected falsy values: 0, '', [], None")

print()
print("=" * 60)
print("TASK 9: None CHECKS")
print("=" * 60)
print("Write a function find_value(items, target) that returns the position")
print("of target in items, or None when it is missing.")
print("Call it with [10, 20, 30] and 20, then with 99.")
print("Expected: 1 and None")
print("Use 'is None' in the check, not '== None'.")

print()
print("=" * 60)
print("TASK 10: TYPE CHECKING")
print("=" * 60)
print("Write a function describe(value) that returns a short description:")
print("  'no value'        when value is None")
print("  'a boolean'       when it is True or False")
print("  'a whole number'  when it is an int")
print("  'a decimal'       when it is a float")
print("  'text'            when it is a str")
print("Order matters: check bool before int, because bool is a subclass.")
print("Test it with None, True, 42, 3.14 and 'hello'.")

print()
print("=" * 60)
print("TASK 11: TYPE CONVERSION")
print("=" * 60)
print("Convert the following and print the result with its type:")
print('  int("42"), float("3.14"), str(42), bool(""), int(42.9), round(42.9)')
print("Then show what happens with int('abc') by catching the ValueError.")

print()
print("=" * 60)
print("TASK 12: SAFE CONVERSION")
print("=" * 60)
print("Write to_int(text, default=0) that returns int(text) when possible and")
print("default when it fails.")
print("Print to_int('50'), to_int('abc') and to_int('abc', -1).")

print()
print("=" * 60)
print("TASK 13: MUTABLE VS IMMUTABLE")
print("=" * 60)
print("Create list_a = [1, 2] and list_b = list_a, then append 3 to list_b.")
print("Print both lists and comment why list_a changed.")
print("Repeat with a .copy() and comment why list_a stays the same this time.")

print()
print("=" * 60)
print("TASK 14: A SMALL GRADES REPORT")
print("=" * 60)
print("Create constants MAX_MARKS = 100 and PASS_MARKS = 40.")
print("Create a list of marks: [88, 92, 79, 35, 56]")
print("Calculate and print the number of students, the highest mark, the")
print("lowest mark, the average, and how many passed.")

print()
print("=" * 60)
print("BONUS TASK A: TEXT ANALYSIS")
print("=" * 60)
print("Take a sentence, then print:")
print("  its length")
print("  it in upper case")
print("  the number of words")
print("  the first and last word")
print("  whether the word 'python' appears, using 'in'")

print()
print("=" * 60)
print("BONUS TASK B: TEMPERATURE CONVERTER")
print("=" * 60)
print("Write celsius_to_fahrenheit(c) that returns c * 9/5 + 32.")
print("Write is_freezing(c) that returns a boolean.")
print("Print a table for 0, 10, 25, 37.5 and 100 Celsius.")

print()
print("=" * 60)
print("=" * 60)
print("ANSWER SECTION - READ AFTER YOU FINISH THE TASKS")
print("=" * 60)
print("=" * 60)

print()
print("--- ANSWER 1: IDENTIFY THE TYPE ---")
for value in [42, 3.14, "Python", True, None, -7]:
    print(f"{str(value):<10} -> {type(value).__name__}")

print()
print("--- ANSWER 2: INTEGER ARITHMETIC ---")
a = 17
b = 5
print("a + b   =", a + b)
print("a - b   =", a - b)
print("a * b   =", a * b)
print("a / b   =", a / b, "  (/ always returns a float)")
print("a // b  =", a // b, "  (// returns the whole part only)")
print("a % b   =", a % b)
print("a ** b  =", a ** b)

print()
print("--- ANSWER 3: SPLIT A BILL ---")
total_bill = 1000
friends = 3
each = total_bill // friends
left_over = total_bill % friends
print("Each friend pays:", each)
print("Left over       :", left_over)

print()
print("--- ANSWER 4: FLOAT PRECISION ---")
print("0.1 + 0.2        =", 0.1 + 0.2)
print("equals 0.3       :", 0.1 + 0.2 == 0.3)
print("difference       :", 0.1 + 0.2 - 0.3)


def nearly_equal(first, second, tolerance=1e-9):
    """Return True when two floats differ only by rounding error."""
    return abs(first - second) < tolerance


print("nearly_equal     :", nearly_equal(0.1 + 0.2, 0.3))

print()
print("--- ANSWER 5: STRING INDEXING AND SLICING ---")
word = "Introduction to Python"
print("word[0]     =", repr(word[0]))
print("word[-1]    =", repr(word[-1]))
print("word[:12]   =", repr(word[:12]))
print("word[15:]   =", repr(word[15:]))
print("word[-6:]   =", repr(word[-6:]))
print("word[::-1]  =", repr(word[::-1]))
print("len(word)   =", len(word))
print("count of o  =", word.count("o"))

print()
print("--- ANSWER 6: STRING OPERATIONS ---")
name = "ahmed khan"
print("upper :", name.upper())
print("title :", name.title())
print("length:", len(name))
print("split :", "Ali,Sara,Ahmed".split(","))
print("replace:", "Python is fun".replace("o", "0"))

print()
print("--- ANSWER 7: F-STRINGS ---")
name = "Ali"
age = 20
price = 1234.5
print(f"Name: {name:<10} | Price: {price:.2f} | Age: {age:>5}")
print("Expected: Name: Ali        | Price: 1234.50 | Age:    20")

print()
print("--- ANSWER 8: BOOLEANS AND TRUTHINESS ---")
print("10 == 10            :", 10 == 10)
print("10 != 10            :", 10 != 10)
print("10 > 5              :", 10 > 5)
print("'apple' < 'banana'  :", "apple" < "banana")
print("1 < 2 < 3           :", 1 < 2 < 3)
print()
for value in [0, 1, "", "text", [], [0], None]:
    print(f"bool({value!r:<8}) -> {bool(value)}")

print()
print("--- ANSWER 9: None CHECKS ---")


def find_value(items, target):
    """Return the position of target, or None when it is missing."""
    for position, item in enumerate(items):
        if item == target:
            return position
    return None


print("searching for 20 ->", find_value([10, 20, 30], 20))
print("searching for 99 ->", find_value([10, 20, 30], 99), "(None means not found)")
print("The check inside the function uses 'is None'.")

print()
print("--- ANSWER 10: TYPE CHECKING ---")


def describe(value):
    """Return a short description of a value based on its type."""
    if value is None:
        return "no value"
    if isinstance(value, bool):
        return "a boolean"
    if isinstance(value, int):
        return "a whole number"
    if isinstance(value, float):
        return "a decimal"
    if isinstance(value, str):
        return "text"
    return "unknown"


for value in [None, True, False, 42, 3.14, "hello"]:
    print(f"{str(value):<8} -> {describe(value)}")

print()
print("--- ANSWER 11: TYPE CONVERSION ---")
conversions = [
    ("int('42')", lambda: int("42")),
    ("float('3.14')", lambda: float("3.14")),
    ("str(42)", lambda: str(42)),
    ("bool('')", lambda: bool("")),
    ("int(42.9)", lambda: int(42.9)),
    ("round(42.9)", lambda: round(42.9)),
]
for label, action in conversions:
    result = action()
    print(f"{label:<18} -> {result!r:<12} type: {type(result).__name__}")

print()
try:
    int("abc")
except ValueError as error:
    print("int('abc') ->", type(error).__name__, ":", error)

print()
print("--- ANSWER 12: SAFE CONVERSION ---")


def to_int(text, default=0):
    """Return text as an int, or default when it is not a valid integer."""
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


print("to_int('50')      =", to_int("50"))
print("to_int('abc')     =", to_int("abc"))
print("to_int('abc', -1) =", to_int("abc", -1))

print()
print("--- ANSWER 13: MUTABLE VS IMMUTABLE ---")
list_a = [1, 2]
list_b = list_a
list_b.append(3)
print("list_a =", list_a)
print("list_b =", list_b)
print("Both names point at one list, so appending to list_b changed list_a too.")

print()
list_a = [1, 2]
list_b = list_a.copy()
list_b.append(3)
print("list_a =", list_a)
print("list_b =", list_b)
print("copy() created a second list, so list_a was not affected.")

print()
print("--- ANSWER 14: GRADES REPORT ---")
MAX_MARKS = 100
PASS_MARKS = 40
marks = [88, 92, 79, 35, 56]

student_count = len(marks)
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
passed = len([mark for mark in marks if mark >= PASS_MARKS])

print(f"Students : {student_count}")
print(f"Highest  : {highest}")
print(f"Lowest   : {lowest}")
print(f"Average  : {average:.2f}")
print(f"Passed   : {passed} out of {student_count}")

print()
print("--- BONUS ANSWER A: TEXT ANALYSIS ---")
sentence = "Python is a high level programming language and it is fun to learn"
print("Sentence  :", sentence)
print("Length    :", len(sentence))
print("Upper     :", sentence.upper())
print("Words     :", len(sentence.split()))
print("First word:", sentence.split()[0])
print("Last word :", sentence.split()[-1])
print("Has python:", "python" in sentence.lower())

print()
print("--- BONUS ANSWER B: TEMPERATURE CONVERTER ---")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def is_freezing(celsius):
    """Return True when the temperature is at or below freezing."""
    return celsius <= 0


print(f"{'Celsius':<10}{'Fahrenheit':<12}{'Freezing?'}")
print("-" * 32)
for celsius in [0, 10, 25, 37.5, 100]:
    print(f"{celsius:<10}{celsius_to_fahrenheit(celsius):<12.1f}{is_freezing(celsius)}")