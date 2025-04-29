**Code Review: SGBE1.java**  
- **Code smell no.** 1  
- **Code smell name** - Primitive Obsession  
- **Code smell description** - The code uses primitive data types (String, double, int) directly instead of encapsulating related properties in objects which can improve clarity and flexibility.  
- **Found in line no.** - 7, 8, 9, 10, 13, 14, 15, 21, 22, 33, 34  
- **Possible treatments** - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object  
- **Possible solution** - Create an `Address` class for the address details, and a `StayDetails` class to encapsulate booking details such as number of days and cost, replacing primitives with these objects for better encapsulation.

---

- **Code smell no.** 2  
- **Code smell name** - Shotgun Surgery  
- **Code smell description** - Changes to a booking or details printing affect multiple parts of the class, indicating that related data and behavior are scattered and not well encapsulated.  
- **Found in line no.** - 21-23, 27-35, 37-39  
- **Possible treatments** - Extract Method, Extract Class  
- **Possible solution** - Extract booking details and printing into separate classes such as `Booking`, `BookingPrinter` to isolate changes and improve maintainability.

---

- **Code smell no.** 3  
- **Code smell name** - Long Method  
- **Code smell description** - The `printAccomodationDetails()` method contains multiple responsibilities such as conditional checks and printing different pieces of information, making it lengthy and complex.  
- **Found in line no.** - 26-35  
- **Possible treatments** - Extract Method  
- **Possible solution** - Split the method into smaller methods, e.g., `printBasicDetails()`, `printCostDetails()`, to improve readability and single responsibility principle.

---

- **Code smell no.** 4  
- **Code smell name** - Data Class  
- **Code smell description** - The class `HotelBad` primarily holds data attributes without adding much behavior, making it a data class.  
- **Found in line no.** - 7-10, 13-15  
- **Possible treatments** - Encapsulate Field, Move Method and Extract Method  
- **Possible solution** - Encapsulate data and add behavior related to hotel booking within the class. Alternatively, refactor data into specialized classes representing hotel details.

---

**Summary recommendation:**  
Refactor primitive data into dedicated classes for address and booking details, split large methods into smaller, more manageable methods, and further encapsulate data to improve the overall design and reduce code smells.