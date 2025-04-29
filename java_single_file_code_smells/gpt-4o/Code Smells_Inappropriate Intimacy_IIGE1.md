**Code Review: IIGE1.java**

- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - A long method is difficult to understand and maintain. The constructor in the `SubjectMarksGood` class has multiple responsibilities such as setting up the `gradeScale`.
- Found in line no. - [7-16]
- Possible treatments - ['Extract Method']
- Possible solution - Create a separate method like `initializeGradeScale()` to handle the initialization of the `gradeScale`.

```java
class SubjectMarksGood {
  private int marks;
  private SortedMap<Character, Integer> gradeScale;

  public SubjectMarksGood() {
    this.marks = 0;
    this.gradeScale = initializeGradeScale();
  }

  private SortedMap<Character, Integer> initializeGradeScale() {
    SortedMap<Character, Integer> scale = new TreeMap<>();
    scale.put('A', 90);
    scale.put('B', 80);
    scale.put('C', 70);
    scale.put('D', 60);
    scale.put('E', 50);
    scale.put('F', 0);
    return scale;
  }
  
  // Remaining code unchanged

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

class EnglishGood extends SubjectMarksGood {
  public EnglishGood() {
    super();
  }
  
  public void printMarksAndGrade() {
    System.out.println("English Marks: " + getMarks() + " Grade: " + getGrade());
  }
}

class TeacherGood {
  private EnglishGood englishSubject;
  private String name;
  
  public TeacherGood(String name, EnglishGood englishSubject) {
    this.name = name;
    this.englishSubject = englishSubject;
  }
  
  public void setMarksPrintGrade(int marks) {
    System.out.println("Grading by English teacher: " + name);
    englishSubject.setMarks(marks);
    englishSubject.printMarksAndGrade();
  }
}

public class IIGE1 {
  public static void main(String[] args) {
    EnglishGood english = new EnglishGood();
    TeacherGood teacher = new TeacherGood("John", english);
    teacher.setMarksPrintGrade(85);
  }
}
```

This refactoring makes the constructor of `SubjectMarksGood` easier to read and understand by moving the gradeScale setup to a separate method.