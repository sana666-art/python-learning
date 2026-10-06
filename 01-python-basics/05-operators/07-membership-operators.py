"""Topic 7: Membership Operators

in and not in ask whether a value appears inside something else. They work on
text, lists, tuples, sets and dictionaries.

Run with:  python 07-membership-operators.py
"""

print("=" * 60)
print("THE TWO OPERATORS")
print("=" * 60)
print("""
x in y      True when x is found in y
x not in y  True when x is not found in y

not in is simply the opposite of in, so you never need to write
'not (x in y)'.
""")

print("=" * 60)
print("MEMBERSHIP IN TEXT")
print("=" * 60)
print("For a string, in checks whether the left side appears as a substring.")

language = "Python"
print('language = "Python"')
print()
print('"Py" in language     ->', "Py" in language)
print('"py" in language     ->', "py" in language, "  (case sensitive)")
print('"thon" in language   ->', "thon" in language)
print('"Java" in language   ->', "Java" in language)
print('"P" not in language  ->', "P" not in language)
print('"" in language       ->', "" in language, "  (the empty text is in everything)")
print('"" not in language   ->', "" not in language)

print()
print("Single characters are matched by their Unicode code point, so in on a")
print("character is the same as comparing with ==")
print('"t" in "Python" ->', "t" in "Python")
print('"t" == "t"      ->', "t" == "t")

print()
print("=" * 60)
print("MEMBERSHIP IN A LIST")
print("=" * 60)
print("For a list, in checks whether the value is one of the items.")

fruits = ["apple", "banana", "cherry", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, None, True]

print("fruits =", fruits)
print('"banana" in fruits    ->', "banana" in fruits)
print('"grape" in fruits     ->', "grape" in fruits)
print('"grape" not in fruits ->', "grape" not in fruits)
print()
print("numbers =", numbers)
print("3 in numbers   ->", 3 in numbers)
print("9 in numbers   ->", 9 in numbers)
print()
print("mixed =", mixed)
print("1 in mixed     ->", 1 in mixed)
print('None in mixed  ->', None in mixed)
print('"one" in mixed ->', "one" in mixed)

print()
print("in on a list compares each item with ==, one at a time, until it")
print("finds a match or reaches the end.")

print()
print("=" * 60)
print("MEMBERSHIP IN A TUPLE, SET AND DICTIONARY")
print("=" * 60)

coordinates = (3, 7)
print("coordinates = (3, 7)")
print("3 in coordinates   ->", 3 in coordinates)
print("(3, 7) in coordinates ->", (3, 7) in coordinates, "  (the whole tuple)")
print("8 in coordinates   ->", 8 in coordinates)
print()

unique_numbers = {1, 2, 3}
print("unique_numbers = {1, 2, 3}")
print("2 in unique_numbers ->", 2 in unique_numbers)
print("5 in unique_numbers ->", 5 in unique_numbers)
print("5 not in unique_numbers ->", 5 not in unique_numbers)
print()

student = {"name": "Ali", "age": 20}
print("student =", student)
print('"name" in student  ->', "name" in student, "  (keys, not values)")
print('"Ali" in student   ->', "Ali" in student, "  (values are not searched)")
print('"age" in student   ->', "age" in student)

print()
print("This is a common trap. in on a dictionary checks the keys only.")
print("To search the values, check the list of values yourself:")
print('"Ali" in student.values() ->', "Ali" in student.values())
print('"Ali" in student.keys()   ->', "Ali" in student.keys())

print()
print("=" * 60)
print("WHICH OPERATOR IS FASTER?")
print("=" * 60)
print("The type of the container decides the cost, not the operator.")

print("""
list, tuple   in scans every item in turn, so it slows down as the list
              grows.  Cost grows with the number of items.
set, dict     in uses a hash lookup, so it finds or rules out a match in
              about one step.  Cost barely changes with size.
string        in scans the text, similar to a list.
""")

small_list = list(range(0, 2000))
small_set = set(range(0, 2000))

print("Both hold the same 2000 numbers, but lookups differ:")
print("999 in small_list ->", 999 in small_list, "  (scanned up to 999 items)")
print("999 in small_set  ->", 999 in small_set, "  (hashed, found immediately)")
print()
print("For repeated lookups, convert a list to a set once:")
print("   lookup = set(my_list)")
print("   if value in lookup: ...")

print()
print("=" * 60)
print("in IN CONDITIONS AND LOOPS")
print("=" * 60)

allowed_roles = ["admin", "editor", "viewer"]
current_role = "editor"
print("allowed_roles =", allowed_roles)
print("current_role  =", current_role)
print()
print("if current_role in allowed_roles:  ->",
      "allowed" if current_role in allowed_roles else "denied")

current_role = "guest"
print("after current_role = 'guest'      ->",
      "allowed" if current_role in allowed_roles else "denied")

print()
print("Membership also reads well in a guard clause:")

values = []
if not values:
    print("values is empty, so the work is skipped")

print()
print("And in filtering:")
marks = [88, 45, 92, 33, 67, 40]
wanted = [45, 67, 92]
kept = [mark for mark in marks if mark in wanted]
print("marks =", marks)
print("wanted =", wanted)
print("kept  =", kept)

print()
print("=" * 60)
print("in WITH A RANGE")
print("=" * 60)
print("ranges support membership, which makes range checks neat.")

age = 25
print("age =", age)
print("age in range(0, 121)      ->", age in range(0, 121))
print("age in range(65, 121)     ->", age in range(65, 121))
print("age not in range(18, 65)  ->", age not in range(18, 65))
print()
print("It reads like English: age in range(18, 65) means between 18 and 64.")

print()
print("=" * 60)
print("CHAINED MEMBERSHIP")
print("=" * 60)
print("Because in returns a bool, it can be combined with and and or.")

colour = "blue"
print('colour = "blue"')
print('colour in ["red", "blue"] or colour in ["cyan", "navy"] ->',
      colour in ["red", "blue"] or colour in ["cyan", "navy"])
print()
print("A shorter form uses a single tuple:")
print('colour in ("red", "blue", "cyan", "navy") ->',
      colour in ("red", "blue", "cyan", "navy"))
print("Build one container once rather than writing several tests.")

print()
print("=" * 60)
print("EMPTY VALUES AND MEMBERSHIP")
print("=" * 60)
print("Testing the empty case is where beginners lose time.")

print('"" in "Python"    ->', "" in "Python")
print('[] in [[]]        ->', [] in [[]], "  (the empty list is an item)")
print("[] in []          ->", [] in [])
print("None in [None]    ->", None in [None])
print()
print("To ask whether a container has any items at all, test it directly:")
print("bool([])          ->", bool([]))
print("bool('')          ->", bool(""))
print("if not container: ->", "the container is empty")

print()
print("=" * 60)
print("in AND is: NOT THE SAME TEST")
print("=" * 60)
print("in uses equality, is uses identity.")

a = [1, 2]
b = [1, 2]
c = a
print("a = [1, 2], b = [1, 2], c = a")
print()
print("b in [a]     ->", b in [a], "  (equal in content, so found)")
print("c in [a]     ->", c in [a], "  (also found, sharing helps nothing)")
print("a is b        ->", a is b, "  (different objects)")
print("a is c        ->", a is c, "  (same object)")
print()
print("in answers a content question. is answers an identity question.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Checking a dictionary value when you meant a key. 'Ali' in student is
   False even though Ali is the name, because in looks at keys.
2. Expecting in on a list to be fast. It scans, so convert to a set for
   repeated lookups.
3. Forgetting that in is case sensitive for text.
4. Writing 'not (x in y)' instead of the cleaner 'x not in y'.
5. Assuming in checks identity. It uses equality.
6. Searching for an empty string or list and getting True unexpectedly,
   because every container contains the empty version of itself.
7. Using in on a value and then expecting the index to come with it. Use
   .index() or a loop when you need the position.
""")

print("Quick proofs:")
print('   "py" in "Python"  ->', "py" in "Python", "  (case)")
print('   "Ali" in {"name": "Ali"} ->', "Ali" in {"name": "Ali"}, "  (key only)")
print("   [] in []          ->", [] in [])
print("   999 in list(range(1000)) ->", 999 in list(range(1000)))

print()
print("Getting the position when you need it:")
fruits = ["apple", "banana", "cherry"]
target = "banana"
if target in fruits:
    print(f"   {target} found at index", fruits.index(target))
else:
    print(f"   {target} not present")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- in and not in test whether a value appears in a container.
- Text checks substrings, lists and tuples check items, sets check members,
  and dictionaries check keys only.
- Lookup cost depends on the container: sets and dicts are near constant
  time, lists and tuples are scanned.
- in uses equality, so it is not the same as is.
- Use in for guards, filtering and range checks.
""")