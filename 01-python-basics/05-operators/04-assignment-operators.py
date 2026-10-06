"""Topic 4: Assignment Operators

Assignment stores a value in a name. This file goes beyond the basics covered
in 02-variables: how the augmented forms really work, what happens with
mutable values, and the walrus operator.

Run with:  python 04-assignment-operators.py
"""

print("=" * 60)
print("THE FULL SET")
print("=" * 60)
print("""
Operator   Equivalent to      Reads as
--------   ---------------    ----------------------
=          value              assign
+=         a = a + b          add then assign
-=         a = a - b          subtract then assign
*=         a = a * b          multiply then assign
/=         a = a / b          divide then assign
//=        a = a // b         floor divide then assign
%=         a = a % b          modulus then assign
**=        a = a ** b         power then assign
&= |= ^=   a = a & b          bitwise, advanced
<<= >>=    a = a << b         bit shifts, advanced
:=         (expression)       walrus, assign inside an expression
""")

print("=" * 60)
print("PLAIN ASSIGNMENT: BINDING A NAME")
print("=" * 60)
print("Plain = does not calculate anything. It takes the value on the right")
print("and makes the name on the left refer to it.")

value = 10
print("value = 10  ->", value)
value = value + 5
print("value = value + 5  ->", value, "  (the old value is replaced)")
value = "now text"
print('value = "now text" ->', value, "  (the type changed too)")

print()
print("Right side first, then left. Python always evaluates the whole right")
print("before touching any name on the left.")

a = 1
b = 2
a, b = b, a
print("a, b = b, a  swaps -> a =", a, "| b =", b)

print()
print("=" * 60)
print("AUGMENTED ASSIGNMENT: THE SHORTHAND")
print("=" * 60)
print("a += b means a = a + b, but it is not always identical. The next two")
print("sections explain the difference.")

count = 10
print("count   =", count)
count += 5
print("+= 5    =", count)
count -= 3
print("-= 3    =", count)
count *= 2
print("*= 2    =", count)
count /= 4
print("/= 4    =", count, "  (note it became a float)")
count //= 1
print("//= 1   =", count, "  type:", type(count).__name__)
count %= 7
print("%= 7    =", count)
count **= 2
print("**= 2   =", count)

print()
print("Watch the type change with /=:")
value = 10
print("value    =", value, " type:", type(value).__name__)
value /= 2
print("value /= 2 ->", value, " type:", type(value).__name__)
print("True division always produces a float, even from two ints.")
print("Use //= when you want to stay on whole numbers.")

print()
print("=" * 60)
print("AUGMENTED ON TEXT: IT EXTENDS, IT DOES NOT ADD")
print("=" * 60)
print("+ on text concatenates, so += on text appends the piece.")

text = "Hello"
print('text    =', text)
text += " World"
print('+= " World" ->', text)
text *= 3
print("*= 3        ->", text, "  (repetition)")

print()
print("=" * 60)
print("THE KEY DIFFERENCE: REBINDING VS CHANGING IN PLACE")
print("=" * 60)
print("""
For immutable types such as int and str, += creates a new object and points
the name at it.

For mutable types such as list, += changes the object itself, so any other
name sharing that list sees the change.
""")

print("Immutable, so nothing else is affected:")

number_a = 10
number_b = number_a
number_b += 5
print("number_a =", number_a, "  (unchanged)")
print("number_b =", number_b)

print()
print("Mutable, so the shared list changes too:")

list_a = [1, 2]
list_b = list_a
list_b += [3]
print("list_a =", list_a, "  (changed!)")
print("list_b =", list_b)

print()
print("Compare that with =, which always rebinds:")
list_a = [1, 2]
list_b = list_a
list_b = list_b + [3]
print("list_a =", list_a, "  (unchanged this time)")
print("list_b =", list_b)

print()
print("So:")
print("  += on a list  mutates the object, both names see it")
print("  =  on a list  points the name somewhere new, only one name moves")
print("This is a common source of bugs when passing lists between functions.")

print()
print("=" * 60)
print("AUGMENTED ASSIGNMENT EVALUATES THE TARGET ONCE")
print("=" * 60)
print("The long form looks up the name twice. The short form looks it up once.")
print("That matters when getting the value has a side effect.")

calls = {"count": 0}


def get_value():
    """Print when called so the difference is visible."""
    calls["count"] += 1
    print("   get_value() called, now", calls["count"], "times")
    return 5


print("Long form a = get_value() + 1:")
value = get_value() + 1
print("   result:", value)

print()
print("Short form a += 1 needs the current value too, but a += on a name")
print("already holds it, so no extra call happens for a plain variable.")

value = 10
value += 1
print("value += 1 on a plain name ->", value)

print()
print("The real difference shows on an object with a method:")

index = {"items": [1, 2]}
index["items"] += [3]
print('index["items"] += [3] ->', index["items"])
print("The subscript was evaluated once, then the list was extended.")

print()
print("=" * 60)
print("CHAINED ASSIGNMENT")
print("=" * 60)
print("One value can be given to several names in a single statement.")

a = b = c = 0
print("a = b = c = 0  ->", a, b, c)
b = 99
print("then b = 99    -> a =", a, "| b =", b, "| c =", c)
print("a and c kept 0, because each name is bound separately after the value")
print("is computed once.")

print()
print("Different values at once, matched by position:")
x, y, z = 1, 2, 3
print("x, y, z = 1, 2, 3 ->", x, y, z)

x, y = y, x
print("x, y = y, x  swaps -> x =", x, "| y =", y)

print()
print("=" * 60)
print("MULTIPLE ASSIGNMENT IS NOT A COMPARISON")
print("=" * 60)
print("a, b = b, a looks like an equation but is really two stores at once.")

a, b = 10, 20
print("before:", a, b)
a, b = b, a
print("after :", a, b)
print("Python builds the tuple (b, a) first, then unpacks it into a and b.")

print()
print("=" * 60)
print("THE WALRUS OPERATOR :=")
print("=" * 60)
print("""
:= assigns as part of an expression, so you can compute a value once, store
it and use it in the same line. It was added in Python 3.8.
""")

data = [1, 2, 3, 4, 5]
print("data =", data)
if (length := len(data)) > 3:
    print("   length =", length, "is greater than 3")
print("len(data) ran once, and length kept the result for the print above.")

print()
print("The loop pattern that most often uses it:")

values = [4, 8, 15, 16, 23, 42]
print("values =", values)
while values:
    value = values.pop()
    if value > 10:
        print("   popped", value, "which is over 10, remaining", values)
print("A plain = inside the loop body is clearer here. := earns its place")
print("when the value is needed inside the condition itself, as below:")

print()
data = "python-operators"
print('data = "python-operators"')
if (position := data.find("-")) != -1:
    print("   first dash at index", position)
    print("   everything before it:", data[:position])
    print("   everything after it :", data[position + 1:])
print("find() ran once, and position was reused in both print lines above.")

print()
print("A cleaner example with strings:")

words = ["", "python", "", "operators"]
for word in words:
    if (cleaned := word.strip()):
        print(f"   found a non-empty word: {cleaned!r}")
    else:
        print("   skipped an empty word")
print("strip() ran once, and cleaned was reused inside the print.")

print()
print("When NOT to use it:")
print("  - Simple one-off values: plain = reads better.")
print("  - Deep inside a complex condition: it hides the test.")
print("  - When the name adds nothing: 'if (n := len(x)) > 0' is noise when")
print("    'if len(x) > 0' says the same thing.")

print()
print("=" * 60)
print("ASSIGNMENT IS A STATEMENT, NOT AN EXPRESSION")
print("=" * 60)
print("Plain = cannot appear inside another expression. That is why := exists.")

try:
    compile("value = (x = 5)", "<string>", "exec")
except SyntaxError as error:
    print("   value = (x = 5)  ->", type(error).__name__, ":", error.msg)

print()
print("The walrus form is legal because := is an expression:")
value = (x := 5)
print("   value = (x := 5) -> value =", value, "| x =", x)

print()
print("=" * 60)
print("AUGMENTED ASSIGNMENT ON THE WRONG TYPE")
print("=" * 60)
print("The same rules as the plain operator apply, so bad pairs still fail.")

for label, run in [
    ("number += 'text'", lambda: (lambda n: n + "text")(5)),
    ("number -= 1.5", lambda: (lambda n: n - 1.5)("10")),
    ("number /= 0", lambda: (lambda n: n / 0)(5)),
]:
    try:
        print(f"   {label:<20} -> {run()!r}")
    except (TypeError, ValueError, ZeroDivisionError) as error:
        print(f"   {label:<20} -> {type(error).__name__}: {error}")

print()
print("Not every odd looking pair is an error, though. Some operators accept")
print("more than one type, which is why knowing the type matters:")
print("   3 * 'ab' ->", 3 * "ab", "  (int times text repeats it, and that is legal)")
print("   'ab' * 3 ->", "ab" * 3, "  (the same thing, written the other way round)")

print()
print("Mixing types in an augmented form fails just as it does without it:")

try:
    number = 10
    number += "5"
except TypeError as error:
    print("   number += '5' ->", type(error).__name__, ":", error)

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Forgetting that /= returns a float, so a whole number silently becomes
   a decimal. Use //= when the type must stay int.
2. Using = inside a condition. Comparison needs ==.
3. Using += on a shared list when you meant a separate copy. Use
   list_b = list_a.copy() first.
4. Chaining a = b = c = 0 and then mutating a mutable value, which makes
   all three names share one object.
5. Expecting plain = to work inside an expression. Use := only when the
   name is genuinely needed.
6. Assuming a, b = b, a needs a temporary variable. It does not.
""")

print("Quick proofs:")
value = 7
value /= 2
print("   7 /= 2     ->", value, type(value).__name__)
list_a = [1]
list_b = list_a
list_b += [2]
print("   shared +=  ->", list_a, "(list_a changed)")
try:
    compile("if (v = 5): pass", "<string>", "exec")
except SyntaxError as error:
    print("   if (v = 5) ->", type(error).__name__)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- = binds a name; the augmented forms compute then store in one step.
- /= always returns a float; //= keeps whole numbers.
- += mutates a list in place but creates a new object for ints and strings.
- Chained assignment computes the value once and binds each name separately.
- The walrus := assigns inside an expression, for when a name is needed
  while testing.
- Plain = is a statement, so it can never be used inside an expression.
""")