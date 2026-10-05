"""Topic 7: Running Python Programs

There are two main ways to run a program: press the Run button in VS Code, or
type a command in a terminal.

Run with:  python 07-running-python-programs.py
"""

import os
import sys

print("=" * 60)
print("HOW THIS SCRIPT IS BEING RUN RIGHT NOW")
print("=" * 60)
print("Script name   :", os.path.basename(sys.argv[0]))
print("Script folder :", os.path.dirname(os.path.abspath(sys.argv[0])))
print("Arguments     :", sys.argv)
print("Arguments count:", len(sys.argv), "(index 0 is always the script name)")

print()
print("=" * 60)
print("METHOD 1: RUNNING FROM VS CODE")
print("=" * 60)
print("""
1. Open your folder in VS Code (File > Open Folder).
2. Open the .py file you want to run.
3. Click the play button in the top-right corner, the Run Python File icon.
   Or press Ctrl+F5.

VS Code then runs the file in a terminal panel at the bottom and prints the
output there. Errors appear with the exact line number.

Useful shortcuts:
  Ctrl+F5    Run without debugging
  F5         Run with debugging (you can stop at any line)
  Shift+F5   Stop the program

Note: if the run button does nothing, press Ctrl+Shift+P, run
"Python: Select Interpreter" and choose your Python 3 installation.
""")

print("=" * 60)
print("METHOD 2: RUNNING FROM POWERSHELL OR COMMAND PROMPT")
print("=" * 60)
print("""
Open a terminal in your project folder and use:

    python filename.py

Examples:

    python 07-running-python-programs.py
    python hello.py
    python .\\scripts\\main.py

If python is not recognised on Windows, use the launcher instead:

    py filename.py

Also useful:

    python filename.py arg1 arg2    pass values into your program
    python filename.py 10 20        numbers stay as strings, use int() to convert
""")

print()
print("=" * 60)
print("DECODING THE ARGUMENTS")
print("=" * 60)

if len(sys.argv) > 1:
    for index, value in enumerate(sys.argv[1:], start=1):
        print(f"Argument {index}: {value}")
else:
    print("No arguments were passed.")
    print("Try: python 07-running-python-programs.py Sara 20")
    print("Everything after the filename arrives inside sys.argv[1:].")

print()
print("=" * 60)
print("THE WORKING DIRECTORY MATTERS")
print("=" * 60)
print("Python starts in the folder where you launched it, not always where")
print("the file lives. That decides which relative paths work.")
print("Current folder:", os.getcwd())

print()
print("=" * 60)
print("SEEING THE OUTPUT")
print("=" * 60)
print("""
stdout    normal output goes here (what you see)
stderr    error messages go here
Both appear in the same place when you run from a terminal or VS Code.
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
VS Code        Ctrl+F5, or the play button
PowerShell     python filename.py
Command Prompt python filename.py
Windows alt    py filename.py
REPL           python, then type commands after the >>> prompt
""")