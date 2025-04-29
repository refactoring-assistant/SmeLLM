**Code Review: POBE2.java**

- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The code makes extensive use of primitive data types instead of small objects for simple tasks, such as representing an employee type and salary.
- Found in line no. - 5, 6, 7, 8, 10, 14, 15, 25
- Possible treatments - Replace Data Value with Object, Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy
- Possible solution - Replace the `empType` String with an enumeration for employee roles and create a class to encapsulate salary details.

```java
enum EmployeeType {
    PROFESSOR(100000),
    ASSISTANT_PROFESSOR(80000),
    ASSOCIATE_PROFESSOR(50000);

    private final double salary;

    EmployeeType(double salary) {
        this.salary = salary;
    }

    public double getSalary() {
        return salary;
    }
}

class EmployeeId {
    private String empId;

    public EmployeeId(String empId) {
        validateEmployeeId(empId);
        this.empId = empId;
    }

    private void validateEmployeeId(String empId) {
        if(empId.length() != 6) {
            throw new IllegalArgumentException("Invalid employee id");
        }
    }

    public String getEmpId() {
        return empId;
    }
}

interface Staff {
    void printStaffDetails();
}

class TeachingStaff implements Staff {
    private EmployeeType empType;
    private String empName;
    private EmployeeId empId;

    public TeachingStaff(EmployeeType empType, String empName, String empId) {
        this.empType = empType;
        this.empName = empName;
        this.empId = new EmployeeId(empId);
    }

    public void printStaffDetails() {
        System.out.println("Employee Name: " + empName);
        System.out.println("Employee ID: " + empId.getEmpId());
        System.out.println("Employee Type: " + empType);
        System.out.println("Employee Salary: " + empType.getSalary());
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

- Code smell no. - 2
- Code smell name - Switch Statements
- Code smell description - The `setSalary` method uses a series of if-else statements to differentiate between employee types, which can be prone to errors and is difficult to maintain.
- Found in line no. - 25
- Possible treatments - Replace Type Code with Subclasses or Replace Type Code with State/Strategy, Replace Conditional with Polymorphism
- Possible solution - Use an enumeration for `EmployeeType` with their associated salaries as demonstrated above, eliminating the need for the `setSalary` function with conditional logical flows.