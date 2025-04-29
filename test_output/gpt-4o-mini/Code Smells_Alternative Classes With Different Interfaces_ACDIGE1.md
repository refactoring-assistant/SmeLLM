```markdown
**Code Review: ACDIGE1.java**
    - Code smell no. - 1
    - Code smell name - Large Class
    - Code smell description - The class ACDIGE1 contains multiple responsibilities and serves as the main entry point for the application while also housing all the functionality of the animal classes.
    - Found in line no. - [43]
    - Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
    - Possible solution - 
    ```java
    public class AnimalApp {
        public static void main(String[] args) {
            Animal lion = new LionGood("Simba", 5);
            lion.animalVoice();
            lion.animalInfo();
            Animal rabbit = new RabbitGood("Bunny", 2);
            rabbit.animalVoice();
            rabbit.animalInfo();
        }
    }

    interface Animal {
        void animalVoice();
        void animalInfo();
    }

    abstract class AbstractAnimal implements Animal {
        private String name;
        private int age;

        public AbstractAnimal(String name, int age) {
            this.name = name;
            this.age = age;
        }

        abstract public void animalVoice();

        public void animalInfo() {
            System.out.println("Name: " + name + ", Age: " + age);
        }
    }

    class LionGood extends AbstractAnimal {
        public LionGood(String name, int age) {
            super(name, age);
        }

        @Override
        public void animalVoice() {
            System.out.println("Roar");
        }
    }

    class RabbitGood extends AbstractAnimal {
        public RabbitGood(String name, int age) {
            super(name, age);
        }

        @Override
        public void animalVoice() {
            System.out.println("Squeak");
        }
    }
    ```
```