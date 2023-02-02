#from __future__ import annotations
# annotations is required for Python 3.7 and earlier for generic types

def odd(n: int) -> bool: # dynamic typing
    return n % 2 != 0

def add(arg1: int, arg2: int) -> int: # static typing
    return arg1+arg2

def main() -> None:
    print(odd(10))


if __name__ == "__main__":
    main()
    print(add(1, 2)) # no issue
    #print(add("Hello", "World")) # issue here...

