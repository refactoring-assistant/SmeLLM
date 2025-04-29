# Code Review: MCBE1.java

- **Code smell no.** - 2
- **Code smell name** - Primitive Obsession
- **Code smell description** - The code uses primitive data types (e.g., String for address components, String for order status) which can be better represented as objects to encapsulate related behavior and data.
- **Found in line no.** - 15, 16, 55, 70, 71, 74
- **Possible treatments** - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object
- **Possible solution** - Develop specific classes such as Address and OrderStatus to encapsulate related data and behaviors, replacing strings with rich domain objects for better maintainability and clarity.