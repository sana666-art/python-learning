"""Topic 7: Variable Scope (Introduction)

Scope tells you where a variable can be used. You already saw one example in
Topic 4: a variable inside a function was not visible outside it.

This file gives a first look. Functions and scope in depth belong to a later
topic.

Run with:  python 07-variable-scope-introduction.py
"""

print("=" * 60)
print("WHAT IS SCOPE?")
print("=" * 60)
print("""
Scope is the region of code where a variable exists and can be read or
changed.

If a variable is not in scope, Python raises NameError.
""")

print("=" * 60)
print("LEVEL 1: GLOBAL SCOPE")
print("=" * 60)
print("A variable written at the top level of a file is global. It can be")
print("used anywhere in that file, including inside functions.")

company_name = "Tech Academy"
company_city = "Lahore"

print("company_name =", company_name)
print("company_city =", company_city)


def show_company():
    print("Inside the function, the global variable is visible.")
    print("company_name =", company_name)
    print("company_city =", company_city)


show_company()

print()
print("=" * 60)
print("LEVEL 2: LOCAL SCOPE")
print("=" * 60)
print("A variable created inside a function is local. It disappears when the")
print("function ends and it cannot be used outside.")


def calculate_bill():
    price = 100
    quantity = 3
    total = price * quantity
    print("Inside the function: total =", total)
    return total


calculate_bill()

print()
print("The variable total no longer exists here. Uncomment to see the error:")
print()
print("#   print(total)   # NameError: name 'total' is not defined")

print()
print("=" * 60)
print("GLOBAL AND LOCAL TOGETHER")
print("=" * 60)
print("A function can read a global value and create its own local values.")
print("A local name that matches a global name hides it inside the function.")


def order_summary(order_id, items):
    """Uses the global TAX_RATE and creates its own local values."""
    order_id_local = order_id
    item_count = len(items)
    subtotal = sum(items)
    total = subtotal + (subtotal * TAX_RATE)
    print("Order id    :", order_id_local)
    print("Items       :", item_count)
    print("Subtotal    :", subtotal)
    print("Total       :", round(total, 2))


TAX_RATE = 0.05
print("TAX_RATE =", TAX_RATE, "(a global constant)")
order_summary(101, [500, 300, 200])
print("All of this worked because TAX_RATE was visible inside the function.")

print()
print("=" * 60)
print("SHADOWING")
print("=" * 60)
print("A local variable with the same name as a global hides the global only")
print("inside that function.")


def show_shadowing():
    country = "Pakistan"
    print("Inside the function: country =", country)


show_shadowing()

print()
print("=" * 60)
print("READING A VARIABLE BEFORE THE FUNCTION DEFINES IT")
print("=" * 60)
print("Python does not care where in a function a variable is first assigned.")
print("It reads the whole function first, so the function cannot use the")
print("variable before its own assignment line. Uncomment to see the error:")


def order_wrong():
    print("Subtotal is", subtotal)   # error: subtotal is assigned below
    subtotal = 500


print()
print("#   order_wrong()   # UnboundLocalError")
print("The safe pattern is to read parameters first, then compute:")


def order_right(subtotal, rate):
    """Reads its inputs before computing anything."""
    tax_amount = subtotal * rate
    grand_total = subtotal + tax_amount
    print("Subtotal     :", subtotal)
    print("Tax          :", round(tax_amount, 2))
    print("Grand total  :", round(grand_total, 2))


order_right(1000, 0.17)

print()
print("=" * 60)
print("THE FOUR SCOPE LEVELS")
print("=" * 60)
print("""
Global      written at the top level of a file
Local       written inside a function
Enclosing   a function inside another function (not yet used here)
Built-in    names Python already knows, such as print, len, type

Functions and their scopes are studied properly in the functions topic.
""")

print("=" * 60)
print("CHECKING A NAME SAFELY")
print("=" * 60)
print("locals() and globals() show what names are available right now.")

def show_names():
    """Prints the local names and confirms the global one is readable."""
    print("Local names here  :", [n for n in locals() if not n.startswith("__")])
    print("company_city      :", company_city, "(read from the global scope)")
    print("'company_city' in globals():", "company_city" in globals())


show_names()

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- A global variable can be used anywhere in the file.
- A local variable exists only inside its function.
- Using a name outside its scope raises NameError.
- Using a local name before its assignment line raises UnboundLocalError.
- globals() and locals() show the names available at any point.
""")