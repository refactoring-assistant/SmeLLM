# Code Review: IIBE1.java

- **Code smell no.** - 1
- **Code smell name** - Primitive Obsession
- **Code smell description** - Uses primitive data types (int, char) to represent domain concepts instead of encapsulating them into objects.
- **Found in line no.** - 8, 20, 21, 22, 37, 38, 44, 58
- **Possible treatments** - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class or Subclasses.
- **Possible solution** - Create `Grade` class to encapsulate grade value and label, replace raw char and int with `Grade` objects. Instead of raw `marks`, `gradeScale`, and char `F`, use `Grade` class instances to improve clarity and flexibility.

---

- **Code smell no.** - 2
- **Code smell name** - Lazy Class
- **Code smell description** - Classes are doing too little or only wrapping data without adding meaningful behavior.
- **Found in line no.** - 30, 31
- **Possible treatments** - Inline Class, Collapse Hierarchy
- **Possible solution** - Merge `SubjectMarksBad` functionality into related classes if it does not contain independent logic, or extensively refactor to extract meaningful behavior.

---

- **Code smell no.** - 3
- **Code smell name** - Data Clumps
- **Code smell description** - Repeatedly passing sets of variables that logically belong together.
- **Found in line no.** - 58
- **Possible treatments** - Extract Class, Introduce Parameter Object, Preserve Whole Object
- **Possible solution** - Use a `MarksAndGrade` object to group `marks` and `grade`, passing it around instead of separate variables.

---

- **Code smell no.** - 4
- **Code smell name** - Inappropriate Intimacy
- **Code smell description** - Classes are too familiar with each other's internal details, violating encapsulation.
- **Found in line no.** - 58
- **Possible treatments** - Move Method & Move Field, Extract Class & Hide Delegate
- **Possible solution** - Make `marks` private in `SubjectMarksBad` and provide appropriate setter and getter methods, avoiding direct access from `TeacherBad`.

---

- **Code smell no.** - 5
- **Code smell name** - Feature Envy
- **Code smell description** - A method seems more interested in another class's data than its own.
- **Found in line no.** - 44, 58
- **Possible treatments** - Move Method, Extract Method, Extract Method with Move Method
- **Possible solution** - Move `printMarksAndGrade()` to `SubjectMarksBad`, so it manages its own data rather than being called externally, reducing feature envy.

---

**Summary:**  
The code exhibits instances of Primitive Obsession with primitive data types for grades and marks, and features issues like Data Clumps and Inappropriate Intimacy. Refactoring into domain-specific classes such as `Grade` and `Marks` objects, and encapsulating internal data properly would greatly improve maintainability and clarity.