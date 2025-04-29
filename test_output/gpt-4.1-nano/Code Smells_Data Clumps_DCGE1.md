**Code Review: DCGE1.java**
- Code smell no. - 1
- Code smell name - Duplicate Code
- Code smell description - There is duplicated logic in updating contact details across multiple classes, leading to code redundancy.
- Found in line no. - 12, 38, 61, 98, 104
- Possible treatments - Extract Method, Extract Superclass
- Possible solution - Create a common interface or superclass for entities with contact details to centralize update logic and reduce duplication.  

- Code smell no. - 2
- Code smell name - Long Method
- Code smell description - The method printFlightDetails() performs multiple print operations, making it lengthy and complex.
- Found in line no. - 122
- Possible treatments - Extract Method, Decompose Conditional
- Possible solution - Break down printFlightDetails() into smaller, focused methods such as printBookingDetails() and printTravelDetails() for each segment.

- Code smell no. - 3
- Code smell name - Primitive Obsession
- Code smell description - Usage of primitive data types (String, LocalDate) for complex entities like contact info and travel dates instead of dedicated value objects.
- Found in line no. - 4-5, 72-73, 138-140
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object
- Possible solution - Define specific classes for contact info and dates to encapsulate related behavior and data.

- Code smell no. - 4
- Code smell name - Shotgun Surgery
- Code smell description - The need to update multiple related classes to maintain consistency, such as contact info and travel details.
- Found in line no. - 152-154
- Possible treatments - Move Method & Move Field, Inline Class
- Possible solution - Consolidate related data and behaviors into fewer classes to simplify updates and reduce the spread of changes.

**No other significant code smells detected.**