# Object-Oriented Design

- Topics
    1. object-oriented definition
    2. difference between OOP and OOD
    3. the basic principles of object-oriented design
    4. basic UML and when it isn't evil

## Object Oriented
- Objects - real-world things that can be felt, touched, sensed, manipulated, etc.
- Software objects are not tangible, but they're models of the real-world objects
- object is a collection of **data** called **state** and associated **behaviors** called **methods** that act upon the data

## Object-oriented analysis (OOA)

- analyzing software design; modeling problems, tasks, or a system as software objects and their interactions
- part of software requirement analysis to understand what needs to be done and how
- find out what features that users/actors/stakeholders of the software need to solve the problem
- this phase of software engineering may be better called *object-oriented exploration*
- gather requirements, interview clients, understand business logic, etc.

## Object-oriented design (OOD)

- the process of converting requirements into an implementation specification
- name the objects, define the behaviors, and their interactions with each other
- transforming *what* should be done into *how* using OOP

## Objects and Classes
- *object* is a collection of data with associated behaviors
- *class* is a kind or *type* of object
- Unified Modeling Language (UML) is commonly used to design the classes and their interactions

## Object-oriented programming (OOP)
- process of converting a design into a working program that does what the product owner originally requested
- use OOP concepts to implement the OOD

## Software Development Models
- some popular development models are: **waterfall**, **iterative**, **agile**, etc.
- **waterfall** is the traditional model where each phase is completed before the next phase begins
- **agile** is a more modern model where focus is on delivering working software in short iterations
    - ci-cd (continuous integration, continuous deployment) is a popular agile model
    - scrum, kanban, pair programming, etc. are popular agile methodologies
    - focus is on delivering working software quickly and frequently as a team effort with high customer satisfaction


## Object members

- objects have members: 
    1. variables/attributes/states
    2. behaviors/functions
- a class instance is a specific object with its own set of data/attributes and behaviors (functions)

## Object attributes/states

- objects have states; depicted by the value of specific attributes
    - Orange has a state e.g., ripe or raw
- attributes are frequently referred to as **members** or **properties** or **instance variables**
- some may use strict rules that **attributes** are settable/read-write while **proerties** are *read-only*
- Python doesn't have a concept of *constant* to make properties read-only; here use attributes and properties interchangeably
- the following UML diagram depicts classes with attributes
![](resources/UML-attributes.png)

- the following figure is more detailed with Python-specific type hints
![](resources/UML-type-hints.png)

## Object behaviors

- behaviors/methods/functions are actions that occur on object
- like functions, methods accept **parameters** and may **return values**
- each method performs certain tasks or change the internal state of the object using the data passed as parameters and return the results of the tasks
- UML showing the behaviors/actions:
![](resources/UML-behaviors.png)

## Hiding details and creating the public interface (API)

- the key purpose of modeling an object in OOD is to determine the public interface of that object
- interface is the collection of attributes and methods that other objects can access to interact with that object
- other objects do not need and are not allowed, to access the internal workings of the object
- E.g., real-world example of working of TV and remote
- this technique of hiding the internal details is called **information hiding** or broadly **encapsulation**
- proper design of the public interface is very important in software design as many other objects may depend on just those interfaces to interact with the objects and changing them often may be difficult
- the interface is designed with ease of use in mind (KISS principle) and NEVER ease of implementation

## Abstraction
- another key OOD term related to information hiding and encapsulation
- abstraction means dealing with the level of detail that is most appropriate to a given task
- the process of extracting a public interface from inner details
    - e.g., a car's driver needs to interact with the steering wheel, accelerator, and brakes; everything else under the hood is ignored
    - mechanic works at a different level of abstraction
- UML depicting different levels of abstractions for different actors
![](resources/UML-abstraction.png)

## Class relationship types
- there are three types of class relationships: 
    1. **Association**
    2. **Composition**
    3. **Aggregation**
- Association is the simplest of the relationship that tells how the objects are related
    - e.g., many apples go into a barrel
    - any one orange can go into exactly one basket
    - a basket can hold many oranges


## Composition

- important OOD principle; many design patterns use it
- composition is: **has-a** relationship
- act of collecting several objects together to create a new one
- composition is a good choice when one object is a part of another object
    - e.g., a fossil-fueled car is composed of an engine, transmission, starter, headlights, windshields, and dashboard, among many other parts
    - engine in turn is composed of a crankshaft, valves, pistons, etc.
- an aggregate relationship is more general
- a composite relationship is also an aggregate relationship but not vice versa    

### Difference between composition and aggregation

- the lifespan of objects can help differentiate the two relationships:
    1. if the composite (outside) object controls when the related (inside) objects are created and destroyed, the composition is most suitable
    2. if the related object is created independently of the composite object, or can outlast that object, an aggregate relationship makes more sense
    
### Designing a computer-based Chess game

- define the game of *Chess* - gather the requirements
- *italicized* words are objects/nouns/attributes and **bold** faced words are verbs/behaviors
- a *game* of chess is **played** between two *players*
- *Chessboard* is 8x8 grid containing 64 *positions*
- *board* contains two sets of 16 *pieces* that can be **moved**
- *player* alternate *turns*
- each *piece* can **take** other piece
- *board* will be required to **draw** itself on the computer *screen* after each turn
- the following is the UML object/instance diagram representing a Chess system at a specific state in time

![](resources/UML-chess.png)

![](resources/UML-chess-class.png)

### Aggregation and Composition in Chess Game

- Chess set is an **aggregate** of 16 chess pieces and 1 chessboard
    - when the chessboard is deleted, chess pieces may remain
      
- a chessboard is **composed** of 64 chess positions
    - when the chessboard is deleted, chess positions are also deleted


## Inheritance
- the **is-a** relationship is formed by inheritance, e.g.
    - Deep Blue is a chess player
    - Gary Kasparov is a player
- inheritance is modeled from biology
- child class inherits members of parent class similar to genotype and phenotype inheritance in biology
- in Chess set, among 32 pieces, there are only six different types of pieces (pawns, rooks, bishops, knights, king, and queen)
- a powerful tool for extending behavior and reusing features
- the following UML diagram shows, how 6 types of pieces can inherit from a Piece class

![](resources/UML-inheritance.png)

## Multiple inheritance
- just like in the biological world, in Python, a child class can inherit features from multiple parent classes
- multiple inheritance can be tricky and messy
    - Java doesn't support it

![Multiple Inheritance](resources/MultipleInheritance.png)


```python

```
