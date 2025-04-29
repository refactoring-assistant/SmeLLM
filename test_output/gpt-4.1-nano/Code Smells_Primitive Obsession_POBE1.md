# Code Review: POBE1.java

---

### 1.  
- **Code smell no.** - 1  
- **Code smell name** - Primitive Obsession  
- **Code smell description** - Usage of primitive data types (e.g., Strings, arrays) to represent complex data, leading to lack of encapsulation and increased likelihood of errors.  
- **Found in line no.** - 8-14, 24-29, 124-128  
- **Possible treatments** - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object  
- **Possible solution** - Create specific classes like `PatientName`, `Address`, `MedicalBiodata`, `Medication`, `Allergy`, etc., to encapsulate related data and improve code clarity.

---

### 2.  
- **Code smell no.** - 2  
- **Code smell name** - Long Method  
- **Code smell description** - Methods are excessively long, handling multiple responsibilities, reducing readability and maintainability.  
- **Found in line no.** - 80-87, 89-118  
- **Possible treatments** - Extract Method, Decompose Conditional  
- **Possible solution** - Break down `printMedicalRecord()` into smaller methods: `printPatientInfo()`, `printMedications()`, `printAllergies()`, etc.

---

### 3.  
- **Code smell no.** - 3  
- **Code smell name** - Data Clumps  
- **Code smell description** - Several parameters are often passed or stored together, indicating they should be encapsulated in their own class.  
- **Found in line no.** - 16-30, 32-37, 39-49, 53-64, 66-75, 79-86  
- **Possible treatments** - Extract Class, Introduce Parameter Object, Preserve Whole Object  
- **Possible solution** - Create classes like `MedicalData`, `MedicationDetails`, `AllergyDetails`, `DiseaseHistory` to group related fields.

---

### 4.  
- **Code smell no.** - 4  
- **Code smell name** - Switch Statements  
- **Code smell description** - Conditional logic based on string matching or type codes, which could be replaced with polymorphism or strategy pattern.  
- **Found in line no.** - 40-50, 55-65, 68-76, 94-98, 104-108, 112-116  
- **Possible treatments** - Replace Conditional with Polymorphism, Replace Type Code with Subclasses or State/Strategy  
- **Possible solution** - Use objects like `Patient`, `Medication`, `Allergy`, etc., with methods tailored to their types, eliminating switch cases.

---

### 5.  
- **Code smell no.** - 5  
- **Code smell name** - Long Parameter List  
- **Code smell description** - Methods take many parameters, making them hard to understand and maintain.  
- **Found in line no.** - 39, 53, 66, 127-129  
- **Possible treatments** - Replace Parameter with Method Call, Introduce Parameter Object, Preserve Whole Object  
- **Possible solution** - Use parameter objects (`MedicationInfo`, `PatientIdentifier`) to pass grouped data.

---

**Summary:**  
The primary issues are Primitive Obsession, Data Clumps, Long Methods, and Switch Statements. Refactoring into proper classes and methods will improve modularity, readability, and maintainability.