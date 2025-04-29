**Code Review: ACDIBE1.java**

- **Code smell no. 1**
- **Code smell name:** Data Clumps
- **Code smell description:** Repeated grouping of the same data (name and age) in multiple classes indicates data clumps, which should be encapsulated into a separate class.
- **Found in line no.:** 17-31
- **Possible treatments:** Extract Class, Introduce Parameter Object, Preserve Whole Object
- **Possible solution:** Create a `AnimalInfo` class to encapsulate `name` and `age`, then pass an instance of it to each animal class to reduce redundancy and improve maintainability.