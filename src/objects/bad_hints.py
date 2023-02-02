"""
Python 3 Object-Oriented Programming 4th ed.
Chapter 2, Objects in Python.
NOTE. Remove the ``# type: ignore`` comments to reproduce examples in the text.
"""
#from __future__ import annotations
# annotations is required for Python 3.7 and earlier for generic types

def odd(n): # dynamic typing
    return n % 2 != 0

def add(arg1, arg2): # static typing
    return arg1+arg2

def main():
    print(odd("Hello, world!"))


if __name__ == "__main__":
    main()
    print(add(1, 2)) # no issue
    print(add("Hello", "World")) # issue here...

