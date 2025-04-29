**Code Review: SWSBE2.java**  
- Code smell no. - 1  
- Code smell name - Switch Statements  
- Code smell description - The use of switch statements to handle different route types can lead to fragile code that is hard to extend and maintain, especially if adding new route types. It often indicates a violation of the Open/Closed Principle.  
- Found in line no. - 13, 14, 17, 20, 23, 26  
- Possible treatments - Extract Method & then Move Method, Replace Type Code with Subclasses or Replace Type Code with State/Strategy, Replace Conditional with Polymorphism  
- Possible solution - Refactor the code to implement the Strategy pattern by creating separate classes for each route calculation strategy, thereby removing the switch statement and making the code more flexible and maintainable.