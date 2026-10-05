"""Topic 2: Integers

int stores whole numbers with no decimal part. Python has no fixed limit on
the size of an int.

Run with:  python 02-integers.py
"""

print("=" * 60)
print("WHAT IS AN INTEGER?")
print("=" * 60)
print("An int holds a whole number: positive, negative or zero.")

positive = 100
negative = -50
zero = 0
print("positive =", positive)
print("negative =", negative)
print("zero     =", zero)
print("type     =", type(positive).__name__)

print()
print("=" * 60)
print("NO UPPER LIMIT ON SIZE")
print("=" * 60)
print("Other languages overflow on very large numbers. Python grows as needed.")

big = 2 ** 100
print("2 ** 100                       =", big)
print("type                           =", type(big).__name__)
print("digit count                    =", len(str(big)))
print("bigger than 64 bit maximum     =", 2 ** 100 > (2 ** 64 - 1))

print()
print("=" * 60)
print("ARITHMETIC ON INTEGERS")
print("=" * 60)

a = 17
b = 5
print("a =", a, "| b =", b)
print("a + b   addition       =", a + b)
print("a - b   subtraction    =", a - b)
print("a * b   multiplication =", a * b)
print("a / b   true division  =", a / b, "  <- always gives a float")
print("a // b  floor division =", a // b, "  <- whole part only")
print("a % b   remainder      =", a % b, "  <- also called modulo")
print("a ** b  exponent       =", a ** b)
print("-a      negation       =", -a)
print("+a      unary plus     =", +a)

print()
print("=" * 60)
print("FLOOR DIVISION vs TRUE DIVISION")
print("=" * 60)
print("This is the most common beginner surprise.")

print("17 / 5  =", 17 / 5, " -> float, keeps the decimal part")
print("17 // 5 =", 17 // 5, " -> int, drops the decimal part")
print("17 % 5  =", 17 % 5, "  -> what is left over")

print()
print("With negative numbers // rounds down, not toward zero:")
print("17 // 5  =", 17 // 5)
print("-17 // 5 =", -17 // 5, "(rounds down to -4)")
print("-17 % 5  =", -17 % 5, "(the remainder keeps the sign of the divisor)")

print()
print("=" * 60)
print("ORDER OF OPERATIONS")
print("=" * 60)
print("Arithmetic follows the same rules as maths.")
print("() first, then **, then * / // %, then + -")

print("2 + 3 * 4      =", 2 + 3 * 4, "  (3 * 4 first)")
print("(2 + 3) * 4    =", (2 + 3) * 4, "  (brackets change the result)")
print("2 ** 3 ** 2    =", 2 ** 3 ** 2, "  (** works right to left)")
print("(2 ** 3) ** 2  =", (2 ** 3) ** 2)

print()
print("=" * 60)
print("A PRACTICAL EXAMPLE: DIVIDING THE TOTAL BILL")
print("=" * 60)
print("If 100 rupees must be split between 3 people, the total is 33.33")
print("but you cannot split a coin, so each person gets 33 and 1 is left.")
print("That leftover is the remainder.")

total_bill = 100
people = 3
each = total_bill // people
left_over = total_bill % people
print("each person gets :", each)
print("left over        :", left_over)
print("check            :", each * people, "+", left_over, "=", each * people + left_over)

print()
print("=" * 60)
print("READING INTEGERS WITH UNDERSCORES")
print("=" * 60)
print("Underscores only improve readability. The value is unchanged.")

million = 1_000_000
billion = 1_000_000_000
print("1_000_000      =", million)
print("1_000_000_000  =", billion)
print("Without them it would be 1000000 and 1000000000.")
print("type(1_000_000) =", type(million).__name__)

print()
print("=" * 60)
print("HOW TO CREATE AN INTEGER")
print("=" * 60)
print("""
Direct literals:     42, -7, 0, 1_000_000
From other types:     int(42.9), int("42")
From calculations:    10 + 5, 3 * 4, 7 // 2
From input:           int(input("Enter a number: "))
""")

print("int(42.9)  =", int(42.9), "  (truncates toward zero)")
print("int(-42.9) =", int(-42.9), " (also truncates toward zero)")
print('int("42")  =', int("42"))
print('int("42.9") -> ValueError, a text decimal is not accepted')
print("int(42.9)  =", int(42.9), " (truncates toward zero)")

print()
print("=" * 60)
print("BOOLEAN RESULTS FROM COMPARISONS ARE INTS TOO")
print("=" * 60)
print("In Python, comparisons return True or False, which are int subclasses:")
print("True  is like 1, False is like 0")
print("True + True     =", True + True)
print("True * 10       =", True * 10)
print("int(True)       =", int(True))
print("int(False)      =", int(False))

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print('1. 0.5 + 1 gives 1.5, not an int. A single decimal makes a float.')
print('2. Dividing with / always gives a float. Use // when you want an int.')
print('   10 / 2 =', 10 / 2, " type:", type(10 / 2).__name__)
print('   10 // 2 =', 10 // 2, " type:", type(10 // 2).__name__)
print('3. Dividing by zero fails:')
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("   10 / 0 ->", type(error).__name__, ":", error)
print("   // and % also fail the same way.")
print('4. int("abc") fails:')
try:
    int("abc")
except ValueError as error:
    print('   int("abc") ->', type(error).__name__, ":", error)
print('5. int("42.9") works but int("42.9.1") does not.')

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- int holds whole numbers, and there is no size limit.
- / gives a float, // gives a whole number, % gives the remainder.
- Underscores in large numbers are only for readability.
- Order of operations: () then ** then * / // % then + -
- Dividing by zero raises ZeroDivisionError.
""")