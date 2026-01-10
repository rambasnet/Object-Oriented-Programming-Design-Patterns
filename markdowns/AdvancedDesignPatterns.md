# Advanced Design Patterns

- learn more design patterns with cannonical examples and Python way of implementing those patterns

- the Adapter pattern
- the Facade pattern
- Lazy initialization and the Flyweight pattern
- the Abstract Factory pattern
- the Compositie pattern
- the template pattern

## The Adapter pattern

- designed to interact with existing code
- adapters are used to allow two preexisting objects to work together
    - even their interfaces are not compatible
- just like the hardware adapter that helps two differnt devices talk to each other
    - adapter object sits between two interfaces/objects tranlating between them on the fly
- adapter may perform various tasks:
    - converting parameters to different formats
    - rearranging the order of arguments
    - calling a different named method
    - suppying default arguments
- conceptually, similar to the Decorator pattern
    - decorators provide the same interface that they replace
- example from: https://refactoring.guru/design-patterns/adapter/python/example


```python
class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")
    
```


```python
print("Client: I can work just fine with the Target objects:")
target = Target()
client_code(target)
print("\n")
```

    Client: I can work just fine with the Target objects:
    Target: The default target's behavior.
    



```python
adaptee = Adaptee()
print("Client: The Adaptee class has a weird interface. "
      "See, I don't understand it:")
print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

```

    Client: The Adaptee class has a weird interface. See, I don't understand it:
    Adaptee: .eetpadA eht fo roivaheb laicepS
    



```python
print("Client: But I can work with it via the Adapter:")
adapter = Adapter()
client_code(adapter)
```

    Client: But I can work with it via the Adapter:
    Adapter: (TRANSLATED) Special behavior of the Adaptee.

## The Façade pattern

- https://refactoring.guru/design-patterns/facade
- Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes

- example see `plantuml/main.py`
    - must install graphviz, java runtime - see details here https://plantuml.com/starting
    - download `plantuml.jar` file
    - .uml files are in `plantuml/data` folder


```python

```
