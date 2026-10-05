"""Topic 8: Practice

Tasks for variables. Try each one yourself first, then compare with the
answer section at the bottom of this file.

How to practise:
  1. Run the file once to see the expected output.
  2. Write your own solution under each task.
  3. Run again and compare.
"""

print("=" * 60)
print("TASK 1: STORE AND PRINT BASIC INFORMATION")
print("=" * 60)
print("Create three variables for your name, your age and your city.")
print("Print all three with labels using an f-string.")
print('Expected: Name: <name> | Age: <age> | City: <city>')

print()
print("=" * 60)
print("TASK 2: FOLLOW THE NAMING RULES")
print("=" * 60)
print("Create variables with these names, correcting any that break the rules:")
print("  2nd place, my name, Student-Age, total marks, CLASS")
print("Write a one line comment for each explaining what you changed.")

print()
print("=" * 60)
print("TASK 3: REASSIGNMENT AND CALCULATION")
print("=" * 60)
print("Start with price = 1000.")
print("Add 500, then subtract 200, then multiply by 1.1.")
print("Print the value after every step.")
print("Expected final value: 1430.0")

print()
print("=" * 60)
print("TASK 4: MULTIPLE ASSIGNMENT AND SWAP")
print("=" * 60)
print("Assign a = 10, b = 20, c = 30 in one line.")
print("Swap a and c without using a temporary variable.")
print("Expected: a = 30, b = 20, c = 10")

print()
print("=" * 60)
print("TASK 5: UNPACK A LIST")
print("=" * 60)
print("Unpack the list [88, 92, 79] into three variables named")
print("english, maths and physics, then print each with its subject name.")

print()
print("=" * 60)
print("TASK 6: USE CONSTANTS")
print("=" * 60)
print("Create the constants MAX_MARKS = 100 and PASS_MARKS = 40.")
print("Set obtained_marks to 73 and print the percentage and whether the")
print("student passed, using the constants in your calculation.")

print()
print("=" * 60)
print("TASK 7: SCOPE INSIDE A FUNCTION")
print("=" * 60)
print("Write a function called discount_price that takes price and percent")
print("and returns the price after the discount.")
print("Call it with 2500 and 15, and print the result.")
print("Expected: 2125.0")
print("Then comment out any attempt to use a variable defined inside the")
print("function from outside it, and read the error message.")

print()
print("=" * 60)
print("BONUS TASK A: A SMALL RECEIPT")
print("=" * 60)
print("Create constants for a tax rate and a discount rate, create")
print("variables for item price and quantity, then calculate:")
print("  subtotal  = price * quantity")
print("  discount  = subtotal * discount rate")
print("  tax       = (subtotal - discount) * tax rate")
print("  total     = subtotal - discount + tax")
print("Print each value clearly.")

print()
print("=" * 60)
print("BONUS TASK B: VALUES IN A DICTIONARY")
print("=" * 60)
print("Store four pieces of information in one dictionary named profile:")
print("name, age, city and course.")
print("Print the whole dictionary, then print one value using its key.")

print()
print("=" * 60)
print("=" * 60)
print("ANSWER SECTION - READ AFTER YOU FINISH THE TASKS")
print("=" * 60)
print("=" * 60)

print()
print("--- ANSWER 1: BASIC INFORMATION ---")
name = "Ahmed"
age = 20
city = "Karachi"
print(f"Name: {name} | Age: {age} | City: {city}")

print()
print("--- ANSWER 2: NAMING RULES ---")
second_place = 2       # renamed: cannot start with a digit
my_name = "Ahmed"      # renamed: no spaces allowed
student_age = 20       # renamed: no hyphens allowed
total_marks = 450      # renamed: no spaces allowed
course = "Python"      # renamed: class is a reserved keyword

print()
print("--- ANSWER 3: REASSIGNMENT ---")
price = 1000
print("start        :", price)
price += 500
print("after + 500  :", price)
price -= 200
print("after - 200  :", price)
price *= 1.1
print("after * 1.1  :", round(price, 2))

print()
print("--- ANSWER 4: SWAP ---")
a, b, c = 10, 20, 30
print("before: a =", a, "| b =", b, "| c =", c)
a, c = c, a
print("after : a =", a, "| b =", b, "| c =", c)

print()
print("--- ANSWER 5: UNPACK A LIST ---")
english, maths, physics = [88, 92, 79]
print("English :", english)
print("Maths   :", maths)
print("Physics :", physics)

print()
print("--- ANSWER 6: CONSTANTS ---")
MAX_MARKS = 100
PASS_MARKS = 40
obtained_marks = 73

percentage = obtained_marks / MAX_MARKS * 100
is_pass = obtained_marks >= PASS_MARKS

print(f"Obtained : {obtained_marks} / {MAX_MARKS}")
print("Percentage:", round(percentage, 2))
print("Passed   :", is_pass)

print()
print("--- ANSWER 7: SCOPE INSIDE A FUNCTION ---")


def discount_price(price, percent):
    """Returns the price after applying a percentage discount."""
    discount_amount = price * (percent / 100)
    final_price = price - discount_amount
    return final_price


result = discount_price(2500, 15)
print("Price after 15 percent discount:", result)
print("The variables discount_amount and final_price are local, so using")
print("them outside the function raises NameError. Uncomment to check:")
print()
print("#   print(discount_amount)   # NameError")

print()
print("--- BONUS ANSWER A: SMALL RECEIPT ---")
TAX_RATE = 0.17
DISCOUNT_RATE = 0.10
price = 1200
quantity = 3

subtotal = price * quantity
discount = subtotal * DISCOUNT_RATE
tax = (subtotal - discount) * TAX_RATE
total = subtotal - discount + tax

print("Subtotal :", subtotal)
print("Discount :", round(discount, 2))
print("Tax      :", round(tax, 2))
print("Total    :", round(total, 2))

print()
print("--- BONUS ANSWER B: DICTIONARY ---")
profile = {
    "name": "Ahmed",
    "age": 20,
    "city": "Karachi",
    "course": "Computer Science",
}
print(profile)
print("Course   :", profile["course"])
print("Age      :", profile["age"])