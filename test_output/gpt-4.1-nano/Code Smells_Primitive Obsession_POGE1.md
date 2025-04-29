# Code Review: POGE1.java

- **Code smell no.** - 1
- **Code smell name** - Primitive Obsession
- **Code smell description** - Use of primitive data types for complex data elements such as height, weight, age, which could be better represented as dedicated value objects.
- **Found in line no.** - 23, 24, 25, 26, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47
- **Possible treatments** - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object
- **Possible solution** - Introduce dedicated classes for measurements like Height, Weight, Age with appropriate validation and behavior instead of using String types.

- **Code smell no.** - 2
- **Code smell name** - Data Clumps
- **Code smell description** - Groups of variables that tend to be passed around together (e.g., address components) could be grouped into a single value object.
- **Found in line no.** - 52, 53, 54, 55
- **Possible treatments** - Extract Class, Introduce Parameter Object, Preserve Whole Object
- **Possible solution** - Create an Address class to encapsulate street, city, state, and country.

- **Code smell no.** - 3
- **Code smell name** - Long Method
- **Code smell description** - Methods that have too many lines or complex conditional logic, such as `printPatientDetails()` or `printMedicalHistory()`.
- **Found in line no.** - 90, 140
- **Possible treatments** - Extract Method & then Move Method, Consolidate Conditional Fragments
- **Possible solution** - Break down large print methods into smaller, specialized methods for each section (e.g., printName, printAddress, printMedicalData).

- **Code smell no.** - 4
- **Code smell name** - Switch Statements / Long Parameter List
- **Code smell description** - Methods like `addPreviousMedication`, `addAllergy`, etc., use repeated verification and control flow.
- **Found in line no.** - 164-186
- **Possible treatments** - Replace Parameter with Method Call, Preserve Whole Object
- **Possible solution** - Instead of passing `patientIdentifier` to each method, consider introducing an abstract `Patient` object with methods that accept only the data or use a unified context object.

- **Code smell no.** - 5
- **Code smell name** - Comments
- **Code smell description** - Excessive comments explaining simple code, which could be clarified or self-explanatory through better naming.
- **Found in line no.** - 199, 201, 202, 203, 204, 205
- **Possible treatments** - Extract Variable, Extract Method, Rename Method
- **Possible solution** - Remove or minimize comments by making code more self-explanatory, such as renaming variables or methods.

**Summary:**  
The main smell is Primitive Obsession, indicated by primitive data types that should be encapsulated into value objects. There are also instances of Long Methods in print functions, and Data Clumps in address-related fields. Refactoring suggestions include creating dedicated classes for measurements and address, breaking down large functions, and improving code clarity to reduce comments.