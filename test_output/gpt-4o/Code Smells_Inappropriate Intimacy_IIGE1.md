**Code Review: IIGE1.java**

- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The `gradeScale` is being stored using primitive data (character for grades and integers for marks cut-off) in a `TreeMap`. This reliance on primitives can make the code less expressive and more error-prone as it grows.
- Found in line no. - [6, 10, 11, 12, 13, 14, 15]
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - Replace the `SortedMap` for gradeScale with a dedicated `Grade` class that encapsulates the grade and its criteria:
  
  ```java
  import java.util.ArrayList;
  import java.util.List;
  
  class Grade {
      private char gradeLetter;
      private int minMark;
  
      public Grade(char gradeLetter, int minMark) {
          this.gradeLetter = gradeLetter;
          this.minMark = minMark;
      }
  
      public char getGradeLetter() {
          return gradeLetter;
      }
  
      public int getMinMark() {
          return minMark;
      }
  }
  
  class SubjectMarksGood {
      private int marks;
      private List<Grade> gradeScale;
  
      public SubjectMarksGood() {
          this.marks = 0;
          this.gradeScale = new ArrayList<>();
          gradeScale.add(new Grade('A', 90));
          gradeScale.add(new Grade('B', 80));
          gradeScale.add(new Grade('C', 70));
          gradeScale.add(new Grade('D', 60));
          gradeScale.add(new Grade('E', 50));
          gradeScale.add(new Grade('F', 0));
      }
  
      public Character getGrade() {
          for (Grade grade : gradeScale) {
              if (marks >= grade.getMinMark()) {
                  return grade.getGradeLetter();
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

Note that the rest of the implementation stays intact and properly aligned with the structure suggested by the dedicated class for grades.