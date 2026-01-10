## SOLID principle

- a popular software design principle using OOP
- must know it by heart!
- it's a great starting point of OOD

### S: Single Responsibility Principle (SRP)

- a class should have one responsibility
- "one and only reason" to change when the requirements change
- a class should have a single, well-defined purpose; should be responsible for one aspect of the system's functionality

#### How to Achieve the Single Responsibility Principle:

- **Identify Responsibilities**:
    - carefully analyze the responsibilities of each class in your design

- **Separate Concerns**: 
    - if a class has multiple responsibilities, break it down into smaller classes, each with a single responsibility
    
- **Use Cohesion**:
    - aim for high cohesion within classes, meaning that all the elements within a class should be related to its single responsibility
    
- **Avoid God Objects**:
    - "God objects" are classes that try to do everything
    
- **Refactor**: 
    - if you find that a class is violating the SRP, refactor it to separate its responsibilities
    
#### What does "reason to change" mean?

- A "reason to change" refers to a specific actor or requirement that could cause the class to be modified; e.g.:

    - A class that handles both data persistence and user interface logic has two reasons to change: changes in the database schema and changes in the UI design
    - A class that both calculates employee salary and generates reports has two reasons to change: changes in salary calculation rules and changes in report formatting


```python
# violates SRP

class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        # Calculate employee pay
        pass

    def generate_report(self):
        # Generate employee report
        pass

    def save_to_database(self):
        # Save employee data to database
        pass
```


```python
# adheres to SRP by refactoring the God class into three separate classes

class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

class PayCalculator:
    def calculate_pay(self, employee: Employee):
        # Calculate employee pay
        pass

class ReportGenerator:
    def generate_report(self, employee: Employee):
        # Generate employee report
        pass

class EmployeeRepository:
    def save_to_database(self, employee: Employee):
        # Save employee data to database
        pass

    
```

### O: Open/Closed Principle (OCP)

- "Software entities (packages, modules, classes, functions, etc.) should be open for extension, but closed for modification."
- Open for Extension: 
    - you should be able to add new functionality to your software without changing the existing code
    
- Closed for Modification
    - once a piece of code is written and tested, you shouldn't need to modify its source code to accommodate new requirements
    
#### Why is this important?

- reduced risk of introducing bugs
    - modifying existing code can introduce unintended side effects and break working functionality
    - by extending instead of modifying, you minimize this risk
    
- increased maintainability
    - code that adheres to the OCP is easier to maintain and adapt to changing requirements

- improved reusability
    - well-designed, extensible code can be reused in different parts of your application or in other projects
    
- enhanced stability
    - stable, unmodified code provides a reliable foundation for building new features
    
#### How to Achieve the Open/Closed Principle:

- common techniques for achieving the OCP include:

- **Abstraction**: 
    - using abstract classes or interfaces to define a contract that concrete classes must adhere to
    
- **Inheritance**: 
    - creating new classes that inherit from existing classes and override or extend their behavior

- **Polymorphism**: 
    - writing code that can work with objects of different types through a common interface
    
- **Composition**: 
    - building complex objects by combining simpler objects, rather than inheriting from them
    
- **Design Patterns**: 
    - using design patterns like the Strategy, Template Method, and Observer patterns, which are specifically designed to promote extensibility


```python
# Violation of Open/Closed Principle

class Shape:
    def __init__(self, sh_type, width, height=None):
        self.type = sh_type
        self.width = width
        self.height = height

    def calculate_area(self):
        if self.type == "rectangle":
            return self.width * self.height
        elif self.type == "circle":
            return 3.14159 * (self.width / 2) ** 2  # Assuming width is diameter
        # If we add a new shape (e.g., triangle), we have to modify this function!

# Usage examples
print("--- Violation of OSP Principle ---")
rectangle = Shape("rectangle", 5, 10)
circle = Shape("circle", 6)
print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Circle area: {circle.calculate_area()}")
```


```python
# Correct implementation using Open/Closed Principle

# Shape Interface
class ShapeCorrect:
    def area(self):
        raise NotImplementedError

# Extend with Rectangle
class RectangleCorrect(ShapeCorrect):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Extend with Circle
class CircleCorrect(ShapeCorrect):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

# Extend with Triangle
class TriangleCorrect(ShapeCorrect):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```


```python
print("--- Correct Implementation adhering to Open/Closed Principle ---")
rectangle_correct = RectangleCorrect(5, 10)
circle_correct = CircleCorrect(3)
triangle_correct = TriangleCorrect(4, 6)

print(f"Rectangle area: {rectangle_correct.area()}")
print(f"Circle area: {circle_correct.area()}")
print(f"Triangle area: {triangle_correct.area()}")
```

### L: Liskov Substitution Principle (LSP)

- states that **inheritance** must follow LSP - Liskov Substitution principle
- named after Barbara Liskov creator of CLU programming language
- any subclass can be substituted for its superclass
    - any code that uses superclass can be replaced with it's subclass without breaking any code!
    - the inverse is not true!


```python
# Violation of Liskov Substitution Principle

class Rectangle:
    # make sure no dynamic attibute are allowed!
    __slots__ = ['_width', '_height']
    
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def area(self):
        return self._width * self._height

# Square is a special case of rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        # _width and _height are equal!
        return self._width
    
    # ensure both sides are equal
    @side.setter
    def side(self, side):
        self._width = side
        self._height = side
        
    @Rectangle.width.setter
    def width(self, width):
        self.side = width
        
    @Rectangle.height.setter
    def height(self, height):
        self.side = height

def calculate_area_rect(obj: Rectangle):
    # this function assumes it can change properties of rectangle!
    obj.width = 5
    obj.height = 4
    return obj.area()

print("--- Violation of LSP ---")
square = Square(2)
print(f"Square area: {calculate_area_rect(square)}") #incorrect ?
# can't subsititute Square with Rectangle
rect = Rectangle(2, 3)
print(f"Rectangle area: {calculate_area_rect(rect)}") #correct
```


```python
def calculate_area_sq(obj: Square):
    # assumes it can change property of Square
    obj.side = 5
    return obj.area()
```


```python
print("--- Violation of LSP ---")
square = Square(2)
print(f"Square area: {calculate_area_sq(square)}") #correct
```


```python
# can't subsititute Rectangle for Square
rect = Rectangle(2, 3)
print(f"Rectangle area: {calculate_area_sq(rect)}") #AttributeError
```


```python
# Correct implementation using Liskov Substitution Principle

class Shape:
    # no dynamic attributes are allowed!
    __slots__ = []
    
    def area(self):
        raise NotImplementedError

class RectangleCorrect(Shape):
    __slots__ = ['_width', '_height']
    
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def area(self):
        return self._width * self._height

class SquareCorrect(Shape):
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        self._side = side

    def area(self):
        return self._side ** 2

```


```python
def calculate_area_correct(shape: Shape):
    # no assumption of attributes of shape!
    # shape.side = 10 # AttributeError
    return shape.area()

print("\n--- Correct Implementation adheres to LSP ---")
rectangle_correct = RectangleCorrect(2, 3)
square_correct = SquareCorrect(2)
print(f"Rectangle area: {calculate_area_correct(rectangle_correct)}")
print(f"Square area: {calculate_area_correct(square_correct)}")
```

    
    --- Correct Implementation adheres to LSP ---
    Rectangle area: 6
    Square area: 4


### I: Interface Segregation - ISP

- a class should have the smallest interface possible
- classes should be relatively small and isolated

#### Core Idea

- the ISP states that "clients should not be forced to depend on interfaces they do not use."
- it advocates for creating smaller, more specific interfaces rather than large, general-purpose ones
- it reduces coupling
    - when interfaces are smaller and more focused, classes that implement them only need to depend on the methods they actually use
    - this reduces unnecessary dependencies between classes
- in the following example Robot is forced to implement eat method; though robot doesn't eat!


```python
# Violation of Interface Segregation Principle

class Worker:
    def work(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

class Human(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        # Robots don't eat, but we're forced to implement this method
        raise NotImplementedError("Robots don't eat!")

```


```python
# Usage examples
print("--- Violation of ISP ---")
human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
#robot.eat() # raises NotImplementedError
try:
  robot.eat() #raises NotImplementedError
except NotImplementedError as e:
  print(f'Error: {e}')
```

    --- Violation of ISP ---
    Human working
    Human eating
    Robot working
    Error: Robots don't eat!



```python
# Correct implementation using Interface Segregation Principle
class Workable:
    def work(self):
        raise NotImplementedError

# Eatable interface class
class Eatable:
    def eat(self):
        raise NotImplementedError

# uses Workable and Eatble class interfaces
class HumanCorrect(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

# only uses Workable interfaces
class RobotCorrect(Workable):
    def work(self):
        print("Robot working")
```


```python
print("\n--- Correct Implementation adhering ISP ---")
human_correct = HumanCorrect()
human_correct.work()
human_correct.eat()

robot_correct = RobotCorrect()
robot_correct.work()

# robot_correct.eat() would cause an error, because robot_correct does not implement Eatable.
```

    
    --- Correct Implementation adhering ISP ---
    Human working
    Human eating
    Robot working


### D: Dependency Inversion Principle (DIP)

- convert bad dependency relationships into good ones
- if two classes depend on each other, use a mixin class/interface to reuse the dependence

#### Core Idea

- high-level modules should not depend on low-level modules. Both should depend on abstractions

- abstractions should not depend on details. Details (concrete implementations) should depend on abstractions

- aids in decoupling of components by reducing the tight coupling between modules/components/classes, meaning changes in low-level modules are less likely to affect high-level modules
- in the following example:
    - the high-level Switch class directly depends on the concrete low-level LightBulb class
    - if we wanted to control a different device (e.g., a fan), we would have to modify the Switch class, which violates the DIP


```python
# Violation of Dependency Inversion Principle
# Low-level LighBulb class
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on...")

    def turn_off(self):
        print("LightBulb: Bulb turned off...")

# Switch depends on LightBulb 
# what if you want to use switch to a Fan
class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def operate(self, command):
        if command == "ON":
            self.bulb.turn_on()
        elif command == "OFF":
            self.bulb.turn_off()

# Usage
bulb = LightBulb()
switch = Switch(bulb)
switch.operate("ON")
switch.operate("OFF")
```

    LightBulb: Bulb turned on...
    LightBulb: Bulb turned off...



```python
# Correct implementation using Dependency Inversion Principle
# Abstraction (Interface)
class Switchable:
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

# Low level class LightBulb
class LightBulbCorrect(Switchable):
    def turn_on(self):
        print("LightBulbCorrect: Bulb turned on...")

    def turn_off(self):
        print("LightBulbCorrect: Bulb turned off...")

# Low level, new device implementation
class Fan(Switchable):
    def turn_on(self):
        print("Fan: Fan turned on...")

    def turn_off(self):
        print("Fan: Fan turned off...")

# High level module
class SwitchCorrect:
    # depend on abstraction
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self, command):
        if command == "ON":
            self.device.turn_on()
        elif command == "OFF":
            self.device.turn_off()

# Usage correct implementation
bulb_correct = LightBulbCorrect()
fan = Fan()

switch_correct_bulb = SwitchCorrect(bulb_correct)
switch_correct_fan = SwitchCorrect(fan)

switch_correct_bulb.operate("ON")
switch_correct_bulb.operate("OFF")

switch_correct_fan.operate("ON")
switch_correct_fan.operate("OFF")
```

    LightBulbCorrect: Bulb turned on...
    LightBulbCorrect: Bulb turned off...
    Fan: Fan turned on...
    Fan: Fan turned off...



```python

```
