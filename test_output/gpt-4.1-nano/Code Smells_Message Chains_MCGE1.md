# Code Review: MCGE1.java

- **Code smell no.** - 1
- **Code smell name** - Data Class
- **Code smell description** - Classes primarily used to store data with minimal or no behavior, exposing fields directly or through simple getters/setters, leading to an anemic object model.
- **Found in line no.** - 5-12, 21-28, 41-52, 78-82
- **Possible treatments** - Encapsulate Field, Encapsulate Collection, Move Method and Extract Method, Remove Setting Method and Hide Method
- **Possible solution** - Refactor classes to include behavior relevant to their data, encapsulate the fields, and add methods that operate on the data to promote better object-oriented design.

- **Code smell no.** - 2
- **Code smell name** - Long Method
- **Code smell description** - Methods that are excessively long making understanding and maintaining them difficult.
- **Found in line no.** - 65-71 (`printOrderDetails`)
- **Possible treatments** - Extract Method, Extract Method & then Move Method
- **Possible solution** - Break down `printOrderDetails()` into smaller, well-defined methods such as `printOrderNumber()`, `printItems()`, `printPersonDetails()`, etc.

- **Code smell no.** - 3
- **Code smell name** - Primitive Obsession
- **Code smell description** - Use of primitive data types (like String for address components or order status) instead of dedicated value objects which can lead to fragile code and duplicated logic.
- **Found in line no.** - 9-12, 15-17, 22-28, 50-51
- **Possible treatments** - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object
- **Possible solution** - Create dedicated classes for OrderStatus, or Address components, replacing strings with enums or value objects for better type safety and clarity.

- **Code smell no.** - 4
- **Code smell name** - Long Parameter List
- **Code smell description** - Methods or constructors that take many parameters, reducing readability and increasing error-prone code.
- **Found in line no.** - 25-29, 46-52
- **Possible treatments** - Replace Parameter with Method Call, Preserve Whole Object, Introduce Parameter Object
- **Possible solution** - Use parameter objects such as `OrderDetails` encapsulating multiple parameters for constructors or methods, like `OrderDetails`.

- **Code smell no.** - 5
- **Code smell name** - Comments
- **Code smell description** - Excessive or unnecessary comments indicating possible code that is not self-explanatory or needs clarification.
- **Found in line no.** - 34, 73, 74
- **Possible treatments** - Extract Variable, Extract Method, Rename Method, Introduce Assertion
- **Possible solution** - Refactor complex expressions into well-named methods or variables, and remove comments that state obvious or redundant information.

*No other significant code smells detected.*