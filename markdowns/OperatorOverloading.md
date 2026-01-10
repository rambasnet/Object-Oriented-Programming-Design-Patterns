# Operator Overloading

- Python operators +, /, -, \*, etc. can be overloaded with special methods on classes
- operator overloading where applicable makes classes work more like fundamental types such as int, float and str
- we can add two objects, multiply them, etc.


```python
class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
        """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs
        # Calculate total seconds to represent
        self.__normalize()
        
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    
    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def increment(self, secs):
        self.seconds += secs
        self.__normalize()
        
    def __normalize(self):
        totalsecs = self.to_seconds()
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        
    def add_time(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
```


```python
# now let's use MyTime class and its methods again
current_time = MyTime(9, 50, 45)
bake_time = MyTime(2, 35, 20)
done_time = current_time.add_time(bake_time)
print(done_time)
```


```python
# add_time is replaced with __add__ built-in special function

class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
        """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs
        # Calculate total seconds to represent
        self.__normalize()
        
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds)
    
    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def increment(self, secs):
        self.seconds += secs
        self.normalize()
        
    def __normalize(self):
        totalsecs = self.to_seconds()
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        
    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
```


```python
current_time = MyTime(9, 50, 45)
bread_time = MyTime(2, 35, 20)
done_time = current_time + bread_time 
# equivalent to: done_time = current_time.__add__(bread_time)
print(done_time)
```

### some special methods
- list of all the special methods can be found here: https://docs.python.org/3/reference/datamodel.html

#### \__len__(self)
   - called by len(x)

#### \__iter__(self)
   - called by iter(); for statement
   
#### \__contains__(self)
   - called by built-in **in** operator
    
#### \__del__(self)
   - destructor - called when an instance is about to be destroyed

#### \__str__(self)
   - called by str(object)
   - called by format() and print() functions to format and print string representation
   - must return string representation of object

#### \__lt__(self, other)
   - x < y calls x.__lt__(y)

#### \__gt__(self, other)
   - x > y calls x.__gt__(y)

#### \__eq__(self, other)
   - x == y calls x.__eq__(y)

#### \__ne__(self, other)
#### \__ge__(self, other) 
#### \__le__(self, other)

### Emulating numeric types

#### \__add__(self, other)
#### \__sub__(self, other)
#### \__mul__(self, other)
#### \__mod__(self, other)
#### \__truediv__(self, other)
#### \__pow__(self, other)
#### \__xor__(self, other)
#### \__or__(self, other)
#### \__and__(self, other)


### adding two points in 2-d coordinates



```python
from typing import Any

class Point:
    """
    Point class represents and manipulates x,y coords
    """
    count = 0
    
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coordinates"""
        self.x = xx
        self.y = yy
        Point.count += 1
        
    def dist_from_origin(self):
        import math
        dist = math.sqrt(self.x**2+self.y**2)
        return dist
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def move(self, xx, yy):
        self.x = xx
        self.y = yy
        
    def __add__(self, other: "Point"):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __mul__(self, other: "Point"):
        """
        computes the dot product of two points
        """
        return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other: Any):
        """
        if the left operand is a primitive type (int or float) 
        and the right operand is a Point, Python invokes __rmul__
        which performs scalar multiplication
        """
        return Point(other * self.x, other * self.y)
```


```python
p1 = Point(2, 2)
p2 = Point(10, 10)
p3 = p1 + p2
print(p3)
print(p1 * p3)
print(4 * p1)
```

    (12, 12)
    48
    (8, 8)



```python
# not allowed as it calls __mul__
print(p1 * 5)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[9], line 2
          1 # not allowed as it calls __mul__
    ----> 2 print(p1 * 5)


    Cell In[5], line 34, in Point.__mul__(self, other)
         30 def __mul__(self, other: "Point"):
         31     """
         32     computes the dot product of two points
         33     """
    ---> 34     return self.x * other.x + self.y * other.y


    AttributeError: 'int' object has no attribute 'x'



```python

```
