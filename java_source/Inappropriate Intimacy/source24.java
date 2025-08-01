import java.util.SortedMap;
import java.util.TreeMap;

class SubjectMarks {
  private int marks;
  private SortedMap<Character, Integer> gradeScale;
  public SubjectMarks() {
    this.marks = 0;
    this.gradeScale = new TreeMap<>();
    gradeScale.put('A', 90);
    gradeScale.put('B', 80);
    gradeScale.put('C', 70);
    gradeScale.put('D', 60);
    gradeScale.put('E', 50);
    gradeScale.put('F', 0);
  }
  public Character getGrade() {
    for(SortedMap.Entry<Character, Integer> entry : gradeScale.entrySet()) {
      if(marks >= entry.getValue()) {
        return entry.getKey();
      }
    }
    return 'F';
  }

  public int getMarks() {
    return marks;
  }

  public void setMarks(int marks) {
    this.marks = marks;
  }
}

class English extends SubjectMarks {
  public English() {
    super();
  }

  public void printMarksAndGrade() {
    System.out.println("English Marks: " + getMarks() + " Grade: " + getGrade());
  }
}

class Teacher {
  private English englishSubject;
  private String name;

  public Teacher(String name, English englishSubject) {
    this.name = name;
    this.englishSubject = englishSubject;
  }

  public void setMarksPrintGrade(int marks) {
    System.out.println("Grading by English teacher: " + name);
    englishSubject.setMarks(marks);
    englishSubject.printMarksAndGrade();
  }

}
public class source24 {
  public static void main(String[] args) {
    English english = new English();
    Teacher teacher = new Teacher("John", english);
    teacher.setMarksPrintGrade(85);
  }
}
