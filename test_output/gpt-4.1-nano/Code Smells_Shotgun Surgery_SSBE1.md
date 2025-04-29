# Code Review: SSBE1.java

---

### 1. Code Smell No. - 1
- **Code smell name:** Switch Statements
- **Code smell description:** Multiple `if-else` chains evaluate the value of `subjectGrad` to determine the output message, which can be replaced with polymorphism or a lookup table for better clarity and maintainability.
- **Found in line no.:** 12-24
- **Possible treatments:** Extract Method & then Move Method, Replace Type Code with Subclasses or Replace Type Code with State/Strategy, Replace Conditional with Polymorphism
- **Possible solution:** Refactor the `checkGrade()` method to utilize a polymorphic approach, possibly by creating subclasses for each grade or using a map/dictionary to associate grades with messages.

---

### 2. Code Smell No. - 2
- **Code smell name:** Long Method
- **Code smell description:** The `checkGrade()` method contains lengthy if-else statements, making it harder to maintain and understand.
- **Found in line no.:** 12-24
- **Possible treatments:** Extract Method & then Move Method, Decompose Conditional
- **Possible solution:** Break the method into smaller methods, each handling a particular grade message or use a data structure for message retrieval.

---

### 3. Code Smell No. - 3
- **Code smell name:** Primitive Obsession
- **Code smell description:** The use of `char` values to represent grades ('A', 'B', 'C', etc.) instead of using a dedicated `Grade` enum or class leads to fragile and error-prone code.
- **Found in line no.:** 2, 13-23
- **Possible treatments:** Replace Data Value with Object, Replace Type Code with Class
- **Possible solution:** Replace the `char` grade with an enumeration `Grade { A, B, C, D, F }` for type safety and clarity.

---

### 4. Code Smell No. - 4
- **Code smell name:** Data Clumps
- **Code smell description:** The `setMathGrade()` and `setEnglishGrade()` methods repeatedly pass the `marks` parameter with similar logic, indicating a bundle of data that can be extracted into an object.
- **Found in line no.:** 34-54
- **Possible treatments:** Extract Class, Introduce Parameter Object, Preserve Whole Object
- **Possible solution:** Create a `Marks` class that encapsulates the marks value, reducing duplicated code.

---

### 5. Code Smell No. - 5
- **Code smell name:** Duplicate Code
- **Code smell description:** Similar logic exists in `setMathGrade()` and `setEnglishGrade()` methods for assigning grades based on marks, leading to redundant code.
- **Found in line no.:** 34-54
- **Possible treatments:** Extract Method, Consolidate Conditional Expression and use Extract Method
- **Possible solution:** Create a shared method for grade determination that both classes call, reducing duplication.

---

### 6. Code Smell No. - 6
- **Code smell name:** Large Class
- **Code smell description:** The `SubjectsGradingBad` class handles grade checking and setting, but all logic is contained within it, which might grow complex if more subjects or features are added.
- **Found in line no.:** 1-25
- **Possible treatments:** Extract Class, Extract Subclass
- **Possible solution:** Consider splitting the class into separate subclasses for different grading strategies or subjects if it expands further.

---

**Note:** There are no comments, dead code, or other significant smells evident in this snippet beyond those listed.