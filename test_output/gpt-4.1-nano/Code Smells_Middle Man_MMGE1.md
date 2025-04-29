**Code Review: MMGE1.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - Methods are performing multiple actions, making them lengthy and hard to understand. This reduces maintainability.
- Found in line no. - 27, 36
- Possible treatments - Extract Method & then Move Method, Replace Conditional with Polymorphism
- Possible solution - Refactor the `printAssignedTasks()` and `printSupervisorDetails()` methods into smaller, more focused methods to improve clarity and single responsibility adherence.