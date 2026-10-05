"""Topic 5: Your First Python Program

The print() function is how Python shows output on the screen. Everything a
beginner writes starts with print().

Run with:  python 05-first-python-program.py
"""

print("=" * 60)
print("THE CLASSIC HELLO WORLD")
print("=" * 60)
print("This is the first program almost every programmer writes.")

# The line below is the whole program.
print("Hello, World!")

print()
print("=" * 60)
print("HOW print() WORKS")
print("=" * 60)
print("Syntax:  print(value)")
print("print() with no argument prints an empty line.")

print()
print()
print("That was two empty lines from two print() calls.")

print()
print("=" * 60)
print("PRINTING TEXT (STRINGS)")
print("=" * 60)
print("Text must be inside quotes. Both quote styles work in Python 3.")
print('Single quotes: Hello')
print("Double quotes: Hello")
print("""Triple quotes span multiple lines:
this is still part of the same string.""")

print()
print("=" * 60)
print("PRINTING MULTIPLE VALUES")
print("=" * 60)
print("print() accepts many values at once, separated by commas.")
print("It adds a space between them and moves to a new line at the end.")

name = "Ali"
age = 20
city = "Lahore"
print("Name:", name, "Age:", age, "City:", city)

print()
print("Without commas, use string concatenation instead.")
print("Name: " + name + " Age: " + str(age))

print()
print("sep= changes the separator between values")
print("2026", "01", "05", sep="-")
print("A", "B", "C", sep=" | ")

print()
print("end= changes what comes after the last value")
print("Loading", end="...")
print(" done!")
print("This stays on one line:", end="\n")
print("(the end= above ended with a newline, so this is a new line)")

print()
print("=" * 60)
print("ESCAPE CHARACTERS IN STRINGS")
print("=" * 60)
print("New line        :", "Line 1\nLine 2")
print("Tab             :", "Name\tMarks")
print("Backslash       :", "C:\\Users\\Student")
print("Double quote    :", 'She said "Hello"')

print()
print("=" * 60)
print("SEPARATE ARGUMENT FOR FORMATTING")
print("=" * 60)
print("You can move values out of the string with an index.")
language = "Python"
year = 1991
print("{0} was created in {1}.".format(language, year))
print("{0} is used by {1:,.0f} developers.".format(language, 10_000_000))

print()
print("=" * 60)
print("F-STRINGS (THE MODERN WAY)")
print("=" * 60)
print("Prefix a string with f and put variables inside {}.")
print(f"{language} was created in {year}.")
print(f"{language} is in its {2026 - year}th year of development.")
print(f"Uppercase: {language.upper()}  |  Length: {len(language)}")
print(f"Calculation inside braces: {10 * 3 + 1}")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("1. Missing quotes      -> NameError because bare words are not text.")
print("2. Missing parenthesis -> SyntaxError.")
print("3. Wrong quotes        -> the ' and \" characters must match.")
print("4. Mixing f and +      -> you can use f-strings OR +, not both in one")
print("   expression. Both of these work separately:")
print(f"   Correct: f'{name}'")
print("   Correct: " + name)