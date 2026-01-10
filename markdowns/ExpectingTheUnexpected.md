# Expecting the Unexpected

- programmers have to deal with three types of errors:
    1. Syntax Error
    2. Logical Error
    3. Run-time Error
    
- systems built with software can be fragile due to mostly run-time error
- while the software is highly predictable, the runtime context can provide unexpected inputs and situations
- **exceptions** - run-time error raised when a normal response is impossible

- learn:
    1. how to cause an exception to occur
    2. how to recover when an exception has occurred
    3. how to handle different exception types in different ways
    4. cleaning up when an exception has occurred
    5. creating new types of exception
    6. using the exception syntax for flow control

## Raising exceptions

- an exception is an object raised, that interrupts the sequential execution of statements
- all exceptions derive from *BaseException*
- let's see some exceptions by doing some silly stuff


```python
print("hello world")
```


      Cell In[10], line 1
        print(hello world")
                    ^
    SyntaxError: invalid syntax




```python
x = 5/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    Cell In[3], line 1
    ----> 1 x = 5/0


    ZeroDivisionError: division by zero



```python
lst = [1, 2, 3]
print(lst[3])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[4], line 2
          1 lst = [1, 2, 3]
    ----> 2 print(lst[3])


    IndexError: list index out of range



```python
lst.add
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[5], line 1
    ----> 1 lst.add


    AttributeError: 'list' object has no attribute 'add'



```python
lst + 10
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[6], line 1
    ----> 1 lst+10


    TypeError: can only concatenate list (not "int") to list



```python
d = {'a': 1}
```


```python
d['b']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[8], line 1
    ----> 1 d['b']


    KeyError: 'b'



```python
print(some_var)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[9], line 1
    ----> 1 print(some_var)


    NameError: name 'some_var' is not defined


## Explicitly raising an exception

- at times, you may have to raise exceptions in your code for some unexpected situation explictly
- we can use the same mechanism, that Python uses
- the following is a simple custom list class that adds an item to a list if it's an even-numbered integer


```python
from typing import List

class EvenOnly(List[int]):
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f'Not an integer: {value}')
        if value % 2 != 0:
            raise ValueError(f'Not an even integer: {value}')
        super().append(value)
    def insert(self, value: int) -> None:
        pass
```


```python
e = EvenOnly()
```


```python
type(e)
```




    __main__.EvenOnly




```python
e.append(4)
```


```python
e.append(5)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[15], line 1
    ----> 1 e.append(5)


    Cell In[11], line 8, in EvenOnly.append(self, value)
          6     raise TypeError(f'Not an integer: {value}')
          7 if value % 2 != 0:
    ----> 8     raise ValueError(f'Not an even integer: {value}')
          9 super().append(value)


    ValueError: Not an even integer: 5



```python
e.append('a string')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[16], line 1
    ----> 1 e.append('a string')


    Cell In[11], line 6, in EvenOnly.append(self, value)
          4 def append(self, value: int) -> None:
          5     if not isinstance(value, int):
    ----> 6         raise TypeError(f'Not an integer: {value}')
          7     if value % 2 != 0:
          8         raise ValueError(f'Not an even integer: {value}')


    TypeError: Not an integer: a string



```python
e.append(-10)
```


```python
print(e)
```

    [4, -10]



```python
# EvenOnly inherits all the methods from List
e.insert(0, 5)
```


```python
e
```




    [5, 4, -10]



- additional methods/behaviors need to be overriden to make EvenOnly more robust/complete in what it does
    - e.g., insert(), extend(), __setitem__(), __init__(), etc.

## The effects of an exception

- when an exception is raised, program halts at the line number
- the code after the problem statement will not be executed, unless the exception is handled by an exception clause


```python
from typing import NoReturn

def never_returns() -> NoReturn:
    print('Before exception is raised.')
    raise Exception('This is always raised.')
    print('This line will never be executed.')
    return "This will never be returned."
```


```python
never_returns()
```

    Before exception is raised.



    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    Cell In[23], line 1
    ----> 1 never_returns()


    Cell In[22], line 5, in never_returns()
          3 def never_returns() -> NoReturn:
          4     print('Before exception is raised.')
    ----> 5     raise Exception('This is always raised.')
          6     print('This line will never be executed.')
          7     return "This will never be returned."


    Exception: This is always raised.



```python
# called within the function
def call_exceptor() -> None:
    print('call_exceptor starts here...')
    never_returns()
    print('an exception was raised')
    print("...so these lines don't run")
```


```python
call_exceptor()
```

    call_exceptor starts here...
    Before exception is raised.



    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    Cell In[25], line 1
    ----> 1 call_exceptor()


    Cell In[24], line 4, in call_exceptor()
          2 def call_exceptor() -> None:
          3     print('call_exceptor starts here...')
    ----> 4     never_returns()
          5     print('an exception was raised')
          6     print("...so these lines don't run")


    Cell In[22], line 5, in never_returns()
          3 def never_returns() -> NoReturn:
          4     print('Before exception is raised.')
    ----> 5     raise Exception('This is always raised.')
          6     print('This line will never be executed.')
          7     return "This will never be returned."


    Exception: This is always raised.


## Handling exceptions

- use try and except blocks
- try statement has several separate clauses/parts
- can also handle multiple excetions within the same except block

```python

    try:
        # statement(s) thay may potentially raise an exception
    except ExceptionName1:
        # catch/handle specific exception ExceptionName1
        # statement(s) to handle the exception
    [except ExceptionName2 as err:
        # statements
    ]
    [except:
        # catch any error not caught by previous except blocks
    ]
    [else:
        # follows all except clause
        # executes if try clause does NOT raise an exception
    ]
    [finally:
        # clean-up actions that must be executed under all circumstances; 
        # exectued on the way out when try block is left via a break, continue, or return statement
    ]

```
- [ ... ] optional
- finally clause can be used for:
    - cleaning up an open database connection
    - closing an open file
    - sending a closing handshake over the network


```python
from typing import Union

def funnier_divison(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero."
```


```python
for val in (0, 'hello', 50.0, 3, 13):
    print(f'Testing {val!r:}', end=' ')
    print(funnier_divison(val))
```

    Testing 0 Enter a number other than zero.
    Testing 'hello' Enter a number other than zero.
    Testing 50.0 2.0
    Testing 3 33.333333333333336
    Testing 13 


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[27], line 3
          1 for val in (0, 'hello', 50.0, 3, 13):
          2     print(f'Testing {val!r:}', end=' ')
    ----> 3     print(funnier_divison(val))


    Cell In[26], line 6, in funnier_divison(divisor)
          4 try:
          5     if divisor == 13:
    ----> 6         raise ValueError("13 is an unlucky number")
          7     return 100 / divisor
          8 except (ZeroDivisionError, TypeError):


    ValueError: 13 is an unlucky number



```python
# excepting and re-raising the exception
def funniest_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError('13 is an unlucky number')
        return 100 / divisor
    except ZeroDivisionError as ex:
        return f'{ex}: Enter a number other than zero'
    except TypeError as ex:
        return f'{ex}: Enter a numerical value'
    except ValueError: 
        print('No, No, not 13!')
        raise # re-raise the ValueError
        
```


```python
# let's test funniest_division with some values
divisors = (10, 5, 0, 'hi', 13)
for divisor in divisors:
    print(f'funniest_division({divisor!r})=', funniest_division(divisor))
```

    funniest_division(10)= 10.0
    funniest_division(5)= 20.0
    funniest_division(0)= division by zero: Enter a number other than zero
    funniest_division('hi')= unsupported operand type(s) for /: 'int' and 'str': Enter a numerical value
    No, No, not 13!



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[29], line 4
          2 divisors = (10, 5, 0, 'hi', 13)
          3 for divisor in divisors:
    ----> 4     print(f'funniest_division({divisor!r})=', funniest_division(divisor))


    Cell In[28], line 5, in funniest_division(divisor)
          3 try:
          4     if divisor == 13:
    ----> 5         raise ValueError('13 is an unlucky number')
          6     return 100 / divisor
          7 except ZeroDivisionError as ex:


    ValueError: 13 is an unlucky number



```python
# example of finally and else clauses

some_exceptions = [ValueError, TypeError, IndexError, None]

for ex in some_exceptions:
    try:
        print(f'\nRaising {ex}')
        if ex:
            raise ex("An error")
        else:
            print('no exception raised')
    except ValueError:
        print('Caught a ValueError')
    except TypeError:
        print('Caught a TypeError')
    except Exception as e:
        print(f'Caught some other error: {e.__class__.__name__}')
    else:
        print('this code called if there is no exception')
    finally:
        print('this clean up code is always called')
```

    
    Raising <class 'ValueError'>
    Caught a ValueError
    this clean up code is always called
    
    Raising <class 'TypeError'>
    Caught a TypeError
    this clean up code is always called
    
    Raising <class 'IndexError'>
    Caught some other error: IndexError
    this clean up code is always called
    
    Raising None
    no exception raised
    this code called if there is no exception
    this clean up code is always called


## Exception hierarchy

- when we use `except: ` clause without specifying any type of exception, it'll catch all subclasses of BaseException
- always catch specific Exception type explictly
    - except: without type is an error and will flag it in code review by mypy
![Exception Hieararchy](resources/ExceptionHierarchy.png)

## Defining your Exception

- if the Python-provided built-in exception classes are not adequate, you can create your own
- create a sub-class that inherits from the Exception class


```python
class InvalidWithdrawl(ValueError):
    pass
```


```python
raise InvalidWithdrawl("You don't have $50 in your account")
```


    ---------------------------------------------------------------------------

    InvalidWithdrawl                          Traceback (most recent call last)

    Cell In[32], line 1
    ----> 1 raise InvalidWithdrawl("You don't have $50 in your account")


    InvalidWithdrawl: You don't have $50 in your account



```python
# more complete example
from decimal import Decimal

class InvalidWithdrawl(ValueError):
    def __init__(self, balance:Decimal, amount:Decimal) ->None:
        super().__init__(f"account doesn't have {amount} amount")
        self.amount = amount
        self.balance = balance
        
    # how overdrawn the withdraw request is  
    def overage(self) -> Decimal:
        return self.amount - self.balance
```


```python
raise InvalidWithdrawl(Decimal('25.00'), Decimal('50.00'))
```


    ---------------------------------------------------------------------------

    InvalidWithdrawl                          Traceback (most recent call last)

    Cell In[34], line 1
    ----> 1 raise InvalidWithdrawl(Decimal('25.00'), Decimal('50.00'))


    InvalidWithdrawl: account doesn't have 50.00 amount



```python
balance = Decimal('25.00')
```


```python
withdrawal = Decimal(input('Enter amount to withdraw: '))
if withdrawal > balance:
    raise InvalidWithdrawl(balance, withdrawal)
new_balance = balance - withdrawal
```


    ---------------------------------------------------------------------------

    InvalidWithdrawl                          Traceback (most recent call last)

    Cell In[38], line 3
          1 withdrawal = Decimal(input('Enter amount to withdraw: '))
          2 if withdrawal > balance:
    ----> 3     raise InvalidWithdrawl(balance, withdrawal)
          4 new_balance = balance - withdrawal


    InvalidWithdrawl: account doesn't have 30 amount



```python
new_balance
```




    Decimal('10.00')




```python
balance = Decimal('25.00')
try:
    withdraw = Decimal(input('Enter amount to withdraw: '))
    if withdraw > balance:
        raise InvalidWithdrawl(balance, withdraw)
except InvalidWithdrawl as ex:
    print("I'm sorry, but your withdrawl "
          " is more than your balance by "
         f'{ex.overage()}')
```

    I'm sorry, but your withdrawl  is more than your balance by 5.00


## When to raise Exceptions

- should you use `if` statements for checking unknowns or just execute code using try... except and see what happens?
- Python developers tend to follow the model: **EAFP**
    - **It's easier to ask for forgiveness than permission**
    - execute code then deal with anything that goes wrong
- less popular model: **LBYL**
    - **Look Before You Leap**
    - you're burning some CPU cycles looking for unusual situations that is not going to arise in the normal path through the code
- it is wise to use exceptions for exceptional circumstances, even if those circumstances are only a little bit exceptional
- e.g, the following two functions are identical!


```python
def divide_with_exception(dividend: int, divisor: int) -> None:
    try:
        print(f'{dividend/divisor=}')
    except ZeroDivisionError:
        print("You can't divide by zero")

def divide_with_if(dividend: int, divisor: int) -> None:
    if divisor == 0:
        print("You can't divide by zero")
    else:
        print(f"{dividend/divisor=}")
```


```python
divide_with_exception(10, 0)
```

    You can't divide by zero



```python
divide_with_if(10, 0)
```

    You can't divide by zero


## Exercises

- Solve the following Kattis Problems using OOD
- Must write atleast one Exception class and use it to solve the problem using OOP

1. A New Alphabet - https://open.kattis.com/problems/anewalphabet
2. Babelfish - https://open.kattis.com/problems/babelfish


```python

```
