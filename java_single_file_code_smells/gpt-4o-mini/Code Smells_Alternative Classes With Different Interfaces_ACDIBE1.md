```markdown
**Code Review: ACDIBE1.java**
    - Code smell no. - 1
    - Code smell name - Duplicate Code
    - Code smell description - Duplicate code occurs when the same code structure or logic appears in multiple places, which can lead to inconsistencies and makes maintenance harder.
    - Found in line no. - 1, 17
    - Possible treatments - ['Extract Class', 'Extract Method', 'Extract Method & Pull Up Field', 'Pull Up Constructor Body', 'Form Template Method', 'Substitute Algorithm', 'Extract Superclass', 'Extract ClassConsolidate Conditional Expression and use Extract Method', 'Consolidate Duplicate Conditional Fragments']
    - Possible solution - 
    ```java
    abstract class Animal {
        private String name;
        private int age;

        public Animal(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public abstract void makeSound();
        
        public void showInfo() {
            System.out.println("Name: " + name + ", Age: " + age);
        }
    }

    class Lion extends Animal {
        public Lion(String name, int age) {
            super(name, age);
        }

        @Override
        public void makeSound() {
            System.out.println("Roar");
        }
    }

    class Rabbit extends Animal {
        public Rabbit(String name, int age) {
            super(name, age);
        }

        @Override
        public void makeSound() {
            System.out.println("Squeak");
        }
    }

    public class ACDIBE1 {
        public static void main(String[] args) {
            Lion lion = new Lion("Simba", 5);
            lion.makeSound();
            lion.showInfo();

            Rabbit rabbit = new Rabbit("Bunny", 2);
            rabbit.makeSound();
            rabbit.showInfo();
        }
    }
    ```
```