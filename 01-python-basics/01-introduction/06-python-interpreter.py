"""Topic 6: The Python Interpreter

The interpreter is the program that reads your .py file and carries out your
instructions. Python has no compiler step: the interpreter does the work.

Run with:  python 06-python-interpreter.py
"""

import sys
import platform
import site

print("=" * 60)
print("WHAT THE INTERPRETER DOES")
print("=" * 60)
print("""
1. Reads your source code from the .py file.
2. Checks the syntax. If there is a mistake, it stops and reports the
   line number.
3. Translates the code into instructions the computer understands.
4. Executes the instructions and prints the result.
""")

print("The whole cycle is called the Read-Compile-Execute cycle.")
print("Because it happens line by line, a syntax error stops everything,")
print("and you can test small pieces of code instantly.")

print()
print("=" * 60)
print("YOUR INTERPRETER DETAILS")
print("=" * 60)
print("sys.executable :", sys.executable)
print("sys.version    :", sys.version.replace("\n", " "))
print("Implementation :", sys.implementation.name)
print("Compiled on    :", platform.python_implementation())
print("Python version :", platform.python_version())
print("Operating sys  :", platform.system())
print("Machine type   :", platform.machine())
print("Byte order     :", sys.byteorder)
print("Default encoding:", sys.getdefaultencoding())

print()
print("=" * 60)
print("WHERE THE INTERPRETER FINDS ITS STANDARD LIBRARY")
print("=" * 60)
print("sys.prefix      :", sys.prefix)
print("sys.executable  :", sys.executable)
try:
    print("site-packages   :", site.getsitepackages()[0])
except Exception as error:
    print("site-packages   : could not read ->", error)

print()
print("=" * 60)
print("INTERACTIVE PYTHON SHELL")
print("=" * 60)
print("""
The interactive shell (also called the REPL) runs Python commands directly
instead of running a saved file. It is perfect for practice.

Start it in PowerShell:

    python

You will see three prompt characters:

    >>>   the normal prompt, ready for a command
    ...   continuation prompt, the statement is not finished yet

Example session:

    >>> 2 + 2
    4
    >>> name = "Ali"
    >>> name
    'Ali'
    >>> if name == "Ali":
    ...     print("Hi Ali")
    ...
    Hi Ali
    >>> exit()

Useful REPL tips:
- Press Up/Down to reuse earlier commands.
- Type help() to browse built-in help.
- Type dir() to see what an object can do.
- exit() or Ctrl+Z then Enter closes the shell.
""")

print("=" * 60)
print("RUNNING COMMANDS DIRECTLY (WITHOUT SAVING A FILE)")
print("=" * 60)
print("You can pass a command straight to the interpreter with -c:")
print()
print("python -c \"print('Hello from one line of code')\"")
print()
print("And print a statement and the result in REPL style:")
print()
print("python -i -c \"2 + 2\"")
print()
print("Other useful flags:")
print("  python -V                 print the version and exit")
print("  python -m pip install X   run a module, e.g. the package installer")
print("  python -c 'import sys; print(sys.argv)'  see the arguments passed")

print()
print("=" * 60)
print("LIVE EXAMPLE: CODE AND RESULT IN THIS FILE")
print("=" * 60)

# Statements are read and executed in order, exactly like the REPL.
x = 10
print("x =", x)
x = x * 2
print("x = x * 2  ->  x =", x)

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("sum of", numbers, "is", total)

print()
print(">>> import sys; print(sys.executable)")
import sys
print(sys.executable)