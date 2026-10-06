"""Topic 9: Common Operator Mistakes

A tour of the mistakes learners actually make, with the failing line, why it
fails, and the version that works.

Run with:  python 09-common-operator-mistakes.py
"""

print("=" * 60)
print("MISTAKE 1: = USED WHERE == WAS MEANT")
print("=" * 60)
print("A single = assigns. It cannot be used inside an if or while, because")
print("Python has no assignment expression there and raises SyntaxError.")

try:
    compile("if score = 10:\n    pass", "<string>", "exec")
except SyntaxError as error:
    print("if score = 10:   -> SyntaxError:", error.msg)

print()
print("score = 10 is a statement. score == 10 is a test.")
score = 10
print("if score == 10 ->", "matched" if score == 10 else "no match")
print()
print("The rule: = makes, == asks.")

print()
print("=" * 60)
print("MISTAKE 2: FLOATS ARE NOT EXACT")
print("=" * 60)
print("Some decimal numbers cannot be stored exactly in binary, so equality")
print("on floats quietly gives the wrong answer.")

total = 0.1 + 0.2
print("0.1 + 0.2            ->", total)
print("total == 0.3         ->", total == 0.3, "  (surprising)")
print("total                 ->", repr(total))
print()
print("Fix 1, compare with a tolerance:")
print("abs(total - 0.3) < 1e-9  ->", abs(total - 0.3) < 1e-9)

print()
print("Fix 2, for serious work use the math module:")
import math

print("math.isclose(total, 0.3) ->", math.isclose(total, 0.3))
print()
print("Never use == on floats that came from a calculation.")

print()
print("=" * 60)
print("MISTAKE 3: / ALWAYS RETURNS A FLOAT")
print("=" * 60)
print("Whole numbers quietly become decimals, and later code that expects an")
print("int fails.")

print("6 / 3   ->", 6 / 3, "  type:", type(6 / 3).__name__)
print("6 // 3  ->", 6 // 3, "  type:", type(6 // 3).__name__)
print()
print("Where the result must be a whole number, use // or round():")
print("int(7 / 2)   ->", int(7 / 2), "  (truncates toward zero: 3)")
print("7 // 2       ->", 7 // 2, "  (floor division: 3)")
print("-7 // 2      ->", -7 // 2, "  (floors down: -4, not -3)")
print("int(-7 / 2)  ->", int(-7 / 2), "  (truncates toward zero: -3)")
print()
print("Floor and truncate disagree for negative numbers. Choose deliberately.")

print()
print("=" * 60)
print("MISTAKE 4: THE SAME OPERATOR ON THE WRONG TYPE")
print("=" * 60)
print("Mixing families raises TypeError rather than converting for you.")

for label, run in [
    ('"5" + 5', lambda: "5" + 5),
    ('"5" * 3', lambda: "5" * 3),
    ("[1] + (2,)", lambda: [1] + (2,)),
    ("5 > '3'", lambda: 5 > "3"),
]:
    try:
        print(f"   {label:<22} -> {run()!r}")
    except TypeError as error:
        print(f"   {label:<22} -> TypeError: {error}")

print()
print("Not every mix is an error, which is what makes this confusing:")
print('   "5" * 3 ->', "5" * 3, "  (text repeated 3 times, legal)")
print("   5 * 3   ->", 5 * 3, "  (arithmetic, also legal)")
print("Same symbol, two different meanings depending on the type on the left.")

print()
print("Python does not guess. Convert explicitly when you mean to mix types:")
print('   int("5") + 5      ->', int("5") + 5)
print('   str(5) + " items" ->', str(5) + " items")

print()
print("=" * 60)
print("MISTAKE 5: COMPARING DIFFERENT TYPES")
print("=" * 60)
print("Numbers and text have no common order, so < and > refuse to answer.")

for label, run in [
    ("5 > '3'", lambda: 5 > "3"),
    ("[] > 0", lambda: [] > 0),
    ("None < 1", lambda: None < 1),
]:
    try:
        print(f"   {label:<14} -> {run()!r}")
    except TypeError as error:
        print(f"   {label:<14} -> TypeError: {error}")

print()
print("== is different from < here. Unequal types are simply not equal:")
print("   5 == '5'  ->", 5 == "5", "  (no error, just False)")

print()
print("=" * 60)
print("MISTAKE 6: and and or RETURN OPERANDS, NOT BOOLEANS")
print("=" * 60)
print("Code that expects True or False from them breaks in subtle ways.")

result = "" or "fallback"
print('   "" or "fallback"  ->', repr(result), type(result).__name__)
result = 0 and "text"
print("   0 and 'text'      ->", repr(result), type(result).__name__)
print()
print("Where a real bool is needed, wrap it:")
print("   bool(0 and 'text') ->", bool(0 and "text"))
print("   bool('' or 1)      ->", bool("" or 1))

print()
print("The default value trap is the same problem:")
count = 0
label = count or "unknown"
print("   count = 0")
print("   label = count or 'unknown' ->", label, "  <- 0 was thrown away")
label = count if count is not None else "unknown"
print("   label = count if count is not None else 'unknown' ->", label)
print()
print("or only gives the fallback when the left side is falsy, and 0, '' and")
print("[] are all falsy but perfectly valid values.")

print()
print("=" * 60)
print("MISTAKE 7: is USED FOR EQUALITY")
print("=" * 60)
print("is asks about the object, == asks about the content. Numbers and text")
print("make this fail in ways that look random.")

print("   a = 257, b = 257 built at run time")
a = int("257")
b = int("257")
print("   a == b ->", a == b)
print("   a is b ->", a is b, "  <- do not rely on this either way")
print()
print("   value = None; value is None ->", None is None)
print("   value == None               ->", True, "  <- works but is not the")
print("                                              standard form")
print()
print("Rule: == for content, is only for None and for questions about")
print("which object a name references.")

print()
print("=" * 60)
print("MISTAKE 8: CHAINED ASSIGNMENT ON A MUTABLE VALUE")
print("=" * 60)
print("Assigning the same list to two names creates two names for one list,")
print("not two lists.")

row_a = row_b = [1, 2]
print("row_a = row_b = [1, 2]")
row_b.append(3)
print("row_b.append(3)")
print("   row_a ->", row_a, "  <- changed as well")
print("   row_b ->", row_b)
print()
print("Build a separate copy when separate data is wanted:")
row_c = [1, 2]
row_d = row_c.copy()
row_d.append(3)
print("   row_c ->", row_c, "  (untouched)")
print("   row_d ->", row_d)

print()
print("=" * 60)
print("MISTAKE 9: += ON A MUTABLE SHARED BY ANOTHER NAME")
print("=" * 60)
print("Augmented assignment on a list modifies it in place, so every name")
print("that shares it sees the change. On an int it creates a new value, so")
print("the other name is unaffected. The two operators behave differently.")

number_a = 10
number_b = number_a
number_a += 5
print("number_a = 10, number_b = number_a, number_a += 5")
print("   number_a ->", number_a)
print("   number_b ->", number_b, "  (ints are immutable, so untouched)")

list_a = [1, 2]
list_b = list_a
list_a += [3]
print()
print("list_a = [1, 2], list_b = list_a, list_a += [3]")
print("   list_a ->", list_a)
print("   list_b ->", list_b, "  (same object, so it changed too)")

print()
print("Read += as 'modify in place if the type allows, otherwise rebuild'.")

print()
print("=" * 60)
print("MISTAKE 10: DIVISION BY ZERO AND MODULO BY ZERO")
print("=" * 60)
print("Both are runtime errors, not warnings, and they stop the program.")

for label, run in [("10 / 0", lambda: 10 / 0),
                   ("10 // 0", lambda: 10 // 0),
                   ("10 % 0", lambda: 10 % 0),
                   ("10 ** 0", lambda: 10 ** 0)]:
    try:
        print(f"   {label:<10} -> {run()}")
    except ZeroDivisionError:
        print(f"   {label:<10} -> ZeroDivisionError")
print()
print("Note 10 ** 0 is 1, because anything to the power zero is one.")

print()
print("=" * 60)
print("MISTAKE 11: in CHECKS DICTIONARY KEYS ONLY")
print("=" * 60)
print("Searching a dictionary for a value with in returns False even when the")
print("value is clearly present.")

student = {"name": "Ali", "age": 20}
print("student =", student)
print('   "Ali" in student           ->', "Ali" in student)
print('   "Ali" in student.values()  ->', "Ali" in student.values())
print()
print("The same trap appears when a beginner expects a list to contain a")
print("substring, because in on a list looks for whole items:")
words = ["red", "green"]
print('   "green" in words  ->', "green" in words)
print('   "gre" in words    ->', "gre" in words, "  (not a whole item)")
print('   "gre" in "green"  ->', "gre" in "green", "  (in text it is a substring)")

print()
print("=" * 60)
print("MISTAKE 12: PRECEDENCE MISREAD")
print("=" * 60)
print("These four lines each answer a different question.")

print("   -2 ** 2                 ->", -2 ** 2, "  (not 4)")
print("   2 ** 3 ** 2             ->", 2 ** 3 ** 2, "  (not 64)")
print("   not True or False       ->", not True or False, "  (not True)")
print("   1 + 2 * 3 == 9          ->", 1 + 2 * 3 == 9,
      "  (the left side is 7)")
print()
print("If the answer surprises you, brackets will settle it.")
print("   (-2) ** 2               ->", (-2) ** 2)
print("   (2 ** 3) ** 2           ->", (2 ** 3) ** 2)
print("   not (True or False)     ->", not (True or False))

print()
print("=" * 60)
print("MISTAKE 13: INPUT IS ALWAYS TEXT")
print("=" * 60)
print("input() returns str, so arithmetic on it either fails or repeats text.")

print('   "2" + 3   -> TypeError (different types)')
print('   "2" * 3   ->', "2" * 3, "  (legal but not what was meant)")
print('   "5" * "2" -> TypeError (text times text is not allowed)')
print()
print("Convert at the point of reading:")
value = int("42")
print('   int("42") + 8 ->', value + 8)
print()
print("And guard against text that is not a number:")
for text in ["42", "forty-two"]:
    try:
        print(f"   int({text!r:>14}) ->", int(text))
    except ValueError as error:
        print(f"   int({text!r:>14}) -> ValueError: {error}")

print()
print("=" * 60)
print("MISTAKE 14: BOOLEANS ACT AS NUMBERS")
print("=" * 60)
print("Because bool is a subclass of int, True is 1 and False is 0 in")
print("arithmetic. That is sometimes handy and often confusing.")

print("   True + True  ->", True + True)
print("   True * 10    ->", True * 10)
print("   5 - False    ->", 5 - False)
print("   sum([1, 0, 1, 1]) ->", sum([1, 0, 1, 1]),
      "  (bools would count the same way)")
print()
print("Use it on purpose, such as counting matches:")
flags = [True, False, True, True]
print("   flags =", flags)
print("   sum(flags) ->", sum(flags), "  (three True values)")

print()
print("=" * 60)
print("MISTAKE 15: OPERATOR ON A CUSTOM OBJECT")
print("=" * 60)
print("Python does not know how to add two of your own objects unless you")
print("teach it. Comparing them without a rule raises TypeError too.")


class Money:
    """A tiny value type that defines + and == for demonstration."""

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __repr__(self):
        return f"Money({self.amount})"


first = Money(10)
second = Money(5)
print("first  =", first)
print("second =", second)
print("first + second ->", first + second)
print("first == second ->", first == second)

try:
    first + 5
except TypeError as error:
    print("first + 5 -> TypeError:", error)
print()
print("Without __add__, even the first line would fail. This is why == and +")
print("work on lists but not on every object you create.")

print()
print("=" * 60)
print("SUMMARY OF FIXES")
print("=" * 60)
print("""
 = vs ==          use == to test, = to assign
 floats           never compare with ==, use math.isclose or a tolerance
 / vs //          / always returns float, // returns int
 mixed types      convert explicitly, Python will not guess
 ordering         < across different types raises TypeError
 and / or         they return operands, wrap in bool() when needed
 is               reserve it for None and identity questions
 chained =        builds one shared object, use .copy() for separate data
 += on lists      modifies in place, so every name sharing it sees the change
 zero             / // and % all raise on 0, ** does not
 in on dict       checks keys, use .values() for values
 precedence       brackets when in doubt
 input()          always returns str
 bool as int      True is 1 and False is 0 in arithmetic
 custom objects   define __add__ and __eq__ before using operators
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Most operator bugs come from type mismatches, precedence, or expecting
  Python to convert values on its own.
- Equality on floats, identity on numbers and in on dictionaries are the
  three traps that look correct until they quietly are not.
- Read the error message first. TypeError almost always means the two
  sides belong to different families.
- Brackets and explicit conversions remove nearly all ambiguity.
""")