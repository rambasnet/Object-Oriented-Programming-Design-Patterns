## Unified Modeling Language (UML)

- used while explaining classes and their relationships
- can help us examine a problem from various angles
    - understand and describe the problem diagrammatically
- can be used as the document for the design phase
    - can be cumbersome to update UML if you use *agile/iterative* software engineering model instead of *waterfall/cascading* model
- provides a common language to talk among developers, managers, designers, clients, etc.
    - fairly intuitive to visually understand the big picture of the project
- this resource provides a good overview of UML - [https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-uml/](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-uml/)
- this resource provides a tool to generate UML diagrams: https://plantuml.com/ automatically
    - textbook authors used **plantuml** to generate all the UML diagrams

## 4+1 Views

- we can create a collection of diagrams using UML to help depict and summarize the software we're going to build
- provides high-level views of the complete architecture of a software product
- the views are used to describe the system from the viewpoint of different stakeholders, such as end-users, developers, system engineers, and project managers, project owners, etc.

### Logical View

- a logical view of the data entities, their static attributes, and their relationships
- the heart of object-oriented design
- concerned with the functionalities the software provides to the end users

### Process View

- describes how the data is processed or essentially describes the runtime behavior of the system 
- can be of a variety of forms: state models, activity diagrams, and sequence diagrams
- addresses concurrency, distribution, integrator, performance, and scalability, etc.

### Development View

- shows relationships among software components
- can be used to show how class definitions are gathered into modules and packages
- aka **implementation view** illustrates the programmer's perspective and is concerned with software management

### Physical View

- view of the application to be integrated and deployed
- if the application follows a well-known common design pattern, a sophisticated physical view diagram isn't necessary
- otherwise, a diagram is essential to show how a collection of components is integrated and deployed
- depicts the software from the system engineer's point of view

### Context View

- provides a unifying context for the previous four views
- often describes the actors that use (or interact) with the system to be built
- can involve human actors as well as automated interfaces outside the system
- the system must respond to these external actors
- can also be called **scenarios or use case view** or system design view (a big picture view)


## Example UML diagrams show OOD for Fruit Inventory
![](resources/UML-class.png)
- rectangular box represents a class
- line shows the *association* between two classes
- the following is a better UML diagram
- shows the proper relationships
  
![](resources/UML-relationship.png)

- use plantuml - https://plantuml.com/
- must create description file
    - see guide for syntax - https://plantuml.com/guide
    - shows how to create plantuml description files
- can use plantuml from local Terminal to generate diagrams or VS Code extension

### VS Code Extension

- install VS Code extension by jebbs - https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml
- allows to preview UML diagrams using local or remote render
- install recommended libraries following the extension documentation
- configure the extension
    - search for `PlantUML` in Extensions and click on `Settings` menu
    - click `Workspace` tab set PlantUML: Render to `Remote`
    - click `Workspace` tab set PlantUML: Output Format to `png`
    - enter server URL: `http://www.plantuml.com/plantuml` in PlantUML: Server
- to render UML diagrams:
- on VS Code, create .plantuml file and enter `option+D` (Mac) or `alt+D` (Win)
- to save image file:
    - enter command+P and > PlantUML: Export Current Diagram and pick image type
    
### Local System and Makefile

- to render UML images locally, must install **Java** runtime and **Graphviz** library
- follow the instruction for your platform here - https://plantuml.com/starting
- on a local Terminal type the following command
- you must also download plantuml.jar file

```bash
java -jar <path_to_plantuml.jar> <folder/file.plantuml>
```
- it automatically creates <file_name>.png in the same folder where <file_name>.plantuml file is

- see Makefile for demo: `demo-assignments/A1-OOP/Makefile`
- to render UML diagrams run the following commands from the Terminal

```bash
cd demo-assignments/A1-OOP/Makefile
make create-uml
```


