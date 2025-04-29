**Code Review: PIHGE1.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The code uses multiple String fields to represent vehicle attributes, which could benefit from encapsulation into dedicated classes or value objects for better type safety and clarity.
- Found in line no. - 8, 9, 10, 12, 13, 14, 15
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object
- Possible solution - Encapsulate vehicle attributes into a separate class, e.g., VehicleAttributes, and replace individual string parameters and fields with this object.

- Code smell no. - 2
- Code smell name - Long Method
- Code smell description - The main method contains a lengthy sequence of multiple method calls, which could be decomposed into smaller, more manageable methods.
- Found in line no. - 62 to 82
- Possible treatments - Extract Method
- Possible solution - Break the main method into smaller helper methods, such as createAndTestCar, createAndTestBike, for better readability and maintenance.