"""Topic 6: Identity Operators

is and is not ask whether two names refer to the same object in memory. That
is a different question from ==, which asks whether two values are equal.

Run with:  python 06-identity-operators.py
"""

print("=" * 60)
print("TWO DIFFERENT QUESTIONS")
print("=" * 60)
print("""
==  equality     Do these two values have the same content?
is  identity     Are these two names pointing at the same object?

Equality compares what a value is. Identity compares where it lives.
""")

print("=" * 60)
print("THE OPERATORS")
print("=" * 60)

print("a is b      True when a and b reference the same object")
print("a is not b  True when a and b reference different objects")

a = [1, 2, 3]
b = a
print()
print("a = [1, 2, 3]")
print("b = a")
print("a is b     ->", a is b, "  (same list, so same object)")
print("a == b     ->", a == b, "  (also equal in content)")

c = [1, 2, 3]
print()
print("c = [1, 2, 3]  built separately")
print("a is c     ->", a is c, "  (different objects)")
print("a == c     ->", a == c, "  (but equal in content)")

print()
print("That is the whole distinction: equal does not mean identical.")

print()
print("=" * 60)
print("HOW id() SHOWS IDENTITY")
print("=" * 60)
print("id() returns the memory address of an object, which stands in for its")
print("identity. Two values with the same id are the same object.")

a = [1, 2]
b = a
c = [1, 2]
print("a = [1, 2], b = a, c = [1, 2]")
print()
print("id(a) =", id(a))
print("id(b) =", id(b), "  <- same as a")
print("id(c) =", id(c), "  <- different from a")
print()
print("a is b ->", a is b)
print("a is c ->", a is c)
print("a == c ->", a == c)

print()
print("Do not store id() values and compare them later. They are only")
print("meaningful while both objects are alive, and ids can be reused.")

print()
print("=" * 60)
print("NONE IS THE CASE THAT MATTERS MOST")
print("=" * 60)
print("None is a singleton: Python keeps exactly one None object, so identity")
print("is the correct and fastest check.")

value = None
print("value = None")
print("value is None     ->", value is None)
print("value == None     ->", value == None, "  (works, but less precise)")
print("value is not None ->", value is not None)
print()
print("The Python community standard is 'is None'. Use it consistently.")

print()
print("Why is rather than ==")
print("  - None has only one instance, so identity says exactly what you mean.")
print("  - == can be redefined by a class, which a custom object could get")
print("    wrong. is never changes behaviour.")
print("  - is is a little faster, because it compares addresses directly.")

print()
print("None appears as a placeholder, so checking it is routine:")


def find_item(items, target):
    """Return the position of target, or None when it is missing."""
    for position, item in enumerate(items):
        if item == target:
            return position
    return None


fruits = ["apple", "banana", "mango"]
result = find_item(fruits, "banana")
print("searching for 'banana' ->", result)
result = find_item(fruits, "grape")
print("searching for 'grape'  ->", result)
print("'result is None' ->", result is None)

print()
print("=" * 60)
print("SMALL INTEGERS ARE CACHED")
print("=" * 60)
print("Python keeps one shared copy of the integers from -5 to 256, so is can")
print("return True for numbers you built separately. This is an implementation")
print("detail of CPython, not a language rule, so never rely on it.")

a = 256
b = 256
print("a = 256, b = 256")
print("a is b ->", a is b, "  (inside the cache, so the same object)")

print()
print("Building the same value at runtime shows the boundary clearly. The")
print("literals below would be merged by the compiler, so int() is used to")
print("create them while the program runs:")
print()
print(f"{'value':<10}{'runtime is'}")
print("-" * 30)
for number in [-6, -5, 0, 256, 257, 1000]:
    first = int(str(number))
    second = int(str(number))
    print(f"{number:<10}{first is second}")

print()
print("-5 and 256 are True because they sit inside the cache. Every value")
print("outside that range gives False, while == stays True for all of them:")
print()
print("int('257') == int('257') ->", int(str(257)) == int(str(257)))
print("int('257') is int('257') ->", int(str(257)) is int(str(257)))

print()
print("=" * 60)
print("THE COMPILER HIDES THIS FROM YOU")
print("=" * 60)
print("Two identical literals written in the same code block are stored")
print("once, so is reports True even for values far outside the cache. This")
print("is why a naive test seems to disprove the rule.")


def two_literals():
    first = 99999
    second = 99999
    return first is second


def two_calculations():
    first = sum([50000, 49999])
    second = sum([49999, 50000])
    return first is second


print("first = 99999, second = 99999  written as literals ->", two_literals())
print("both sides built while the program runs            ->",
      two_calculations())
print()
print("Same value, same ==, different identity. The literal pair was")
print("coalesced into a single object at compile time, while the summed")
print("values were created fresh at run time. Even constant sums such as")
print("50000 + 49999 are folded by the compiler, so the whole line is")
print("evaluated before either name exists.")

print()
print("=" * 60)
print("TEXT IS INTERNED")
print("=" * 60)
print("Short text is often stored once and shared, which gives the same")
print("confusing result.")

a = "hello"
b = "hello"
print('a = "hello", b = "hello"')
print("a is b ->", a is b, "  (one literal, one object)")

a = "hello"
b = "".join(["he", "llo"])
print()
print('a = "hello"                 (a literal)')
print('b = "".join(["he", "llo"])  (built while running)')
print("a is b ->", a is b, "  (built separately, so a different object)")
print("a == b ->", a == b, "  (identical content, which is what matters)")

print()
print("Python interns text that looks like a name, which is why 'python-' +")
print("'operators' can still come out identical to the literal. That is")
print("another implementation detail, and the same warning applies.")

print()
print("The lesson: never write a program that depends on is with numbers or")
print("text. Use == for value, and reserve is for None and for checking")
print("which object a name points at.")
print()
print("=" * 60)
print("is ON TRUE AND FALSE")
print("=" * 60)
print("True and False are also singletons, so identity works, but ==")
print("usually expresses the intent better because truthiness may be what")
print("you actually care about.")

flag = True
print("flag = True")
print("flag is True   ->", flag is True)
print("flag == True   ->", flag == True)
print("bool(flag)     ->", bool(flag))
print()
print("A value that is merely truthy behaves the same in a condition but")
print("fails an identity test:")
value = 1
print("value = 1")
print("value is True  ->", value is True, "  (not the True object)")
print("value == True  ->", value == True, "  (True behaves as 1)")
print("bool(value)    ->", bool(value))
print()
print("Write 'if flag:' rather than 'if flag is True:', because it also")
print("accepts other truthy values.")

print()
print("=" * 60)
print("MUTABLE VALUES AND SHARING")
print("=" * 60)
print("Identity is where shared mutable data becomes visible.")

original = [1, 2]
alias = original
copy = original.copy()

print("original = [1, 2]")
print("alias    = original")
print("copy     = original.copy()")
print()
print("original is alias ->", original is alias, "  (one list, two names)")
print("original is copy  ->", original is copy, "  (two separate lists)")
print()
print("Changing one affects only the shared object:")
alias.append(3)
print("alias.append(3)")
print("original =", original, "  <- changed, because it is the same list")
print("copy     =", copy, "  <- untouched")

print()
print("This is the concrete reason to ask 'is' about lists. Knowing whether")
print("two names share an object tells you what a mutation will do.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Using == when you mean is, or is when you mean ==.
2. Writing x == None instead of x is None.
3. Comparing numbers with is and expecting it to match ==. The cache makes
   it work for small ints and then fail for large ones.
4. Assuming is is a faster way to check equality of content. It is not
   checking content at all.
5. Storing id() results for later comparison.
6. Writing 'if value is True' where 'if value' is the better test.
""")

print("Quick proofs:")
print("   int('256') is int('256') ->", int(str(256)) is int(str(256)),
      "  <- cached")
print("   int('257') is int('257') ->", int(str(257)) is int(str(257)),
      "  <- outside the cache")
print("   int('257') == int('257') ->", int(str(257)) == int(str(257)),
      "  <- always True")
print()
print("   value = None; value is None ->", None is None)
value = 1
print("   1 is True  ->", value is True, "  (identity, so False)")

print()
print("=" * 60)
print("A DECISION GUIDE")
print("=" * 60)
print("""
Use is None / is not None    when testing for the absence of a value
Use ==                       when comparing numbers, text or other content
Use is                       when asking whether two names share an object
Use == on collections        when comparing lists, tuples, sets or dicts
Never use is with            plain numbers or literals you did not build
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- == asks about content, is asks about the object itself.
- id() exposes identity, but is and is not are how you test for it.
- None is a singleton, so 'is None' is the correct check.
- Small ints and some text are cached, which makes is unreliable for values.
- Identity matters for mutable data, because shared objects change together.
- Reserve is for None and for questions about sharing, not for equality.
""")