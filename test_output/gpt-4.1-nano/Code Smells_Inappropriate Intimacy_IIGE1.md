**Code Review: IIGE1.java**

- **Code smell no.** - 1
- **Code smell name** - Primitive Obsession
- **Code smell description** - The use of primitive types (int) and raw data structures (SortedMap) instead of dedicated Value Objects makes the code less expressive and harder to maintain.
- **Found in line no.** - 6, 10-15
- **Possible treatments** - Replace Data Value with Object
- **Possible solution** - Create a GradeScale class encapsulating the grade mappings, which improves clarity and flexibility.

- **Code smell no.** - 2
- **Code smell name** - Long Method
- **Code smell description** - The method getGrade() contains a loop with multiple statements, which could be extracted for better readability and maintainability.
- **Found in line no.** - 18-22
- **Possible treatments** - Extract Method
- **Possible solution** - Extract the grade determination logic into a separate method, e.g., determineGrade().

- **Code smell no.** - 3
- **Code smell name** - Data Clumps
- **Code smell description** - The 'marks' and 'gradeScale' are used together frequently, indicating data clumps which could be encapsulated into a dedicated object.
- **Found in line no.** - 6, 17, 26-28, 30-32
- **Possible treatments** - Extract Class, Introduce Parameter Object, Preserve Whole Object
- **Possible solution** - Create a StudentResult class containing marks and grade, passing this object instead of individual values.

---

No other significant code smells detected.