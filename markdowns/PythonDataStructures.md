# Python Data Structures

- discuss the object-oriented features of some commonly used Python built-in data structures
- learn when they should be used instead of a regular class and when they shouldn't:
    - Tuples and Named Tuples
    - Dataclasses
    - Dictionaries
    - Lists and Sets
    - Three types of queues
    
## Empty objects

- every class we've created, we implicitly used `object` class
- instantiating an object class is useless
    - can't add attributes dynamically


```python
o = object()
```


```python
help(o)
```

    Help on object object:
    
    class object
     |  The base class of the class hierarchy.
     |  
     |  When called, it accepts no arguments and returns a new featureless
     |  instance that has no instance attributes and cannot be given any.
     |  
     |  Built-in subclasses:
     |      anext_awaitable
     |      async_generator
     |      async_generator_asend
     |      async_generator_athrow
     |      ... and 88 other subclasses
     |  
     |  Methods defined here:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __dir__(self, /)
     |      Default dir() implementation.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __format__(self, format_spec, /)
     |      Default object formatter.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __reduce__(self, /)
     |      Helper for pickle.
     |  
     |  __reduce_ex__(self, protocol, /)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __sizeof__(self, /)
     |      Size of object in memory, in bytes.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  __init_subclass__(...) from builtins.type
     |      This method is called when a class is subclassed.
     |      
     |      The default implementation does nothing. It may be
     |      overridden to extend subclasses.
     |  
     |  __subclasshook__(...) from builtins.type
     |      Abstract classes can override this to customize issubclass().
     |      
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __class__ = <class 'type'>
     |      type(object) -> the object's type
     |      type(name, bases, dict, **kwds) -> a new type
    



```python
o.x = 5
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[10], line 1
    ----> 1 o.x = 5


    AttributeError: 'object' object has no attribute 'x'



```python
class MyClass(object):
    pass
```


```python
m = MyClass()
m.x = "hello"
```


```python
m.x
```




    'hello'



## Tuples and named tuples

- tuples are objects that can store a specific number of other objects in sequence
- tuples are *immutable*
    - can't modify - add, remove, or replace members on the fly
- tuples are hashable which makes them candidates for keys in dictionaries and members in sets
- tuples overlap with the idea of coordinates or dimensions
    - e.g., (x, y) pair or (r, g, b) color
    - order matters


```python
# ticker, the current price, the 52-week high, and the 52-week low
stock = "AAPL", 123.52, 53.15, 137.98
```


```python
stock2 = ("AAPL", 123.52, 53.15, 137.98)
```


```python
import datetime

def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)
```


```python
middle(("AAPL", 123.52, 53.15, 137.98), datetime.date(2020, 12, 4))
```




    (95.565, datetime.date(2020, 12, 4))




```python
# single value tuple; must add a trailing ,
a = (42,)
```


```python
a
```




    (42,)




```python
# no trailing , required for two or more values 
nums = (1, 2, 3,)
```


```python
nums
```




    (1, 2, 3)




```python
a, b, c = nums
```


```python
a, c
```




    (1, 3)




```python
a, b, c = nums[0], nums[1], nums[2]
```


```python
a, b, c
```




    (1, 2, 3)



## Named tuple via typing.NamedTuple

- named tuples are tuples with attributes
- a great way to create an immutable grouping of values
- can be thought of as similar to `C struct` but with immutable read-only attributes
- we don't need `__init__` method, it's created for us
- names are created at the class level, but we're not creating class-level attributes


```python
from typing import NamedTuple

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float
```


```python
help(Stock)
```

    Help on class Stock in module __main__:
    
    class Stock(builtins.tuple)
     |  Stock(symbol: str, current: float, high: float, low: float)
     |  
     |  Stock(symbol, current, high, low)
     |  
     |  Method resolution order:
     |      Stock
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getnewargs__(self)
     |      Return self as a plain tuple.  Used by copy and pickle.
     |  
     |  __repr__(self)
     |      Return a nicely formatted representation string
     |  
     |  _asdict(self)
     |      Return a new dict which maps field names to their values.
     |  
     |  _replace(self, /, **kwds)
     |      Return a new Stock object replacing specified fields with new values
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  _make(iterable) from builtins.type
     |      Make a new Stock object from a sequence or iterable
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(_cls, symbol: str, current: float, high: float, low: float)
     |      Create new instance of Stock(symbol, current, high, low)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  symbol
     |      Alias for field number 0
     |  
     |  current
     |      Alias for field number 1
     |  
     |  high
     |      Alias for field number 2
     |  
     |  low
     |      Alias for field number 3
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __annotations__ = {'current': <class 'float'>, 'high': <class 'float'>...
     |  
     |  __match_args__ = ('symbol', 'current', 'high', 'low')
     |  
     |  __orig_bases__ = (<function NamedTuple>,)
     |  
     |  _field_defaults = {}
     |  
     |  _fields = ('symbol', 'current', 'high', 'low')
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
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
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from builtins.tuple:
     |  
     |  __class_getitem__(...) from builtins.type
     |      See PEP 585
    



```python
s2 = Stock("AAPL", 123.52, high=137.98, low=53.15)
```


```python
s2.high
```




    137.98




```python
s2.symbol
```




    'AAPL'




```python
s2.current = 100
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[37], line 1
    ----> 1 s2.current = 100


    AttributeError: can't set attribute



```python
# tuple can contain mutable types
t = ("Relayer", ["Gates of Delirium", "Sound Chaser"])
```


```python
t[1].append('To Be Over')
```


```python
t
```




    ('Relayer', ['Gates of Delirium', 'Sound Chaser', 'To Be Over'])




```python
hash(t)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[41], line 1
    ----> 1 hash(t)


    TypeError: unhashable type: 'list'



```python
hash(s2)
```




    5097746135868899230




```python
# NamedTuple with property
from typing import NamedTuple

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float
    
    @property
    def middle(self) -> float:
        return (self.high + self.low)/2
```


```python
stoc = Stock('APPL', 10, 300, 200)
```


```python
stoc.middle
```




    250.0



## Dataclasses

- since Python 3.7, dataclass class decorator let us define ordinary objects
  - provides a clean syntax for specifying attributes
- similar to `C struct` where attributes are mutable
- let's create a `dataclass` similar to Stock class above


```python
from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    current: float
    high: float
    low: float
```


```python
help(Stock)
```

    Help on class Stock in module __main__:
    
    class Stock(builtins.object)
     |  Stock(symbol: str, current: float, high: float, low: float) -> None
     |  
     |  Stock(symbol: str, current: float, high: float, low: float)
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __init__(self, symbol: str, current: float, high: float, low: float) -> None
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __annotations__ = {'current': <class 'float'>, 'high': <class 'float'>...
     |  
     |  __dataclass_fields__ = {'current': Field(name='current',type=<class 'f...
     |  
     |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
     |  
     |  __hash__ = None
     |  
     |  __match_args__ = ('symbol', 'current', 'high', 'low')
    



```python
s = Stock("AAPL", 123.52, 137.98, 53.15)
```


```python
s.current
```




    123.52




```python
s.current = 145.99
```


```python
s.unexpected_attribute = 'allowed'
```


```python
s.unexpected_attribute
```




    'allowed'




```python
class StockOrdinary:
    def __init__(self, 
                 name: str, 
                 current: float, 
                 high: float, 
                 low: float) -> None:
        
        self.name = name
        self.current = current
        self.high = high
        self.low = low
```


```python
s_ord = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
```


```python
s_ord_2 = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
```


```python
# can't compare two objects of regular Stock class
s_ord == s_ord_2
```




    False




```python
stock2 = Stock(symbol='AAPL', current=122.25, high=137.98, low=53.15)
```


```python
stock1 = Stock(symbol='AAPL', current=122.25, high=137.98, low=53.15)
```


```python
# dataclass stocks support comparison out of the box
stock1 == stock2
```




    True




```python
# dataclass also let's you initialize attributes
from dataclasses import dataclass

@dataclass
class StockDefaults:
    name: str
    current: float = 0
    high: float = 0
    low: float = 0
```


```python
# default values are used
s1 = StockDefaults('GOOG')
```


```python
s1
```




    StockDefaults(name='GOOG', current=0, high=0, low=0)




```python
# can still provide values for attributes
StockDefaults("GOOG", 1826.77, 1847.20, 1013.54)
```




    StockDefaults(name='GOOG', current=1826.77, high=1847.2, low=1013.54)




```python
# equal comparison is provided by default; we can also order the objects if needed
@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0
    high: float = 0
    low: float = 0
```


```python
stock_ordered1 = StockOrdered("GOOG", 1826.77, 1847.20, 1013.54)
stock_ordered2 = StockOrdered("GOOG")
stock_ordered3 = StockOrdered("GOOG", 1728.28, high=1733.18, low=1666.33)
```


```python
# stock_ordeered2 has default 0s for all other attributes
stock_ordered1 < stock_ordered2
```




    False




```python
stock_ordered1 > stock_ordered2
```




    True




```python
from pprint import pprint
```


```python
# let's print the sorted order of three stock objects
pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))
```

    [StockOrdered(name='GOOG', current=0, high=0, low=0),
     StockOrdered(name='GOOG', current=1728.28, high=1733.18, low=1666.33),
     StockOrdered(name='GOOG', current=1826.77, high=1847.2, low=1013.54)]



```python
# create a frozen class similar to typing.NamedTuple
@dataclass(frozen=True, order=True)
class StockFrozen:
    name: str
    current: float = 0
    high: float = 0
    low: float = 0
```


```python
goog = StockFrozen("GOOG")
```


```python
goog.high
```




    0




```python
# can't updates attributes of Frozen instance
goog.high = 100
```


    ---------------------------------------------------------------------------

    FrozenInstanceError                       Traceback (most recent call last)

    Cell In[74], line 2
          1 # can't updates attributes of Frozen instance
    ----> 2 goog.high = 100


    File <string>:4, in __setattr__(self, name, value)


    FrozenInstanceError: cannot assign to field 'high'


## Dictionary

- a super useful data structure that allows us to map objects directly to other objects
- extremely efficient at looking up a **value**, given a specific **key** that maps to a value
- this is possible due to the use of the **hash** of the key to locate the value
- every immutable Python object has a numeric hash code 
    - a relatively simple table is used to map the numeric hashes directly to values
- Python class/objects are mutable; but if they are **hashable** can be used as key
    - provide `__hash__()` that is used by built-in **hash** function when hashing
- the order of the key/value inserted is maintained by the dictionary class from Python 3.7
- for two values (strings, numbers, tuples, etc.) to be equal, they must have the same characters or values, and their **hash** values must also be equal
- **hash** collision can occur, so the look-up may be **not always** efficient (`O(1)`)
    - **hash** collision can slow down the insert and lookup process
- there are several ways to create a dictionary


```python
help(hash)
```

    Help on built-in function hash in module builtins:
    
    hash(obj, /)
        Return the hash value for the given object.
        
        Two objects that compare equal must also have the same hash value, but the
        reverse is not necessarily true.
    



```python
hash('abc')
```




    -5637168351579206829




```python
hash(123)
```




    123




```python
hash(('a', 'b', 'c'))
```




    -6442756086383675623




```python
hash([1, 2, 3])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[79], line 1
    ----> 1 hash([1, 2, 3])


    TypeError: unhashable type: 'list'



```python
# Hash collision example!
x = 2021
y = 2305843009213695972
```


```python
hash(x)
```




    2021




```python
hash(y)
```




    2021




```python
hash(x) == hash(y)
```




    True




```python
# using keyword parameters; similar to dataclass and NamedTuple
stock = dict(current=1235.20, high=1242.54, low=1231.06)
```


```python
stock
```




    {'current': 1235.2, 'high': 1242.54, 'low': 1231.06}




```python
stocks = {
    "GOOG": (1235.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84) 
}
```


```python
stocks
```




    {'GOOG': (1235.2, 1242.54, 1231.06), 'MSFT': (110.41, 110.45, 109.84)}




```python
# accessing value
stocks["GOOG"]
```




    (1235.2, 1242.54, 1231.06)




```python
stocks['APPL']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[89], line 1
    ----> 1 stocks['APPL']


    KeyError: 'APPL'



```python
# better approach
print(stocks.get('APPL'))
```

    None



```python
# provide default value
print(stocks.get('APPL', 'NOT FOUND'))
```

    NOT FOUND



```python
# updating existing key/value pairs
stocks['GOOG'] = (100, 100, 100)
```


```python
stocks.get("GOOG")
```




    (100, 100, 100)




```python
# adding new key/value iff the key doesn't exist
# if key is in the dictionary, it behaves just like get
stocks.setdefault("GOOG", "INVALID")
```




    (100, 100, 100)




```python
stocks.setdefault("BB", (10.87, 10.76, 11.90))
```




    (10.87, 10.76, 11.9)




```python
stocks['BB']
```




    (10.87, 10.76, 11.9)




```python
# mypy type hints; can use built-in types as type hints from Python 3.9 and mypy 0.812
# need: from __future__ import annotations as the first import 
# for older version of Python and mypy
#from typing import Tuple

stocks: dict[str, tuple[float, float, float]] = {}
```


```python
stocks.setdefault('APPL', (150, 175, 125))
```




    (150, 175, 125)




```python
stocks
```




    {'APPL': (150, 175, 125)}




```python
for stock, values in stocks.items():
    print(f"{stock} last value is {values[0]}")
```

    APPL last value is 150



```python
# using objects as key
class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue
        
    def __repr__(self):
        return f'AnObject: {self.avalue}'
```


```python
random_keys = {}
```


```python
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"
```


```python
random_keys
```




    {'astring': 'somestring',
     5: 'aninteger',
     25.2: 'floats work too',
     ('abc', 123): 'so do tuples'}




```python
my_object = AnObject(14)
```


```python
random_keys[my_object] = "We can even store objects"
```


```python
random_keys
```




    {'astring': 'somestring',
     5: 'aninteger',
     25.2: 'floats work too',
     ('abc', 123): 'so do tuples',
     AnObject: 14: 'We can even store objects'}




```python
# change of my_objects doesn't affect the dictionary; Key changes if __repr__() changed!
my_object.avalue = 100
```


```python
# random_keys has type hints: dict[Union[str, int, float, Tuple[str, int], AnObject], str]
for key in random_keys:
    print(f"{key!r} has value {random_keys[key]!r}")
```

    'astring' has value 'somestring'
    5 has value 'aninteger'
    25.2 has value 'floats work too'
    ('abc', 123) has value 'so do tuples'
    AnObject: 100 has value 'We can even store objects'


## Dictionary use cases

- dictionaries are extremely versatile and have numerous uses
- a couple of important ones:
    1. dict[str, tuple[float, float, float]] or dict[str, Stock]
        - similar to the stock example where the symbol maps to a tuple of prices
    2. dict[str, Union[str, float, Tuple[float, float]]
        - e.g., {'name': 'GOOG', 'current': 1245.21, 'range': (1252.64, 1245.18)}
        - this case overlaps with named tuples, dataclass, and objects in general
        
- technically, most classes are implemented using a dictionary


```python
# let's look into my_object
help(my_object)
```

    Help on AnObject in module __main__ object:
    
    class AnObject(builtins.object)
     |  AnObject(avalue)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, avalue)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    



```python
my_object.__dict__
```




    {'avalue': 100}




```python
my_object.__dict__['avalue']
```




    100




```python
my_object.avalue
```

## Using defaultdict

- we've used `setdefault` method to set the default value if the key doesn't exist in `dict` instance
- this can get monotonous/expensive to check or `setdefault` value every time a new key is inserted or an existing key is updated
- e.g. let's find letter frequencies using a regular dictionary


```python
def letter_frequency(sentence: str) -> dict[str, int]:
    frequencies: dict[str, int] = {} # regular dictionary
    for letter in sentence:
        frequencies.setdefault(letter, 0)  # step 1
        frequencies[letter] += 1 # step 2
    return frequencies
```


```python
hist = letter_frequency("Mississippi river is the longest river in Mississippi")
```


```python
hist
```




    {'M': 2,
     'i': 12,
     's': 10,
     'p': 4,
     ' ': 7,
     'r': 4,
     'v': 2,
     'e': 4,
     't': 2,
     'h': 1,
     'l': 1,
     'o': 1,
     'n': 2,
     'g': 1}




```python
from collections import defaultdict

def letter_frequency_2(sentence: str) -> defaultdict[str, int]:
    frequencies: defaultdict[str, int] = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1 # one step !!
    return frequencies
```


```python
hist1 = hist = letter_frequency("Mississippi river is the longest river in Mississippi")
```


```python
hist1
```


```python
# int() function returns 0
int()
```




    0




```python
# we can pass a whole bunch of built-in and user 
# defined functions to initilize the new key with!
str()
```




    ''




```python
float()
```




    0.0




```python
list()
```




    []




```python
dict()
```




    {}




```python
# initializing distance dict in Diajkstra's SSSP algorithm
# dist[(u, v)] = infinity
import math
dist: defaultdict[tuple[int, int], int] = defaultdict(lambda: math.inf)
```


```python
dist[(1, 2)]
```




    inf




```python
if dist[(1, 2)] > 100:
    dist[(1, 2)] = 1+2
```


```python
dist[(1, 2)]
```




    3




```python
# we can create our own functions and dataclass with default values
# to pass as a default function for defaultdict
from dataclasses import dataclass

@dataclass
class Price:
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0
```


```python
Price()
```


```python
portfolio = defaultdict(Price)
```


```python
portfolio['GOOG']
```


```python
portfolio
```


```python
portfolio["AAPL"] = Price(current=122.25, high=137.98, low=53.15)
```


```python
from pprint import pprint
```


```python
pprint(portfolio)
```


```python
# jupyter notebook uses pprint to print values of variables/objects
portfolio
```


```python
# what if we wanted prices for stocks grouped by month
# dictionary within dictionary by month!
# within inner dictionary we want Price

def make_defaultdict():
    return defaultdict(Price)
```


```python
by_month = defaultdict(make_defaultdict)
```


```python
by_month["APPL"]["Jan"] = Price(current=122.25, high=137.98, low=53.15)
```


```python
by_month
```


```python
by_month['APPL']
```


```python
by_month['APPL']['Jan']
```


```python
# shortcut is to use lambda function
by_month1 = defaultdict(lambda: defaultdict(Price))
```


```python
by_month1["APPL"]["Jan"] = Price(current=122.25, high=137.98, low=53.15)
```


```python
by_month1
```

## Counter

- counting is a very important task developers do:
    - *I want to count specific instances in an iterable* use case is so common that Python developers thought it deserved a special built-in data structure!


```python
from collections import Counter
```


```python
freq = Counter("Mississippi river is the longest river in Mississippi")
```


```python
freq.most_common()
```


```python
freq.most_common(5)
```


```python
help(Counter)
```

## Lists

- generic `list` structure is integrated 
- list should be used to store several instances of the same type of objects
    - however, Python list can store any type of objects
- lists also maintain the order of the elements
- lists are mutable
- don't use the `list` for collecting different attributes of the same object
    - tuple, namedtuple, dataclass, and dictionary may be better
- some example of list: list[str], list[int], list[tuple], list[float], etc.


```python
numbers = list(range(20, -1, -1))
```


```python
numbers
```


```python
nums = [2, 4, 6, 8]
```


```python
nums.append(10)
```


```python
help(nums)
```


```python
nums.reverse()
```


```python
nums
```


```python
numbers.sort()
```


```python
numbers
```

### Sorting lists

- see this article on Python sorting algorithms: [https://realpython.com/sorting-algorithms-python/](https://realpython.com/sorting-algorithms-python/)
- an important task in working with lists is to sort them!
- sorting is a popular topic studied in algorithm class
    - many sorting algorithms with different running times!
- Python uses the `Timsort` algorithm created by Tim Peters 
- `Timsort` algorithm is considered a hybrid sorting algorithm
    - employs the best-of-both-worlds combination of insertion sort and merge sort


```python
numbers.sort(reverse=True)
```


```python
numbers
```


```python
# sorting objects with multiple values
values = [(1, 'a'), (2, 'b'), (1, '1'), (2, 'a')]
```


```python
values.sort()
```


```python
values
```


```python
values.sort(key=lambda t: t[0])
```


```python
values
```


```python
values.sort(key=lambda t: t[1])
```


```python
values
```


```python
# another option
import operator
```


```python
values.sort(key=operator.itemgetter(0))
```


```python
values
```


```python
# sorting user-defined objects
# use order=True parameter to dataclass 
# if you want to order based on all the attributes in the order declared...
@dataclass
class Student:
    first_name: str
    last_name: str
    id: int
    gpa: float
    
    # you need to define __lt__ function to compare two objects of Student type
    def __lt__(self, other: 'Student') -> bool:
        return self.gpa < other.gpa
```


```python
s1 = Student('John', 'Smith', 123, 2.5)
s2 = Student('Jake', 'Jordan', 200, 3.5)
s3 = Student('Alice', 'Wonderland', 300, 4.5)
```


```python
students = [s1, s2, s3]
```


```python
students
```


```python
# use the __lt__ function provided in each object to order
students.sort()
```


```python
students
```


```python
# also sort based on each attribute
students.sort(reverse=True, key=lambda item: item.last_name)
```


```python
students
```


```python
students.sort(key=lambda item: item.id)
```


```python
students
```


```python
# another option is to use the operator module
import operator
```


```python
students.sort(key=operator.attrgetter("gpa"))
```


```python
students
```

### List comprehension

- list shortcuts can make you an efficient programmer
- E.g., an arithmetic set $S = \{x^2 : x \in \{0 ... 9\}\}$
    - is equivalent to: 
    ```python
    S = [x**2 for x in range(10)]
    ```
- consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses
    - the expressions can be anything
    - always results in a new list from evaluating an expression
- syntax:
```python
someList = [expression for item in list if conditional] # one-way selector
someList = [expression if conditional else expression for item in list] # two-way selector
```


```python
# Beginner way to create a list of squared values from 0 to 9?
sq = []
for i in range(10):
    sq.append(i**2)
```


```python
sq
```


```python
# Professional way: List comprehension:
S = [x**2 for x in range(10)]
```


```python
S
```

In Math: $V = \{2^0, 2^1, 2^2, 2^3, ... 2^{12}\}$


```python
V = [2**x for x in range(13)]
print(V)
```

In Math: $M = \{x | x \in S \ and \ x \ even\}$


```python
# List comprehension
M1 = [x for x in S if x%2==0]
```


```python
M1
```


```python
evens = [True if x%2==0 else False for x in range(1, 21)]
```


```python
evens
```


```python
sentence = "The quick brown fox jumps over the lazy dog"
# words = sentence.split()
# can make a list of tuples or list of lists
wlist = [(w.upper(), w.lower(), len(w)) for w in sentence.split()]
```


```python
wlist
```

### Nested list comprehension

- syntax to handle the nested lists with a nested loop-in-loop comprehension

```python
lst = [value for innerList in outerList for value in innerList]
lst = [value for innerList in outerList for value in innerList if condition]
lst = [value if condition else value1 for innerList in outerList for value in innerList]
```


```python
# let's create a nestedList of [[1, 2, 3, 4]*4]
nestedList = [list(range(1, 5))]*5
```


```python
nestedList
```


```python
# let's keep the even values from each nested list
even = [ x for lst in nestedList for x in lst if x%2==0 ]
```


```python
even
```


```python
# let's create a single boolean list
evenOdd = [True if x%2 == 0 else False for lst in nestedList for x in lst]
```


```python
evenOdd
```

## Sets

- lists are great and versatile, but sometimes we need all the elements of a container to be unique
- Python sets can store any hashable objects, not just strings and numbers
    - hashable object must implement `__hash__()` method
- sets are inherently unordered due to the hash-based data structure used for efficient access to the members
- it's easy to check if an item is **in** the set
- if you need to order the set, must convert it into a `list`
    - the iterator of Set will access elements in alphabetical order, however!
- not literal syntax to create an empty list
- must use `set()` function to create an empty set


```python
song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"), ]
```


```python
artists = set()
```


```python
for song, artist in song_library:
    artists.add(artist)
```


```python
artists
```


```python
'Opeth' in artists
```


```python
'Michael' in artists
```


```python
alphabetical = sorted(list(artists))
```


```python
alphabetical
```


```python
aset = set([1, 2, 3, 4, 5, 6])
bset = set([3, 4, 7, 8, 9, 10])
```


```python
# set operations
help(set)
```


```python
aset.difference(bset)
```


```python
# operator for difference
aset - bset
```


```python
aset.intersection(bset)
```


```python
# operator for intersection
aset & bset
```


```python
aset.symmetric_difference(bset)
```


```python
# operator for symmetric difference
aset ^ bset
```


```python
aset.union(bset)
```


```python
# union operator
aset | bset
```

## Stack

- **Last In First Out** data structure
- Python doesn't provide stack data structure; but **list** can be easily adapted as stack
    - use append() to push
    - use pop() to pop the last element pushed
- extend List class to create Stack class
    - we'll learn this in "When Objects are Alike (Inheritance)" chapter


```python
stack = list()
```


```python
stack.append(1)
stack.append(2)
stack.append((3, 4))
```


```python
stack.pop()
```


```python
stack.pop()
```


```python
stack.pop()
```

## Queues

- **First In First Out (FIFO)** data structure
- Python doesn't provide a queue data structure, but the list can be easily adapted to use it as a queue
- `queue` module provides a queue often used for multithreading
- there are three important types of queues:
    1. simple queue using `append()` and `pop()` on `list`
    2. double-ended queue (`deque`) from `collections.deque`
    3. `heapq` (priority queue) from `heapq` module
        - creates a min-priority queue; smaller values have higher priorities
- extend List class to create Queue class
    - we'll learn this in "When Objects are Alike (Inheritance)" chapter


```python
q = list()
```


```python
q.append(1)
```


```python
q.append(2)
```


```python
q.append((3, 4))
```


```python
q.pop(0)
```


```python
q.pop(0)
```


```python
q.pop(0)
```


```python
from collections import deque
```


```python
help(deque)
```


```python
deq = deque()
```


```python
deq.append(10)
```


```python
deq.appendleft(9)
```


```python
deq
```


```python
deq.insert(0, 100)
```


```python
deq
```


```python
deq.pop()
```


```python
deq.popleft()
```


```python
import heapq
```


```python
help(heapq)
```


```python
heap = []
```


```python
heapq.heappush(heap, (10, 'Go to Work'))
```


```python
heapq.heappush(heap, (5, 'Eat Breakfast'))
```


```python
heapq.heappush(heap, (1, 'Wake up'))
```


```python
heap
```


```python
heapq.heappop(heap)
```


```python

```
