**Code Review: CBE3.java**

- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - The class `UserAddressBad` primarily holds data without much behavior, which may indicate it is a simple data container, possibly leading to duplication or lack of encapsulation.
- Found in line no. - 4-20
- Possible treatments - Encapsulate Field, Encapsulate Collection, Move Method and Extract Method, Remove Setting Method and Hide Method
- Possible solution - Refactor `UserAddressBad` into a more robust class with meaningful behaviors or behaviors encapsulation, or rename it to clearly indicate it is a data holder, possibly combining it with domain logic or eliminating unnecessary data classes.

- Code smell no. - 2
- Code smell name - Long Method
- Code smell description - The method `printFormattedAddress()` contains string concatenation and printing logic which could be more modular and potentially extracted for reusability.
- Found in line no. - 17-19
- Possible treatments - Extract Method & then Move Method, Consolidate Duplicate Conditional Fragments
- Possible solution - Extract the address formatting into a separate method or utility class to improve clarity and reusability.