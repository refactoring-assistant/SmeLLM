```markdown
**Code Review: SSGE1.java**
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - The `setGradeBasedOnMarks` method in the `SubjectsGradingGood` class (~8~-~20~) and the `checkGrade` method in the same class (~27~-~39~) use multiple if-else statements to handle different grades, which is a form of switch statement.
- Found in line no. - [8-20], [27-39]
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - Extract the grade logic into separate methods or use a polymorphic approach with subclasses representing each grade.

```java
class SubjectsGradingGood {
    private char subjectGrad;

    public SubjectsGradingGood() {
        this.subjectGrad = '\0';
    }

    public void setGradeBasedOnMarks(int marks) {
        this.subjectGrad = determineGrade(marks);
    }

    private char determineGrade(int marks) {
        if (marks >= 90) {
            return 'A';
        } else if (marks >= 80) {
            return 'B';
        } else if (marks >= 70) {
            return 'C';
        } else if (marks >= 60) {
            return 'D';
        } else {
            return 'F';
        }
    }

    public void checkGrade() {
        System.out.println(determineGradeMessage(this.subjectGrad));
    }

    private String determineGradeMessage(char grade) {
        switch (grade) {
            case 'A':
                return "Excellent";
            case 'B':
                return "Good";
            case 'C':
                return "Average";
            case 'D':
                return "Poor";
            default:
                return "Fail";
        }
    }
}

class MathClassGood {
    private SubjectsGradingGood subjectsGrading;

    public MathClassGood() {
        this.subjectsGrading = new SubjectsGradingGood();
    }

    public void setMathMarks(int marks) {
        subjectsGrading.setGradeBasedOnMarks(marks);
    }

    public void checkMathsGrade() {
        this.subjectsGrading.checkGrade();
    }
}

class EnglishClassGood {
    private SubjectsGradingGood subjectsGrading;

    public EnglishClassGood() {
        this.subjectsGrading = new SubjectsGradingGood();
    }

    public void setEnglishMarks(int marks) {
        subjectsGrading.setGradeBasedOnMarks(marks);
    }

    public void checkEnglishGrade() {
        this.subjectsGrading.checkGrade();
    }
}

public class SSGE1 {
    public static void main(String[] args) {
        MathClassGood math = new MathClassGood();
        math.setMathMarks(85);
        EnglishClassGood english = new EnglishClassGood();
        english.setEnglishMarks(75);
        math.checkMathsGrade();
        english.checkEnglishGrade();
    }
}
```
```