"""Topic 9: Mutable vs Immutable

A mutable value can be changed after it is created. An immutable value cannot,
so any change produces a new object.

Run with:  python 09-mutable-vs-immutable.py
"""

print("=" * 60)
print("WHAT IS MUTABILITY?")
print("=" * 60)
print("""
Mutable   you can change the value in place, for example with a method or
          by assigning to an index.
Immutable any change creates a new object and leaves the original alone.

In this folder:
    int, float, str, bool, None  immutable
    list, dict, set               mutable

tuple is immutable too, but it gets its own section later.
""")

print("=" * 60)
print("IMMUTABLE TYPES: CHANGE MAKES A NEW OBJECT")
print("=" * 60)

number = 10
print("number =", number)
number += 5
print("number = 10, then number += 5  ->", number)
print("The original 10 is still there. A new object was created.")

print()
text = "hello"
print('text =', text)
text = text.upper()
print('text = text.upper()             ->', text)
print('The original "hello" is untouched. upper() returned a new string.')

print()
print("Proof that strings are immutable:")
word = "cat"
try:
    word[0] = "b"
except TypeError as error:
    print('word[0] = "b" ->', type(error).__name__, ":", error)
print("Rebuilding the string is the only way:")
word = "b" + word[1:]
print("new word =", word)

print()
print("Proof that integers are immutable:")
value = 10
print("value   =", value, " id:", id(value))
value = value + 1
print("value+1 =", value, " id:", id(value))
print("Different ids, so these are two different objects.")

print()
print("=" * 60)
print("MUTABLE TYPES: CHANGE HAPPENS IN PLACE")
print("=" * 60)
print("Lists, dicts and sets can be changed without creating a new object.")

fruits = ["apple", "banana"]
original_id = id(fruits)
fruits.append("mango")
print("fruits =", fruits)
print("id before =", original_id)
print("id after  =", id(fruits))
print("The same object was modified, so the id is unchanged.")

print()
print("Other ways to change a list in place:")

numbers = [3, 1, 2]
print("start        :", numbers)
numbers.append(4)
print("append(4)    :", numbers)
numbers.insert(0, 0)
print("insert(0, 0) :", numbers)
numbers.remove(1)
print("remove(1)    :", numbers)
numbers.sort()
print("sort()       :", numbers)
numbers.reverse()
print("reverse()    :", numbers)
numbers[0] = 99
print("numbers[0]=99:", numbers)

print()
print("A dict can also be changed in place:")

student = {"name": "Ali"}
student["age"] = 20
print("after adding a key :", student)
student["age"] = 21
print("after changing     :", student)
del student["age"]
print("after deleting     :", student)

print()
print("=" * 60)
print("THE BIG DIFFERENCE: SHARED REFERENCES")
print("=" * 60)
print("""
Immutable values are safe to share, because nobody can change them.
Mutable values can surprise you, because two names can point at one list.
""")

print("Mutable, so both names see the change:")

list_a = [1, 2]
list_b = list_a
list_b.append(3)
print("list_a =", list_a)
print("list_b =", list_b)
print("append on list_b also changed list_a, because it is the same list.")

print()
print("Immutable, so nothing is shared:")

number_a = 42
number_b = number_a
number_b += 1
print("number_a =", number_a)
print("number_b =", number_b)
print("number_a is unchanged, because rebinding one name cannot touch the other.")

print()
print("Make a copy when you want independent lists:")

list_a = [1, 2]
list_b = list_a.copy()
list_b.append(3)
print("list_a =", list_a)
print("list_b =", list_b, " (copy, so list_a stayed the same)")

print()
list_c = list(list_a)
list_c.append(99)
print("list(list_a) also copies:", list_a, "|", list_c)

print()
print("=" * 60)
print("NESTED MUTABLE VALUES")
print("=" * 60)
print("A shallow copy copies the outer level only.")

original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow.append([5, 6])
print("original =", original)
print("shallow  =", shallow)
print("append did not touch original, because the outer list is a new object.")

print()
print("But the inner lists are still shared:")
shallow[0].append(99)
print("after shallow[0].append(99):")
print("original =", original, " <- the inner list changed too")
print("shallow  =", shallow)

print()
print("To copy every level you need a deep copy:")

import copy as copy_module

original = [[1, 2], [3, 4]]
deep = copy_module.deepcopy(original)
deep[0].append(99)
print("original =", original, " <- untouched this time")
print("deep     =", deep)

print()
print("=" * 60)
print("PASSING VALUES TO FUNCTIONS")
print("=" * 60)
print("Mutable values can be changed inside a function. Immutable ones cannot.")


def add_item(items, item):
    """Appends to the list that was passed in."""
    items.append(item)
    return items


shopping = ["bread"]
add_item(shopping, "milk")
print("shopping =", shopping, " <- the function changed the caller's list")


def rename(text, new_name):
    """Rebinds a local name, which cannot affect the caller."""
    text = new_name
    return text


name = "Ali"
renamed = rename(name, "Sara")
print()
print("name    =", name, " <- unchanged")
print("renamed =", renamed)

print()
print("=" * 60)
print("SUMMARY TABLE")
print("=" * 60)
print("Type      Mutable?  How to change it")
print("-" * 58)
print("int       no        assign a new value")
print("float     no        assign a new value")
print("str       no        build a new string")
print("bool      no        it is always True or False")
print("None      no        it is always None")
print("list      yes       append, insert, remove, sort, index assignment")
print("dict      yes       add keys, change values, delete keys")
print("set       yes       add, remove")
print("tuple     no        create a new tuple")
print()
print("=" * 60)
print("HOW TO CHECK IF A TYPE IS MUTABLE")
print("=" * 60)
print("""
There is no builtin flag for this. Two ways to find out:

1. Read the documentation, for example list is mutable and tuple is not.
2. Try it. Attempt the change and see whether it raises TypeError.
""")

candidates = [42, "text", (1, 2), [1, 2], {"a": 1}, {1, 2}]
for value in candidates:
    print(f"{str(value):<12} type: {type(value).__name__}")

print()
print("Attempting an in place change on each candidate:")


def try_mutate(value):
    """Try to change a value in place and report what happened."""
    if isinstance(value, list):
        value.append(0)
        return "changed in place"
    if isinstance(value, dict):
        value["new"] = 0
        return "changed in place"
    if isinstance(value, set):
        value.add(0)
        return "changed in place"
    return "cannot change in place, a new object is needed"


for value in [42, 3.14, "text", True, None, [1], (1,), {"a": 1}, {1, 2}]:
    print(f"   {str(value):<12} -> {try_mutate(value)}")

print()
print("=" * 60)
print("WHY IT MATTERS")
print("=" * 60)
print("""
1. Sharing is safe for numbers and text, so you can pass them to functions
   without worrying.
2. A function that appends to a list argument changes the caller's data,
   which can be a bug. Copy the list first if that is not wanted.
3. Dictionary keys must be immutable. A list cannot be a key because it can
   change and the key would no longer be findable.
4. Tuples are used instead of lists when the data must not change.
""")

print("A dictionary key must be immutable, so a list cannot be used as a key:")
try:
    bad_key = {[1, 2]: "value"}
except TypeError as error:
    print("   {[1, 2]: 'value'} ->", type(error).__name__, ":", error)

print("A tuple works as a key because it cannot change:")
good_key = {(1, 2): "value"}
print("   {(1, 2): 'value'}  ->", good_key)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- Mutable means changeable in place: list, dict, set.
- Immutable means any change creates a new object: int, float, str, bool,
  None, tuple.
- Two names can share one mutable value, so changing it affects both.
- Immutable values are safe to share, which is why they make good keys.
- Use .copy() for a shallow copy and copy.deepcopy() for a full copy.
""")