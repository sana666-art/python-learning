"""Topic 5: Print Formatting

Formatting makes output readable: aligned columns, fixed decimals, thousands
separators and values placed inside sentences.

Run with:  python 05-print-formatting.py
"""

print("=" * 60)
print("WHY FORMAT OUTPUT?")
print("=" * 60)
print("Raw output is hard to read. Formatting gives you alignment, fixed")
print("precision and a consistent layout.")

print()
print("Three ways to format, from newest to oldest:")
print("  f-strings     Python 3.6+   the modern default")
print("  str.format()  Python 2.7+   older, still common in older code")
print("  % formatting  very old     seen in legacy scripts")

print()
print("=" * 60)
print("F-STRINGS")
print("=" * 60)
print("Prefix the string with f and put expressions in braces {}.")

name = "Ali"
age = 20
price = 1234.5

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Name is {name} and age is {age}")
print(f"Next year you will be {age + 1}")
print(f"Double the price: {price * 2}")

print()
print("Expressions work inside the braces, so any calculation is allowed:")
total = 10 * 4
print(f"10 x 4 = {total}")
print(f"2 ** 10 = {2 ** 10}")
print(f"Uppercase: {name.upper()}")

print()
print("Reuse a value as many times as you like:")
student = "Sara"
marks = 92
print(f"{student} scored {marks}. {student} passed with {marks} marks.")

print()
print("=" * 60)
print("ALIGNMENT AND WIDTH")
print("=" * 60)
print("Format spec: {value:<width} or {value:>width} or {value:^width}")

for fruit in ["apple", "banana", "cherry"]:
    print(f"left   |{fruit:<10}|")
for fruit in ["apple", "banana", "cherry"]:
    print(f"right  |{fruit:>10}|")
for fruit in ["apple", "banana", "cherry"]:
    print(f"centre |{fruit:^10}|")

print()
print("A table with names, ages and scores aligned:")

records = [("Ahmed", 20, 88.5), ("Sara", 21, 92.25), ("Bilal", 19, 75.0)]

print(f"{'Name':<10}{'Age':>5}{'Score':>10}")
print("-" * 25)
for record_name, record_age, record_score in records:
    print(f"{record_name:<10}{record_age:>5}{record_score:>10.2f}")

print()
print("Note the .2f inside the column spec: it sets precision and alignment")
print("at the same time.")

print()
print("=" * 60)
print("FIXING DECIMAL PLACES WITH .nf")
print("=" * 60)

pi = 3.14159265
value = 19.995
total = 1234.5678

print(f"{pi:.0f}   {pi:.1f}   {pi:.2f}   {pi:.3f}")
print(f"value   : {value:.2f}")
print(f"total   : {total:.2f}")
print()
print("round() changes the value, format only changes how it looks:")
print(f"round(pi, 2)       = {round(pi, 2)}")
print(f"pi formatted .2f   = {pi:.2f}  (the value still has all its digits)")

print()
print("=" * 60)
print("THOUSANDS SEPARATORS WITH COMMAS")
print("=" * 60)

population = 240000000
revenue = 1234567.891

print(f"{population:,}")
print(f"{population:_}")
print(f"{revenue:,.2f}")
print(f"Revenue: {revenue:,.2f}")
print(f"Population: {population:,}")
print()
print("The comma inserts a group separator every three digits.")

print()
print("=" * 60)
print("PERCENTAGES AND SCIENTIFIC NOTATION")
print("=" * 60)

correct = 45
total_questions = 55
ratio = correct / total_questions

print(f"{ratio:.1%}")
print(f"{ratio:.2%}")
print(f"You answered {correct} of {total_questions}: {ratio:.1%}")
print()
print("Scientific notation uses the e specifier:")
print(f"{123456789:.2e}")
print(f"{0.0000045:.2e}")
print(f"{1500000000000:.3e}")

print()
print("=" * 60)
print("ZERO PADDING AND SIGNED NUMBERS")
print("=" * 60)

print(f"Zero padded : {42:05d}")
print(f"Negative    : {-42:05d}")
print(f"Signed +    : {42:+d}")
print(f"Signed -    : {-42:+d}")
print(f"Spaces      : {42: 5d}")
print(f"Positive    : {abs(-42):d}")

print()
print("=" * 60)
print("USING str.format() INSTEAD")
print("=" * 60)
print("Older code uses .format() with {} or with numbered placeholders.")

print("Name: {}".format("Ali"))
print("Name: {0}, Age: {1}".format("Ali", 20))
print("Name: {n}, Age: {a}".format(n="Ali", a=20))
print("Price: {:,.2f}".format(1234.5))
print("Aligned: {:<10}|".format("apple"))
print()
print("It does everything f-strings do, it is just longer to write.")

print()
print("=" * 60)
print("USING % FORMATTING IN LEGACY CODE")
print("=" * 60)
print("You will meet this in older scripts. It uses % as a placeholder.")

print("Name: %s" % "Ali")
print("Age: %d" % 20)
print("Price: %.2f" % 1234.5)
print("Score: %s scored %d" % ("Sara", 92))
print()
print("%s text, %d whole numbers, %f floats, %% prints a literal percent.")

print()
print("=" * 60)
print("MULTI-LINE ALIGNMENT WITH TEMPLATES")
print("=" * 60)
print("Build a template once and reuse it.")

template = "{:<10}{:>8}{:>10}"
print(template.format("Product", "Qty", "Price"))
print("-" * 28)
products = [("Rice", 3, 450.5), ("Sugar", 1, 120.0), ("Tea", 2, 340.75)]
for product_name, quantity, price in products:
    print(template.format(product_name, quantity, f"{price:.2f}"))

print()
print("=" * 60)
print("RAW f-STRINGS WITH repr() FOR DEBUGGING")
print("=" * 60)
print("Prefix with r or !r to see the exact value including quotes.")

name = "Ali"
value = None
empty = ""

print(f"{name!r}")
print(f"{value!r}")
print(f"{empty!r}")
print(f"raw f-string: fr'{{name}}'")
print(f"normal     : {name}")
print(f"debugging  : {name!r} is {type(name).__name__}")

print()
print("=" * 60)
print("ESCAPING BRACES IN F-STRINGS")
print("=" * 60)
print("A double brace prints a single brace, because braces mean a field.")

width = 5
print(f"Width is {width} so {{width}} is shown literally")
print("This is useful when printing JSON or format examples.")
print(f"A single brace: {{ and }}")
print(f"Real value    : {width}")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Forgetting the f prefix, so the braces print literally.
   print("{name}")  prints  {name}
2. Using a colon inside the braces by mistake in a nested f-string.
3. Mixing precision and width the wrong way round.
   {value:10.2f} is width 10 with 2 decimals, not the reverse.
4. Formatting an int with %s works, but %d fails on non-numbers.
5. Using .format() with positional indexes that do not match the values.
""")

name = "Ali"
print('Without f: "{name}"')
print(f"With f   : {name}")
print(f"Correct   : {name:10}|")
print(f"Reversed  : {name:.2f}" if False else f"Reversed spec would fail: {name!r}")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- f-strings are the modern choice: f"{value:<width.precisionf}"
- {:<10} left, {:>10} right, {:^10} centre
- .2f fixes two decimals, :.1% shows a percentage, :, adds separators
- round() changes the value, formatting only changes the display
- str.format() and % formatting appear in older code and are worth knowing
""")