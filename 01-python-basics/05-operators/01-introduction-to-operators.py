"""Topic 1: Introduction to Operators

Operators are the symbols that ask Python to do something: add, compare,
check membership, and so on. The values they work on are called operands.

Run with:  python 01-introduction-to-operators.py
"""

from typing import Any, cast

print("=" * 60)
print("WHAT IS AN OPERATOR?")
print("=" * 60)
print("""
An operator is a symbol that performs an operation on one or more values.

    5 + 3
    ^ ^ ^
    | | |
    | | the right operand
    | the operator
    the left operand

The values around an operator are called operands. The result of an operator
is called the value of the expression.
""")

print("=" * 60)
print("OPERATORS AND OPERANDS IN ACTION")
print("=" * 60)

left = 5
right = 3
result = left + right

print("left   =", left, "  (left operand)")
print("right  =", right, "  (right operand)")
print("+      is the operator")
print("result =", result, "  (value of the expression)")
print()
print("Every operator in this folder follows the same pattern: symbols in the")
print("middle, operands on the sides, one result out.")

print()
print("=" * 60)
print("WHAT IS AN EXPRESSION?")
print("=" * 60)
print("""
An expression is any combination of values and operators that produces a
value. A statement does something, an expression produces something.

Expression:  5 + 3,  total * 1.17,  name.upper(),  10 > 5
Statement:   print(5 + 3),  total = 5 + 3,  if 10 > 5:

The statement  total = 5 + 3  contains the expression  5 + 3, whose value is
8, and then stores that value in total.
""")

total = 5 + 3
print("5 + 3   is an expression, its value is", 5 + 3)
print("total = 5 + 3   is a statement, it stores", total)
print("10 > 5   is an expression too, its value is", 10 > 5)

print()
print("=" * 60)
print("EXPRESSIONS PRODUCE A TYPE")
print("=" * 60)
print("Every operator returns a value of some type. The type is the clue to")
print("what the operator was really doing.")

pairs = [
    ("5 + 3", 5 + 3),
    ("5 - 3", 5 - 3),
    ("5 * 3", 5 * 3),
    ("5 / 3", 5 / 3),
    ("5 > 3", 5 > 3),
    ("5 == 3", 5 == 3),
    ('"a" + "b"', "a" + "b"),
    ('"ab" in "cab"', "ab" in "cab"),
    ("5 is 5", 5 is 5),
]

print(f"{'expression':<16}{'value':<14}{'type'}")
print("-" * 44)
for expression, value in pairs:
    print(f"{expression:<16}{str(value):<14}{type(value).__name__}")

print()
print("Notice the pattern:")
print("  Arithmetic operators return numbers.")
print("  Comparison operators return bool.")
print("  The + operator on text returns text, because + is overloaded to work")
print("  on more than one type.")

print()
print("=" * 60)
print("THE CATEGORIES OF OPERATORS")
print("=" * 60)
print("""
Arithmetic     +  -  *  /  //  %  **          numbers
Comparison     ==  !=  >  <  >=  <=           True or False
Assignment     =  +=  -=  *=  /=  //=  %=  **=  stores a value
Logical        and  or  not                   combines conditions
Identity       is  is not                    same object?
Membership     in  not in                     inside something?
Bitwise        &  |  ^  ~  <<  >>            binary digits, advanced
""")

print("=" * 60)
print("SOME OPERATORS WORK ON SEVERAL TYPES")
print("=" * 60)
print("+ on numbers adds. + on text joins. This is called operator overloading.")

print("5 + 3    =", 5 + 3, "  (numbers, added)")
print('"a" + "b" =', "a" + "b", "  (text, joined)")
print("[1] + [2] =", [1] + [2], "  (lists, joined)")

print()
print("* is the same idea:")
print('5 * 3    =', 5 * 3, "  (number, multiplied)")
print('"ab" * 3  =', "ab" * 3, "  (text, repeated)")

print()
print("=" * 60)
print("UNARY VS BINARY OPERATORS")
print("=" * 60)
print("""
Binary operators sit between two operands:   5 + 3
Unary operators take one operand:            -5,   not True

The minus sign is both. It is unary when it appears alone and binary when it
is between two values.
""")

value = -5
print("-5            unary minus, one operand:", value)
print("10 - 5        binary minus, two operands:", 10 - 5)
print("-value        unary again:", -value)
print("value - -5    binary with a unary inside:", value - -5)

print()
print("=" * 60)
print("OPERATORS CAN BE CHAINED AND COMBINED")
print("=" * 60)

a = 10
b = 20
c = 30
print("a = 10, b = 20, c = 30")
print("a + b + c      =", a + b + c)
print("a + b * c      =", a + b * c, "  (* runs before +, see topic 8)")
print("(a + b) * c    =", (a + b) * c, "  (brackets change the order)")
print("a < b < c      =", a < b < c, "  (comparison chaining)")
print("a > 0 and b > 0 =", a > 0 and b > 0, "  (logical operator)")

print()
print("=" * 60)
print("WHERE OPERATORS APPEAR IN REAL CODE")
print("=" * 60)

price = 500
quantity = 3
rate = 0.17
discount = 0.10

subtotal = price * quantity
discount_amount = subtotal * discount
after_discount = subtotal - discount_amount
tax = after_discount * rate
total = after_discount + tax

print("price * quantity              :", subtotal)
print("subtotal * discount           :", round(discount_amount, 2))
print("subtotal - discount_amount    :", round(after_discount, 2))
print("after_discount * rate         :", round(tax, 2))
print("after_discount + tax          :", round(total, 2))
print()
print("Five operators, one calculation, and the result reads like the maths.")
print("Writing the same formula in code is mostly a matter of using the")
print("right operator in the right place.")

print()
print("=" * 60)
print("A NOTE ON OPERATOR OVERLOADING AND ERRORS")
print("=" * 60)
print("Not every operator accepts every type. Mixing types raises TypeError.")

for expression, run in [
    ("5 + 'a'", lambda: cast(Any, 5) + cast(Any, "a")),
    ("5 > 'a'", lambda: cast(Any, 5) > cast(Any, "a")),
    ("5 + None", lambda: cast(Any, 5) + cast(Any, None)),
    ("5 in 'abc'", lambda: cast(Any, 5) in cast(Any, "abc")),
]:
    try:
        value = run()
        print(f"   {expression:<12} -> {value!r}")
    except TypeError as error:
        print(f"   {expression:<12} -> TypeError: {error}")

print()
print("5 > 'a' fails because there is no sensible ordering between a number")
print("and text, whereas 5 in 'abc' fails because text only holds characters.")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- An operator is a symbol, operands are the values it works on.
- An expression produces a value; a statement does something.
- Each operator returns a value of a specific type.
- Categories: arithmetic, comparison, assignment, logical, identity,
  membership and bitwise.
- The same symbol can work on several types, and some combinations are
  illegal and raise TypeError.
""")