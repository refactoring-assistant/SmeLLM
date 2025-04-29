**Code Review: SSGE1.java**

- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - A sequence of if-else statements acting as a switch on conditions, leading to rigid and hard-to-maintain code.
- Found in line no. - [8-20, 27-38]
- Possible treatments - ['Extract Method & then Move Method', ' Replace Conditional with Polymorphism']
- Possible solution - Replace the conditionals in `setGradeBasedOnMarks` and `checkGrade` methods with polymorphism to handle different grade levels. Define an interface or use an enum for Grade, with each grade handling its own grading logic and message.

```java
interface Grade {
    void setGrade(SubjectsGradingGood subject);
    void printMessage();
}

class GradeA implements Grade {
    public void setGrade(SubjectsGradingGood subject) {
        subject.setGrade('A');
    }
    public void printMessage() {
        System.out.println("Excellent");
    }
}

class GradeB implements Grade {
    public void setGrade(SubjectsGradingGood subject) {
        subject.setGrade('B');
    }
    public void printMessage() {
        System.out.println("Good");
    }
}

class GradeC implements Grade {
    public void setGrade(SubjectsGradingGood subject) {
        subject.setGrade('C');
    }
    public void printMessage() {
        System.out.println("Average");
    }
}

class GradeD implements Grade {
    public void setGrade(SubjectsGradingGood subject) {
        subject.setGrade('D');
    }
    public void printMessage() {
        System.out.println("Poor");
    }
}

class GradeF implements Grade {
    public void setGrade(SubjectsGradingGood subject) {
        subject.setGrade('F');
    }
    public void printMessage() {
        System.out.println("Fail");
    }
}

class SubjectsGradingGood {
    private char subjectGrad;
    private Grade gradeStrategy;

    public SubjectsGradingGood() {
        this.subjectGrad = '\0';
    }

    public void setGradeBasedOnMarks(int marks) {
        if (marks >= 90) {
            gradeStrategy = new GradeA();
        } else if (marks >= 80) {
            gradeStrategy = new GradeB();
        } else if (marks >= 70) {
            gradeStrategy = new GradeC();
        } else if (marks >= 60) {
            gradeStrategy = new GradeD();
        } else {
            gradeStrategy = new GradeF();
        }
        gradeStrategy.setGrade(this);
    }

    public void checkGrade() {
        gradeStrategy.printMessage();
    }

    void setGrade(char grade) {
        this.subjectGrad = grade;
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