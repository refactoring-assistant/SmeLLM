**Code Review: LCGE2.java**
   - Code smell no. - 1
   - Code smell name - Inappropriate Intimacy
   - Code smell description - Inheritance is used when a delegation might be more appropriate. The `StudentGood` class extends `PersonGood` and also implements `IStudentGood`, creating tight coupling through unnecessary inheritance.
   - Found in line no. - 21
   - Possible treatments - ['Move Method & Move Field', 'Extract Class & Hide Delegate', 'Change Bidirectional Association to Unidirectional', ' Replace Delegation with Inheritance']
   - Possible solution - Implement delegation instead of inheritance by using a `PersonGood` object within the `StudentGood` class.

```java
interface IPersonGood {
   void printPersonDetails();
}

interface IStudentGood {
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

class StudentGood implements IStudentGood {
   private PersonGood person;
   private String studentId;
   private String major;

   public StudentGood(String name, String studentId, String major) {
     this.person = new PersonGood(name);
     this.studentId = studentId;
     this.major = major;
   }

   public void printStudentDetails() {
     person.printPersonDetails();
     System.out.println("Student ID: " + this.studentId);
     System.out.println("Major: " + this.major);
   }
}

public class LCGE2 {
   public static void main(String[] args) {
     IStudentGood person1 = new StudentGood("John", "123456", "Computer Science");
     System.out.println("Only person details:");
     person1.printStudentDetails();
     System.out.println("Student details:");
     person1.printStudentDetails();
   }
}
```