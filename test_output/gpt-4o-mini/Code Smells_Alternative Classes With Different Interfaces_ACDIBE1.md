```markdown
**Code Review: ACDIBE1.java**
    
    - Code smell no. - 1
    - Code smell name - Large Class
    - Code smell description - A class that has an excessive number of fields or methods, making it complex and hard to understand.
    - Found in line no. - 1, 17, 32
    - Possible treatments - Extract Class, Extract Subclass, Extract Interface, Duplicate Observed Data
    - Possible solution - 
    ```java
    class Animal {
        private String name;
        private int age;

        public Animal(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public void showInfo() {
            System.out.println("Name: " + name + ", Age: " + age);
        }
    }

    class Lion extends Animal {
        public Lion(String name, int age) {
            super(name, age);
        }

        public void lionVoice() {
            System.out.println("Roar");
        }
    }

    class Rabbit extends Animal {
        public Rabbit(String name, int age) {
            super(name, age);
        }

        public void rabbitVoice() {
            System.out.println("Squeak");
        }
    }
    
    public class ACDIBE1 {
        public static void main(String[] args) {
            Lion lion = new Lion("Simba", 5);
            lion.lionVoice();
            lion.showInfo();
            Rabbit rabbit = new Rabbit("Bunny", 2);
            rabbit.rabbitVoice();
            rabbit.showInfo();
        }
    }
    ```

    - Code smell no. - 2
    - Code smell name - Duplicate Code
    - Code smell description - The same or similar code structure is repeated in multiple locations of the code.
    - Found in line no. - 12, 28
    - Possible treatments - Extract Method, Extract Method & Pull Up Field, Pull Up Constructor Body, Form Template Method, Substitute Algorithm, Extract Superclass, Extract ClassConsolidate Conditional Expression and use Extract Method, Consolidate Duplicate Conditional Fragments
    - Possible solution - 
    ```java
    class Animal {
        private String name;
        private int age;

        public Animal(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public void showInfo() {
            System.out.println("Name: " + name + ", Age: " + age);
        }
    }

    class Lion extends Animal {
        public Lion(String name, int age) {
            super(name, age);
        }

        public void lionVoice() {
            System.out.println("Roar");
        }
    }

    class Rabbit extends Animal {
        public Rabbit(String name, int age) {
            super(name, age);
        }

        public void rabbitVoice() {
            System.out.println("Squeak");
        }
    }
    
    public class ACDIBE1 {
        public static void main(String[] args) {
            Lion lion = new Lion("Simba", 5);
            lion.lionVoice();
            lion.showInfo();
            Rabbit rabbit = new Rabbit("Bunny", 2);
            rabbit.rabbitVoice();
            rabbit.showInfo();
        }
    }
    ```

``` 

This report highlights the Large Class and Duplicate Code code smells present in the code snippet and provides possible solutions for improvement.
