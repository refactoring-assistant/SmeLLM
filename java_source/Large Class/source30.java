interface IPerson {
   void printPersonDetails();
}

interface IStudent extends IPerson {
  void printStudentDetails();
}

class Person implements IPerson {
  private String name;

  public Person(String name) {
    this.name = name;
  }

  public void printPersonDetails() {
    System.out.println("Name: " + this.name);
  }
}

class Student extends Person implements IStudent {
  private String studentId;
  private String major;

  public Student(String name, String studentId, String major) {
    super(name);
    this.studentId = studentId;
    this.major = major;
  }

  public void printStudentDetails() {
    printPersonDetails();
    System.out.println("Student ID: " + this.studentId);
    System.out.println("Major: " + this.major);
  }
}

public class source30 {
  public static void main(String[] args) {
    IStudent person1 = new Student("John", "123456", "Computer Science");
    System.out.println("Only person details:");
    person1.printPersonDetails();
    System.out.println("Student details:");
    person1.printStudentDetails();
  }
}
