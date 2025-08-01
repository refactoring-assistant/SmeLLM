class SubjectsGrading {
  private char subjectGrad;

    public SubjectsGrading() {
        this.subjectGrad = '\0';
    }

    public void setSubjectGrade(char grade) {
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
      setMathGrade(marks);
  }

  public void checkMathsGrade() {
    this.subjectsGrading.checkGrade();
  }

  private void setMathGrade(int marks) {
    if(marks >= 90) {
      this.subjectsGrading.setSubjectGrade('A');
    } else if(marks >= 80) {
      this.subjectsGrading.setSubjectGrade('B');
    } else if(marks >= 70) {
      this.subjectsGrading.setSubjectGrade('C');
    } else if(marks >= 60) {
      this.subjectsGrading.setSubjectGrade('D');
    } else {
      this.subjectsGrading.setSubjectGrade('F');
    }
  }
}

class EnglishClass {
  private SubjectsGrading subjectsGrading;

  public EnglishClass() {
    this.subjectsGrading = new SubjectsGrading();
  }

  public void setEnglishMarks(int marks) {
    setEnglishGrade(marks);
  }

  public void checkEnglishGrade() {
    this.subjectsGrading.checkGrade();
  }

  private void setEnglishGrade(int marks) {
    if(marks >= 90) {
      this.subjectsGrading.setSubjectGrade('A');
    } else if(marks >= 80) {
      this.subjectsGrading.setSubjectGrade('B');
    } else if(marks >= 70) {
      this.subjectsGrading.setSubjectGrade('C');
    } else if(marks >= 60) {
      this.subjectsGrading.setSubjectGrade('D');
    } else {
      this.subjectsGrading.setSubjectGrade('F');
    }
  }
}
public class source60 {
  public static void main(String[] args) {
    MathClass math = new MathClass();
    math.setMathMarks(85);
    EnglishClass english = new EnglishClass();
    english.setEnglishMarks(75);
    math.checkMathsGrade();
    english.checkEnglishGrade();
  }
}
