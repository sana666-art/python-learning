"""Topic 1: What is Python?

Python is a high-level, general-purpose programming language created by
Guido van Rossum and first released in 1991. It is designed to be readable,
so beginners can focus on solving problems instead of syntax details.

Run with:  python 01-what-is-python.py
"""

import sys

print("=" * 60)
print("WHAT IS PYTHON?")
print("=" * 60)

print("""
Python is:
- A high-level programming language
- Interpreted, so no separate compilation step is needed
- Dynamically typed, so you do not declare variable types
- Object-oriented, meaning code is organised around objects and classes
- Open source, with a large free community behind it
""")

print("=" * 60)
print("WHERE PYTHON IS USED")
print("=" * 60)

print("""
Web development      Django, Flask, FastAPI
Data analysis        pandas, NumPy, Matplotlib
Automation           Excel reports, file handling, scheduled scripts
Artificial AI        PyTorch, TensorFlow, scikit-learn
Testing              pytest, unittest
Desktop apps          Tkinter, PyQt
Scientific computing NumPy, SciPy
""")

print("=" * 60)
print("PYTHON'S POPULARITY")
print("=" * 60)

print("Python is consistently ranked among the most used languages")
print("worldwide. Beginners like it because the syntax is close to English,")
print("and employers like it because it is used across every industry.")
print("Common rankings: TIOBE Index, Stack Overflow Developer Survey.")

print()
print("=" * 60)
print("PYTHON 2 vs PYTHON 3")
print("=" * 60)

print("""
Python 2 (released 2000): older version, reached end of life in 2020.
Python 3 (released 2008): current version, actively developed.

Main differences:
- print:      Python 2 used print "hi", Python 3 uses print("hi")
- Division:   Python 2 turned 7 / 2 into 3, Python 3 keeps 3.5
- Input:      Python 2 used raw_input(), Python 3 uses input()
- Support:    Python 2 receives no updates, Python 3 does

Learn Python 3. Everything in this course uses Python 3.
""")

print("=" * 60)
print("THE INTERPRETER YOU ARE USING RIGHT NOW")
print("=" * 60)

print("Python version :", sys.version.split()[0])
print("Implementation  :", sys.implementation.name)
print("Executable used :", sys.executable)