"""Topic 5: Variable Reassignment

A variable can be given a new value as many times as you want. The old value
is replaced.

Run with:  python 05-variable-reassignment.py
"""

print("=" * 60)
print("ASSIGNING A NEW VALUE REPLACES THE OLD ONE")
print("=" * 60)

count = 10
print("count =", count)
count = 20
print("count =", count)
count = 100
print("count =", count)
print("Each assignment overwrites the previous value.")

print()
print("=" * 60)
print("A REALISTIC EXAMPLE: A BANK BALANCE")
print("=" * 60)

balance = 10000
print("Opening balance :", balance)
balance = balance + 2500          # salary credited
print("After salary    :", balance)
balance = balance - 3200          # rent paid
print("After rent      :", balance)
balance -= 150                    # utility bill
print("After bill      :", balance)
balance *= 2                      # doubled by a bonus round
print("After bonus x2  :", balance)

print()
print("=" * 60)
print("REASSIGNING A VALUE THAT CHANGES ITS TYPE")
print("=" * 60)
print("Because Python is dynamically typed, one name can hold values of")
print("different kinds over time. Each type is explored in 03-data-types.")

value = 5
print("value =", value)
value = "five"
print("value =", value)
value = [5]
print("value =", value)
print("No error was raised. The name simply points somewhere new.")

print()
print("=" * 60)
print("REASSIGNING FROM ITSELF")
print("=" * 60)
print("You can use the old value to build the new one.")

score = 50
score = score + 10
print("score = 50, then score + 10   ->", score)

total = 100
total = total * 3
print("total = 100, then total * 3   ->", total)

balance = 500
balance = balance - balance * 0.1
print("10 percent off 500            ->", round(balance, 2))

print()
print("The shorter form is an augmented assignment:")
balance = 500
balance -= balance * 0.1
print("10 percent off 500, shorter   ->", round(balance, 2))

print()
print("=" * 60)
print("REASSIGNING FROM OTHER VARIABLES")
print("=" * 60)
print("One variable often grows from two others.")

width = 4
length = 6
area = width * length
print("width =", width, "| length =", length)
print("area = width * length ->", area)

per_unit_price = 250
quantity = 4
total_price = per_unit_price * quantity
print("per_unit_price =", per_unit_price, "| quantity =", quantity)
print("total_price =", total_price)

discount = 10
price_after_discount = total_price - (total_price * discount / 100)
print("discount =", discount, "% ->", price_after_discount)

print()
print("=" * 60)
print("CAREFUL: TWO NAMES CAN SHARE ONE VALUE")
print("=" * 60)
print("Assigning a = b points both names at the same object, so changing")
print("one variable changes what the other sees.")

a = 50
b = a
b = 99
print("a = 50, then b = a")
print("after b = 99  ->  a =", a, "| b =", b)
print("b held a reference to the same object, so a changed too.")

print()
print("This only affects mutable values such as lists:")
list_a = [1, 2]
list_b = list_a
list_b.append(3)
print("list_a =", list_a)
print("list_b =", list_b, "(both show the same list)")

print()
print("Use a copy when you want separate lists:")
list_a = [1, 2]
list_b = list_a.copy()
list_b.append(3)
print("list_a =", list_a)
print("list_b =", list_b, "(now they are different)")

print()
print("=" * 60)
print("RESETTING A VARIABLE")
print("=" * 60)
print("You can reuse a name for a completely new purpose. It works, but")
print("clear names are better than reusing one name.")

data = "hello"
print("data =", data)
data = [1, 2, 3]
print("data =", data)
print("Legal, but prefer a fresh name such as items or message.")

print()
print("=" * 60)
print("WHICH VALUE DOES THE VARIABLE HOLD AT THE END?")
print("=" * 60)
print("""Python runs statements in order, so a later assignment wins.

    x = 10
    x = 20
    x = 30
    print(x)      # prints 30

This only becomes confusing when the same name is reused for unrelated
values. Use descriptive names and the order of your code explains itself.
""")

value = 10
value = 20
value = 30
print("After three reassignments, value =", value)