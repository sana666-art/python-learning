"""Topic 3: Comparison Operators

Comparison operators test two values and answer with True or False. They are
the foundation of every if statement and every loop condition.

Run with:  python 03-comparison-operators.py
"""

print("=" * 60)
print("THE SIX COMPARISON OPERATORS")
print("=" * 60)
print("""
Symbol   Reads as            Example      Result
------   ------------------  -----------  ------
==       equal to            5 == 5       True
!=       not equal to        5 != 5       False
>        greater than        5 > 3        True
<        less than           5 < 3        False
>=       greater or equal    5 >= 5       True
<=       less or equal       5 <= 4       False
""")

print("=" * 60)
print("BASIC COMPARISONS")
print("=" * 60)

print("5 == 5       ->", 5 == 5)
print("5 == 6       ->", 5 == 6)
print("5 != 6       ->", 5 != 6)
print("5 > 3        ->", 5 > 3)
print("5 < 3        ->", 5 < 3)
print("5 >= 5       ->", 5 >= 5)
print("5 <= 4       ->", 5 <= 4)
print("10 >= 10     ->", 10 >= 10)
print("10 <= 9      ->", 10 <= 9)

print()
print("Every result is a bool:")
print("type(5 == 5) ->", type(5 == 5).__name__)

print()
print("=" * 60)
print("THE SINGLE = VERSUS DOUBLE ==")
print("=" * 60)
print("This is the most expensive beginner mistake, because = assigns and")
print("== compares, yet both run without complaint in different places.")

value = 5
print("value = 5      is an assignment. It stores and returns the value.")
print("value == 5     is a comparison. It answers True or False.")
print()
print("value = 5  ->", value)
print("value == 5 ->", value == 5)
print()
print("Inside an if, only the comparison works. The assignment raises a")
print("SyntaxError because Python refuses to hide a bug in a condition:")

try:
    compile("if value = 5:\n    pass", "<string>", "exec")
except SyntaxError as error:
    print("   if value = 5:  ->", type(error).__name__, ":", error.msg)

print()
print("=" * 60)
print("COMPARING DIFFERENT TYPES")
print("=" * 60)
print("Numbers compare by value across int and float:")

print("5 == 5.0      ->", 5 == 5.0, "  (same value, different type)")
print("type(5)       ->", type(5).__name__)
print("type(5.0)     ->", type(5.0).__name__)
print("5 is 5.0      ->", 5 is 5.0, "  (different objects, see topic 6)")
print("5 > 4.5       ->", 5 > 4.5)
print("10 == 10.001  ->", 10 == 10.001)

print()
print("Text compares by character order, one position at a time:")
print('"apple" == "apple" ->', "apple" == "apple")
print('"apple" == "Apple" ->', "apple" == "Apple", "  (case matters)")
print('"apple" < "banana" ->', "apple" < "banana")
print('"abc" < "abd"      ->', "abc" < "abd")
print('"abc" < "ab"       ->', "abc" < "ab", "  (a shorter prefix is smaller)")
print('"Z" < "a"          ->', "Z" < "a", "  (uppercase sorts first)")

print()
print("Comparing numbers with text is meaningless, so Python refuses:")
for expression, run in [
    ("5 > 'a'", lambda: 5 > "a"),
    ("'5' > 3", lambda: "5" > 3),
]:
    try:
        run()
    except TypeError as error:
        print(f"   {expression:<10} -> {type(error).__name__}: {error}")

print()
print("Compare like with like, or convert first with int() or str().")

print()
print("=" * 60)
print("CHAINED COMPARISONS")
print("=" * 60)
print("Python lets you write a chain, which behaves like and.")

a, b, c = 10, 20, 30
print("a, b, c =", a, b, c)
print("a < b < c   ->", a < b < c)
print("a < b and b < c ->", a < b and b < c, "  (same answer)")
print()
print("Each form is valid:")
print("a < b <= c  ->", a < b <= c)
print("a == b == c ->", a == b == c)
print("a >= b >= c ->", a >= b >= c)
print("1 <= 2 <= 3 <= 4 ->", 1 <= 2 <= 3 <= 4)

print()
print("A chain must have the operators in the same direction:")
print("a < b > c   ->", a < b > c, "  (legal, but reads oddly)")
print("  This means a < b AND b > c, which is a different question.")

print()
print("Chains avoid repeating a variable, which matters when it costs")
print("something to evaluate:")


def check(value):
    """Print when called, so you can see how often a chain evaluates."""
    print("   check() called with", value)
    return value


print("check(5) < check(10) < check(15):")
print("   result ->", check(5) < check(10) < check(15))
print()
print("The middle operand is evaluated only once. Writing it as two separate")
print("comparisons would call check(10) twice.")

print()
print("=" * 60)
print("COMPARING BOOLEANS")
print("=" * 60)
print("True and False are also ints, so comparisons on them work.")

print("True == True   ->", True == True)
print("True == 1      ->", True == 1, "  (bool is a subclass of int)")
print("False == 0     ->", False == 0)
print("True > False   ->", True > False)
print("True == 'True' ->", True == "True", "  (different types)")

print()
print("Prefer a direct condition over comparing to True:")
is_active = True
print("if is_active:            ->", "clear" if is_active else "not run")
print("if is_active == True:    ->", "works but wordy")
print("if is_active is True:    ->", "works but too strict for truthy values")
print("if not is_active:        ->", "the clearest way to ask for False")

print()
print("=" * 60)
print("COMPARING None")
print("=" * 60)
print("None is neither equal to nor ordered against other values.")

print("None == None   ->", None == None)
print("None != None   ->", None != None)
print("None is None   ->", None is None, "  (the correct check)")
print()
print("Comparing None with a number gives False, not an error:")
print("None == 0      ->", None == 0)
print("None == False  ->", None == False)
print()
print("For None, use 'is None'. Topic 6 covers identity in full.")

print()
print("=" * 60)
print("FLOAT COMPARISONS ARE UNRELIABLE AFTER ARITHMETIC")
print("=" * 60)
print("Binary storage means the result is rarely exact.")

print("0.1 + 0.2 == 0.3     ->", 0.1 + 0.2 == 0.3)
print("0.1 + 0.2            ->", 0.1 + 0.2)
print()
print("Two safe approaches:")

first, second = 0.1 + 0.2, 0.3
print("1. Round both sides  ->", round(first, 9) == round(second, 9))
print("2. Compare the gap   ->", abs(first - second) < 1e-9)

print()
print("Never write float equality checks straight after calculation.")

print()
print("=" * 60)
print("COMPARING COLLECTIONS (PREVIEW)")
print("=" * 60)
print("Lists, tuples, sets and dicts each have their own comparison rules.")
print("They are covered in their own sections, but here is the shape of it:")

print("[1, 2] == [1, 2]     ->", [1, 2] == [1, 2])
print("[1, 2] == [2, 1]     ->", [1, 2] == [2, 1], "  (order matters)")
print("(1, 2) == (1, 2)     ->", (1, 2) == (1, 2))
print("{1, 2} == {2, 1}     ->", {1, 2} == {2, 1}, "  (order does not)")
print('{"a": 1} == {"a": 1} ->', {"a": 1} == {"a": 1})

print()
print("=" * 60)
print("COMPARISONS INSIDE CONDITIONS")
print("=" * 60)

marks = 72
attendance = True
submitted = False

print("marks =", marks, "| attendance =", attendance, "| submitted =", submitted)
print()
print("marks >= 40                ->", marks >= 40)
print("marks >= 40 and attendance ->", marks >= 40 and attendance)
print("not submitted              ->", not submitted)
print("marks < 50 or attendance   ->", marks < 50 or attendance)
print()
print("Combining with a variable is often clearer than a raw comparison:")

is_pass = marks >= 40 and attendance
print("is_pass = marks >= 40 and attendance ->", is_pass)
print("Store it once and read it many times.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Using = instead of == inside an if condition.
2. Forgetting that == on floats fails after arithmetic.
3. Chaining comparisons in different directions and assuming it means or.
   a < b < c is and, not or.
4. Expecting '10' == 10 to be True. Text and numbers never match with ==.
5. Comparing with == when the value may be None. Use 'is None'.
6. Assuming text compares by length. It compares character by character.
7. Expecting == on two different objects of equal content to mean they are
   the same object. That is identity, not equality.
""")

print("Quick proofs:")
print("   'abc' < 'ab'   ->", "abc" < "ab")
print("   '10' == 10     ->", "10" == 10)
print("   0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
print("   a < b < c with a=10 b=5 c=1 ->", 10 < 5 < 1)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Six operators: == != > < >= <=, and each returns a bool.
- = assigns, == compares, and the difference matters inside conditions.
- Chained comparisons use and and evaluate the middle operand once.
- int and float compare by value; text compares character by character;
  mixing the two raises TypeError.
- Float equality needs rounding or a tolerance.
- None is checked with is None, not == None.
""")