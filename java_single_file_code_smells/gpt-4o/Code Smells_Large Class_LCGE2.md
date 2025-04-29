**Code Review: LCGE2.java**
  - Code smell no. - 1
  - Code smell name - Large Class
  - Code smell description - 'StudentGood' class holds too much responsibility by managing both personal and student details, which leads to unnecessary complexity.
  - Found in line no. - 21-35
  - Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
  - Possible solution - Split the 'StudentGood' class into separate classes for managing personal details and student details. Each class should focus on a single responsibility.

```java
interface IPersonGood {
    void printPersonDetails();
}

interface IStudentDetails {
    void printStudentDetails();
}

class PersonGood implements IPersonGood {
    private String name;

    public PersonGood(String name) {
        this.name = name;
    }

    public void printPersonDetails() {
        System.out.println("Name: " + this.name);
    }
}

class StudentDetails implements IStudentDetails {
    private String studentId;
    private String major;

    public StudentDetails(String studentId, String major) {
        this.studentId = studentId;
        this.major = major;
    }

    public void printStudentDetails() {
        System.out.println("Student ID: " + this.studentId);
        System.out.println("Major: " + this.major);
    }
}

class StudentGood extends PersonGood {
    private StudentDetails studentDetails;

    public StudentGood(String name, String studentId, String major) {
        super(name);
        this.studentDetails = new StudentDetails(studentId, major);
    }

    public void printStudentDetails() {
        printPersonDetails();
        studentDetails.printStudentDetails();
    }
}

public class LCGE2 {
    public static void main(String[] args) {
        StudentGood person1 = new StudentGood("John", "123456", "Computer Science");
        System.out.println("Only person details:");
        person1.printPersonDetails();
        System.out.println("Student details:");
        person1.printStudentDetails();
    }
}
```