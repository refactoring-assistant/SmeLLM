interface IPerson {
  void printPersonDetails();
  void printStudentDetails();
}
class Person implements IPerson {
  private String name;
  private String studentId;
  private String major;

  public Person(String name, String studentId, String major) {
    this.name = name;
    this.studentId = studentId;
    this.major = major;
  }

  public void printPersonDetails() {
    System.out.println("Name: " + this.name);
  }

  public void printStudentDetails() {
    printPersonDetails();
    System.out.println("Student ID: " + this.studentId);
    System.out.println("Major: " + this.major);
  }
}

public class source28 {
    public static void main(String[] args) {
        IPerson person1 = new Person("John", "123456", "Computer Science");
        System.out.println("Only person details:");
        person1.printPersonDetails();
        System.out.println("Student details:");
        person1.printStudentDetails();
    }
}
