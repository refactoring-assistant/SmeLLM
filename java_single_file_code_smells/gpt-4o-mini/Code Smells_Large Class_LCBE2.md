**Code Review: LCBE2.java**
- Code smell no. - 1
- Code smell name - Alternative Classes with Different Interfaces
- Code smell description - This code exhibits alternative classes with different interfaces where a single interface can be further refined or a common interface could be implemented to reduce redundancy.
- Found in line no. - 1
- Possible treatments - ['Rename Method', 'Move Method, Add Parameter & Parameterize Method', 'Extract Superclass']
- Possible solution - 
```java
interface IPerson {
    void printDetails();
}

interface IStudent {
    void printStudentDetails();
}

class Person implements IPerson, IStudent {
    private String name;
    private String studentId;
    private String major;

    public Person(String name, String studentId, String major) {
        this.name = name;
        this.studentId = studentId;
        this.major = major;
    }

    public void printDetails() {
        System.out.println("Name: " + this.name);
    }

    public void printStudentDetails() {
        printDetails();
        System.out.println("Student ID: " + this.studentId);
        System.out.println("Major: " + this.major);
    }
}

public class LCBE2 {
    public static void main(String[] args) {
        IStudent person1 = new Person("John", "123456", "Computer Science");
        System.out.println("Only person details:");
        person1.printStudentDetails();
    }
}
```