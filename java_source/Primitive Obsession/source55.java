interface Staff {
  void printStaffDetails();
}
abstract class TeachingStaff implements Staff {
  private String empName;
  private String empId;
  private double salary;

  public TeachingStaff(String empName, String empId) {
    validateEmployeeId(empId);
    this.empName = empName;
    this.empId = empId;
    this.salary = setSalary();
  }

  public void printStaffDetails() {
    System.out.println("Employee Name: " + empName);
    System.out.println("Employee ID: " + empId);
    printEmployeeType();
    System.out.println("Employee Salary: " + salary);
  }

  protected double setSalary() {
    throw new IllegalArgumentException("Invalid employee type");
  }

  protected void printEmployeeType() {
    throw new IllegalArgumentException("Invalid employee type");
  }

  private void validateEmployeeId(String empId) {
    if(empId.length() != 6) {
      throw new IllegalArgumentException("Invalid employee id");
    }
  }
}

class Professor extends TeachingStaff {
  public Professor(String empName, String empId) {
    super(empName, empId);
  }

  @Override
  protected double setSalary() {
      return 100000;
  }

  @Override
  protected void printEmployeeType() {
      System.out.println("Employee Type: Professor");
  }
}

class AssistantProfessor extends TeachingStaff {
  public AssistantProfessor(String empName, String empId) {
    super(empName, empId);
  }

  @Override
  protected double setSalary() {
      return 80000;
  }
  @Override
  protected void printEmployeeType() {
    System.out.println("Employee Type: Assistant Professor");
  }

}

class AssociateProfessor extends TeachingStaff {
  public AssociateProfessor(String empName, String empId) {
    super(empName, empId);
  }

  @Override
  protected double setSalary() {
      return 50000;
  }

  @Override
  protected void printEmployeeType() {
    System.out.println("Employee Type: Associate Professor");
  }
}
public class source55 {
  public static void main(String[] args) {
    Staff staff1 = new Professor("John", "123456");
    staff1.printStaffDetails();
    Staff staff2 = new AssistantProfessor("Jane", "123467");
    staff2.printStaffDetails();
    Staff staff3 = new AssociateProfessor("Doe", "897321");
    staff3.printStaffDetails();
  }
}
