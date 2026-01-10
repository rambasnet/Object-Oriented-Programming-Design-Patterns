# Common Design Patterns

- learn some common design patterns and how they're implemented in Python
- topics:
    - the Singleton pattern
    - the Decorator pattern
    - the Iterator pattern
    - the Observer pattern
    - the Strategy pattern
    - the Command pattern
    - the State pattern

## The Observer pattern

- useful for state monitoring and event-handling situations
- pattern allows a given object to be monitored by an unknown and dynamic group of *observer* objects
- the core object being observed needs to implement an interface that makes it *observable*
- whenever a value on the core object changes, it lets all the observer objects know that a change has occurred
    - by calling a method announcing the changes
- widely used in GUIs

![Observer pattern](resources/observer_pattern.png)

- at a high level, the pattern is also called `Publisher-Subscriber` model
    - Publisher/Subject is observed by many objects called Subscriber 
    - any changes in the state of the Subject/Publisher are notified to the subscribers
- observer pattern example using dice game: Zonk or Zilch or Ten Thousand
- see `src/design_patterns/inventory.py` that implements an observer pattern for the dice game

### Pros

- **Open/Closed Principle**
    - open for extension but closed for modification
    - introducing new subscriber classes is much easier without making changes in existing publisher or observers' code
- **Establishes Relationships**
    - easily establishes and describes the relationships among objects during the runtime between the objects


### Applications

- **Multi-dependency**:
    - when multiple objects are dependent on the state of one object
- **Getting Notifications**
    e.g., social media, RSS feeds, email subscription
- **Reflections of Object**
     - objects are loosely coupled, the change of a state in one object must be reflected in another object

- in the following e.g., every time the publisher changes its data, the subscribers are notified


```python
class Publisher:
    def __init__(self):
        self._observers = []
 
    def notify(self, modifier = None):
        """ Notify the observers and not the modifier """
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
 
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
 
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
        
class Data(Publisher):
    """ Monitor the object"""
    
    def __init__(self, name = ''):
        super().__init__()
        self.name = name
        self._data = 0
 
    @property
    def data(self):
        return self._data
 
    @data.setter
    def data(self, value):
        """ Notify all subscribers when _data is set """
        self._data = value
        self.notify()
```


```python
# create observers/subscribers

class HexViewer:
    """ Updates the Hexviewer. """
    
    def update(self, subject):
        print(f'HexViewer: Subject {subject.name} has data 0x{subject.data:x}')
 

class OctalViewer:
    """ Updates the Octal viewer. """
 
    def update(self, subject):
        print(f'OctalViewer: Subject {subject.name} has data {oct(subject.data)}')
 

class DecimalViewer:
    """ Updates the Decimal viewer. """
 
    def update(self, subject):
        print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))
```


```python
pub1 = Data('Publisher 1')
```


```python
subs1 = DecimalViewer()
subs2 = HexViewer()
subs3 = OctalViewer()
```


```python
pub1.attach(subs1)
pub1.attach(subs2)
pub1.attach(subs3)
```


```python
pub1.data = 10
```

    DecimalViewer: Subject Publisher 1 has data  10
    HexViewer: Subject Publisher 1 has data 0xa
    OctalViewer: Subject Publisher 1 has data 0o12


## The Strategy pattern

- see this resource: [https://refactoring.guru/design-patterns/strategy](https://refactoring.guru/design-patterns/strategy)
- common demonstration of abstraction in OOP
- pattern implements different solutions to a single problem, each in a different object
- the core class can then choose the most appropriate implementation dynamically at runtime
    - usually, different algorithms have different tradeoffs
    - e.g., faster, more RAM, distributed systems, etc.
    
![Strategy pattern](resources/strategy_pattern.png)
- see `src/design_patterns/image_filler.py` for example
- need to install `pillow` third-party library to manipulate images
    - `pillow` is already installed in the Docker image
    - however, the demo doesn't work in Docker as it requires X-Server

```python
python image_filer.py
```


```python
! python -m pip install pillow
```


```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))
    
```


```python
context = Context(ConcreteStrategyA())
print("Client: Strategy is set to normal sorting.")
context.do_some_business_logic()
print()

print("Client: Strategy is set to reverse sorting.")
context.strategy = ConcreteStrategyB()
context.do_some_business_logic()
```

    Client: Strategy is set to normal sorting.
    Context: Sorting data using the strategy (not sure how it'll do it)
    a,b,c,d,e
    
    Client: Strategy is set to reverse sorting.
    Context: Sorting data using the strategy (not sure how it'll do it)
    e,d,c,b,a


## The Command pattern

- the UML diagram of the command pattern looks similar to the strategy pattern
- this pattern generally involves a hierarchy of classes that each do something
- a Core class can create a command (or a sequence of commands) to carry out actions
- the pattern can be viewed as a collaboration between a "passive" observer and the more "active" Commander
- A commander will be actively making state changes in other objects
- An observer is notified that something has changed
    - behaves somewhat like an observer pattern
    
![Command pattern](resources/command_pattern.png)


```python
# Conceptual example from: https://refactoring.guru/design-patterns/command/python/example
from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass
    
    
class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")
        

class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other
    objects, called "receivers."
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)
        

class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")
        
    
class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


```


```python
"""
The client code can parameterize an invoker with any commands.
"""

invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))
```


```python
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(
    receiver, "Send email", "Save report"))
```


```python
invoker.do_something_important()
```

    Invoker: Does anybody want something done before I begin?
    SimpleCommand: See, I can do simple things like printing(Say Hi!)
    Invoker: ...doing something really important...
    Invoker: Does anybody want something done after I finish?
    ComplexCommand: Complex stuff should be done by a receiver object
    Receiver: Working on (Send email.)
    Receiver: Also working on (Save report.)

## The State pattern

- lets an object alter its behavior when its internal state changes
- based on the concept of **Finite State Machine**
- see this article: https://refactoring.guru/design-patterns/state
- the goal is to represent state transition systems:
    - systems where an object's behavior is constrained by the state it's in
    - there are narrowly defined transitions to other states
- there's a manager/context class that provides an interface for switching states
    - this class contains a pointer to the current state
- each state knows what other states will be allowed to transition to

![State pattern](resources/state_pattern.png)
- applications:
    - parsing text such as JSON, XML, HTML, YAML, etc.
    - parsing and interpreting/compiling programming languages


```python
from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. 
    It also maintains a reference to an instance of a State 
    subclass, which represents the current state of the Context.
    """
    _state = None
    
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior 
    to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""
class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())

```


```python
context = Context(ConcreteStateA())
context.request1()
context.request2()
```

    Context: Transition to ConcreteStateA
    ConcreteStateA handles request1.
    ConcreteStateA wants to change the state of the context.
    Context: Transition to ConcreteStateB
    ConcreteStateB handles request2.
    ConcreteStateB wants to change the state of the context.
    Context: Transition to ConcreteStateA


### IoT Example

- parging data from GPS statement
- GPS uses NMEA 0183 language from the National Marine Electronics Association
- a typical message looks like:
```
 $GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A*41
 ```

| value | meaning |
| :--- | :--- |
| \$ | Starts the sentence |
| GPGLL | The "talker," GP, and the type of message, GLL |
| 3723.2475 | Latitude, 37°23.2475 |
| N | North of the equator |
| 12158.3416 | Longitude, 121°58.3416 |
| W | West of the 0° meridian |
| 161229.487 | The timestamp in UTC: 16:12:29.487 |
| A | Status, A=valid, V=not valid |
| A | Mode, A=Autonomous, D=DGPS, E=DR |
| * | Ends the sentence, starts the checksum |
| 41 | Hexadecimal checksum of the text (excluding the \$ and \* characters) |



```python
# let's see the provided demo in nmesa_state.py module
! cat src/design_patterns/nmea_states.py
```

    """
    Python 3 Object-Oriented Programming
    
    Chapter 11. Common Design Patterns
    """
    from __future__ import annotations
    from typing import Optional, Iterable, Iterator, cast
    
    
    class NMEA_State:
        def __init__(self, message: "Message") -> None:
            self.message = message
    
        def feed_byte(self, input: int) -> "NMEA_State":
            return self
    
        def valid(self) -> bool:
            return False
    
        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self.message})"
    
    
    class Waiting(NMEA_State):
        def feed_byte(self, input: int) -> NMEA_State:
            if input == ord(b"$"):
                return Header(self.message)
            return self
    
    
    class Header(NMEA_State):
        def __init__(self, message: "Message") -> None:
            self.message = message
            self.message.reset()
    
        def feed_byte(self, input: int) -> NMEA_State:
            if input == ord(b"$"):
                # Reset any accumulated bytes
                return Header(self.message)
            size = self.message.body_append(input)
            if size == 5:
                return Body(self.message)
            return self
    
    
    class Body(NMEA_State):
        def feed_byte(self, input: int) -> NMEA_State:
            if input == ord(b"$"):
                return Header(self.message)
            if input == ord(b"*"):
                return Checksum(self.message)
            self.message.body_append(input)
            return self
    
    
    class Checksum(NMEA_State):
        def feed_byte(self, input: int) -> NMEA_State:
            if input == ord(b"$"):
                return Header(self.message)
            if input in {ord(b"\n"), ord(b"\r")}:
                # Incomplete checksum... Will be invalid.
                return End(self.message)
            size = self.message.checksum_append(input)
            if size == 2:
                return End(self.message)
            return self
    
    
    class End(NMEA_State):
        def feed_byte(self, input: int) -> NMEA_State:
            if input == ord(b"$"):
                return Header(self.message)
            elif input not in {ord(b"\n"), ord(b"\r")}:
                return Waiting(self.message)
            return self
    
        def valid(self) -> bool:
            return self.message.valid
    
    
    class Message:
        def __init__(self) -> None:
            self.body = bytearray(80)
            self.checksum_source = bytearray(2)
            self.body_len = 0
            self.checksum_len = 0
            self.checksum_computed = 0
    
        def reset(self) -> None:
            self.body_len = 0
            self.checksum_len = 0
            self.checksum_computed = 0
    
        def body_append(self, input: int) -> int:
            self.body[self.body_len] = input
            self.body_len += 1
            self.checksum_computed ^= input
            return self.body_len
    
        def checksum_append(self, input: int) -> int:
            self.checksum_source[self.checksum_len] = input
            self.checksum_len += 1
            return self.checksum_len
    
        @property
        def valid(self) -> bool:
            return (
                self.checksum_len == 2
                and int(self.checksum_source, 16) == self.checksum_computed
            )
    
        def header(self) -> bytes:
            return bytes(self.body[:5])
    
        def fields(self) -> list[bytes]:
            return bytes(self.body[: self.body_len]).split(b",")
    
        def __repr__(self) -> str:
            body = self.body[: self.body_len]
            checksum = self.checksum_source[: self.checksum_len]
            return f"Message({body}, {checksum}, computed={self.checksum_computed:02x})"
    
        def message(self) -> bytes:
            return (
                b"$"
                + bytes(self.body[: self.body_len])
                + b"*"
                + bytes(self.checksum_source[: self.checksum_len])
            )
    
    
    class Reader:
        def __init__(self) -> None:
            self.buffer = Message()
            self.state: NMEA_State = Waiting(self.buffer)
    
        def read(self, source: Iterable[bytes]) -> Iterator[Message]:
            for byte in source:
                self.state = self.state.feed_byte(cast(int, byte))
                if self.buffer.valid:
                    yield self.buffer
                    self.buffer = Message()
                    self.state = Waiting(self.buffer)
    
    
    test_reader = """
    >>> message = b'''
    ... $GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18
    ... $GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A*41
    ... '''
    >>> rdr = Reader()
    >>> result = list(rdr.read(message))
    >>> result
    [Message(bytearray(b'GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000'), bytearray(b'18'), computed=18), Message(bytearray(b'GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A'), bytearray(b'41'), computed=41)]
    >>> result[0].message()
    b'$GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18'
    >>> result[1].message()
    b'$GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A*41'
    >>> result[0].fields()
    [b'GPGGA', b'161229.487', b'3723.2475', b'N', b'12158.3416', b'W', b'1', b'07', b'1.0', b'9.0', b'M', b'', b'', b'', b'0000']
    >>> result[1].fields()
    [b'GPGLL', b'3723.2475', b'N', b'12158.3416', b'W', b'161229.487', b'A', b'A']
    
    """
    
    
    __test__ = {name: case for name, case in globals().items() if name.startswith("test_")}



```python
from src.design_patterns.nmea_states import Reader
```


```python
message = b'''
$GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18
$GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A*41
'''
```


```python
rdr = Reader()
```


```python
result = list(rdr.read(message))
```


```python
result
```




    [Message(bytearray(b'GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000'), bytearray(b'18'), computed=18),
     Message(bytearray(b'GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A'), bytearray(b'41'), computed=41)]



## Summary

- The decorator pattern is often implemented using Python's more generic decorator syntax
    - `@wraps`
    - useful pattern to extend the functionality of a function or class without modifying the code being decorated
- the Observer pattern is a useful way to decouple events from actions taken on those events
- the Strategy pattern allows different algorithms to be chosen to accomplish the same task
- the Command pattern helps us design active classes that share a common interface but carry out distinct actions
- the Single pattern, popular in some statically typed languages, is almost always an anti-pattern in Python


```python

```
