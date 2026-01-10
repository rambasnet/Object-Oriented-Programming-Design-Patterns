## Functions and Decorator Pattern

### Topics

- handle variable length arguments
- lambda expressions
- higher-order functions
- nested functions
- functions as returned values
- currying
- function decorators
- function and class decorator pattern

## Variable length arguments

- when not sure how many arguments will be passed to a function
- `*args` (non-keyworded variable length arguments)
- `**kwargs` (keyworded variable length arguments)
- e.g., built-in `print` function uses variable length arguments and keyworded arguments

### print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)



```python
help(print)
```


```python
print()
```


```python
# variable length arguments demo
def someFunction(a, b, c, *varargs, **kwargs):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('*args = ', varargs)
    print('type of args = ', type(varargs))
    print('**kwargs = ', kwargs)
    print('type of kwargs = ', type(kwargs))
    try:
        print(kwargs['fname1'])
    except KeyError as ex:
        print(ex)

```


```python
# call someFunction with some arguments
someFunction(1, 'Apple')
```

## Lambda Functions/Expressions

- anonymous functions without names
- typically used in conjunction with higher order functions such as: `map()`, `reduce()`, `filter()`

### lambda function properties and usage

- single line simple functions
- no explicit return keyword is used
- always contains an expression that is implictly returned
- can use a lambda definition anywere a function is expected without assigning to a variable
- syntax: 
```python
    lambda argument(s): expression
```

### difference between lambda and regular function


```python
nums = input('Enter 5 numbers separated by space:')
```


```python
nums
```


```python
nums = list(map(int, nums.split()))
```


```python
nums
```


```python
# regular function
def func(x): return x**2
```


```python
print(func(4))
```


```python
type(func)
```


```python
print(func)
```


```python
g = lambda x: x**2 # no name, no parenthesis, and no return keyword
# a function that takes x and returns x**2
```


```python
g(4)
```


```python
type(g)
```


```python
print(g)
```

## Higher-order functions

https://composingprograms.com/pages/16-higher-order-functions.html
- functions that manipulate other functions are called higher order functions
- functions take function(s) as argument(s)
    - typically, lambda expressions are passed as arguments
- functions can define and return a local function


```python
# compute summations of n natural numbers
# func is a function applied to all the natural numbers between 1 and n inclusive
def sum_naturals(func, n):
    total, k = 0, 1
    while k <= n:
        total += func(k)
        k += 1
    return total
```


```python
n = 100
```


```python
# pass lambda function
print(f'sum of first {n} natural numbers = {sum_naturals(lambda x: x, n)}')
```


```python
# of course you can pass regular function
def even(n): return n if n%2 == 0 else 0
```


```python
print(f'sum of even numbers from 1 to {n} = {sum_naturals(even, n)}')
```


```python
# one-liner lambda
print(f'sum of odd numbers from 1 to {n} = {sum_naturals(lambda x: x if x%2==1 else 0, n)}')
```

## Nested functions

- functions can be defined inside a function with local scope
- locally defined functions also have access to the names defined in their parent function
    - this technique is called lexical scoping
- helps keep the global frame clean and less cluter with functions that are only used inside some functions
- let's redefine sum_natural function again with local functions


```python
# compute summations of n natural numbers
# by default find sum of all the natural numbers between 1 and n inclusive
def sum_naturals1(n, number_type="all"):
    def even(x): return x if x%2 == 0 else 0
    
    def odd(x): return x if x%2 == 1 else 0
    
    def func(x):
        # local function has access to global variables as well as parent frames
        if number_type == 'even':
            return x if x%2 == 0 else 0
        else:
            return x if x%2 == 1 else 0
            
    total, k = 0, 1
    while k <= n:
        if number_type != 'all':
            total += func(k)
        elif number_type == 'odd':
            total += odd(k)
        else:
            total += k
        k += 1
    return total
```


```python
n = 100
print(f'sum of first {n} natural numbers = {sum_naturals1(n)}')
```


```python
print(f'sum of even numbers from 1 to {n} = {sum_naturals1(n, "even")}')
```


```python
# sum of odd numbers from 1 to 100
print(f'sum of odd numbers from 1 to {n} = {sum_naturals1(n, "odd")}')
```

## Functions as returned values

- functions can return a function
- locally defined functions maintain their parent environment when they are returned


```python
from typing import Callable, Any

def number_type(ntype:str ='all') -> Callable[..., Any]:
    def even(x):
        return x if x%2 == 0 else 0
    
    def odd(x):
        return x if x%2 == 1 else 0
    
    def _(x): # function to return x as it is; any()
        return x
    
    if ntype == 'all':
        return _
    elif ntype == 'even':
        return even
    else:
        return odd
```


```python
n = 100
print(f'sum of first {n} natural numbers = {sum_naturals(number_type("all"), n)}')
```


```python
print(f'sum of even numbers from 1 to {n} = {sum_naturals(number_type("even"), n)}')
```


```python
# sum of odd numbers from 1 to 100
print(f'sum of odd numbers from 1 to {n} = {sum_naturals(number_type("odd"), n)}')
```

## Currying

- breaking down the evaluation of a function that takes multiple arguments into evaluating a sequence of single-argument functions
- also used in chaining multiple functions into one

- e.g., given a function `f(x, y)`, we can define a function `g(x)(y)` equivalent to `f(x, y)`
    - `g` is a higher-order function that takes in a single argument `x` and returns another function that takes in a single argument `y`
- a single function can be broken into multiple functions by chaining the smaller functions
    - `f(x) = h(g(x))`
    - the output of inner function `g(x)` is an input for outer function `h()`
    - this transformation is called **currying**


```python
# single function that converts days to seconds
def daysToSeconds(days):
    return days * 24 * 60 * 60
```


```python
# use the function
daysToSeconds(1)
```


```python
# currying application
# convert no. of days into seconds
def convertDaysToSeconds(f1, f2, f3):
    """Higer order function that takes 3 functions."""
    def f(x): 
        return f1(f2(f3(x)))
    return f 

def daysToHours(days): 
    """ Function converts days to hours."""
    return days * 24

def hoursToMinutes(hours): 
    """ Function converts hours to minutes."""
    return hours * 60

def minutesToSeconds(minutes): 
    """ Function converts minutes to seconds."""
    return  minutes * 60
```


```python
# create a single function curry
days_to_seconds = convertDaysToSeconds(minutesToSeconds, hoursToMinutes, daysToHours)
```


```python
days_to_seconds(1)
```


```python
# currying application; function with two arguments
# built-in pow function takes two arguments; 
# let's convert it into a function that takes a single argument
def curried_pow(x):
    def g(y):
        return pow(x, y)
    return g # function preserves the local variables, x and y
```


```python
curried_pow(2)(3) # x=2, y=3; -> pow(2, 3)
# same as 2**3
```


```python
# currying application 2
# function maps each element in alist with func() transformation
def my_map(alist, func):
    for i in range(len(alist)):
        alist[i] = func(alist[i])
```


```python
# let's create a list of integers and map each to a different value
nums = list(range(1, 11))
```


```python
nums
```


```python
my_map(nums, curried_pow(2))
```


```python
nums
```

## Built-in Function Decorators

- `functools` provides `wraps` and many built-in decorators that can be very useful
    - e.g., least recently used (LRU) caching
- See [https://docs.python.org/3/library/functools.html](https://docs.python.org/3/library/functools.html) for all the higher-order functions
- any callable object can be passed to a higher-order function to decorate it!
- See this tutorial for Callbe objects in Python - [https://realpython.com/python-callable-instances/](https://realpython.com/python-callable-instances/)
- built-in decorator example


```python
from functools import cache
```


```python
count = 0
@cache
def factorial(n):
    global count
    count += 1
    return n*factorial(n-1) if n else 1
```


```python
factorial(100)
```


```python
count
```


```python
factorial(50) # use cachaed result
```


```python
count
```


```python
factorial(102) # make 2 more recursive calls
```


```python
count
```


```python
factorial.cache_info()
```


```python
# let's define our own int function using partial decorator
help(int)
```


```python
int(3.5)
```


```python
int('11', base=2)
```


```python
from functools import partial

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int'
```


```python
help(basetwo)
```


```python
basetwo('111111')
```


```python
basetwo('1000')
```


```python
assert basetwo('11') == 3
```

## Defining Function Decorators

- Python provides `wraps()` function to wrap any function that needs to be decorated
- https://realpython.com/primer-on-python-decorators/
- decorators are higher order functions
- decorators take another function as an argument and decorate it
- argument function is decorated by extending its behavior without explictly modifying the function itself

#### How about passing arguments to decorated function and its return values?
1. if the function being decorated takes arguments, provide arguments to the wrapper function
    - wrapper function wraps the argument function
2. if the function being decorated returns a value, call it with `return` statement
    - obviously, must be the last statement

### Real-world Applications

- we've already used: `@classmethod`, `@property`, `@staticmethod`
- many frameworks such as Flask, Django provide lots of decorators
    - e.g. @login_required; @app.route("/route_name"), etc.
    - simply define the functions using the library provided decorators!
- Python `functools` library provides many higher order decorators:
https://docs.python.org/3/library/functools.html


```python
# a simple fruitless function without required parameter
def hello(name=None):
    """Print Hello there!"""
    print("Hello there...")
```


```python
hello('John')
# too simple... let's decorate hello
```


```python
# a simple decorator function to decorate hello
def hello_decorator(func):
    """Decorate func."""
    
    def wrapper_hello_decorator(*args, **kwargs):
        """Wrapper for hello function."""
        # code ...
        print('I see someone...')
        # call the actual function
        func(*args, **kwargs)
        # use ret value...
        if not args:
            print("stranger...")
        else:
            print(f"Great seeing you {args[0]} !!")
        print("Have a great time!")
        # code ...
    return wrapper_hello_decorator
```


```python
# hello is decorated now, without modifying the original function
# just the behavior is modified by added extra print() before and after hello
hello_deco = hello_decorator(hello)
```


```python
hello_deco()
```


```python
hello_deco('John')
```


```python
# Python provides a better syntax, shortcut!
# use @decorter_function name and define the function that needs to be decorated
@hello_decorator
def say_hi(name=None):
    """print Hi there! with some decorations."""
    
    print("Hi there!")
```


```python
say_hi('Jake')
```


```python
# let's check the name name and docstring for say_hi
say_hi.__name__
```


```python
say_hi.__doc__
```


```python
# decorated function lost its identify! 
# Let's preserve the identify of functions being decorated...
from functools import wraps

# a simple decorator function to decorate hello
def hello_better(func):
    """Decorate func."""
    
    @wraps(func)
    def wrapper_hello_better(*args, **kwargs):
        """Wrapper for func."""
        # code ...
        # call the actual function
        ret = func(*args, **kwargs)
        # use ret value...
        if not args:
            print("stranger...")
        else:
            print(f"Great seeing you {args[0]}!!")
        print("Have a great time!")
        # code ...–
    return wrapper_hello_better
```


```python
# let's define a new function with hello_better decorator
@hello_better
def greet(name=None):
    """Print Good morning!"""
    
    print('Good morning!')
```


```python
greet()
```


```python
greet("Jane")
```


```python
greet.__name__
```


```python
greet.__doc__
```

## Decorator Pattern

- the Decorator pattern allows us to *wrap* an object that provides core functionalities with other objects
- two primary uses:
 - enhancing the response of a component as it sends data to a second component
 - supporting multiple optional behaviors
     - suitable alternative to multiple inheritance
- create a core object, and then create a decorator wrapping that core
- we can chain the wrapping as the decorator object has the same interface as the core object
- **Core** and all the decorators implement a specific **Interface**
    - the dash lines show "implements" or "realizes"
- when called, the decorator does some added processing before or after calling its wrapped interface
- see how it looks using the UML diagram
![Decorator Pattern UML](resources/decorator_pattern.png)

## Defining function decorator

- we define higher order function that takes function as an argument to be decorated
- we can use wraps function decorator to wrap any function and return it
    - we don't have to but, it preserves the signature of the function being decorated



```python
from functools import wraps
from typing import Callable, Any
import sys

def log_args(function: Callable[..., Any]) -> Callable[..., Any]:
    
    @wraps(function)
    def wrapped_function(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {function.__name__}(*{args}, **{kwargs})", file=sys.stderr)
        #if len(args) == 3:
        kwargs['1'] = 1
        return function(*args, **kwargs)
        #return result
    
    return wrapped_function
```


```python
def test1(a: int, b: int, c:int, *args, **kwargs) -> float:
    return sum(range(a, b + 1)) / c
```


```python
test1 = log_args(test1)
```


```python
test1(1, 9, 2)
```


```python
test1(1, 9, c=2)
```


```python
# better option/syntax
@log_args
def test2(a: int, b: int, c:int, *args, **kwargs) -> float:
    return sum(range(a, b + 1)) / c
```


```python
test2(1, 9, 2)
```

### Defining class decorator

- in the following example; we have an original class Coffee
- MilkDecorator decorates Coffee by adding cost of milk
- similarly, Coffee can be wrapped with more decorators (e.g., SugarDecorator, WhippedCreamDecorator, etc.)
- this decorator pattern utilizes the **Open-Closed Principle (OCP) of SOLID** principles
    - making it easy to extend functionality without modifying the original class


```python
class Coffee:
    def cost(self):
        return 5
    

#Decorator class
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 2 # Add cost of mile
```


```python
# without using the decorator
black_coffee  = Coffee()
print("Black Coffee Cost:", black_coffee.cost())
```


```python
# using the decorator
milk_coffee = MilkDecorator(black_coffee)
print("Milk Coffee Cost:", milk_coffee.cost())
```


```python
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  # Add cost of sugar
```


```python
# Applying multiple decorators
coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(Coffee()))
print("Coffee with Milk and Sugar Cost:", coffee_with_milk_and_sugar.cost())
```


```python
# Useful class decorators example
# Generates demo.log when applied to a function
# __call__ overrides when the class is called like a function

from functools import wraps
from typing import Callable, Any
import logging
import time

class NamedLogger:
    # configure logger
    logging.basicConfig(filename="demo.log",
                format='{message}', style='{',
                filemode='w')
        
    def __init__(self, logger_name: str) -> None:
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        
    def __call__(
           self,
           function: Callable[..., Any]
    ) -> Callable[..., Any]:
        @wraps(function)
        def wrapped_function(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            try:
                result = function(*args, **kwargs)
                μs = (time.perf_counter() - start) * 1_000_000
                self.logger.info(
                    f"{function.__name__}(*{args}), {μs:.1f}μs")
                return result
            except Exception as ex:
                μs = (time.perf_counter() - start) * 1_000_000
                self.logger.error(
                    f"{ex}, {function.__name__}(*{args}), { μs:.1f}μs")
                raise
        return wrapped_function
```


```python
@NamedLogger("app_log")
def test4(median: float, sample: float) -> float:
    return sample - median
```


```python
test4(4, 10)
```


```python
@NamedLogger("app_log")
def add(a: float, b: float) -> float:
    return a+b
```


```python
add(106565656, 35435354354545454)
```




    35435354461111110




```python
! cat demo.log
```

    test4(*(4, 10)), 0.5μs
    test4(*(4, 10)), 0.7μs
    add(*(106565656, 35435354354545454)), 0.8μs



```python

```
