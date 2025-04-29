**Code Review: IIGE1.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The code uses primitive types (int for marks, char for grades) where more complex types or objects would better encapsulate the data and behavior associated with these values.
- Found in line no. - ~5~, ~10~, ~12~, ~15~, ~26~, ~30~
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object.
- Possible solution: 
```java
import java.util.SortedMap;
import java.util.TreeMap;

class Grade {
    private final char letter;
    private final int threshold;

    public Grade(char letter, int threshold) {
        this.letter = letter;
        this.threshold = threshold;
    }

    public char getLetter() {
        return letter;
    }

    public int getThreshold() {
        return threshold;
    }
}

class SubjectMarksGood {
    private int marks;
    private SortedMap<Character, Grade> gradeScale;

    public SubjectMarksGood() {
        this.marks = 0;
        this.gradeScale = new TreeMap<>();
        gradeScale.put('A', new Grade('A', 90));
        gradeScale.put('B', new Grade('B', 80));
        gradeScale.put('C', new Grade('C', 70));
        gradeScale.put('D', new Grade('D', 60));
        gradeScale.put('E', new Grade('E', 50));
        gradeScale.put('F', new Grade('F', 0));
    }

    public char getGrade() {
        for (Grade grade : gradeScale.values()) {
            if (marks >= grade.getThreshold()) {
                return grade.getLetter();
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