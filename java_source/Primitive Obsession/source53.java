interface Staff {
    void printStaffDetails();
}
class TeachingStaff implements Staff {
  private String empType;
  private String empName;
  private String empId;
  private double salary;

    public TeachingStaff(String empType, String empName, String empId) {
        validateEmployeeId(empId);
        this.empName = empName;
        this.empId = empId;
        this.salary = setSalary(empType);
        this.empType = empType;
    }

    public void printStaffDetails() {
        System.out.println("Employee Name: " + empName);
        System.out.println("Employee ID: " + empId);
        System.out.println("Employee Type: " + empType);
        System.out.println("Employee Salary: " + salary);
    }

    private double setSalary(String empType) {
        if(empType.equals("Professor")) {
          return 100000;
        } else if(empType.equals("Assistant Professor")) {
          return 80000;
        } else if(empType.equals("Associate Professor")) {
          return 50000;
        } else {
          throw new IllegalArgumentException("Invalid employee type");
        }
    }

    private void validateEmployeeId(String empId) {
        if(empId.length() != 6) {
            throw new IllegalArgumentException("Invalid employee id");
        }
    }
}
public class source53 {
    public static void main(String[] args) {
        TeachingStaff staff1 = new TeachingStaff("Professor", "John", "123456");
        staff1.printStaffDetails();
        TeachingStaff staff2 = new TeachingStaff("Assistant Professor", "Jane", "123467");
        staff2.printStaffDetails();
        TeachingStaff staff3 = new TeachingStaff("Associate Professor", "Doe", "897321");
        staff3.printStaffDetails();
    }
}
