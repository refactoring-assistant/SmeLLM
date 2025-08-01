class SubjectsGrading {
  private char subjectGrad;

  public SubjectsGrading() {
    this.subjectGrad = '\0';
  }

  public void setGradeBasedOnMarks(int marks) {
    if(marks >= 90) {
      setGrade('A');
    } else if(marks >= 80) {
      setGrade('B');
    } else if(marks >= 70) {
      setGrade('C');
    } else if(marks >= 60) {
      setGrade('D');
    } else {
      setGrade('F');
    }
  }

  private void setGrade(char grade) {
    this.subjectGrad = grade;
  }


  public void checkGrade() {
    if (this.subjectGrad == 'A') {
      System.out.println("Excellent");
    } else if (this.subjectGrad == 'B') {
      System.out.println("Good");
    } else if (this.subjectGrad == 'C') {
      System.out.println("Average");
    } else if (this.subjectGrad == 'D') {
      System.out.println("Poor");
    } else {
      System.out.println("Fail");
    }
  }
}

class MathClass {
  private SubjectsGrading subjectsGrading;

  public MathClass() {
    this.subjectsGrading = new SubjectsGrading();
  }

  public void setMathMarks(int marks) {
    subjectsGrading.setGradeBasedOnMarks(marks);
  }

  public void checkMathsGrade() {
    this.subjectsGrading.checkGrade();
  }
}

class EnglishClass {
  private SubjectsGrading subjectsGrading;

  public EnglishClass() {
    this.subjectsGrading = new SubjectsGrading();
  }

  public void setEnglishMarks(int marks) {
    subjectsGrading.setGradeBasedOnMarks(marks);
  }

  public void checkEnglishGrade() {
    this.subjectsGrading.checkGrade();
  }
}
public class source61 {
  public static void main(String[] args) {
    MathClass math = new MathClass();
    math.setMathMarks(85);
    EnglishClass english = new EnglishClass();
    english.setEnglishMarks(75);
    math.checkMathsGrade();
    english.checkEnglishGrade();
  }
}
