# Code Review: POGE2.java

- **Code smell no.** - 1
- **Code smell name** - Missing Null Object Handling
- **Code smell description** - The methods `setSalary()` and `printEmployeeType()` throw `IllegalArgumentException` for invalid employee types, which can lead to unhandled exceptions during execution.
- **Found in line no.** - 24, 28, 44, 50, 60, 64, 76, 81
- **Possible treatments** - Replace Conditional with Polymorphism, Introduce Null Object
- **Possible solution** - Implement a Null Object class for `TeachingStaffGood` that provides default behaviors for `setSalary()` and `printEmployeeType()` to avoid exceptions and ensure smoother runtime behavior.

- **Code smell no.** - 2
- **Code smell name** - Primitive Obsession
- **Code smell description** - Employee IDs are represented as strings with format validation, which is a primitive data type usage that could be encapsulated in a dedicated EmployeeId class.
- **Found in line no.** - 31-35
- **Possible treatments** - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object
- **Possible solution** - Create an `EmployeeId` class to handle ID validation and formatting, encapsulating the ID logic and improving type safety.

- **Code smell no.** - 3
- **Code smell name** - Long Method
- **Code smell description** - The `printStaffDetails()` contains multiple print statements and method calls, making it somewhat verbose and potentially clearer if split.
- **Found in line no.** - 16-21
- **Possible treatments** - Extract Method, Decompose Conditional
- **Possible solution** - Extract specific print routines into smaller methods, e.g., `printHeader()`, `printType()`, etc., to improve clarity and maintainability.

---

*Note: The code overall is well-structured with proper use of inheritance and polymorphism. The main concern is exception handling in base class methods which can be improved for robustness.*