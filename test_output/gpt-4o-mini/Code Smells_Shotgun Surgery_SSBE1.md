**Code Review: SSBE1.java**
    - Code smell no. - 1
    - Code smell name - Primitive Obsession
    - Code smell description - The use of a primitive type (char) for representing the subject grade, which can be replaced with a more descriptive and meaningful object (like a Grade class).
    - Found in line no. - 2, 8, 44, 74
    - Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class.
    - Possible solution - 
    ```java
    class Grade {
        private char value;

        public Grade(char value) {
            this.value = value;
        }

        public char getValue() {
            return value;
        }

        @Override
        public String toString() {
            switch (value) {
                case 'A': return "Excellent";
                case 'B': return "Good";
                case 'C': return "Average";
                case 'D': return "Poor";
                default: return "Fail";
            }
        }
    }

    class SubjectsGrading {
        private Grade subjectGrad;

        public SubjectsGrading() {
            this.subjectGrad = new Grade('\0');
        }

        public void setSubjectGrade(Grade grade) {
            this.subjectGrad = grade;
        }

        public void checkGrade() {
            System.out.println(subjectGrad.toString());
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
            if (marks >= 90) {
                this.subjectsGrading.setSubjectGrade(new Grade('A'));
            } else if (marks >= 80) {
                this.subjectsGrading.setSubjectGrade(new Grade('B'));
            } else if (marks >= 70) {
                this.subjectsGrading.setSubjectGrade(new Grade('C'));
            } else if (marks >= 60) {
                this.subjectsGrading.setSubjectGrade(new Grade('D'));
            } else {
                this.subjectsGrading.setSubjectGrade(new Grade('F'));
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
            if (marks >= 90) {
                this.subjectsGrading.setSubjectGrade(new Grade('A'));
            } else if (marks >= 80) {
                this.subjectsGrading.setSubjectGrade(new Grade('B'));
            } else if (marks >= 70) {
                this.subjectsGrading.setSubjectGrade(new Grade('C'));
            } else if (marks >= 60) {
                this.subjectsGrading.setSubjectGrade(new Grade('D'));
            } else {
                this.subjectsGrading.setSubjectGrade(new Grade('F'));
            }
        }
    }

    public class SSBE1 {
        public static void main(String[] args) {
            MathClass math = new MathClass();
            math.setMathMarks(85);
            EnglishClass english = new EnglishClass();
            english.setEnglishMarks(75);
            math.checkMathsGrade();
            english.checkEnglishGrade();
        }
    }
    ``` 

    - Code smell no. - 2
    - Code smell name - Duplicate Code
    - Code smell description - The logic for setting grades in `setMathGrade` and `setEnglishGrade` methods is duplicated, which violates DRY (Don't Repeat Yourself) principle.
    - Found in line no. - 42-52, 72-82
    - Possible treatments - Extract Method, Consolidate Duplicate Conditional Fragments.
    - Possible solution - 
    ```java
    private void setGrade(int marks, SubjectsGrading grading) {
        if (marks >= 90) {
            grading.setSubjectGrade(new Grade('A'));
        } else if (marks >= 80) {
            grading.setSubjectGrade(new Grade('B'));
        } else if (marks >= 70) {
            grading.setSubjectGrade(new Grade('C'));
        } else if (marks >= 60) {
            grading.setSubjectGrade(new Grade('D'));
        } else {
            grading.setSubjectGrade(new Grade('F'));
        }
    }

    public void setMathMarks(int marks) {
        setGrade(marks, this.subjectsGrading);
    }

    public void setEnglishMarks(int marks) {
        setGrade(marks, this.subjectsGrading);
    }
    ``` 

    - Code smell no. - 3
    - Code smell name - Large Class
    - Code smell description - The `SubjectsGrading`, `MathClass`, and `EnglishClass` classes are doing multiple tasks and could be split into smaller classes that each handle a single responsibility.
    - Found in line no. - 1, 27, 57
    - Possible treatments - Extract Class, Extract Interface.
    - Possible solution - 
    (Split each class into more specific responsibilities, like grading, reporting on performance, etc. For instance, you could create a class to manage grades separately from the classes that represent subjects.)
