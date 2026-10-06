"""Topic 2: The input() Function

input() pauses the program and waits for the user to type a line. It always
returns text, no matter what the user typed.

This file uses a scripted stand-in so it can run on its own. Every interactive
line is also shown in its real form.

Run with:  python 02-input-function.py
"""

import builtins

print("=" * 60)
print("HOW input() WORKS")
print("=" * 60)
print("""
Syntax:  input(prompt)

- prompt is text shown to the user. It usually ends with a space and a colon.
- The program pauses until the user presses Enter.
- Whatever they typed is returned as a str.
- No value is typed is returned as an empty string ''.
""")

print("=" * 60)
print("A FIRST EXAMPLE")
print("=" * 60)
print("The real code is one line:")
print()
print('    name = input("Enter your name: ")')
print()
print("Below, the answers are supplied by a script so this file does not wait.")
print("Type your own answer if you run it interactively.")
print()

real_input = builtins.input


def scripted_input(prompt: object = "", answers=None):
    """Return input() with a scripted answer instead of blocking."""
    print(prompt, end="", flush=True)
    if answers:
        answer = answers.pop(0)
    else:
        answer = real_input(str(prompt))
    print(answer)
    return answer


answers = ["Ahmed"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)

name = input("Enter your name: ")

builtins.input = real_input

print("Returned value :", repr(name))
print("Its type       :", type(name).__name__)
print("This is text, not a name object.")

print()
print("=" * 60)
print("input() ALWAYS RETURNS A STRING")
print("=" * 60)
print("Even when the user types digits, you get text.")

answers = ["20"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
age_text = input("Enter your age: ")
builtins.input = real_input

print("value   :", repr(age_text))
print("type    :", type(age_text).__name__)
print("isdigit :", age_text.isdigit())
print()
print('Type 20 in your own program and you get "20", so this fails:')
print("Convert the text before doing arithmetic:")
print("   int(age_text) + 1 =", int(age_text) + 1)

print()
print("=" * 60)
print("THE PROMPT ARGUMENT")
print("=" * 60)
print("A good prompt tells the user exactly what to enter.")

answers = ["Bilal"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
first = input("First name: ")
builtins.input = real_input

answers = ["Khan"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
last = input("Last name : ")
builtins.input = real_input

print("first =", repr(first), " last =", repr(last))

print()
print("A prompt can be built with an f-string too:")
answers = ["45"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
total = input("Enter total for 45 items: ")
builtins.input = real_input
print("total =", repr(total))

print()
print("=" * 60)
print("EMPTY INPUT")
print("=" * 60)
print("Pressing Enter with nothing typed returns ''.")
print("An empty string is falsy, which makes a nice validation check.")

answers = [""]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
city = input("City (press Enter to skip): ")
builtins.input = real_input

print("city   :", repr(city))
print("truthy :", bool(city))
if city:
    print("City was given:", city)
else:
    print("No city was entered.")

print()
print("=" * 60)
print("MULTIPLE LINES AND SPACES")
print("=" * 60)
print("input() reads up to the next newline, so spaces around the text are")
print("kept unless you remove them.")

answers = ["  Sara  "]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
name = input("Name: ")
builtins.input = real_input

print("as typed     :", repr(name))
print("strip()      :", repr(name.strip()))
print("length typed :", len(name), "| length cleaned:", len(name.strip()))

print()
print("=" * 60)
print("READING A NUMBER, THE CORRECT PATTERN")
print("=" * 60)
print("Convert the text right after reading it.")


def read_number(prompt):
    """Ask for a whole number until a valid one is given."""
    while True:
        text = real_input(prompt)
        try:
            return int(text)
        except ValueError:
            print("Please enter a whole number.")


print("The function below waits for valid input. Uncomment to try it:")
print()
print("#   marks = read_number('Enter your marks: ')")
print("#   print('You entered', marks)")
print()
print("Shorter version for a known clean value:")
answers = ["42"]
builtins.input = lambda prompt="": scripted_input(prompt, answers)
marks = int(input("Enter your marks: "))
builtins.input = real_input
print("marks =", marks, "type =", type(marks).__name__)

print()
print("=" * 60)
print("WHY THE PROGRAM SEEMS TO DO NOTHING")
print("=" * 60)
print("""
If input() has no prompt, the cursor blinks and nothing appears. That is
usually reported as the program hanging. Always give a clear prompt, and
remember the line is reached only after earlier statements have run.
""")

print("=" * 60)
print("input() AND KEYBOARD INTERRUPT")
print("=" * 60)
print("Press Ctrl+C at the prompt to stop a program waiting for input.")
print("Python reports KeyboardInterrupt. That is normal and expected.")

print()
print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)
print("""
1. Forgetting that the result is text.
   age = input('Age: ')  then  age + 1  raises TypeError.
2. Forgetting the parenthesis on input.
3. Converting too early inside the call, which is fine but harder to
   revalidate:  age = int(input('Age: '))  fails immediately on bad text.
4. Printing a prompt that does not say what is expected.
5. Leaving a program waiting for input inside a script you want to test
   automatically.
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
- input(prompt) pauses the program and returns what the user typed.
- The return value is always a str, so convert it before arithmetic.
- Empty Enter gives ''.
- Always show a prompt, and validate before converting.
- Ctrl+C stops a waiting program.
""")