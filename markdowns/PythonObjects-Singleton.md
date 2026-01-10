# Objects and Single Pattern

## Topics

- defining classes
- creating objects
- different properties of classes
    - attributes and methods
- different types of attributes
- different types of methods
- singleton pattern
- manager object


## Classes and Objects

- classes and objects may be used interchangely
- class is a user defined type of some objectes that will be instantiated of that type
- once the design step is completed, we turn those designs into code and a working program
- we implement UML class diagrams into code

## Defining Python classes
- use `class` keyword to define a Python class
- class helps essentially create new **type**
- class is a synonym for type
- class name must follow standard Python variable naming rules:
    - it must start with a letter or underscore
    - can only be comprised of letters, underscores, or numbers.
    - the Python style guide (PEP 8) recommends using CapWords for the class name


```python
class HelloClass:
    pass
```


```python
# instantiate objects from HelloClass
a = HelloClass()
```


```python
print(a)
```


```python
b = HelloClass()
```


```python
print(b)
```


```python
# a and b are two distinct objects stored at different memory locations
a is b
```

## Adding attributes
- the HelloClass is syntactically valid but useless
- we can dynamically add attributes in Python
- let's define a class representing a point in 2-D geometry
- use the dot `.` operator to add/access attributes


```python
class Point:
    pass
```


```python
p1 = Point()
```


```python
p2 = Point()
```


```python
p1.x = 5
p1.y = 4
```


```python
p2.x = 3
p2.y = 6
```


```python
print(p1.x, p1.y)
```


```python
print(p2.x, p2.y)
```

## Making it do something
- adding behaviors/methods
- `self` is a required parameter which refers to each instance of the class
- `self` is essentially replaced by object name
- `self` is similar to `this` in Java/C++
- `self` is not a keyword in Python, just a naming convention; however,
  it is strongly recommended to use `self` to avoid confusion
- `self` must be the first parameter of any method in a class


```python
class Point:
    def reset(self):
        self.x = 0
        self.y = 0
        
    def reset1(): # not correct!
        self.x = 0
        self.y = 0
```


```python
p = Point()
```


```python
p.reset()
```


```python
print(p.x, p.y)
```


```python
p.reset1()
```


```python
# self is not defined!
Point.reset1()
```

## More arguments
- add more methods that take arguments


```python
import math

class Point:
    def move(self, x: float, y:float) -> None:
        self.x = x
        self.y = y
    
    def reset(self) -> None:
        self.move(0, 0)
        
    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
```


```python
point1 = Point()
```


```python
point2 = Point()
```


```python
point1.reset()
```


```python
point2.move(5, 0)
```


```python
print(point2.calculate_distance(point1))
```


```python
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
```


```python
point1.move(3, 4)
```


```python
print(point1.calculate_distance(point2))
```


```python
print(point1.calculate_distance(point1))
```

## Initializing the object
- attributes are dynamically attached in Python
- it's hard for tools like mypy to know what attributes are available on objects of a class (could be very inconsistent)
- most programming languages have constructors to properly construct and initialize the objects with required attributes
- Python provides `__new__()` constructor method, but is rarely used
- `__init__()` - initializer method is more common to initialize the required attributes across all the instances of a given class 


```python
point = Point()
```


```python
point.x = 5
```


```python
print(point.x)
```


```python
print(point.y)
```


```python
import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.move(x, y)
        
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def reset(self) -> None:
        self.move(0, 0)
        
    def calculate_distance(self, other: "Point") -> None:
        return math.hypot(self.x - other.x, self.y - other.y)
    
```


```python
point = Point(3, 5)
```


```python
print(point.x, point.y)
```


```python
point.z = 100
```


```python
print(point.x, point.y, point.z)
```


```python
# preventing dynamic attribute addition using __slots__ attribute

import math

class Point:
    # prevents adding new attributes dynamically
    __slots__ = ['x', 'y']
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
```


```python
p1 = Point(4, 5)
```


```python
print(p1.x, p1.y)
```


```python
p1.z = 100
```

## Type hints and defaults

- sometimes providing the default values for parameters may be useful making them optional


```python
class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y
```


```python
# Multiline parameters; not common but may be used to 
# keep the line short and easier to read
class Point:
    def __init__(
        self,
        x: float = 0,
        y: float = 0
    ) -> None:
        self.x = x
        self.y = y
```

## Class Member Access Control

- who can access my data and methods?
- OOP languages such as C++, Java have the concept of **access control**
- keywords such as private, protected, and public are used to qualify access controls on class members
- Python doesn't believe in rules that may come on your way
- Python makes use of saying: "We're all adults here."
    - no need to declare a variable private, if we can all see the source code!
- Python recommends using a single `_` leading underscore/prefix
    - *notion that this is an internal member variable/method*
    - *think three times before accessing it directly* from objects
- use `__` double leading underscores/prefix:
    - *to strongly demand that the method/variable remain private* and never access from outside the object
- `_` and `__` prefixes are just guidance/recommendation/best practices but never enforced as syntax

## Property

- Object's properties/attributes should not be accessed directly
- they should be treated as private; use leading `_` or `__`
- peroperties should be exposed via getter and setter API's
- `@propery` builtin-function decorator allows us to define methods that can be accessed like an attribute
- `@property` makes a method getter
- `@<method_name>.setter` makes it a setter method
- `@<method_name>.deleter` deletes an attribute
    - use `del object.attribute` to delete an attribute


```python
class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name # public
        self._last_name: str = last_name # treat as private
        
    # define the getter method using property decorator
    @property
    def last_name(self) -> str:
        """
        Getter for _last_name property 
            - doc should be written to getter property!!
        """
        return self._last_name
    
    # define the setter method using decorator
    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Setter for _last_name property
        """
        if value.isalpha:
            self._last_name = value
        else:
            raise TypeError('Non-alphabetic in value:', value)
            
    @last_name.deleter
    def last_name(self) -> None:
        del self._last_name

    def __str__(self):
        """
        String representation of the object
        """
        return f'{self._last_name}, {self.first_name}'
    
    # using getter and setter functions - not recommended!!
    def _get_last_name(self) -> str:
        return self._last_name
    
    def _set_last_name(self, last_name: str) -> None:
        if last_name.isalpha:
            self._last_name = last_name
        else:
            raise TypeError('Non-alphabetic in last_name', last_name)
    
    def _del_last_name(self) -> None:
        del self._last_name
        
    # using property function to define getter and setter, deleter, doc
    l_name = property(fget=_get_last_name, 
                      fset=_set_last_name,
                      fdel=_del_last_name,
                      doc="Last Name property."
                      )
```


```python
student = Student("John", "Doe")
```


```python
# access the first name using data property
print(student.first_name)
```


```python
student.first_name = "2323asfs_"
```


```python
# access the last name using data property
print(student._last_name)
```


```python
# access the last name using getter property
print(student.last_name)
```


```python
# @property makes method more like an attribute property
# the following will raise an Exception
print(student.last_name())
```


```python
student.last_name = "Smith"
```


```python
print(student)
```


```python
student.l_name
```


```python
student.l_name = "Johnson"
```


```python
student.last_name
```


```python
help(student)
```


```python
# let's delete l_name attribute
del student.l_name
```


```python
# this will now throw an AttributeError
print(student)
```


```python
del student.last_name
```

## Types of Class Methods

- functions are normally called methods within a class
- see this resource: https://realpython.com/instance-class-and-static-methods-demystified/

### Instance Properties

- attached to each instances with (self)
- special methods:
    - `getter`, `setter`, `deleter` methods
    - use `@property` `@method.setter`, `@method.deleter` decorators
- used as attribues/variables
- see example above

### Instance Methods
    
- regular *instance method*
- methods take **self** first parameter which points to an instance itself
- they freely access all the attributes and other methods on the same object
- gives them lot of power when modifying an object's state
- see example below
    
### Class Methods

- methods belong to the class itself and are shared across all the instances
- takes `cls` parameter that points to class and not the object instance
- use `@classmethod` decorator to mark method as class method
- can't modify/access object attributes and methods
    - but can access/modify only class state/variables that are shared across all the instances

### Static Methods

- use `@staticmethod` decorator to mark static methods
- acts as a regular function within a Class namespace
- doesn't take `cls` or `self` parameters
    - but can take any other arguments
- neither modify class state nor object state


```python
class MyClass:
    class_var = 10

    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b
    
    def set_method(self, a, b):
        self.a = a
        self.b = b
        return 'instance method called', self, self.__add()

    def __add(self):
        return self.a + self.b + MyClass.class_var

    @classmethod
    def classmethod(cls, a, b):
        return 'class method called', cls, a+b+cls.class_var

    @staticmethod
    def staticmethod(a, b):
        return 'static method called', a+b+MyClass.class_var
```


```python
instance = MyClass()
instance.set_method(2, 3)
```


```python
# call class method
MyClass.classmethod(3, 5)
```


```python
# call static method
MyClass.staticmethod(3, 5)
```


```python
# multiple instances of MyClass is allowed and expected
instance1 = MyClass()
instance2 = MyClass()
```


```python
# those instances are in fact different objects
instance1 is instance2
```

## The Singleton Pattern

- also called anti-pattern 
- more common in more strict OOP languages such as Java than in scripting languages such as Python
- the basic idea is to allow exactly one instance of certain objects in the program

![Single pattern](resources/singleton_pattern.png)

- singletons are normally enforced by making the constructor private (so no one can create additional instances of it)
- then providing a static method to retrieve the single instance. 
    - this method creates a new instance the first time it is called and then returns that same instance for all subsequent calls
    
- since python doesn't have a private access specifier, we've to be a little creative
- can use `__new__()` method and class variable to ensure that only one instance is created
- also called anti-pattern because there is only one instance of the class
- `__new__()` is a class method that is called before the `__init__()` instance method
- use `cls` parameter to check if the instance is already created
- return the instance if it's already created
- otherwise, create a new instance and return it
- `__new__()` method takes the `cls` as the first argument
    - also takes the rest of the arguments that are passed to the `__init__` method


```python
from __future__ import annotations


class MySingletonClass:
    _instance: "MySingletonClass" | None = None

    # singleton pattern
    def __new__(cls, *args, **kwargs):
        # we don't care about (a, b) so use args and kwargs within __new__
        # not providing them will create syntax error because __init__ is defined with two arguments
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f'{self.a}, {self.b}'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MySingletonClass):
            return NotImplemented
        return self.a == other.a and self.b == other.b
```


```python
obj1 = MySingletonClass(2, 3)
obj2 = MySingletonClass(3, 4)
```


```python
obj1 is obj2
```




    True




```python
print(obj1)
print(obj2)
```

    3, 4
    3, 4



```python
obj1 == obj2
```




    True




```python
def test_singleton():
    obj1 = MySingletonClass(2, 3)
    obj2 = MySingletonClass(30, 40)
    assert obj1 is obj2
```


```python
test_singleton()
```

### Python singleton

- Python provides two built-in Singleton patterns we can leverage
- rather than invent something hard to read, there are two choices:

1. Python *module*:
    - One `import` will create a module
    - all other attempts to import the module return the one-and-only singleton instance of the module

2. Python *class* definition:
    - a Python class can only be created once in a given namespace
    - consider using a class with class-level attributes as a singleton object
    - use `@staticmethod` decorator to not have to use instance variable `self`
    
- see `demo-assignments/A1-OOP` and `demo-assignments/A2-ABC` for single pattern examples

## Manager objects

- higher-level objects that manage other objects
    - the object that ties everything together
- these are sometimes called Facade objects because they present a pleasant, easy-to-use facade over some underlying complexity
    - Facade is also a design pattern that's covered in more detail later in the course
- similar to managers in officers, management object, may not do the actual work
- the attributes of a management class tend to refer to other objects that do the actual work
    - managers typically delegate to other classes at the right time and pass messages between them
- assemble manager objects by knitting other objects together
- to an extent, a manager is also an Adapter among the various interfaces
    - another design pattern covered later in the course
- Solution/Main class in demo-assignments `A0-OOP, A1-OOP` are examples of a manager class
- Manger class can use Singleton pattern to ensure only one instance of the manager object is created

## Exercies

- Solve the following Kattis problems using OOD
- must use at least two classes; property, methods, attributes, etc.
- must use docstrings for each class and method
- must use mypy to ensure you're using variables and functions type correctly
- attributes must be privates
- must use getter and setter methods for each attribute where appropriate
- must generate HTML documentation of the docstrings into a documentations directory
- must create UML diagrams of each class and their interactions

1. Sum Kind of Problem - https://open.kattis.com/problems/sumkindofproblem
2. Convex Polygon Area - https://open.kattis.com/problems/convexpolygonarea


```python

```
