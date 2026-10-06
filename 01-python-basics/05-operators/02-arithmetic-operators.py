"""Topic 2: Arithmetic Operators

Python's seven arithmetic operators, explored systematically: what they
return, how they handle negatives, and where the surprises are.

Run with:  python 02-arithmetic-operators.py
"""

print("=" * 60)
print("THE SEVEN OPERATORS")
print("=" * 60)
print("""
Symbol   Name              Example      Result
------   ----------------  -----------  ------
+        addition          17 + 5       22
-        subtraction       17 - 5       12
*        multiplication    17 * 5       85
/        true division     17 / 5       3.4
//       floor division    17 // 5      3
%        modulus           17 % 5       2
**       exponentiation    17 ** 5      1419857
""")

a = 17
b = 5
print("a =", a, "| b =", b)
print()
print(f"{'expression':<14}{'result':<14}{'type'}")
print("-" * 42)
for expression, value in [
    ("a + b", a + b),
    ("a - b", a - b),
    ("a * b", a * b),
    ("a / b", a / b),
    ("a // b", a // b),
    ("a % b", a % b),
    ("a ** b", a ** b),
]:
    print(f"{expression:<14}{str(value):<14}{type(value).__name__}")

print()
print("Key rule: only / always returns a float. The others return an int when")
print("both operands are ints, except ** which follows the operands.")

print()
print("=" * 60)
print("/ ALWAYS RETURNS A FLOAT")
print("=" * 60)
print("This is the single most common arithmetic surprise.")

for expression in ["10 / 2", "9 / 3", "1 / 3", "-7 / 2"]:
    value = eval(expression)
    print(f"   {expression:<10} = {value:<12} type: {type(value).__name__}")

print()
print("So 10 / 2 gives 5.0, not 5. Compare with //:")

print("10 / 2  =", 10 / 2, " type:", type(10 / 2).__name__)
print("10 // 2 =", 10 // 2, " type:", type(10 // 2).__name__)
print()
print("Use / when you want a decimal and // when you want a whole number.")

print()
print("=" * 60)
print("// FLOOR DIVISION: ROUNDS DOWN, NOT TOWARD ZERO")
print("=" * 60)
print("Floor means toward negative infinity. That differs from truncation for")

print("Positive numbers look obvious:")
print("17 // 5   =", 17 // 5)
print("20 // 6   =", 20 // 6)
print("100 // 7  =", 100 // 7)

print()
print("Negative numbers are where people get caught out:")
print("-17 // 5  =", -17 // 5, "  (not -3)")
print("-20 // 6  =", -20 // 6, "  (not -3)")
print("-100 // 7 =", -100 // 7)
print()
print("-17 / 5 is -3.4, and // rounds that DOWN to -4.")
print("Truncating toward zero would give -3, which is why this surprises.")
print()
print("The same applies to float operands:")
print("-17.0 // 5.0 =", -17.0 // 5.0)

print()
print("=" * 60)
print("% MODULUS: THE REMAINDER")
print("=" * 60)
print("The sign follows the DIVISOR, not the dividend, because")

print("Positive cases:")
print("17 % 5   =", 17 % 5)
print("20 % 6   =", 20 % 6)
print("10 % 3   =", 10 % 3)
print("5 % 5    =", 5 % 5, "  (exactly divisible, so 0)")

print()
print("Negative cases, where the sign matters:")
print("17 % 5   =", 17 % 5, "   positive dividend")
print("-17 % 5  =", -17 % 5, "   positive divisor, so the result is positive")
print("17 % -5  =", 17 % -5, "   negative divisor, so the result is negative")
print("-17 % -5 =", -17 % -5)
print()
print("Always:  a == (a // b) * b + (a % b)")

a, b = -17, 5
print(f"   {a} == ({a} // {b}) * {b} + ({a} % {b})")
print(f"   {a} == {a // b} * {b} + {a % b}")
print(f"   {a} == {(a // b) * b + a % b}   ->", a == (a // b) * b + a % b)

print()
print("=" * 60)
print("PRACTICAL USES OF %")
print("=" * 60)

print("1. Even or odd")
for number in [4, 7, 10, 15, 0, -3]:
    kind = "even" if number % 2 == 0 else "odd"
    print(f"   {number:>3} % 2 = {number % 2}  -> {kind}")

print()
print("2. Wrapping around a range, such as positions in a circle")
print("   A clock: (hour + offset) % 12")
print("   (10 + 5) % 12 =", (10 + 5) % 12, " -> 3 o'clock")
print("   (10 + 14) % 12 =", (10 + 14) % 12)

print()
print("3. Isolating digits")
number = 4827
print("   number =", number)
print("   last digit  :", number % 10)
print("   first digit :", end=" ")
probe = number
while probe >= 10:
    probe //= 10
print(probe)

print()
print("4. Every nth item")
values = list(range(1, 16))
print("   values                :", values)
print("   positions where i % 3 == 0 :", [i for i in values if i % 3 == 0])
print("   positions where i % 5 == 0 :", [i for i in values if i % 5 == 0])

print()
print("=" * 60)
print("** EXPONENTIATION")
print("=" * 60)
print("** raises the left operand to the power of the right one.")

print("2 ** 10   =", 2 ** 10, "  (1024, powers of two)")
print("5 ** 2    =", 5 ** 2)
print("9 ** 0.5  =", 9 ** 0.5, "  (a fractional power is a root)")
print("2 ** -1   =", 2 ** -1, "  (a negative power is a fraction)")
print("10 ** 0   =", 10 ** 0, "  (anything to the power 0 is 1)")
print("0 ** 0    =", 0 ** 0, "  (Python defines this as 1)")

print()
print("Integer powers stay exact, which floats cannot manage:")
print("(3 ** 20) =", 3 ** 20, "  exact")
print("(3.0 ** 20) =", 3.0 ** 20, "  may lose a little precision")

print()
print("Floating point division in a power is also fine:")
print("8 ** (1/3) =", 8 ** (1 / 3), " (the cube root of 8)")
print("round it   :", round(8 ** (1 / 3), 10))

print()
print("=" * 60)
print("NEGATIVE VALUES AND UNARY MINUS")
print("=" * 60)
print("Unary minus has lower precedence than **, which produces a classic")

print("-2 ** 2      =", -2 ** 2, "   (means -(2 ** 2))")
print("(-2) ** 2    =", (-2) ** 2, "  (means (-2) * (-2))")
print("-(2 ** 2)    =", -(2 ** 2), "  (spelled out, same as the first)")
print("-2 * 2       =", -2 * 2)
print("2 - -2       =", 2 - -2, "  (subtracting a negative adds)")
print("--5          =", --5, "  (two unary minuses)")

print()
print("=" * 60)
print("DIVISION BY ZERO")
print("=" * 60)
print("Python refuses to guess, so all three forms raise ZeroDivisionError.")

for expression, run in [
    ("10 / 0", lambda: 10 / 0),
    ("10 // 0", lambda: 10 // 0),
    ("10 % 0", lambda: 10 % 0),
]:
    try:
        run()
    except ZeroDivisionError as error:
        print(f"   {expression:<10} -> {type(error).__name__}: {error}")

print()
print("Checking first is the normal approach:")
divisor = 0
if divisor != 0:
    print("   result:", 10 / divisor)
else:
    print("   divisor is 0, so the division was skipped")

print()
print("=" * 60)
print("FLOAT ARTIFACTS IN ARITHMETIC")
print("=" * 60)
print("Binary storage makes some decimal results inexact.")

print("0.1 + 0.2        =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 :", 0.1 + 0.2 == 0.3)
print("3 * 0.1          =", 3 * 0.1)
print("round(0.1 + 0.2, 2) =", round(0.1 + 0.2, 2))

print()
print("Division is not exempt either:")
print("1 / 3        =", 1 / 3)
print("1 / 3 * 3    =", 1 / 3 * 3)
print("(1 / 3) * 3 == 1 ->", (1 / 3) * 3 == 1)
print()
print("For money, work in whole units or use the decimal module. For ordinary")
print("display, round or format to the digits you actually need.")

print()
print("=" * 60)
print("LARGE NUMBERS AND INT DIVISION")
print("=" * 60)
print("ints have no size limit, so big calculations stay exact.")

big = 2 ** 200
print("2 ** 200      =", big)
print("big // 7      =", big // 7)
print("big % 7       =", big % 7)
print("digits        =", len(str(big)))
print()
print("The same calculation with floats loses accuracy:")
print("2.0 ** 200    =", 2.0 ** 200)
print("The float has about 15 to 16 significant digits, so the tail is gone.")

print()
print("=" * 60)
print("ARITHMETIC BUILT FROM THE OPERATORS")
print("=" * 60)
print("Everyday formulas translate almost word for word.")

price = 1200
quantity = 4
rate = 0.17

subtotal = price * quantity
discount = subtotal * 0.10
after_discount = subtotal - discount
tax = after_discount * rate
total = after_discount + tax
average = subtotal / quantity
each_share = total // quantity
left_over = total % quantity

print(f"price * quantity            = {subtotal:>10.2f}")
print(f"subtotal * 0.10             = {discount:>10.2f}")
print(f"subtotal - discount         = {after_discount:>10.2f}")
print(f"after_discount * rate       = {tax:>10.2f}")
print(f"after_discount + tax        = {total:>10.2f}")
print(f"subtotal / quantity         = {average:>10.2f}")
print(f"total // quantity           = {each_share:>10.0f}")
print(f"total % quantity            = {left_over:>10.2f}")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Expecting 10 / 2 to be an int. It is 5.0. Use // for whole numbers.
2. Assuming // rounds toward zero. It floors, so -17 // 5 is -4, not -3.
3. Assuming % follows the sign of the left operand. It follows the divisor.
4. Forgetting ** binds tighter than unary minus, so -2 ** 2 is -4.
5. Writing 1 / 0 by accident when a count could be zero.
6. Comparing floats with == after arithmetic. Use a tolerance instead.
7. Mixing * and ** in one line without brackets and hoping for the best.
""")

print("Quick proofs:")
print("   10 / 2      =", 10 / 2)
print("   -17 // 5    =", -17 // 5)
print("   -17 % 5     =", -17 % 5)
print("   -2 ** 2     =", -2 ** 2)
print("   2 + 3 * 4   =", 2 + 3 * 4, "  (not 20, see topic 8)")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Seven operators: + - * / // % **
- / always gives a float; // gives a whole number floored toward -infinity.
- % gives the remainder, with the sign of the divisor.
- ** handles powers, roots and reciprocals through fractional and negative
  exponents.
- Unary minus has lower precedence than **, so -2 ** 2 equals -4.
- Division by zero raises ZeroDivisionError in all three forms.
""")