# Iterator Pattern

- Topics
    - what design patterns are
    - the iterator protocol
    - list, set, and dictionary comprehensions
    - generator functions, and how they build on other patterns

## Design patterns

- great resource on Refactoring, Design Patterns and Clean code - https://refactoring.guru/
- design patterns are a formalized way of describing a solution to a problem
- the analogy: engineers and architects designing to build bridges, towers, buildings, and physical structures
    - they follow certain principles to ensure structural integrity
- design patterns are an attempt to bring this formal definition to software engineering
- design patterns are applied to solve a common problem faced by developers in some specific situations
    - a suggestion as to the ideal solution for a problem, in terms of OOD
- central to a pattern is that it is reused often in unique contexts
    - one clever solution is a good idea
    - two similar solutions might be a coincidence
    - three or more reuses of an idea start to look like a repeating pattern
- knowing design patterns and choosing to use them in our software doesn't guarantee a *correct* solution
    - in 1907, the Quebec Bridge collapsed before construction was completed
   
## Iterators

- one of the most powerful design patterns
- for loop (the foundational concept) is a lightweight wrapper around a set of object-oriented principles
- conceptually, **iterator** is an object with a `next()` and a `done()` methods
- the general idea of iterators without using iterators but using loop is as follows:

```python
while not iterator.done():
    item = iterator.next()
    # do something with the item
```

- iterators are objects with `__next__()` method that is called using `next(iterator)` built-in
- raises `StopIteration` exception to notify the client that the iterator has completed

## Iterator protocol

- `Iterator` abstract base class, in the `collections.abc` module, defines the *iterator* protocol
- the following diagram depicts the hierarchy of iterator protocol:
![Iterator Protocol](resources/iterator_abstraction.png)


```python
print(range(20))
```

    range(0, 20)



```python
help(range)
```

    Help on class range in module builtins:
    
    class range(object)
     |  range(stop) -> range object
     |  range(start, stop[, step]) -> range object
     |  
     |  Return an object that produces a sequence of integers from start (inclusive)
     |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
     |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
     |  These are exactly the valid indices for a list of 4 elements.
     |  When step is given, it specifies the increment (or decrement).
     |  
     |  Methods defined here:
     |  
     |  __bool__(self, /)
     |      True if self else False
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(...)
     |      Return a reverse iterator.
     |  
     |  count(...)
     |      rangeobject.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      rangeobject.index(value) -> integer -- return index of value.
     |      Raise ValueError if the value is not present.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  start
     |  
     |  step
     |  
     |  stop
    



```python
for i in range(1, 20, 2):
    print(i)
```

    1
    3
    5
    7
    9
    11
    13
    15
    17
    19



```python
10 in range(1, 20, 1)
```




    True




```python
# example of how an iterable is implemented in a detailed and verbose way...
from typing import Iterable, Iterator

# create an Iterable class that we can iterate over
class CapitalIterable(Iterable[str]):
    def __init__(self, string: str) -> None:
        self.string = string
        
    def __iter__(self) -> Iterator[str]:
        return CapitalIterator(self.string)
```


```python
class CapitalIterator(Iterator[str]):
    def __init__(self, string: str) -> None:
        # for char of each word is capitalized
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0
        
    def __next__(self) -> str:
        if self.index == len(self.words):
            raise StopIteration()
        
        word = self.words[self.index]
        self.index += 1
        return word
```


```python
iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
```


```python
help(iter)
```

    Help on built-in function iter in module builtins:
    
    iter(...)
        iter(iterable) -> iterator
        iter(callable, sentinel) -> iterator
        
        Get an iterator from an object.  In the first form, the argument must
        supply its own iterator, or be a sequence.
        In the second form, the callable is called until it returns the sentinel.
    



```python
iterator = iter(iterable)
```


```python
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
```

    The
    Quick
    Brown
    Fox
    Jumps
    Over
    The
    Lazy
    Dog



```python
# Behind the scene, for loop uses iterator OOD pattern
for word in iterable:
    print(word)
```

    The
    Quick
    Brown
    Fox
    Jumps
    Over
    The
    Lazy
    Dog


## Comprehensions

- recall comprehension syntaxes from the Python Data Structures chapter
- comprehensions are simple but powerful, syntaxes that allow us to transform or filter an iterable object
- the result can be a list, set, dictionary, or a *generator expression*

### List comprehension

- one of the most powerful and fundamental tools in Python
- can be very useful in solving a lot of real-world software applications as well as Kattis problems


```python
numbers = input('Enter some integers separated by space: ')
```


```python
numbers
```




    '1 00 45 565 7676'




```python
lst_numbers = numbers.split()
```


```python
lst_numbers
```




    ['1', '00', '45', '565', '7676']




```python
lst_integers = [int(num) for num in lst_numbers]
```


```python
lst_integers
```




    [1, 0, 45, 565, 7676]




```python
map_obj = map(str, lst_integers)
```


```python
print(map_obj)
```

    <map object at 0x7fd3aae86440>



```python
for n in map_obj:
    print(f'{n}')
```

    1
    0
    45
    565
    7676



```python
# another technique using map generators
integers = list(map(int, lst_numbers))
```


```python
integers
```




    [1, 0, 45, 565, 7676]



## Generator expressions

- sometimes we want to process a large sequence without creating a new list, set, or dictionary data structures in memory
    - having all the contents in some data structure in memory may not be needed
    - it can be CPU and memory-intensive
- e.g., processing a large log file and looking for specific information
    - finding max, min, range, average, etc. of a large list of numbers
- generator expressions use the same syntax as comprehension, but they don't create a final container object
    - called **lazy** evaluation; reluctantly produce values on demand
- to create a generator expression, warp the comprehension in `( )` INSTEAD of `[ ]` or `{ }`
- wrapping a generator in `{ }` creates a set
- warpping a generator in `{ : }` creates a dict
- warpping a generator in `[ ]` creates a list
- wrapping a generator in `( )` creates a generator expression NOT a tuple


```python
numbers = ['1', '10', '5', '5', '11', '1']
```


```python
# try using the list as a generator
next(numbers)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[2], line 2
          1 # try using the list as a generator
    ----> 2 next(numbers)


    TypeError: 'list' object is not an iterator



```python
# Create a set of ints from the list of string ints
set_ints = {int(n) for n in numbers}
```


```python
set_ints
```




    {1, 5, 10, 11}




```python
set_ints1 = set(numbers)
```


```python
set_ints1
```




    {'1', '10', '11', '5'}




```python
# Converting a list into a dictionary
# create a dictionary using the index as the key and value as the value
some_dict = {i: v for i, v in enumerate(numbers)}
```


```python
some_dict
```




    {0: '1', 1: '10', 2: '5', 3: '5', 4: '11', 5: '1'}




```python
# Creating a generator expression from a list of numbers
int_gen = (int(n) for n in numbers)
```


```python
int_gen
```




    <generator object <genexpr> at 0x7f88d6bae9d0>




```python
# let's get the next integer
next(int_gen)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    Cell In[17], line 2
          1 # let's get the next integer
    ----> 2 next(int_gen)


    StopIteration: 



```python
for n in int_gen:
    print(n, n**2)
```

    1 1
    10 100
    5 25
    5 25
    11 121
    1 1



```python
# let's look at a more useful example
from pathlib import Path
```


```python
# there's a file in the data directory called system.log
# let's read it in using a generator expression
! cat data/system.log
```

    Apr 05, 2021 20:03:29 DEBUG This is a debugging message.
    Apr 05, 2021 20:03:41 INFO This is an information method.
    Apr 05, 2021 20:03:53 WARNING This is a warning. It could be serious.
    Apr 05, 2021 20:03:59 WARNING Another warning sent.
    Apr 05, 2021 20:04:05 INFO Here's some information.
    Apr 05, 2021 20:04:17 DEBUG Debug messages are only useful if you want
    to figure something out.
    Apr 05, 2021 20:04:29 INFO Information is usually harmless, but
    helpful.
    Apr 05, 2021 20:04:35 WARNING Warnings should be heeded.
    Apr 05, 2021 20:04:41 WARNING Watch for warnings.



```python
from pathlib import Path
```


```python
full_log_path = Path.cwd() / "data" / "system.log"
```


```python
Path.cwd()
```




    PosixPath('/Users/rbasnet/projects/Object-Oriented-Programming-Design-Patterns/notebooks')




```python
# create a log file containing power keyword
warn_log_path = Path.cwd() / "data" / "warn.log"
```


```python
full_log_path
```




    PosixPath('/Users/rbasnet/projects/Object-Oriented-Programming-Design-Patterns/notebooks/data/system.log')




```python
with full_log_path.open() as source:
    # create a generator expression that will yield lines from the log file
    # that contain the word 'WARN'
    power_lines = (line for line in source if 'WARN' in line)
    with warn_log_path.open('w') as target:
        # iterate over the lines to write each line to the new file
        for line in power_lines:
            target.write(line)
```


```python
! cat data/warn.log
```

    Apr 05, 2021 20:03:53 WARNING This is a warning. It could be serious.
    Apr 05, 2021 20:03:59 WARNING Another warning sent.
    Apr 05, 2021 20:04:35 WARNING Warnings should be heeded.
    Apr 05, 2021 20:04:41 WARNING Watch for warnings.


## Generator functions

- generator functions embody the essential features of a generator expression
    -  which is the generalization of comprehension
- special functions that return an iterator which returns a stream of values
- resumable functions that can retain local variable information to resume the function where it left off
- uses `yield` keyword to yield the next value as opposed to `return`
    - when `yield` is executed, the generator's state of execution is suspended and local variables are preserved
- `next(genObject)` calls the built_in `__next__()` method to resume executing, when the function is called again
- similar in concept to `range()`, however, `range class` is not an iterator
    - `range` doesn't implement `__next__()`


```python
help(range)
```

    Help on class range in module builtins:
    
    class range(object)
     |  range(stop) -> range object
     |  range(start, stop[, step]) -> range object
     |  
     |  Return an object that produces a sequence of integers from start (inclusive)
     |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
     |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
     |  These are exactly the valid indices for a list of 4 elements.
     |  When step is given, it specifies the increment (or decrement).
     |  
     |  Methods defined here:
     |  
     |  __bool__(self, /)
     |      True if self else False
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(...)
     |      Return a reverse iterator.
     |  
     |  count(...)
     |      rangeobject.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      rangeobject.index(value) -> integer -- return index of value.
     |      Raise ValueError if the value is not present.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  start
     |  
     |  step
     |  
     |  stop
    



```python
r = range(10, 100)
```


```python
# Not an iterator!
next(r)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[31], line 2
          1 # Not an iterator!
    ----> 2 next(r)


    TypeError: 'range' object is not an iterator



```python
len(r)
```




    90




```python
50 in r
```




    True




```python
# let's create my_range by making range a generator
def my_range(N):
    for i in range(N):
        yield i # This makes the function a generator/iterator!
```


```python
gen = my_range(10)
```


```python
print(gen)
```

    <generator object my_range at 0x7f88d6d6a490>



```python
next(gen)
```




    0




```python
next(gen)
```




    1




```python
# iterate over the next of the values
for n in gen:
    print(n)
```

    2
    3
    4
    5
    6
    7
    8
    9



```python
# you can convert range to an iterator using built-in iter function
my_r = iter(range(20))
```


```python
next(my_r)
```




    0




```python
# function reads full_log_path and writes all the WARNING logs to warning_log_path
# function does NOT user iterator/generator pattern
import csv
import re
from pathlib import Path

from typing import Match, cast

# regular function without an iterator
def extract_and_parse(
        full_log_path: Path, warning_log_path: Path
        ) -> None:
    with warning_log_path.open("w") as target:
        writer = csv.writer(target, delimiter="\t")
        pattern = re.compile(
            # Apr 05, 2021 20:04:41
            r"(\w\w\w \d\d, \d\d\d\d \d\d:\d\d:\d\d) (\w+) (.*)")
        with full_log_path.open() as source:
            for line in source:
                if "WARN" in line:
                    line_groups = cast(Match[str], pattern.match(line)).groups()
                    writer.writerow(line_groups)
                    
```


```python
# create a log file containing WARNING keyword
warn1_log_path = Path.cwd() / "data" / "warn1.log"
```


```python
extract_and_parse(full_log_path, warn1_log_path)
```


```python
! cat data/warn1.log
```

    Apr 05, 2021 20:03:53	WARNING	This is a warning. It could be serious.
    Apr 05, 2021 20:03:59	WARNING	Another warning sent.
    Apr 05, 2021 20:04:35	WARNING	Warnings should be heeded.
    Apr 05, 2021 20:04:41	WARNING	Watch for warnings.



```python
from typing import Iterable, Sequence, Iterator

# generator function
def warnings_filter(source: Iterable[str]) -> Iterator[Sequence[str]]:
    pattern = re.compile(
        r"(\w\w\w \d\d, \d\d\d\d \d\d:\d\d:\d\d) (\w+) (.*)")
    for line in source:
        if match := pattern.match(line):
            if "WARN" in match.group(2):
                yield match.groups()
```


```python
for t in warnings_filter(full_log_path.open()):
    print(t)
```

    ('Apr 05, 2021 20:03:53', 'WARNING', 'This is a warning. It could be serious.')
    ('Apr 05, 2021 20:03:59', 'WARNING', 'Another warning sent.')
    ('Apr 05, 2021 20:04:35', 'WARNING', 'Warnings should be heeded.')
    ('Apr 05, 2021 20:04:41', 'WARNING', 'Watch for warnings.')



```python
# The same can be achieved by comprehension short-cut
# generator expression
source = full_log_path.open()
pattern = re.compile(
        r"(\w\w\w \d\d, \d\d\d\d \d\d:\d\d:\d\d) (\w+) (.*)")
warnings_filter_gen = (
    tuple(cast(Match[str], pattern.match(line)).groups())
    for line in source
    if "WARN" in line
)
```


```python
next(warnings_filter_gen)
```




    ('Apr 05, 2021 20:03:53', 'WARNING', 'This is a warning. It could be serious.')




```python
next(warnings_filter_gen)
```




    ('Apr 05, 2021 20:03:59', 'WARNING', 'Another warning sent.')




```python
for t in warnings_filter_gen:
    print(t)
```

    ('Apr 05, 2021 20:03:53', 'WARNING', 'This is a warning. It could be serious.')
    ('Apr 05, 2021 20:03:59', 'WARNING', 'Another warning sent.')
    ('Apr 05, 2021 20:04:35', 'WARNING', 'Warnings should be heeded.')
    ('Apr 05, 2021 20:04:41', 'WARNING', 'Watch for warnings.')



```python
# Creating our own iterator/generator  my_range
class my_range:
    def __init__(self, end):
        self.start = 0
        self.end = end

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration()
        val = self.start
        self.start += 1
        return val
```


```python
r = my_range(10)
```


```python
next(r)
```




    2




```python
# however my_range is not iterable to be used in the for loop!
for val in r:
    print(val)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[58], line 2
          1 # however my_range is not iterable to be used in the for loop!
    ----> 2 for val in r:
          3     print(val)


    TypeError: 'my_range' object is not iterable



```python
# Creating our own iterator/generator  my_range
class my_range_iter:
    def __init__(self, end):
        self.start = 0
        self.end = end

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration()
        val = self.start
        self.start += 1
        return val

    def __iter__(self):
        return self
```


```python
for val in my_range_iter(10):
    print(val)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python

```
