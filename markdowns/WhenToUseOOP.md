# When to Use Object-Oriented Programming

## Topics

- how to recognize objects
- data and behaviors, once again
- wrapping data behaviors using properties
- DRY principle and avoiding repetition

## Treat objects as objects

- identify objects in the problem, and then model their data and behaviors
- if data is the focus of a problem, use Python data structures such as list, dictionary, set, etc.
- if the behavior is the focus, a simple function is more suitable
- objects have both data and behavior and are of equal focus
- e.g., design a program to model polygons in two-dimensional space
    - we could start with each polygon represented as a list of points - a list of tuples
    - then convert it into OOD
- OOD can be verbose; lot more lines of code compared to the functional counterpart
- Code length, however, is not a good indicator of code complexity
- *one-liner* can be a fun exercise but the result is often unreadable, even to the original author the next day
- the more important a set of data is, the more likely it is to have multiple functions specfic to that data
    - more useful to use a class with attributes and methods instead
- certain interactions among objects, and inheritance can't be modeled elegantly without classes
- composition can be modeled with data structures only, but the code is less readable
    - e.g., we can have a list of dictionaries holding tuple values
    - less obvious what those tuples or dictionaries hold/represent!
    
#### NOTE: No one wins at Code Golf. Minimizing the volume of code is rarely desirable.

### Case study of Point and Polygon
- the difference between functional and OOD


```python
# use the built-in data structure to represent a square polygon
square = [(1, 1), (1, 2), (2, 2), (2, 1)]
```


```python
from math import hypot
from typing import Tuple

# now find the perimeter of the square
def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return hypot(p1[0]-p2[0], p1[1]-p2[1])
```


```python
def perimeter(polygon):
    # zip creates: (v[0], v[1]), (v[1], v[2]), and (v[2], v[0])
    pairs = zip(polygon, polygon[1:]+polygon[:1])
    return sum(distance(p1, p2) for p1, p2 in pairs)
```


```python
perimeter(square)
```




    4.0




```python
from math import hypot
from typing import Tuple, List

# Type alias
Point = Tuple[float, float] # this can be converted into a class

def distance(p_1: Point, p_2: Point) -> float:
    return hypot(p_1[0] - p_2[0], p_1[1] - p_2[1])

Polygon = List[Point] # this can be converted into a class

def perimeter(polygon: Polygon) -> float:
    pairs = zip(polygon, polygon[1:] + polygon[:1])
    return sum(distance(p1, p2) for p1, p2 in pairs)
```


```python
from math import hypot
from typing import Tuple, List, Optional, Iterable

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)
    
class Polygon:
    def __init__(self) -> None:
        self._vertices: List[Point] = []
            
    def add_point(self, point: "Point") -> None:
        self._vertices.append((point))
        
    def perimeter(self) -> float:
        pairs = zip(self._vertices, self._vertices[1:] + self._vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)
```


```python
square = Polygon()
```


```python
square.add_point(Point(1, 1))
```


```python
square.add_point(Point(1, 2))
```


```python
square.add_point(Point(2, 2))
```


```python
square.add_point(Point(2, 1))
```


```python
square.perimeter()
```




    4.0




```python
# more verbose/steps compared to functional design
square = [(1, 1), (1, 2), (2, 2), (2, 1)]
```


```python
perimeter(square)
```




    4.0




```python
# we could shorten Polygon class
# just initialized Polygon with point objects
class Polygon_2:
    def __init__(self, vertices: Optional[Iterable[Point]] = None) -> None:
        self._vertices = list(vertices) if vertices else []
        
    def perimeter(self) -> float:
        pairs = zip(self._vertices, self._vertices[1:]+self._vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)
```


```python
square = Polygon_2([Point(1, 1), Point(1, 2), Point(2, 2), Point(2, 1)])
```


```python
square.perimeter()
```




    4.0




```python
# let's take one more step; allow Polygon to accept Tuples too
from typing import Union

Pair = Tuple[float, float]
Point_or_Tuple = Union[Point, Pair]

class Polygon_3:
    def __init__(self, vertices: Optional[Iterable[Point_or_Tuple]] = None) -> None:
        self._vertices: List[Point] = []
        if vertices:
            for point_or_tuple in vertices:
                self._vertices.append(Polygon_3.make_point(point_or_tuple))
                
    def perimeter(self) -> float:
        pairs = zip(self._vertices, self._vertices[1:]+self._vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)
    
    @staticmethod
    def make_point(item: Point_or_Tuple) -> Point:
        return item if isinstance(item, Point) else Point(*item)
    
```


```python
square = Polygon_3([(1, 1), (1, 2), (2, 2), (2, 1)])
```


```python
square.perimeter()
```

## Adding behaviors to class data with properties

- even though classes hold both data and behavior, we've explictly separated them with variables and methods
- the distinction between data and behavior sometimes can be uncannily blurry
- OOD teaches us to never access attributes directly
    - OO developers insist we write setters and getters (methods) to access attributes
- setter and getter methods are not as readable and are not favored in my OOP languages
    - they provide a simpler syntax to access attributes "as if" you're directly accessing them without the methods
- why setters and getters?
    - compile code cleanly as functions
    - write extra code for data validation, caching (avoid complex recomputation), etc. when accessing and setting
- Python gives us a `property` function that makes methods *look* like attributes
- or use **decorators** `@property`, `@method.setter`, `@method.deleter` to define properties


```python
# favored syntax - but not good design
# access attribtues; not use getter and setter methods
class Color:
    def __init__(self, rgb_value: int, name: str) -> None:
        self.rgb_value = rgb_value
        self.name = name
```


```python
c = Color(0xff0000, "bright red")
```


```python
c.name
```


```python
c.name = 'Red'
```


```python
c.name
```


```python
# using decorators to define getter and setter methods
class NorwegianBlue:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str = "N/A"
            
    @property
    def state(self) -> str:
        """ This is a state property. """
        print(f"Getting {self._name}'s State")
        return self._state
    
    @state.setter
    def state(self, state: str) -> None:
        print(f"Setting {self._name}'s State to {state!r}")
        self._state = state
        
    @state.deleter
    def silly(self) -> None:
        print(f"{self._name} is pushing up daisies!")
        del self._state
```


```python
ship = NorwegianBlue("The Norwegian Blue")
```


```python
print(ship.state)
```


```python
ship.state = "pining for the fjords"
```


```python
print(ship.state)
```


```python
del ship.silly
```

## When to use properties

- can be confusing when properties blur the distinction between behavior and data
- properties, data, and behavior are generally called the attributes of a class
- follow these principles:
    - use methods to represent actions; method names are generally verbs
    - use attributes or properties to represent the state of the object; these are nouns, adjectives, and prepositions
        - use properties for attributes in the exceptional case when:
            - complex computation is involved such as data validation, logging, access controls, caching, etc.
- example of caching data using `@property` method
- without the method, you'll not be able to write code logic to use the cache content


```python
from urllib.request import urlopen
from typing import Optional, cast

class WebPage:
    def __init__(self, url: str) -> None:
        self._url = url # private attribute
        self._content: Optional[bytes] = None # private attribute
            
    @property
    def content(self) -> bytes:
        if self._content is None:
            print("Retrieving New Page...")
            with urlopen(self._url) as response:
                self._content = response.read()
        return self._content
```


```python
import time
webpage = WebPage("http://ccphillips.net/")
now = time.perf_counter()
content1 = webpage.content
first_fetch = time.perf_counter() - now

now = time.perf_counter()
content2 = webpage.content
second_fetch = time.perf_counter() - now
assert content2 == content1, "Problem: Pages were different"
print(f"Initial Request     {first_fetch:.5f}")
print(f"Subsequent Requests {second_fetch:.5f}")
```

    Retrieving New Page...
    Initial Request     1.24886
    Subsequent Requests 0.00006


## Removing duplicate code

- Why is duplicate code a bad thing?
    - boils down to 2 reasons: **readability** and **maintainability**
    
- **copy-pasta** programming: copy/pasting similar code to extend/add new functionalities
    - creates a big mess of tangled noodles of code like a bowl of spaghetti
- when we see similar or near duplicate code blocks, we have *additional* intellectual barrier to understanding:
    1. Are they truly identical?
    2. If not, how is one section different from the other?
    3. When do we use one or the other?
       
- you may be the only person working on the project and it may all make sense to you now
    - just easy to copy and paste! However, can you remember the logic behind it the next day/next year?
    - What if someone else takes over/joins the project?

#### NOTE: Code should always be written to be readable first.

### DRY principle

- Python developers prefer elegant, clean code and follow the **Don't Repeat Yourself** principle
- Never copy and paste code! Think thrice before hitting `Ctrl+C`


```python

```
