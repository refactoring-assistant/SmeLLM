```markdown
**Code Review: LCBE2.java**
    - Code smell no. - 1
    - Code smell name - Alternative Classes with Different Interfaces
    - Code smell description - The interface `IPersonBad` has methods that may not apply uniformly across all types of persons, leading to a lack of cohesion between the methods and the classes implementing this interface.
    - Found in line no. - 1
    - Possible treatments - ['Rename Method', 'Move Method, Add Parameter & Parameterize Method', 'Extract Superclass']
    - Possible solution:
    ```java
    interface IPerson {
        void printDetails();
    }

    class Person implements IPerson {
        private String name;

        public Person(String name) {
            this.name = name;
        }

        @Override
        public void printDetails() {
            System.out.println("Name: " + this.name);
        }
    }

    class Student extends Person {
        private String studentId;
        private String major;

        public Student(String name, String studentId, String major) {
            super(name);
            this.studentId = studentId;
            this.major = major;
        }

        @Override
        public void printDetails() {
            super.printDetails();
            System.out.println("Student ID: " + this.studentId);
            System.out.println("Major: " + this.major);
        }
    }

    public class LCBE2 {
        public static void main(String[] args) {
            IPerson person1 = new Student("John", "123456", "Computer Science");
            System.out.println("Details:");
            person1.printDetails();
        }
    }
    ```
```