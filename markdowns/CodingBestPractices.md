# Coding Best Practices


## Style Guidelines
- every language may have its own style guidelines
- Python has PEP 8 - https://peps.python.org/pep-0008/
- common guidelines:
    1. use meaningful and descriptive names for variables, functions, classes, etc.
    2. use consistent indentation and spacing (use 4 spaces); don't mix tabs and spaces
    3. use blank lines to separate logical sections of code; use 2 lines between functions and classes; use one line between methods inside a class
    4. use comments and docstrings to explain the purpose and behavior of code
    5. use consistent naming conventions (e.g., snake_case for variables and functions, CamelCase/CapsCase for classes)
    6. use consistent and appropriate use of quotes (single or double) for strings

- use linter tools to check for style violations
    - pylint, flake8, black, etc.
- use auto-formatters to automatically format code
    - autopep8, black, yapf, etc.

## Type Hints/Annotations

- without type hints it is difficult to know what type of data a function expects and returns
    - especially when working with large codebases or when the code is not well-documented
    - makes the code less readable and maintainable and more error-prone
- type hints were introduced in Python 3.5
- everything in Python is a object that is associated with some type
- Python is dynamically typed language
- type of a variable or object is determined during run-time based on the type of data/object the variable is assigned
- the built-in `type()` function can be used to know the type of an object


```python
type("Hello World!")
```




    str




```python
type(42)
```




    int




```python
type(1.5)
```




    float




```python
msg = 'Hello World'
```


```python
msg = 42
```


```python
type(msg)
```




    int




```python
msg = 1.5
```


```python
type(msg)
```




    float




```python
id(msg)
```




    140554878311024



## Type checking
- issue with dynamic typing and operations


```python
def odd(n):
    return n % 2 == 1
```


```python
odd(3)
```




    True




```python
odd(4)
```




    False




```python
# what about odd of str
odd('Hello World')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[16], line 2
          1 # what about odd of str
    ----> 2 odd('Hello World')


    Cell In[13], line 2, in odd(n)
          1 def odd(n):
    ----> 2     return n % 2 == 1


    TypeError: not all arguments converted during string formatting



```python
# redefining odd using type hint
def odd(n: int) -> bool:
    return n % 2 == 1
```


```python
odd(10)
```




    False




```python
odd('hi')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[19], line 1
    ----> 1 odd('hi')


    Cell In[17], line 3, in odd(n)
          2 def odd(n: int) -> bool:
    ----> 3     return n % 2 == 1


    TypeError: not all arguments converted during string formatting


## annotating advanced types

- only primitive types can be annotated directly
    - int, float, str, and bool
- for advanced types, import capitalized type names from `typing` module
- Union, Optional, Any, Tuple, List, Dict, Set, etc.
- `List[int]` - list of integers
- `Dict[str, int]` - dictionary with string keys and integer values
- `Tuple[int, str, float]` - tuple with an integer, string, and float
- `Set[bool]` - set of booleans
- `Optional[str]` - optional string (can be None)
- `Union[int, float]` - can be either an integer or a float
- `Any` - any type
- `Callable[[int, int], int]` - function that takes two integers and returns an integer
- `Iterable[str]` - iterable of strings
- `Iterator[int]` - iterator of integers
- `a: int | float` - variable `a` can be either an integer or a float
- `def foo(a: int | float) -> int | float:` - function `foo` takes an integer or a float and returns an integer or a float



```python
from typing import List, Tuple

def max_min(lst: List[float]) -> Tuple[float, float]:
    return max(lst), min(lst)
```


```python
assert max_min([1.0, 2.0, 3.0, 4.0]) == (4.0, 1.0)
```

## mypy tool

- [https://mypy-lang.org/](https://mypy-lang.org/)
- mypy tool is commonly used to check the Type hints for consistency
    - it's an effort to make Python type safe similar to static-typed languages
- it's a third-party library that must be installed using `pip` or `conda`
- https://mypy.readthedocs.io/en/stable/getting_started.html#
- if you use `--strict mode`, you'll never get a run-time error in Python unless you explicitly circumvent `mypy`!!
- use `--disallow-untyped-defs` to warn if you add dynamic functions by mistake 
- Docker already has mypy installed from `requirements.txt` file

```bash
conda install mypy
pip install mypy
```


```python
! cat src/objects/bad_hints.py
```

    """
    Python 3 Object-Oriented Programming 4th ed.
    Chapter 2, Objects in Python.
    NOTE. Remove the ``# type: ignore`` comments to reproduce examples in the text.
    """
    #from __future__ import annotations
    # annotations is required for Python 3.7 and earlier for generic types
    
    def odd(n): # dynamic typing
        return n % 2 != 0
    
    def add(arg1, arg2):
        return arg1+arg2
    
    def main():
        print(odd("Hello, world!"))
    
    
    if __name__ == "__main__":
        main()
        print(add(1, 2))
        print(add("Hello", 1))
    



```python
# technically there should be errors, but ...
! mypy src/objects/bad_hints.py
```

    [1m[32mSuccess: no issues found in 1 source file[m



```python
! mypy --disallow-untyped-defs src/objects/bad_hints.py
```

    src/objects/bad_hints.py:9: [1m[31merror:[m Function is missing a type annotation  [m[33m[no-untyped-def][m
    src/objects/bad_hints.py:12: [1m[31merror:[m Function is missing a type annotation  [m[33m[no-untyped-def][m
    src/objects/bad_hints.py:15: [1m[31merror:[m Function is missing a return type annotation  [m[33m[no-untyped-def][m
    src/objects/bad_hints.py:15: [34mnote:[m Use [m[1m"-> None"[m if function does not return a value[m
    [1m[31mFound 3 errors in 1 file (checked 1 source file)[m



```python
! mypy --strict src/objects/good_hints.py
```

    [1m[32mSuccess: no issues found in 1 source file[m



```python
! cat src/objects/good_hints.py
```

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
    


## Explaining yourself with docstrings

- Python is easy to read and is self-documenting (mostly)
- in OOP, it's important to write API documentation that clearly summarizes what each object and method does
- Python supports this through **docstrings**
- **docstrings** are strings with triple-single (''') or triple-double (""") quotes
- one of the best things to include in a **docstring** is a concrete example
- tools like **doctest** can locate and confirm these examples are correct; providing a quick test
- see `src/objects/point.py` file for demo
- run `mypy --strict point.py` to check for type correctness
- run the script with `-i` option to enter into interactive mode
    - `python -i point.py`
- run the `doctest` to test the examples provided in **docstrings**
    - `python -m doctest point.py`
    - provides no output if all the examples are correct


```python
# should provide no error...
! python -m doctest src/objects/point.py
```

### VS Code Extension

- use autoDocString extension to quickly write documentation of your methods/API
- search for audoDocstring from the extension manager in VS Code and install it
- just type ''' or """ under any class or function name to generate boilerplate docstrings

### pdoc3

- https://pypi.org/project/pdoc3/
- auto-generate API documentation for Python projects

```bash
pip install pdoc3
pdoc --help
pdoc your_project
pdoc -o documentations point.py
# Create HTML documentation of point.py into the documentations folder
```
- pdoc3 is installed in Docker image

## Modules and Packages

- it's best practice to refactor code into modules and related packages
- modules are Python files/scripts with .py extension
- package is a collection of modules in a folder
- package is a folder with `__init__.py` file (normally empty!)
- packages help organize modules' folder hierarchy
- never use wildcard **\*** import
    - pollutes the current namespace
    - difficult to understand what names are imported from what modules and packages
- must use import guard to enclose all your executable code


```python
if __name__ == "__main__":
    # executable code; function call
    main()
```

### Importing modules and names into Python scripts

### Absolute imports

- provides a complete path to the module, class, and function we want to import
- let's see the demo packages and modules in the `src/objects` folder


```python
! pwd
```

    /Users/rbasnet/projects/Object-Oriented-Programming-Design-Patterns/notebooks



```python
%cd ./src/objects/
```

    /Users/rbasnet/projects/Object-Oriented-Programming-Design-Patterns/notebooks/src/objects



```python
! ls
```

    [34m__pycache__[m[m    [34mdocs[m[m           [34mecommerce[m[m      import_demo.py
    bad_hints.py   docstrings.py  good_hints.py  point.py



```python
# importing package doesn't work

import ecommerce
```


```python
dir(ecommerce)
```




    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__path__',
     '__spec__',
     'database',
     'db']




```python
product = ecommerce.products.Product("name1")
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[32], line 1
    ----> 1 product = ecommerce.products.Product("name1")


    AttributeError: module 'ecommerce' has no attribute 'products'



```python
# imporing module is okay
import ecommerce.products
```


```python
help(ecommerce.products)
```

    Help on module ecommerce.products in ecommerce:
    
    NAME
        ecommerce.products - Python 3 Object-Oriented Programming 4th ed.
    
    DESCRIPTION
        Chapter 2, Objects in Python.
    
    CLASSES
        builtins.object
            Product
        
        class Product(builtins.object)
         |  Product(name: str) -> None
         |  
         |  Methods defined here:
         |  
         |  __init__(self, name: str) -> None
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
    
    FILE
        /Users/rbasnet/projects/Object-Oriented-Programming-Design-Patterns/notebooks/src/objects/ecommerce/products.py
    
    



```python
# importing and creating alias
import ecommerce.products as pr
```


```python
dir(pr)
```




    ['DB',
     'Database',
     'Product',
     'Query',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'database',
     'send_mail']




```python
product = pr.Product('Some name')
```


```python
# import just one module
from ecommerce import products
```

### Relative imports

- import module, class, and function, relative to the current module
- use `.` for the current package
- use `..` for parent package

```python
from .database import Database
from ..ecommerce.database import Database
```

## Unit testing with assert

- testing is an essential part of software development
- testing helps ensure that the code (functions) work as expected
- testing helps catch bugs and errors early in the development cycle
- testing helps improve code quality and maintainability
- testing helps document the code and its behavior
- testing helps ensure that new changes don't break existing functionality
- testing helps ensure that the code is robust and reliable
- testing helps ensure that the code is secure and performant
- if there was no library and tools provided for unit testing, you could write your own
- use the `assert` statement to assert how the two values are compared
    - mostly equal!


```python
assert 'hello' == 'hello'
```


```python
assert 1.5 == 1.5000
```


```python
assert 2.5 == 3
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    Cell In[4], line 1
    ----> 1 assert 2.5 == 3


    AssertionError: 



```python
def add(a: int, b: int) -> int:
    return a + b
```


```python
def test_add_positives():
    assert add(1, 2) == 3

def test_add_negatives():
    assert add(-1, -2) == -3

def test_add_mixed():
    assert add(-1, 1) == 0
```


```python
test_add_positives()
test_add_negatives()
test_add_mixed()
```

## Automation using Makefile

- projects often require repetitive tasks
- you may have to run the same commands over and over again with different parameters; hard to remember
- it's best to automate these tasks
- **Makefile** is a simple way to do this
- **Makefile** is a file with set of directives used with the **make** build automation tool
- Makefile contains rules with targets and dependencies
- a target is a label for a set of commands
- a dependency is a file that is used as input to create the target
- a rule looks like this:
- **.PHONY** is used to mark targets that are not files

```makefile
target: dependency
    command
```
- the command must be preceded by a **tab** character
- the default target is the first target in the Makefile
- the default target is usually called **all**
- the **all** target is used to build the entire project

```bash
all: type-check style-check unittest all-test clean
    @echo "All tasks completed successfully!"

.PHONY: type-check
type-check:
    @echo "Checking types..."
    mypy --strict src
    @echo "Type checking completed successfully!"

...

```

- you can run a specific target by specifying it as an argument to the **make** command
- for example, to run the **clean** target, you would run the following command in the terminal:

```bash
make clean
```
- you can also run multiple targets at once by specifying them as arguments to the **make** command
- for example, to run the **clean**
- and **test** targets, you would run the following command in the terminal:

```bash
make clean test
```
- see global Makefile in the repo or local Makefiles specific to project in demo-assignments folder
- for details see - https://www.gnu.org/software/make/manual/make.html
- Makefile is installed in Docker image

## Pytest

- Pytest helps your write better programs: [https://docs.pytest.org/en/8.0.x/](https://docs.pytest.org/en/8.0.x/)
- Must explictly install pytest; not a part of standard library
- `pip install -U pytest`
- pytest can be executed for a single file, or all the files and subfolders within a folder
- pytest can discover all the test modules that are named `test_*.py`
- pytest will execute every `test_*()` function in the `test` module

## Code coverage by unit tests

- though not sufficient, code coverage provides measureable metrics to determine how good the test cases are
- more on it here: [https://pytest-cov.readthedocs.io/en/latest/readme.html](https://pytest-cov.readthedocs.io/en/latest/readme.html)
- **code coverage** is a count of the number of lines of code that are executed by a program and by test code
- we can download and use **pytest-cov** plugin to do just that
- install coverage first; Docker image already has it installed

```bash
pip install pytest-cov
```

- use `#pragma: no cover` directive to tell pytest-cov not to count the function/code if you don't know how to test certain code (yet!)
- html report is created in `htmlcov` folder
- note coverage creates `.gitignore` file inside `htmlcov` that ignores all the files in the folder to be tracked
- delete the `.gitignore` file to track and html reports into your repository

### Write more tests for 100% code coverage

- first run coverage on test_averages.py file as it is
- then add more tests to to cover 100% code
- run pytest-cov to verify...
- see Makefile in demo-assignments
- run the Makefile in the root folder of this repo from a terminal

```bash
(py) ╭─rbasnet@M-rbasnetMBP ~/projects/Object-Oriented-Programming-Design-Patterns/demo-assignments 
╰─$ make run-test-coverage

...

---------- coverage: platform darwin, python 3.10.9-final-0 ----------
Name                                                   Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------------
demo-assignments/A2-ABC/egypt/egypt.py                    45      0   100%
demo-assignments/A2-ABC/egypt/kattis.py                   20      0   100%
demo-assignments/A2-ABC/egypt/tests/__init__.py            0      0   100%
demo-assignments/A2-ABC/egypt/tests/test_egypt.py         68      0   100%
demo-assignments/A2-ABC/egypt/tests/test_triangle.py      28      0   100%
demo-assignments/A2-ABC/egypt/triangle.py                 34      0   100%
------------------------------------------------------------------------------------
TOTAL                                                    195      0   100%
```



## Project Structure

- it's best practice to organize code into a well-defined project structure
- a well-defined project structure helps in:
    - better organization of code
    - easier navigation and understanding of the codebase
    - better collaboration among team members
    - easier testing and deployment of the code
- most common project structure in python uses **src layout**

```markdown
project-name/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── cli.py
│       ├── core.py
│       └── utils/
│           ├── __init__.py
│           └── file_helpers.py
│
├── tests/
│   ├── test_core.py
│   └── utils/
│       └── test_file_helpers.py
│
├── docs/
│   └── index.md
|   |__ installation.md
|   |__ usage.md
│
└── scripts/
    └── dev_setup.sh
```


