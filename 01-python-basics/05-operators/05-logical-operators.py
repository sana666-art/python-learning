"""Topic 5: Logical Operators

and, or and not combine conditions. They also have a side effect worth
knowing: they decide how many operands Python evaluates at all.

Run with:  python 05-logical-operators.py
"""

print("=" * 60)
print("THE THREE LOGICAL OPERATORS")
print("=" * 60)
print("""
Operator  Reads as    Needs
--------  ----------  ---------------------------------
and       both        True on the left AND True on the right
or        either      True on the left OR True on the right
not       opposite    Flips the value it is given
""")

print("=" * 60)
print("and: BOTH SIDES MUST BE TRUE")
print("=" * 60)

print("True and True   ->", True and True)
print("True and False  ->", True and False)
print("False and True  ->", False and True)
print("False and False ->", False and False)
print()
print("In words: both conditions must hold before the whole thing is True.")

age = 20
has_id = True
print()
print("age >= 18 and has_id ->", age >= 18 and has_id)
has_id = False
print("age >= 18 and has_id ->", age >= 18 and has_id, "  (one False is enough)")

print()
print("=" * 60)
print("or: ONE SIDE IS ENOUGH")
print("=" * 60)

print("True or True   ->", True or True)
print("True or False  ->", True or False)
print("False or True  ->", False or True)
print("False or False ->", False or False)

print()
day = "Sunday"
print('day == "Saturday" or day == "Sunday" ->', day == "Saturday" or day == "Sunday")
print('day == "Monday"  or day == "Sunday" ->', day == "Monday" or day == "Sunday")

print()
print("=" * 60)
print("not: FLIPS THE VALUE")
print("=" * 60)

print("not True   ->", not True)
print("not False  ->", not False)
print()
print("is_active = True   -> not is_active =", not True)
print("not not True       ->", not not True, "  (two flips, back to True)")

print()
print("not is clearest when asking for the opposite of a plain value:")
has_access = False
print("has_access   ->", has_access)
print("not has_access ->", not has_access)

print()
print("=" * 60)
print("OPERATORS ON NON-BOOLEAN VALUES")
print("=" * 60)
print("and and or do not always return True or False. They return one of the")
print("two operands, which is where the real power and the real confusion lie.")

print("Rule for and:")
print("  If the left value is falsy, return it immediately.")
print("  Otherwise return the right value.")
print()
print("Rule for or:")
print("  If the left value is truthy, return it immediately.")
print("  Otherwise return the right value.")

print()
print(f"{'expression':<26}{'result':<14}{'type'}")
print("-" * 52)
samples = [
    ("0 and 5", 0 and 5),
    ("5 and 0", 5 and 0),
    ('"" and "x"', "" and "x"),
    ('"x" and "y"', "x" and "y"),
    ("1 or 99", 1 or 99),
    ("0 or 99", 0 or 99),
    ('"" or "fallback"', "" or "fallback"),
    ("None or [1, 2]", None or [1, 2]),
    ("[1, 2] or None", [1, 2] or None),
]
for expression, value in samples:
    print(f"{expression:<26}{str(value):<14}{type(value).__name__}")

print()
print("Read '0 and 5' as: the left side is falsy, so stop and return 0.")
print("Read '1 or 99' as: the left side is truthy, so stop and return 1.")

print()
print("=" * 60)
print("THE PATTERN THAT MAKES THIS USEFUL")
print("=" * 60)
print("or with a default value is the standard way to supply a fallback.")

name = ""
label = name or "anonymous"
print('name = ""                ->', repr(name))
print('name or "anonymous"      ->', label)

name = "Ali"
label = name or "anonymous"
print('name = "Ali"             ->', repr(name))
print('name or "anonymous"      ->', label)

print()
print("The same idea for missing data:")
settings = {}
theme = settings.get("theme") or "light"
print("settings.get('theme') ->", settings.get("theme"))
print("theme = settings.get('theme') or 'light' ->", theme)

print()
print("A common guard before doing work:")
items = []
first = items[0] if items else "no items"
print("items =", items)
print("first = items[0] if items else 'no items' ->", first)
print()
print("Shorter with or, which avoids repeating the name:")
items = []
first = (items and items[0]) or "no items"
print("(items and items[0]) or 'no items' ->", first)
print("Read it as: if items is empty, stop and return it, then or supplies")
print("the fallback. These shorthand forms work but read poorly at length,")
print("so an explicit if is often better.")

print()
print("=" * 60)
print("SHORT-CIRCUIT EVALUATION")
print("=" * 60)
print("Python stops as soon as the answer is certain. That means the right")
print("side is sometimes never evaluated, which can prevent errors entirely.")


def check(value, label):
    """Print when evaluated, so short circuiting becomes visible."""
    print("   evaluated:", label, "=", value)
    return value


print("False and check(10, 'right side'):")
print("   result ->", False and check(10, "right side"))
print("   the right side was never touched, because False and anything is")
print("   already False.")

print()
print("True or check(10, 'right side'):")
print("   result ->", True or check(10, "right side"))
print("   again the right side was skipped, because True or anything is True.")

print()
print("True and check(10, 'right side'):")
print("   result ->", True and check(10, "right side"))
print("   needed here, so it ran.")

print()
print("False or check(10, 'right side'):")
print("   result ->", False or check(10, "right side"))
print("   also needed here, so it ran.")

print()
print("=" * 60)
print("SHORT CIRCUITING PREVENTS ERRORS")
print("=" * 60)
print("This is the main reason short circuiting matters in real code.")

values = []
print("values =", values)
print()

result = values and values[0]
print("values and values[0] ->", result, "  (no IndexError, because of 'and')")
print("An empty list is falsy, so 'and' stopped before touching [0].")

print()
safe = None
print("safe = None")
print("safe and safe.upper() ->", safe and safe.upper(), "  (no AttributeError)")

print()
print("Writing it long form would need a guard:")
if values:
    print("   first item would be:", values[0])
else:
    print("   the list is empty, so there is no first item")

print()
print("=" * 60)
print("SHORT CIRCUIT AND FUNCTION CALLS")
print("=" * 60)
print("A function on the skipped side never runs, so its side effects vanish")
print("with it. That is useful when the call would otherwise raise.")


def load_config():
    """Simulate loading a file that only exists sometimes."""
    print("   load_config() ran")
    return None


print("config = load_config()")
print()
print("config and config.get('debug'):")
config = load_config() and {"debug": True}
print("   ->", config, " (get() was never called on None, so no crash)")

print()
print("The explicit version reads better when it matters:")
config = load_config()
value = config.get("debug") if config else None
print("   with an if guard ->", value)

print()
print("=" * 60)
print("COMBINING THE THREE OPERATORS")
print("=" * 60)

age = 25
has_ticket = True
is_banned = False

print("age =", age, "| has_ticket =", has_ticket, "| is_banned =", is_banned)
print()
print("age >= 18 and has_ticket           ->", age >= 18 and has_ticket)
print("is_banned or age >= 18             ->", is_banned or age >= 18)
print("not is_banned                      ->", not is_banned)
print("age >= 18 and has_ticket and not is_banned ->",
      age >= 18 and has_ticket and not is_banned)
print()
print("Mixing and with or needs care. Read it as:")
print("  not binds tightest, then and, then or.")
print("So  a or b and c  means  a or (b and c),  not  (a or b) and c.")

a, b, c = True, False, False
print()
print("a or b and c  ->", a or b and c, "  (= a or (b and c))")
print("(a or b) and c ->", (a or b) and c, "  (a different question)")
print("Use brackets to state the intent, even when the rules give the answer.")

print()
print("=" * 60)
print("READABILITY: PREFER A CLEAR CONDITION")
print("=" * 60)
print("Long chains of and and or become unreadable. Named variables help.")

is_allowed = age >= 18 and has_ticket and not is_banned
print("is_allowed = age >= 18 and has_ticket and not is_banned")
print("is_allowed ->", is_allowed)
print()
print("Now the condition can be read once and reused many times.")
print("When a rule grows beyond three terms, consider an if statement with")
print("comments explaining each part.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Expecting and and or to always return True or False. They return one of
   their operands, which may be text, a number or None.
2. Forgetting that not binds tighter than and, which binds tighter than or.
3. Using Python's word 'and' where another language uses && or 'and'
   where it uses ||.
4. Assuming the right side always runs. Short circuiting skips it, so side
   effects disappear with it.
5. Writing a long chain where an if statement would be clearer.
6. Relying on 'or' for a default when the value could legitimately be 0 or
   an empty string, because those are falsy and would be replaced.
""")

print("Quick proofs:")
print("   0 and 5      ->", 0 and 5, " (returns the operand, not False)")
print("   0 or 5       ->", 0 or 5)
print("   not 0        ->", not 0, "  (0 is falsy, so not 0 is True)")
print("   True or 0    ->", True or 0, "  (returns True, not 1)")
print("   False and 1  ->", False and 1, "  (returns False, not 0)")
print()
print("The default trap:")
zero = 0
print("   zero or 'default' ->", zero or "default", "  <- 0 was replaced!")
print("   Safer: zero if zero is not None else 'default' ->",
      zero if zero is not None else "default")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- and needs both truthy, or needs one, not flips.
- and and or return an operand, not necessarily a bool.
- Short circuit evaluation means the right side may never run, which
  prevents errors such as indexing an empty list.
- Precedence: not, then and, then or. Brackets make the intent obvious.
- or supplies defaults, but beware of falsy values like 0 and ''.
""")