"""Topic 1: The print() Function

print() is Python's output function. It shows values on the screen so you can
see what your program is doing.

Run with:  python 01-print-function.py
"""

print("=" * 60)
print("THE SIMPLEST PRINT")
print("=" * 60)
print("print() takes any value and displays it.")

print("Hello, World!")
print(42)
print(3.14)
print(True)
print(None)

print()
print("=" * 60)
print("PRINTING NOTHING: EMPTY LINES")
print("=" * 60)
print("print() with no argument prints an empty line.")

print("Line one")
print()
print("Line two")
print()
print()

print("Two empty lines above were produced by two print() calls.")

print()
print("=" * 60)
print("PRINTING SEVERAL VALUES")
print("=" * 60)
print("print() accepts any number of values. It separates them with a space.")

name = "Ali"
age = 20
city = "Lahore"
print("Name:", name)
print("Name:", name, "Age:", age, "City:", city)
print("Marks:", 88, 92, 79)
print("No quotes needed around numbers:", 1, 2, 3)

print()
print("With quotes the values are still just text:")
print('"Name:"', name)

print()
print("=" * 60)
print("THE sep AND end ARGUMENTS")
print("=" * 60)

print("sep = the text placed between values")
print("end = the text placed after the last value")

print("2026", "10", "05", sep="-")
print("a", "b", "c", sep=" | ")
print("C", ":", "Users", sep="")
print()
print("First line", end=" ... ")
print("continued on the same line")
print()
print("One line only:", end="\n")
print("Two print() calls, two lines, because end defaults to a newline")

print()
print("Defaults are end='\\n' and sep=' ', so you rarely pass them.")
print("Both must be strings, or None, which means use that default.")

print()
print("=" * 60)
print("PRINTING DIFFERENT KINDS OF VALUES")
print("=" * 60)

print(42)
print(3.14)
print(-7)
print("text")
print(True)
print(False)
print(None)
print([1, 2, 3])
print((1, 2, 3))
print({1, 2, 3})
print({"a": 1, "b": 2})
print(type("text"))
print(len("hello"))

print()
print("None prints as the word None, and a list shows its contents.")
print("Notice print() does not add quotes, so use repr() to see them:")
print(repr("text"))
print(repr(None))
print(repr(42))

print()
print("=" * 60)
print("print() CAN EVALUATE EXPRESSIONS")
print("=" * 60)
print("Anything on the right of a print() call is evaluated first.")

print(2 + 3)
print(10 * 5)
print(100 / 4)
print("Hello" + " " + "World")
print(len("Python"))
print(3 ** 3)
print(max(1, 2, 3))
print(round(3.14159, 2))

print()
print("You can mix expressions and text in one call:")
total = 10 * 4
print("10 items at 4 rupees each =", total)

print()
print("=" * 60)
print("MULTIPLE LINE OUTPUT WITH ONE print()")
print("=" * 60)

print("Line A\nLine B\nLine C")

print()
print("""A triple quoted string keeps the line breaks exactly as you wrote them:
first
second
third""")

print()
print("=" * 60)
print("WHAT print() RETURNS")
print("=" * 60)
print("print() sends text to the screen and returns None. Never store it.")

result = print("side effect")
print("the return value was:", repr(result))
print("That is why this is wrong:  value = print('hi')")

print()
print("=" * 60)
print("WRITING TO A FILE INSTEAD OF THE SCREEN")
print("=" * 60)
print("print() has an optional file argument.")

import io

buffer = io.StringIO()
print("captured line", file=buffer)
print("second line", file=buffer)

print("Captured text instead of screen output:")
print(repr(buffer.getvalue()))
print("The normal print() you have used all along is the same function,")
print("just with file defaulting to the screen.")

print()
print("=" * 60)
print("THE flush ARGUMENT")
print("=" * 60)
print("flush=True pushes the text out immediately. Useful for progress bars")
print("and messages before a long wait.")

print("Writing now ...", end="", flush=True)
print(" done")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("1. Forgetting the closing parenthesis.")
print('   print("hello"      -> SyntaxError')
print("2. Mixing quote styles that break the string.")
print("3. Writing commas when concatenation was intended.")
print('4. Using print where return is meant in a function.')
print("5. Calling print with no parenthesis: print is an object here, not a")
print("   call, so it prints the function address rather than nothing.")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- print(*values, sep=' ', end='\\n', file=None, flush=False)
- It evaluates each value, converts it to text, joins with sep, and adds end.
- It returns None, so never store the result.
- sep and end must be strings, or None to use the default.
- Use f-strings inside print() for values inside a sentence, covered in
  Topic 5 of this folder.
""")