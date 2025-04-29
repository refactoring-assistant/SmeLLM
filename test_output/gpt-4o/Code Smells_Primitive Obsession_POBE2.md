**Code Review: POBE2.java**

- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The code is using primitive data types to represent some domain concepts, such as `empType`. Using string literals to represent employee types is not only error-prone but also makes the code less readable and harder to maintain.
- Found in line no. - 5, 10, 14, 25
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy, Replace Array with Object.
- Possible solution - Use an enum or a class to represent employee type, which will encapsulate the logic associated with each type.

- Code smell no. - 2
- Code smell name - Long Method
- Code smell description - The `setSalary` method contains a long conditional block that could be decomposed.
- Found in line no. - 25-34
- Possible treatments - Extract Method, Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object, Decompose Conditional.
- Possible solution - Decompose the conditions within `setSalary` to separate methods or an enum.

Here is a possible solution after refactoring:

```java
interface Staff {
    void printStaffDetails();
}

class TeachingStaff implements Staff {
    private EmployeeType empType;
    private String empName;
    private String empId;
    private double salary;

    public TeachingStaff(EmployeeType empType, String empName, String empId) {
        validateEmployeeId(empId);
        this.empName = empName;
        this.empId = empId;
        this.salary = empType.getSalary();
        this.empType = empType;
    }

    public void printStaffDetails() {
        System.out.println("Employee Name: " + empName);
        System.out.println("Employee ID: " + empId);
        System.out.println("Employee Type: " + empType);
        System.out.println("Employee Salary: " + salary);
    }

    private void validateEmployeeId(String empId) {
        if(empId.length() != 6) {
            throw new IllegalArgumentException("Invalid employee id");
        }
    }
}

enum EmployeeType {
    PROFESSOR(100000), ASSISTANT_PROFESSOR(80000), ASSOCIATE_PROFESSOR(50000);

    private final double salary;

    EmployeeType(double salary) {
        this.salary = salary;
    }

    public double getSalary() {
        return salary;
    }
}

public class POBE2 {
    public static void main(String[] args) {
        TeachingStaff staff1 = new TeachingStaff(EmployeeType.PROFESSOR, "John", "123456");
        staff1.printStaffDetails();
        TeachingStaff staff2 = new TeachingStaff(EmployeeType.ASSISTANT_PROFESSOR, "Jane", "123467");
        staff2.printStaffDetails();
        TeachingStaff staff3 = new TeachingStaff(EmployeeType.ASSOCIATE_PROFESSOR, "Doe", "897321");
        staff3.printStaffDetails();
    }
}
```

This refactoring eliminates the primitive obsession, simplifies the salary determination using an enum, and cleans up the `setSalary` logic from the original code.