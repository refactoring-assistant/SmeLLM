```markdown
**Code Review: SGBE1.java**
- Code smell no. - 1
- Code smell name - **Primitive Obsession**
- Code smell description - The use of primitive types (like int and double) to represent concepts such as booking days and costs can lead to inconsistency and confusion in the future.
- Found in line no. - 2, 10, 21, 22, 33
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy.
- Possible solution - To address this, create a class to encapsulate accommodation details (e.g., `BookingDetails` class) that includes properties like number of days and cost, thus enhancing clarity and type safety in the code.

**Code Review: SGBE1.java**
- Code smell no. - 2
- Code smell name - **Long Method**
- Code smell description - The `printAccomodationDetails` method contains multiple responsibilities including condition checking and printing functionality, which makes it harder to maintain.
- Found in line no. - 26, 27, 28, 31, 32, 33, 34
- Possible treatments - Extract Method, Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object, Decompose Conditional.
- Possible solution - Extract the logic for printing hotel details into separate methods for cleaner responsibilities, such as `printHotelName`, `printHotelAddress`, and `printTotalCost`.

**Code Review: SGBE1.java**
- Code smell no. - 3
- Code smell name - **Data Class**
- Code smell description - The class `HotelBad` is primarily used to hold data without significant behavior or methods that manipulate the data.
- Found in line no. - 6, 7, 8, 9, 10
- Possible treatments - Encapsulate Field, Encapsulate Collection, Move Method and Extract Method, Remove Setting Method and Hide Method.
- Possible solution - Include methods in the `HotelBad` class that perform operations relevant to the hotel, such as checking availability or calculating offers, enhancing the class’s purpose beyond mere data storage.
```