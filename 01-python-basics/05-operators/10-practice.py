"""Topic 10: Operators Practice

Work through the questions, write your own version, then compare with the
answers at the bottom of this file.

Run with:  python 10-practice.py
"""

print("=" * 60)
print("OPERATORS: PRACTICE EXERCISES")
print("=" * 60)
print("""
Work top to bottom. For each question, predict the result first, then
check yourself. Write your code in a separate file or in the marked
spaces below.

The ANSWER SECTION at the end of the file runs every solution.
""")

print()
print("=" * 60)
print("QUESTIONS")
print("=" * 60)

print("""
Q1. Arithmetic
    Work out each value by hand, then confirm with Python.
    a) 7 + 3 * 2
    b) (7 + 3) * 2
    c) 17 // 5, 17 / 5, 17 % 5
    d) 2 ** 3 ** 2
    e) -7 // 2 and -7 / 2
      # your code here
""")

print("""
Q2. Remainders and even numbers
    Write an expression using % that is True when n is even.
    Test it with n = 4 and n = 7.
      # your code here
""")

print("""
Q3. Conversions
    A temperature of 36.6 Celsius is read as text: "36.6".
    Convert it to a float, check whether it is above 37.5, and report
    True or False.
      # your code here
""")

print("""
Q4. Comparisons
    Set score = 75. Answer True or False and explain why.
    a) score > 70
    b) score == 75 and score != 100
    c) score < 60 or score > 90
    d) not score > 90
      # your code here
""")

print("""
Q5. Chained comparisons
    Rewrite each of these with and, then state the result.
    a) 15 < 20 < 25
    b) 10 < 5 < 8
      # your code here
""")

print("""
Q6. Assignment operators
    Starting with count = 12, apply these in order and give the value
    after each line.
    a) count += 8
    b) count -= 4
    c) count *= 2
    d) count //= 5
    e) count %= 4
    f) count **= 3
      # your code here
""")

print("""
Q7. Swap without a temp variable
    Set a = 5 and b = 9. Swap them in one line using , = , and print both.
      # your code here
""")

print("""
Q8. Logical operators
    age = 20, has_ticket = False, is_banned = False. Evaluate.
    a) age >= 18 and has_ticket
    b) has_ticket or not is_banned
    c) not is_banned and (age >= 18 or has_ticket)
      # your code here
""")

print("""
Q9. Short circuit
    Without running Python, say whether the right side of each is
    evaluated, then check.
    a) False and print("ran")
    b) True or print("ran")
    c) True and print("ran")
    d) False or print("ran")
      # your code here
""")

print("""
Q10. and / or returning values
    Give the result and its type.
    a) 0 or 42
    b) "" or None
    c) 3 and "yes"
    d) None or []
    e) bool(0 or 0.0)
      # your code here
""")

print("""
Q11. Safe defaults
    user = None. Produce the string "guest" using or.
    Then set user = "" and show what happens. Fix it so an empty name
    is still replaced by "guest".
      # your code here
""")

print("""
Q12. Identity
    a) Check that x is None when x = None.
    b) Set n1 = int("256") and n2 = int("256"). Are they ==
       and are they the same object?
    c) Set n3 = int("300") and n4 = int("300"). Same two questions.
    d) Why can you not trust the answer to c?
      # your code here
""")

print("""
Q13. Membership
    fruits = ["apple", "banana", "cherry"]
    student = {"name": "Sara", "grade": 9}
    a) Is "banana" in fruits?
    b) Is "BANANA" in fruits? Explain.
    c) Is "grape" not in fruits?
    d) Is "Sara" in student? Why not?
    e) Is "Sara" in student.values()?
      # your code here
""")

print("""
Q14. Membership and strings
    message = "operators are fun"
    a) Is "are" in message?
    b) Is "Are" in message?
    c) Is "" in message?
    d) Split message into words and check whether "fun" is in the list.
      # your code here
""")

print("""
Q15. Precedence
    Add brackets that make the left side equal the right side, or state
    that it already matches.
    a) 2 + 3 * 4 == 20
    b) -3 ** 2 == -9
    c) not True and False == False
    d) 1 + 2 == 3 and 4 < 5
      # your code here
""")

print("""
Q16. One value from a condition
    temperature = 12. Print "cold" when it is below 15, otherwise
    "mild", using a single conditional expression with if else.
      # your code here
""")

print("""
Q17. Choosing an operator
    For each, write the operator or expression that does the job.
    a) Test whether a value is absent.
    b) Test whether two names point at the same list.
    c) Test whether a number equals 0.
    d) Supply a default only when the value is None.
    e) Round 7.9 down to a whole number keeping the type as int.
      # your code here
""")

print("""
Q18. Build a small report
    price = 49.5, quantity = 3, discount = 0.1.
    a) Total before discount.
    b) Discount amount, rounded to 2 decimals.
    c) Final price rounded to 2 decimals.
    d) Is the final price below 150? Print the answer as text.
      # your code here
""")

print("""
BONUS 1. Guards without conditions
    scores = [].
    Use and and or only (no if) to print the first score, or the string
    "no scores" when the list is empty.
      # your code here
""")

print("""
BONUS 2. Membership timing
    Given words = ["python", "operator", "precedence", "identity"] and
    targets = ["cat", "identity", "dog"], find which targets are missing
    using not in, and print them in one line.
      # your code here
""")

print()
print("=" * 60)
print("WHEN YOU ARE READY")
print("=" * 60)
print("""
Check your work against the ANSWER SECTION below, then run this file to
see every solution printed with its result.

python 10-practice.py
""")


# =====================================================================
# ANSWER SECTION
# =====================================================================
# Everything below solves the questions above. It runs so that you can
# compare your prediction with the real result.

print()
print("=" * 60)
print("ANSWER SECTION")
print("=" * 60)


def show(question, expression, result):
    """Print a question label, the expression, and its result."""
    print(f"   {question:<10} {expression:<34} -> {result}")


print()
print("Q1. Arithmetic")
show("a)", "7 + 3 * 2", 7 + 3 * 2)
show("b)", "(7 + 3) * 2", (7 + 3) * 2)
show("c) //", "17 // 5", 17 // 5)
show("c) /", "17 / 5", 17 / 5)
show("c) %", "17 % 5", 17 % 5)
show("d)", "2 ** 3 ** 2", 2 ** 3 ** 2)
show("e) //", "-7 // 2", -7 // 2)
show("e) /", "-7 / 2", -7 / 2)
print("   / returns -3.5 and // floors to -4. They disagree for negatives.")

print()
print("Q2. Remainders and even numbers")
for n in [4, 7]:
    print(f"   n = {n}   n % 2 == 0 -> {n % 2 == 0}")
print("   Even numbers have no remainder when split into pairs.")
print("   A number is odd when n % 2 == 1, or more safely when n % 2 != 0.")

print()
print("Q3. Conversions")
text = "36.6"
degrees = float(text)
print(f'   float("{text}") -> {degrees}')
print(f"   degrees > 37.5 -> {degrees > 37.5}")
print("   Always convert the text once, then compare the number.")

print()
print("Q4. Comparisons")
score = 75
show("a)", "score > 70", score > 70)
show("b)", "score == 75 and score != 100", score == 75 and score != 100)
show("c)", "score < 60 or score > 90", score < 60 or score > 90)
show("d)", "not score > 90", not score > 90)
print("   d) reads as not (score > 90). not binds looser than >.")
print("      not score > 90 is the same as score <= 90.")

print()
print("Q5. Chained comparisons")
show("a)", "15 < 20 < 25", 15 < 20 < 25)
show("a)", "15 < 20 and 20 < 25", 15 < 20 and 20 < 25)
show("b)", "10 < 5 < 8", 10 < 5 < 8)
show("b)", "10 < 5 and 5 < 8", 10 < 5 and 5 < 8)
print("   b) fails on the first link, so the whole chain is False.")

print()
print("Q6. Assignment operators")
count = 12
print(f"   start          count = {count}")
count += 8
print(f"   a) count += 8  count = {count}")
count -= 4
print(f"   b) count -= 4  count = {count}")
count *= 2
print(f"   c) count *= 2  count = {count}")
count //= 5
print(f"   d) count //= 5 count = {count}   (still an int)")
count %= 4
print(f"   e) count %= 4  count = {count}")
count **= 3
print(f"   f) count **= 3 count = {count}")

print()
print("Q7. Swap")
a, b = 5, 9
print(f"   before  a = {a}, b = {b}")
a, b = b, a
print(f"   after   a = {a}, b = {b}")
print("   The right side (b, a) is built first as a tuple, then unpacked.")

print()
print("Q8. Logical operators")
age = 20
has_ticket = False
is_banned = False
print(f"   age = {age}, has_ticket = {has_ticket}, is_banned = {is_banned}")
show("a)", "age >= 18 and has_ticket", age >= 18 and has_ticket)
show("b)", "has_ticket or not is_banned", has_ticket or not is_banned)
show("c)", "not is_banned and (age >= 18 or has_ticket)",
     not is_banned and (age >= 18 or has_ticket))
print("   a) is False because has_ticket is False, and both were needed.")

print()
print("Q9. Short circuit")
print("   Only the right sides that are needed will print:")
print("   a) False and print(...)")
False and print("      a) side effect happened")
print("   b) True or print(...)")
True or print("      b) side effect happened")
print("   c) True and print(...)")
True and print("      c) side effect happened")
print("   d) False or print(...)")
False or print("      d) side effect happened")
print("   a) and b) print nothing, because the right side was never")
print("   evaluated. c) and d) needed it, so the side effect occurred.")

print()
print("Q10. and / or returning values")
samples = [
    ("a)", "0 or 42", 0 or 42),
    ("b)", '"" or None', "" or None),
    ("c)", '3 and "yes"', 3 and "yes"),
    ("d)", "None or []", None or []),
    ("e)", "bool(0 or 0.0)", bool(0 or 0.0)),
]
for question, expression, value in samples:
    print(f"   {question:<4} {expression:<20} -> {value!r:<12} {type(value).__name__}")
print("   e) is False because 0 and 0.0 are both falsy, so or returns 0.0.")

print()
print("Q11. Safe defaults")
user = None
print("   user = None")
print("   user or 'guest' ->", user or "guest")
user = ""
print("   user = ''")
print("   user or 'guest' ->", user or "guest", "  <- an empty name is")
print("                      replaced too, which may not be wanted")
user = ""
fixed = user if user != "" else "guest"
print("   user if user != '' else 'guest' ->", fixed)
print("   The conditional form tests for empty explicitly rather than for")
print("   every falsy value, so 0 and [] can be kept if they are valid.")

print()
print("Q12. Identity")
x = None
print("   x = None")
print("   x is None     ->", x is None)
print("   x == None     ->", x == None, "  (but is None is the standard)")

n1 = int("256")
n2 = int("256")
print()
print("   n1 = int('256'), n2 = int('256')")
print("   n1 == n2 ->", n1 == n2)
print("   n1 is n2 ->", n1 is n2, "  (256 is the top of the int cache)")

n3 = int("300")
n4 = int("300")
print()
print("   n3 = int('300'), n4 = int('300')")
print("   n3 == n4 ->", n3 == n4)
print("   n3 is n4 ->", n3 is n4, "  (outside the cache)")
print("   d) You cannot trust it: the cache range is an implementation")
print("      detail, literals in one code block get merged, and other")
print("      versions of Python may differ. Use == for values.")

print()
print("Q13. Membership")
fruits = ["apple", "banana", "cherry"]
student = {"name": "Sara", "grade": 9}
print("   fruits  =", fruits)
print("   student =", student)
print('   a) "banana" in fruits ->', "banana" in fruits)
print('   b) "BANANA" in fruits ->', "BANANA" in fruits,
      "  (case sensitive)")
print('   c) "grape" not in fruits ->', "grape" not in fruits)
print('   d) "Sara" in student ->', "Sara" in student,
      "  (in checks keys)")
print('   e) "Sara" in student.values() ->', "Sara" in student.values())

print()
print("Q14. Membership and strings")
message = "operators are fun"
print(f'   message = "{message}"')
print('   a) "are" in message ->', "are" in message)
print('   b) "Are" in message ->', "Are" in message, "  (case sensitive)")
print('   c) "" in message ->', "" in message, "  (empty text is in everything)")
words = message.split()
print("   words =", words)
print('   d) "fun" in words ->', "fun" in words)
print('   and "fun" in message ->', "fun" in message)

print()
print("Q15. Precedence")
print("   a) 2 + 3 * 4 is 14, so brackets are needed for 20:")
print("      (2 + 3) * 4 ->", (2 + 3) * 4, "== 20 ->", (2 + 3) * 4 == 20)
print("   b) -3 ** 2 is -9 already, because ** beats unary minus:")
print("      -3 ** 2 ->", -3 ** 2, "== -9 ->", -3 ** 2 == -9)
print("      Brackets would change it: (-3) ** 2 ->", (-3) ** 2)
print("   c) not binds tighter than and, and == binds tighter than not:")
print("      not True and False ->", not True and False)
print("      grouped as (not True) and False ->", (not True) and False)
print("      Both are False, so the line already matches.")
print("   d) Comparisons run before and:")
print("      1 + 2 == 3 and 4 < 5 ->", 1 + 2 == 3 and 4 < 5)

print()
print("Q16. One value from a condition")
temperature = 12
label = "cold" if temperature < 15 else "mild"
print(f"   temperature = {temperature}")
print('   "cold" if temperature < 15 else "mild" ->', label)
temperature = 21
label = "cold" if temperature < 15 else "mild"
print(f"   temperature = {temperature} ->", label)

print()
print("Q17. Choosing an operator")
print("   a) absence      -> x not in container")
print("   b) same list    -> a is b")
print("   c) equals zero  -> n == 0")
print("   d) default None -> x or 'default' would replace every falsy value,")
print("                      so use  x if x is not None else 'default'")
print("   e) round down   -> 7 // 1 or math.floor(7.9), or int(7.9)")
print()
print("   Proofs:")
print("      7.9 // 1  ->", 7.9 // 1)
print("      int(7.9)  ->", int(7.9))
print("      3 not in [1, 2] ->", 3 not in [1, 2])
value = None
print("      value if value is not None else 'default' ->",
      value if value is not None else "default")

print()
print("Q18. Build a small report")
price = 49.5
quantity = 3
discount = 0.1
total = price * quantity
discount_amount = round(total * discount, 2)
final = round(total - discount_amount, 2)
print(f"   price = {price}, quantity = {quantity}, discount = {discount}")
print(f"   a) total before discount -> {total}")
print(f"   b) discount amount       -> {discount_amount}")
print(f"   c) final price           -> {final}")
print(f"   d) final price below 150 -> {final < 150}")
print("      Write it as a sentence so the output reads clearly:")
answer = "yes, it is below 150" if final < 150 else "no, it is 150 or more"
print("     ", answer)

print()
print("BONUS 1. Guards without conditions")
scores = []
print("   scores =", scores)
first = scores[0] if scores else "no scores"
print("   with an if   ->", first)
first = (scores and scores[0]) or "no scores"
print("   with and / or ->", first)
print("   Read it as: if scores is empty, stop and hand back scores, which")
print("   is falsy, so the or supplies 'no scores'.")
scores = [55]
print()
print("   scores =", scores)
print("   with an if   ->", scores[0] if scores else "no scores")
print("   with and / or ->", (scores and scores[0]) or "no scores")

print()
print("BONUS 2. Membership timing")
words = ["python", "operator", "precedence", "identity"]
targets = ["cat", "identity", "dog"]
print("   words  =", words)
print("   targets =", targets)
missing = [target for target in targets if target not in words]
print("   missing ->", missing)
found = [target for target in targets if target in words]
print("   found   ->", found)
print("   A single line with a comprehension keeps the order of targets.")

print()
print("=" * 60)
print("HOW TO USE THESE ANSWERS")
print("=" * 60)
print("""
1. Predict the result before running anything.
2. Write the expression yourself, not just the answer.
3. Where your prediction differed, identify the rule involved.
4. Re-run this file as often as useful, since every solution prints
   its own result.
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Arithmetic and precedence come first, then comparisons, then and or not.
- and and or return an operand rather than a bool, which is why they make
  good default value operators.
- == for content, is for None and identity, in for membership.
- Brackets beat guesswork, and explicit conversion beats hoping Python
  will convert for you.
""")