**Code Review: POBE2.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - The method `setSalary` is long and has multiple condition checks, which makes it harder to read and maintain.
- Found in line no. - 25-35
- Possible treatments - Extract Method, Decompose Conditional
- Possible solution - 
```java
private double setSalary(String empType) {
    switch (empType) {
        case "Professor":
            return 100000;
        case "Assistant Professor":
            return 80000;
        case "Associate Professor":
            return 50000;
        default:
            throw new IllegalArgumentException("Invalid employee type");
    }
}
```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - The use of `String` for `empType` and `empId` can lead to errors and lacks the expressiveness of an object.
- Found in line no. - 5-7, 10, 25
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object
- Possible solution - Define an `EmployeeType` enum and encapsulate employee details in an `Employee` class to manage their behavior more effectively.

- Code smell no. - 3
- Code smell name - Duplicate Code
- Code smell description - The instantiation of `TeachingStaffBad` and calling `printStaffDetails` is repeated multiple times.
- Found in line no. - 45, 47, 49
- Possible treatments - Extract Method
- Possible solution - 
```java
private static void createAndPrintStaff(String empType, String empName, String empId) {
    TeachingStaffBad staff = new TeachingStaffBad(empType, empName, empId);
    staff.printStaffDetails();
}

// In main method
createAndPrintStaff("Professor", "John", "123456");
createAndPrintStaff("Assistant Professor", "Jane", "123467");
createAndPrintStaff("Associate Professor", "Doe", "897321");
```