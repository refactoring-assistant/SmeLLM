# Code Review: PIHBE1.java
- **Code smell no.** 1
- **Code smell name** - Primitive Obsession
- **Code smell description** - Use of primitive types like String for model and engineType instead of dedicated classes violates the principle of encapsulating data.
- **Found in line no.** - 17-20
- **Possible treatments** - Replace Data Value with Object
- **Possible solution** - Create dedicated classes for Model and EngineType to encapsulate relevant behaviors and validations.

- **Code smell no.** 2
- **Code smell name** - Long Method
- **Code smell description** - The `main` method contains multiple unrelated sequences of vehicle creation, configuration, and printing which could be decomposed.
- **Found in line no.** - 106-128
- **Possible treatments** - Extract Method
- **Possible solution** - Refactor the `main` method into smaller methods like `createCar`, `createBike`, `configureVehicle`, and `displayVehicleInfo`.

- **Code smell no.** 3
- **Code smell name** - Data Clumps
- **Code smell description** - Grouping model and engineType as separate parameters repeatedly indicates data clumps that could be encapsulated.
- **Found in line no.** - 17-20, 45-46, 75-77, 119-120
- **Possible treatments** - Extract Class, Introduce Parameter Object
- **Possible solution** - Encapsulate model and engineType into a `VehicleSpecs` class; pass this object instead of individual strings.

- **Code smell no.** 4
- **Code smell name** - Switch Statements
- **Code smell description** - The `setNewProductionFacility` method relies on `instanceof` checks, which are a form of switch over types.
- **Found in line no.** - 50-54, 83-87, 84-86
- **Possible treatments** - Replace Type Code with Subclasses or Replace Conditional with Polymorphism
- **Possible solution** - Use polymorphism; delegate the responsibility to specific vehicle classes or factories, possibly via a factory method pattern.

- **Code smell no.** 5
- **Code smell name** - Inappropriate Intimacy
- **Code smell description** - Classes directly access internal details of Factory classes and manipulate their state, leading to tight coupling.
- **Found in line no.** - 107-113, 119-125
- **Possible treatments** - Change Bidirectional Association to Unidirectional, Move Method & Move Field
- **Possible solution** - Use dependency injection and adhere to encapsulation; avoid exposing internal details of factories through subclass fields.

---

*No other significant code smells were detected in this snippet.*