"""Topic 3: Floats

float stores numbers with a decimal part. Floats use binary precision, so a few
operations produce surprising results.

Run with:  python 03-floats.py
"""

print("=" * 60)
print("WHAT IS A FLOAT?")
print("=" * 60)
print("A float is any number written with a decimal point or exponent.")

price = 3.99
temperature = -7.5
whole_number = 10.0
print("price         =", price, " type:", type(price).__name__)
print("temperature   =", temperature, " type:", type(temperature).__name__)
print("whole_number  =", whole_number, " type:", type(whole_number).__name__)
print("10.0 is a float even though it looks like a whole number.")

print()
print("A float is created by any of these:")
print("  3.14          decimal point")
print("  -0.5          negative decimal")
print("  10.0          zero with a decimal point")
print("  1e3           scientific notation")
print("  1 / 3         the result of any division with /")
print("  float(5)      explicit conversion")

print()
print("=" * 60)
print("ARITHMETIC ON FLOATS")
print("=" * 60)

a = 10.5
b = 3.2
print("a =", a, "| b =", b)
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b, "  (whole part only, still a float)")
print("a % b  =", a % b)
print("a ** b =", a ** b)

print()
print("Note that // on floats still returns a float:")
print("type(10.5 // 3.2) =", type(10.5 // 3.2).__name__)
print("For whole numbers use int(a // b).")

print()
print("=" * 60)
print("SCIENTIFIC NOTATION")
print("=" * 60)
print("An e moves the decimal point by a power of ten.")

light_speed = 3e8          # 3 x 10^8
small = 1.5e-9             # 1.5 x 10^-9
large = 2.5e12
print("3e8    =", light_speed, " metres per second")
print("1.5e-9 =", small, " metres")
print("2.5e12 =", large)

print()
print("You can do the same with powers:")
print("3 * 10 ** 8 =", 3 * 10 ** 8)
print("3e8         =", 3e8)
print("They are equal:", 3e8 == 3 * 10 ** 8)

print()
print("=" * 60)
print("FLOATING POINT PRECISION")
print("=" * 60)
print("Floats cannot store every decimal exactly, because they are stored in")
print("binary. The gap between the closest two floats is called the precision")
print("limit.")

print("0.1 + 0.2       =", 0.1 + 0.2)
print("Expected result : 0.3")
print("Is it equal?    :", 0.1 + 0.2 == 0.3)
print("The tiny difference:", 0.1 + 0.2 - 0.3)

print()
print("Another well known case:")
print("0.1 * 3 =", 0.1 * 3)
print("type    :", type(0.1 * 3).__name__)

print()
print("Comparing floats: use a small tolerance instead of ==")


def nearly_equal(first, second, tolerance=1e-9):
    """Return True when two floats differ only by rounding error."""
    return abs(first - second) < tolerance


print("nearly_equal(0.1 + 0.2, 0.3)        :", nearly_equal(0.1 + 0.2, 0.3))
print("nearly_equal(0.1 + 0.2, 0.3) via == :", 0.1 + 0.2 == 0.3)
print("tolerance 1e-9 is small enough for most everyday maths.")

print()
print("=" * 60)
print("MONEY AND FLOATS")
print("=" * 60)
print("Floats are risky for money because of that precision problem.")

price = 0.1
tax = 0.2
total = price + tax
print("0.1 + 0.2 =", total)
print("Not exactly 0.3, which is awkward for a bill.")

print()
print("A safer pattern is to work in whole units such as paisa, or to round")
print("at every step:")
print("round(0.1 + 0.2, 2) =", round(0.1 + 0.2, 2))
print("round(19.99, 1)     =", round(19.99, 1))
print("round(2.5)           =", round(2.5), "(banker's rounding, goes to even)")
print("round(3.5)           =", round(3.5))
print("For real projects, use the decimal module instead.")

print()
print("=" * 60)
print("FLOAT SPECIAL VALUES")
print("=" * 60)

print("float('inf')  :", float("inf"))
print("float('nan')  :", float("nan"), "(not a number)")
print("math.inf      :", __import__("math").inf)
print("nan != nan    :", float("nan") != float("nan"), "(a nan never equals itself)")
print("inf > 1000    :", float("inf") > 1000)

print()
print("=" * 60)
print("INT AND FLOAT TOGETHER")
print("=" * 60)
print("Python handles mixed arithmetic smoothly and widens the result.")

count = 3
price = 10.5
print("count =", count, " type:", type(count).__name__)
print("price =", price, " type:", type(price).__name__)
print("count * price =", count * price, " type:", type(count * price).__name__)
print("count + 1     =", count + 1, " type:", type(count + 1).__name__)
print("count / 2     =", count / 2, " type:", type(count / 2).__name__, "(even 4 / 2 gives float)")

print()
print("=" * 60)
print("CONVERTING BETWEEN INT AND FLOAT")
print("=" * 60)

print("float(7)      =", float(7), " type:", type(float(7)).__name__)
print("int(7.9)      =", int(7.9), " (drops the decimal part)")
print("int(-7.9)     =", int(-7.9), " (truncates toward zero)")
print("round(7.9)    =", round(7.9), " (rounds to the nearest int)")
print('float("7.9")  =', float("7.9"), " type:", type(float("7.9")).__name__)
print('int("7")      =', int("7"))

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("1. Comparing floats with == fails after arithmetic.")
print("2. A dot in a literal makes it a float: 5. is 5.0")
print("3. float('abc') raises ValueError.")
try:
    float("abc")
except ValueError as error:
    print("   float('abc') ->", type(error).__name__, ":", error)
print("4. Avoid float for money and identifiers such as phone numbers.")
print("5. Never compare to see if a float is close to zero. Use the tolerance")
print("   function above instead of == 0.")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- float holds decimals and is created by a dot, an e, or division with /.
- Floats are stored in binary, so 0.1 + 0.2 is not exactly 0.3.
- Compare floats with a tolerance, never with ==.
- Use round() to tidy output, and avoid floats for money.
- Mixed int and float arithmetic works and gives a float result.
""")