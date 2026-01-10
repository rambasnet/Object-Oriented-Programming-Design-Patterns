# When Objects are Alike

- in programming, duplicate code is considered evil
    - difficult to debug and maintain code
- there are many ways to merge pieces of code or objects that have similar functions
- the concept of inheritance allows us to create **is-a** relationship between two or more classes
    - inherit common code from base/superclass and extend/override it with specific details in each subclass (aka Polymorphism)

## Basic inheritance

- technically every class inherits from the built-in *object* class
- generally, we extend the base/parent/super class and customize/add more functionalities to the derived/child class
- child class inherits methods and attributes defined in parent classes
- **inheritance** must follow LSP - Liskov Substitution principle
    - child class can replace parent class but not vice-versa

![](resources/UML-inheritance.png)


```python
class MySubClass(object):
    pass
```


```python
help(MySubClass)
```


```python
from typing import List

class Contact:
    # Contact with a regular list
    all_contacts: List["Contact"] = [] # class variable
    
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
    def __repr__(self) -> str:
        """
        :param: None
        :return: str representation of class
        """
        return (f'{self.__class__.__name__}'
                f'({self.name!r}, {self.email!r})'
               )
    
```


```python
c_1 = Contact("Dusty", "dusty@example.com")
```


```python
c_2 = Contact("Steve", "steve@itmaybehack.com")
```


```python
# access all the contacts stored in Contact class
Contact.all_contacts
```


```python
# Supplier inherits from Contact
class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' to '{self.name}'"
        )
```


```python
c = Contact("Some Body", "somebody@example.net")
```


```python
s = Supplier("Sup Plier", "supplier@example.net")
```


```python
from pprint import pprint
```


```python
# each object has access to class variable
# not common notation; confusing as if all_contacts is an instance variable
pprint(c.all_contacts)
```


```python
# better notation
pprint(Contact.all_contacts)
```


```python
# contact objects don't have order
# contact is NOT a supplier
c.order("I need pliers")
```


```python
# however, the supplier object has order
# Supplier is a Contact
s.order("I need pliers")
```

## Extending built-ins
- inheritance allows us to extend the functionalities of built-in classes
- in Contact class, we're adding contacts to a list of Contact
- what if we wanted to search the contact list by name?
- we could add a method in the Contact class to search the list
    - better yet, we could add a search method to **ContactList** itself

### Extending list


```python
from __future__ import annotations
# this will let us use user-defined types in Python 3.9 or lower as type annotations
```


```python
help(list)
```


```python
# Extending list
class ContactList(list["Contact"]):
    def search(self, name:str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        matching_contacts = [contact for contact in self if name in contact.name]
        return matching_contacts
```


```python
class Contact:
    # let's use ContactList instead of List
    all_contacts: 'ContactList' = ContactList() # class variable
    
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
    def __repr__(self) -> str:
        """
        :param: None
        :return: str representation of class
        """
        return (f'{self.__class__.__name__}'
                f'({self.name!r}, {self.email!r})'
               )
       
```


```python
c = Contact("John A",  "john@example.net")
```


```python
c1 = Contact("John B", "john@B.com")
c2 = Contact("Jenna C", "cutty@C.org")
```


```python
print(Contact.all_contacts.search('John'))
```

### Extending `dict` class
- create a dictionary class that extends the built-in `dict` to track the longest key it has seen


```python
from typing import Optional
```


```python
class LongKeyDict(dict[str, int]):
    def longest_key(self) -> Optional[str]:
        """In effect, max(self, key=len) but less obscure"""
        
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest
```


```python
# Test the LongKeyDict
# perhaps key is username and value is the number of articles they read
articles_read = LongKeyDict()
```


```python
help(dict)
```


```python
articles_read['lucy'] = 42
articles_read['philips'] = 10
articles_read['steve'] = 7
```


```python
articles_read.longest_key()
```


```python
help(articles_read)
```


```python
# same as
max(articles_read, key=len)
```

### Duplicate key in Dict

- python quietly overwrites duplicate key without telling user
- create a custom dictionary that doesn't allow duplicate key insert/update
    - extend Dict to not allow duplicate key insert/update


```python
d = {"a": 42, "a": 3.14}
```


```python
d
```


```python
# True is convereted into 1; duplicate key is overwritten
{1: "one", True: "true"}
```


```python
# extending Dict to not allow duplicate key insert/update

from __future__ import annotations
from typing import cast, Any, Union, Tuple, Dict, Iterable, Mapping
from collections.abc import Hashable

DictInit = Union[Iterable[Tuple[Hashable, Any]], Mapping[Hashable, Any], None]

class NoDupDict(dict[Hashable, Any]):
    def __setitem__(self, key: Hashable, value: Any) -> None:
        if key in self:
            raise ValueError(f"duplicate {key!r}")
        super().__setitem__(key, value)

    def __init__(self, init: DictInit = None, **kwargs: Any) -> None:
        if isinstance(init, Mapping):
            #super().__init__(init, **kwargs)
            #print('this is from Mapping init')
            #print(init.items())
            for k, v in init.items():
                #self.__setitem__(k, v)
                self[k] = v
        elif isinstance(init, Iterable):
            for k, v in cast(Iterable[Tuple[Hashable, Any]], init):
                #self[k] = v
                self.__setitem__(k, v)
        elif init is None:
            super().__init__(**kwargs)
        else:
            super().__init__(init, **kwargs)
```


```python
d = NoDupDict()
```


```python
d
```


```python
d[1] = 'a'
```


```python
d[1] = 'b'
```


```python
# how about initilizing with duplicate keys...
# the dictionary literal will eliminate duplicates before passing to __init__
# this means that the second value will overwrite the first
d3 = NoDupDict({1:'One', 1:'uno'})
```


```python
d3
```


```python
d4 = NoDupDict([(1, 'One'), (1, 'uno')])
```


```python
d4
```

## Overriding and super
- inheritance not only allows for adding new behaviors but also overriding/chaining existing behaviors
- any method can be overridden including `__special__` built-ins:
    - such as `__init__`, `__str__`, `__repr__`, etc.


```python
class Friend(Contact):
    """Friend inherits from Contact"""
    # overrides Contact.__init__
    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name = name  # duplicate member
        self.email = email  # duplicate member
        self.phone = phone
        
        # attributes of Contact are not inherited;
        # so if Contact is updated, Friend will not benefit from the updates
```


```python
f = Friend('James1', "james1@email.com", '1231-4567')
# f object will not be added to all_contacts list
```


```python
pprint(f.all_contacts)
```


```python
Contact.all_contacts
```


```python
# better approach is to use super() function
class Friend(Contact):
    
    # overrides Contact.__init__
    def __init__(self, name: str, email: str, phone: str) -> None:
        #super().__init__(name, email)
        # alternatively; useful in multiple inheritance
        # explicitly, call parent's __init__()
        super().__init__(name, email)
        # first bind the instance to the parent class
        self.phone = phone
        
    def call_phone(self):
        print(f'calling {self.phone}')
```


```python
f1 = Friend('Jake', 'jake@jake.com', '234-5678')
```


```python
pprint(f1.all_contacts)
```


```python
f2 = Friend('Joker', 'joker@joker.com', '234-5678')
```


```python
f2.call_phone()
```


```python
pprint(f1.all_contacts)
```

## To Use Inheritance or NOT To...

- inheritance is an "Is-A" relationship
- it should be only used to model "is-a" relationship
- Liskov's substitution principle says that an object of type *Derived*, which inherits from *Base*, can replace an object of type *Base* without altering the desirable properties of a program
- a simple test to use to make sure inheritance is the right design:
    1. Evaluate B is an A: think about the relationship and justify it
    2. Evaluate A is a B: Reverse the relationship and justify it. Does it also make sense?
    3. E.g. square and rectangle are both shapes, but rectangle is not a square
    4. Circle is a Shape but Shape is not a Circle
- if you justify both relationships, then you should **NEVER** inherit those classes from one another
    - meaning, if A is B then B is **not** A should hold or vice-versa for proper inheritance to use
- e.g., when designing Rectangle and Square classes should you use inheritance?
- how about the relationship between Car and Airplane?

## Multiple inheritance

- a tricky and touchy concept!
- conceptually simple - a child class inherits from multiple parent classes
- avoid multiple inheritance if you can!
    - if you think you need multiple inheritance, you might be wrong!
    - if you know you need multiple inheritance, you might be right!
- let's look at this toy example to understand multiple inheritance    


```python
# Recall: by dafault all Python class implicitly inherit from object base class
class A(object):
    def __init__(self):
        self.a = "A"
        
    def printMe(self):
        print("A's printMe called!")
        print(f'{self.a=}')
    
    def sayHi(self):
        print(f'{self.a} says HI!')
```


```python
obja = A()
obja.printMe()
obja.sayHi()
```

    A's printMe called!
    self.a='A'
    A says HI!



```python
class B(object):
    def __init__(self):
        self.a = 'AAAA'
        self.b = 'B'
        
    def printMe(self):
        print("B's printMe called")
        print(f'{self.a=} {self.b=}')
        
    def method_in_B(self):
        print("I'm a method in B")
```


```python
objb = B()
objb.printMe()
```

    B's printMe called
    self.a='AAAA' self.b='B'



```python
# Order of inheritance matters!
class C(B, A):
    # since no __init__ is provided for C,
    # which parent's __init__ is called?
    # Change the order of parents and rerun the code!
    def printMe(self):
        # C may or may not have b depeneding on the order of inheritance
        print("C's printMe called:")
        print(f"Attributes are {self.a}, {self.b}")
        #pass
```


```python
c_default = C()
```


```python
c_default.printMe()
```

    C's printMe called:
    Attributes are AAAA, B



```python
c_default.sayHi()
```


```python
# __mro__ attribute contains method resolution order for a class
C.__mro__
```


```python
# if your override __init__ of parents...
class C_1(A, B):
    # overrides B and C's __init__
    # must explictly call A.__init__ and B.__init__ 
    # if C wants to inherit their properties
    def __init__(self):
        # The order in which the super initializers are called matters!
        # The same attributes of the prior initializer are 
        # overridden by later initializer
        # A.__init__(self)
        B.__init__(self)
        A.__init__(self)
        self.c = 'C'
    
    def printMe(self):
        # overrides printMe of parent classes
        print("C's printMe called:")
        print(f"Attributes are {self.a}, {self.b}, {self.c}")
```


```python
c_1 = C_1()
```


```python
c_1.printMe()
```

    C's printMe called:
    Attributes are A, B, C



```python
help(c_1)
```


```python
class D(C_1):
    # D inherits everything from C
    pass
```


```python
d = D()
d.printMe()
```

    C's printMe called:
    Attributes are A, B, C



```python
class E(D):
    def __init__(self):
        self.e = 'E'
        D.__init__(self)
    
```


```python
e = E()
```


```python
e.printMe()
```

    C's printMe called:
    Attributes are A, B, C



```python
class F(B, A):
    pass
```


```python
# which printMe is called?
f = F()
f.printMe()
```

    B's printMe called
    self.a='AAAA' self.b='B'


## Diamond problem

- Diamond inheritance is a problem!
- superclass/base classes may be called multiple times by sub-classes because of the organization of the class hierarchy
- or the superclass's initializer may never be called

![](resources/ch-2_fig_2.png)


```python
class BaseClass:
    num_base_calls = 0
    def call_me(self) -> None:
        print("Calling method on BaseClass")
        self.num_base_calls += 1 
        # uses class variable num_base_calls to keep track of num of calls
        # not great; but quick way to avoid __init__ function
```


```python
b = BaseClass()
```


```python
b.call_me()
b.num_base_calls
```

    Calling method on BaseClass





    2




```python
class BaseClass:
    num_base_calls = 0
    def call_me(self) -> None:
        print("Calling method on BaseClass")
        BaseClass.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on LeftSubclass")
        LeftSubclass.num_left_calls += 1
        
class RightSubclass(BaseClass):
    num_right_calls = 0 
    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on RightSubclass")
        RightSubclass.num_right_calls += 1
        
class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self) -> None:
        RightSubclass.call_me(self)
        LeftSubclass.call_me(self)
        print("Calling method on Subclass")
        Subclass.num_sub_calls += 1
```


```python
s = Subclass()
s.call_me()
# notice the BaseClass called twice
```

    Calling method on BaseClass
    Calling method on RightSubclass
    Calling method on BaseClass
    Calling method on LeftSubclass
    Calling method on Subclass



```python
print(s.num_sub_calls, s.num_left_calls, 
      s.num_right_calls, s.num_base_calls)
# This may result in buggy logic, e.g., depositing money into 
# bank account twice
```

    1 1 1 2


### use super( )
- `super()` function was originally developed to make complicated forms of multiple inheritance possible for method resolution
- instead of explicitly calling `parent_class.method()` call `super()` and let it resolve the parent function automatically


```python
class BaseClass_S:
    num_base_calls = 0
    def call_me(self) -> None:
        print("Calling method on BaseClass_S")
        BaseClass_S.num_base_calls += 1

class LeftSubclass_S(BaseClass_S):
    num_left_calls = 0
    def call_me(self) -> None:
        super().call_me()
        print("Calling method on LeftSubclass_S")
        LeftSubclass_S.num_left_calls += 1
        
class RightSubclass_S(BaseClass_S):
    num_right_calls = 0 
    def call_me(self) -> None:
        super().call_me()
        print("Calling method on RightSubclass_S")
        RightSubclass_S.num_right_calls += 1
        
class Subclass_S(RightSubclass_S, LeftSubclass_S):
    num_sub_calls = 0
    def call_me(self) -> None:
        super().call_me()
        print("Calling method on Subclass_S")
        Subclass_S.num_sub_calls += 1
```


```python
ss = Subclass_S()
ss.call_me()
```

    Calling method on BaseClass_S
    Calling method on LeftSubclass_S
    Calling method on RightSubclass_S
    Calling method on Subclass_S



```python
# Note that the base class is called only once!
print(ss.num_sub_calls, ss.num_left_calls, 
      ss.num_right_calls, ss.num_base_calls)
```

    1 1 1 1


### Python's Method Resolution Order (MRO)

- python provides `__mro__` attribute as a Tuple to see how the method calls are resolved (similar to stack trace) from various superclasses
- it's a tuple with the last member will always be `object`


```python
from pprint import pprint
```


```python
pprint(Subclass.__mro__)
```

    (<class '__main__.Subclass'>,
     <class '__main__.LeftSubclass'>,
     <class '__main__.RightSubclass'>,
     <class '__main__.BaseClass'>,
     <class 'object'>)



```python
pprint(Subclass_S.__mro__)
```

    (<class '__main__.Subclass_S'>,
     <class '__main__.RightSubclass_S'>,
     <class '__main__.LeftSubclass_S'>,
     <class '__main__.BaseClass_S'>,
     <class 'object'>)


## Polymorphism

- different behaviors happen depending on which subclass is being used, without having to explictly know what the subclass actually is
- also called the Liskov Substitution Principle - honoring Barbara Liskov
    - we should be able to substitute any subclass for its superclass
- polymorphism is one of the most important reasons to use inheritance in many OOD
- let's look at an example of a media player to demonstrate how polymorphism can be used
- different types of media file that requires different decompression and decoding techniques
- simplify design by using a public API `play()` method on an audio_file object to play various files (.wav, .mp3, .ogg, .wma, etc.)


```python
from pathlib import Path

class AudioFile:
    ext: str # just for mypy; not an actual class variable as it's not initialized
        
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath
        
    # can implement a generic play method
    def play(self):
        pass
# Note how AudioFile can access the ext class variable
# from different subclasses (polymorphism at work!)
```


```python
class MP3File(AudioFile):
    ext = '.mp3'
    
    def play(self) -> None:
        # implement mp3 play
        print(f'playing {self.filepath} as MP3')
        
```


```python
class WavFile(AudioFile):
    ext = '.wav'
    
    def play(self) -> None:
        # implement wav play
        print(f'playing {self.filepath} as WAV')
        
```


```python
class OggFile(AudioFile):
    ext = '.ogg'
    
    def play(self) -> None:
        # implement ogg play
        print(f'playing {self.filepath} as OGG')
        
```


```python
p1 = MP3File(Path('Heart of the sunrise.mp3'))
```


```python
p1.play()
```

    playing Heart of the sunrise.mp3 as MP3



```python
p2 = WavFile(Path("Roundabout.wav"))
p2.play()
```

    playing Roundabout.wav as WAV



```python
p3 = OggFile(Path("Roundabout.ogg"))
p3.play()
```

    playing Roundabout.ogg as OGG



```python
p4 = MP3File(Path("Rocky Mountain.mov"))
# .mov is not a valid extension for MP3File
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[114], line 1
    ----> 1 p4 = MP3File(Path("Rocky Mountain.mov"))
          2 # .mov is not a valid extension for MP3File


    Cell In[105], line 8, in AudioFile.__init__(self, filepath)
          6 def __init__(self, filepath: Path) -> None:
          7     if not filepath.suffix == self.ext:
    ----> 8         raise ValueError("Invalid file format")
          9     self.filepath = filepath


    ValueError: Invalid file format


## Duck typing

- polymorphism is one of the coolest things about OOP; makes some programming designs obvious that were not possible in earlier paradigms (procedural programming)
- however, Python makes polymorphism less awesome because of duck-typing
- Python uses the `duck-test` rule to bind operations to data
- duck-test: "If it walks like a duck and it quacks like a duck, then it must be a duck"
- to determine whether a function can be applied to a new type, we apply Python's fundamental rule of polymorphism, called duck typing rule: if all of the operations inside the function can be applied to the type, the function can be applied to the type
- it allows us to use *any* object that provides the required behavior without forcing it to be a subclass
- `FlacFile` doesn't inherit from AudioFile but it can be interacted with using the exact same interface!


```python
# behaves just like any other music file type...
class FlacFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == '.flac':
            raise ValueError('Not a .flac file')
        self.filepath = filepath
        
    def play(self) -> None:
        # implement of .flac play
        print(f'playing {self.filepath} as FLAC')
```


```python
f = FlacFile(Path('NeverGiveup.flac'))
f.play()
```

    playing NeverGiveup.flac as FLAC



```python
def play_music(player: AudioFile) -> None:
    player.play()
```


```python
play_music(f)
```

    playing NeverGiveup.flac as FLAC



```python
type(f)
```




    __main__.FlacFile



## Mixin Design Pattern

- **Mixin** is the simplest and most useful form of multiple inheritance
- a mixin class is not meant to be instantiated, but is meant to be inherited by some other class
    - it is mixed in with other classes to extend their behavior
- the goal is to extend and provide extra functionality without worrying about the correctness of "is-a" relationship
- mixins are sometimes described as being "including" or "using" rather than "inheriting"
- mixins encourage code reuse and can be used to avoid the inheritance ambiguity that multiple inheritance can cause (**diamond problem**)
    - E.g., BirdMan class can use Bird class's `fly()` functionality as a mixin
- a mixin can also be viewed as an interface with implemented methods
- the following AsDictionaryMixin exposes `to_dict()` interface that returns the representation of itself as a dictionary
- Employee and Address are NOT AsDictionaryMixin, but both of them "use" AsDictionaryMixin mixin


```python
# Define a Mixin
class LoggingMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

# Define a Base Class
class Animal:
    def speak(self):
        pass

# Use the Mixin
class Dog(Animal, LoggingMixin):
    def speak(self):
        self.log("Dog is barking")
        return "Woof!"

# Usage
dog = Dog()
print(dog.speak())  # Output: [LOG]: Dog is barking \n Woof!
```

    [LOG]: Dog is barking
    Woof!



```python
# - using dictionary comprehension, `to_dict()` creates a dictionary by 
# mapping prop to value for each item in self.__dict__.items() if the prop is not an internal
class AsDictionaryMixin:
    # API to convert an object into dict representation
    def to_dict(self):
        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop)
        }

    def _represent(self, value):
        """ Recursively return string representation of value
        """
        if isinstance(value, object):
            if hasattr(value, 'to_dict'):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith('_')
```


```python
class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
```


```python
class Address(AsDictionaryMixin):
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)
```


```python
class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'John Smith',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Jane Doe',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': 'Robin Williams',
                'role': 'secretary'
            },
        ]
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        """ Return list of all employees
        """
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        """ Internal method to create Employee object
        """
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.get_role(id)
        return Employee(id, name, address, employee_role)
    
    def get_role(self, emp_id):
        """ Given emp_id, returns their role
        """
        for emp in self._employees:
            if emp['id'] == emp_id:
                return emp['role']
        raise ValueErorr(f'Employee id: {emp_id} not found in database!')
```


```python
class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            2: Address('67 Paperwork Ave', 'Manchester', 'NH', '03101'),
            3: Address('15 Rose St', 'Concord', 'NH', '03301', 'Apt. B-1'),
            4: Address('39 Sole St.', 'Concord', 'NH', '03301'),
            5: Address('99 Mountain Rd.', 'Concord', 'NH', '03301'),
        }

    def get_employee_address(self, employee_id):
        """ Given employee_id, return their address
        """
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(f'Employee_id: {employee_id}')
        return address
```


```python
import json

def print_dict(d):
    print(json.dumps(d, indent=2))

for employee in EmployeeDatabase().employees:
    print_dict(employee.to_dict())
```

    {
      "id": "1",
      "name": "Mary Poppins",
      "address": {
        "street": "121 Admin Rd.",
        "street2": "",
        "city": "Concord",
        "state": "NH",
        "zipcode": "03301"
      },
      "role": "manager"
    }
    {
      "id": "2",
      "name": "John Smith",
      "address": {
        "street": "67 Paperwork Ave",
        "street2": "",
        "city": "Manchester",
        "state": "NH",
        "zipcode": "03101"
      },
      "role": "secretary"
    }
    {
      "id": "3",
      "name": "Kevin Bacon",
      "address": {
        "street": "15 Rose St",
        "street2": "Apt. B-1",
        "city": "Concord",
        "state": "NH",
        "zipcode": "03301"
      },
      "role": "sales"
    }
    {
      "id": "4",
      "name": "Jane Doe",
      "address": {
        "street": "39 Sole St.",
        "street2": "",
        "city": "Concord",
        "state": "NH",
        "zipcode": "03301"
      },
      "role": "factory"
    }
    {
      "id": "5",
      "name": "Robin Williams",
      "address": {
        "street": "99 Mountain Rd.",
        "street2": "",
        "city": "Concord",
        "state": "NH",
        "zipcode": "03301"
      },
      "role": "secretary"
    }


## Inheritance Tax

- "You wanted a banana but what you got was a gorilla holding the banana and the entire jungle" - Joe Armstrong
- inheritance is a powerful tool but it can be misused
- alternatives may be better to avoid the inheritance tax:
    - interfaces and protocols
    - delegation
    - mixins
- interfaces and protocols give us polymorphism without inheritance
- delegation is a way to use composition instead of inheritance
- delegate to services - Has-A relationship Trumps Is-A relationship
- use mixins to share code and functionality


## Exercises

- solve the following Kattis problems using OOD
- must use inheritance (inheritance from built-in object doesn't count)

1. Statistics -  https://open.kattis.com/problems/statistics
2. Datum - https://open.kattis.com/problems/datum
3. Teque - https://open.kattis.com/problems/teque
    - OOD may be slower to pass all the test cases within 2 seconds!


```python

```
