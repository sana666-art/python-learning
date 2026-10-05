"""Topic 4: Strings

str holds text. Strings are immutable, meaning you cannot change the text
inside one; you must create a new string instead.

Run with:  python 04-strings.py
"""

print("=" * 60)
print("CREATING A STRING")
print("=" * 60)
print('Text inside matching quotes becomes a string.')

single = 'Hello'
double = "Hello"
triple = """This string
spans several
lines."""

print("single quotes :", single)
print("double quotes :", double)
print("triple quotes :")
print(triple)
print("all three are type:", type(single).__name__)

print()
print("An empty string is written as two quotes with nothing between:")
empty = ""
print('empty =', repr(empty), "length:", len(empty))

print()
print("=" * 60)
print("QUOTES: WHICH TO USE WHEN")
print("=" * 60)

message_with_apostrophe = "It's a good day"
message_with_quotes = 'She said "Hello"'
escape = "He said \"Hi\""
backslash = "C:\\Users\\Ali"

print("apostrophe inside  :", message_with_apostrophe)
print("quotes inside      :", message_with_quotes)
print("escaped quotes     :", escape)
print("escaped backslash  :", backslash)

print()
print("Quote styles rule:")
print('  "text \'x\'"  works fine')
print('  \'text "x"\'  works fine')
print('  "text "x""   breaks, so escape or switch quotes')

print()
print("=" * 60)
print("ACCESSING A CHARACTER: INDEXING")
print("=" * 60)
print("Positions start at 0. The last position is -1.")

word = "Python"
print("word      =", word)
print("word[0]   =", word[0], "  (first character)")
print("word[1]   =", word[1])
print("word[5]   =", word[5], "  (last character)")
print("word[-1]  =", word[-1], "  (also the last character)")
print("word[-2]  =", word[-2], "  (second from the end)")
print("word[-6]  =", word[-6], "  (first character again)")

print()
print("=" * 60)
print("SLICING")
print("=" * 60)
print("Format: string[start:stop]  where stop is excluded.")

text = "Introduction to Python"
print("text =", repr(text))
print()
print('text[0:12]    =', repr(text[0:12]))
print('text[0:5]     =', repr(text[0:5]), "   (Introduction)")
print('text[15:]     =', repr(text[15:]), "   (from 15 to the end)")
print('text[:6]      =', repr(text[:6]), "   (from start to 6)")
print('text[-6:]     =', repr(text[-6:]), "   (last 6 characters)")
print('text[::2]     =', repr(text[::2]), "   (every second character)")
print('text[::-1]    =', repr(text[::-1]), "   (reversed)")

print()
print("Two colons mean start, stop, step.")
print("text[5:20:3]  =", repr(text[5:20:3]), "   (step of 3)")
print("A slice never raises an error if the bounds are wrong, it just returns")
print("less text. Indexing a single position does raise IndexError:")
try:
    print(text[999])
except IndexError as error:
    print("   text[999] ->", type(error).__name__, ":", error)

print()
print("=" * 60)
print("LENGTH")
print("=" * 60)
print("len() counts the characters.")

for sample in ["", "Python", "Introduction to Python", "  spaces  "]:
    print(f"len({sample!r:<28}) = {len(sample)}")

print()
print("Len counts spaces too, so strip() is often needed first.")
print('len("  hello  ")  =', len("  hello  "))
print('len("  hello  ".strip()) =', len("  hello  ".strip()))

print()
print("=" * 60)
print("COMMON OPERATIONS")
print("=" * 60)

first = "Hello"
last = "World"
full = first + " " + last
print("concatenation  first + last :", full)
print("repetition    'Ha' * 3      :", "Ha" * 3)
print("membership    'World' in full:", "World" in full)
print("membership    'Python' in full:", "Python" in full)
print("membership    'or' not in full :", "or" not in full)
print("comparison    'a' < 'b'      :", "a" < "b", " (alphabetical order)")

print()
print("=" * 60)
print("UPPER AND LOWER CASE")
print("=" * 60)

name = "Ahmed Khan"
print("original :", name)
print("upper()  :", name.upper())
print("lower()  :", name.lower())
print("title()  :", name.title())
print("swapcase :", "PyThOn".swapcase())
print("capitalize:", "hello WORLD".capitalize())

print()
print("=" * 60)
print("WHITESPACE AND SEPARATORS")
print("=" * 60)

padded = "   Python   "
print("padded        :", repr(padded))
print("strip()       :", repr(padded.strip()))
print("lstrip()      :", repr(padded.lstrip()))
print("rstrip()      :", repr(padded.rstrip()))

csv = "Ali,Sara,Ahmed"
print()
print("csv           :", repr(csv))
print("split(',')    :", csv.split(","))
print("'-'.join      :", "-".join(["a", "b", "c"]))

lines = "line one\nline two"
print()
print("multiline     :", repr(lines))
print("splitlines()  :", lines.splitlines())

print()
print("=" * 60)
print("FINDING AND REPLACING")
print("=" * 60)

sentence = "I love Python and Python loves me"
print("sentence            :", sentence)
print("find('Python')       :", sentence.find("Python"))
print("find('Java')         :", sentence.find("Java"), " (-1 means not found)")
print("count('Python')      :", sentence.count("Python"))
print("replace('Python','C'):", sentence.replace("Python", "C"))
print("startswith('I love'):", sentence.startswith("I love"))
print("endswith('me')       :", sentence.endswith("me"))

print()
print("=" * 60)
print("STRINGS ARE IMMUTABLE")
print("=" * 60)
print("You cannot change a character inside a string.")

word = "cat"
print("word =", word)
print("This fails with TypeError:")
try:
    word[0] = "b"
except TypeError as error:
    print("   word[0] = 'b' ->", type(error).__name__, ":", error)

print()
print("To change it, build a new string instead:")
word = "b" + word[1:]
print("new word :", word)

letter = "h"
letter = letter.upper()
print("letter =", letter, "after letter.upper()")

print()
print("=" * 60)
print("ESCAPE CHARACTERS")
print("=" * 60)
print('\\n   new line')
print('\\t   tab')
print('\\r   carriage return')
print('\\\\  backslash')
print('\\\'  single quote')
print('\\"   double quote')
print("\\n is a real newline in the output:")
print("first\nsecond")
print("\\n printed literally looks like this: \\n")

print()
print("=" * 60)
print("F-STRINGS: THE EASY WAY TO BUILD STRINGS")
print("=" * 60)

name = "Ali"
age = 20
score = 87.456
print(f"{name} is {age} years old")
print(f"Name: {name:<10} Age: {age:<4}")
print(f"Name: {name:>10} Age: {age:>4}")
print(f"Score rounded: {score:.2f}")
print(f"Score padded : {score:8.2f}")
print(f"Percentage   : {45 / 55:.1%}")
print(f"Maths        : {2 + 3} and {2 ** 10}")
print(f"Debugging    : name is {name!r}")

print()
print("Format specifiers you will use most:")
print("  :<10   left aligned in 10 spaces")
print("  :>10   right aligned in 10 spaces")
print("  :^10   centred in 10 spaces")
print("  :.2f   two decimal places")
print("  :>8    width 8, right aligned")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- str holds text and needs matching quotes.
- Indexing starts at 0, negative counts from the end.
- Slicing is string[start:stop:step] and stop is excluded.
- len() counts characters including spaces.
- Strings are immutable, so every change creates a new string.
- f-strings are the simplest way to build text with values.
""")