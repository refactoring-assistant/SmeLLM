# Code Review: SWSBE1.java

- **Code smell no.** - 1
- **Code smell name** - Switch Statements
- **Code smell description** - The code uses a switch statement to handle multiple shape types, which violates the Open/Closed Principle, making it harder to extend and maintain.
- **Found in line no.** - 8-20
- **Possible treatments** - Extract Method & then Move Method; Replace Type Code with Subclasses or Replace Type Code with State/Strategy; Replace Conditional with Polymorphism
- **Possible solution** - Refactor by creating a `Shape` interface, and implement subclasses such as `Circle`, `Rectangle`, `Triangle`, `Square`, each with its own `calculateArea()` method. This removes the switch statement and adheres to polymorphism.

---

- **Code smell no.** - 2
- **Code smell name** - Primitive Obsession
- **Code smell description** - Using primitive data types (like `String` for shape and `int...` for dimensions) instead of objects to encapsulate shape-specific attributes and behaviors.
- **Found in line no.** - 2, 7-20
- **Possible treatments** - Replace Data Value with Object; Introduce Parameter Object or Preserve Whole Object
- **Possible solution** - Create dedicated classes for each shape (e.g., `Circle`, `Rectangle`) encapsulating dimensions, shape type, and calculation logic, replacing primitive data types.

---

- **Code smell no.** - 3
- **Code smell name** - Long Method
- **Code smell description** - The `calculateArea` method handles multiple shape calculations, making it lengthy and complex.
- **Found in line no.** - 7-20
- **Possible treatments** - Extract Method; Decompose Conditional
- **Possible solution** - Split `calculateArea()` into multiple smaller methods, each handling a specific shape's area calculation, preferably via polymorphism.

---

**Summary:**  
The current implementation exhibits the "Switch Statements" and "Primitive Obsession" smells. Refactoring towards a polymorphic design with specific shape classes will significantly improve maintainability, extensibility, and readability.