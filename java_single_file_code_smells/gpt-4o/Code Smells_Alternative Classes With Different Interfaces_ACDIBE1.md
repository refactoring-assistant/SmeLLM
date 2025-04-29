**Code Review: ACDIBE1.java**

- Code smell no. - 1
- Code smell name - Duplicate Code
- Code smell description - The classes `LionBad` and `RabbitBad` have similar fields and methods, leading to code duplication.
- Found in line no. - 1-15, 17-31
- Possible treatments - ['Extract Method', 'Extract Class', 'Consolidate Conditional Expression and use Extract Method']
- Possible solution - Introduce a parent class `Animal` to encapsulate common properties and methods.

```java
abstract class Animal {
    private String name;
    private int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void voice() {
        // This method should be overridden by subclasses
    }

    public void info() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

class Lion extends Animal {
    public Lion(String name, int age) {
        super(name, age);
    }

    @Override
    public void voice() {
        System.out.println("Roar");
    }
}

class Rabbit extends Animal {
    public Rabbit(String name, int age) {
        super(name, age);
    }

    @Override
    public void voice() {
        System.out.println("Squeak");
    }
}

public class ACDIBE1 {
    public static void main(String[] args) {
        Lion lion = new Lion("Simba", 5);
        lion.voice();
        lion.info();
        Rabbit rabbit = new Rabbit("Bunny", 2);
        rabbit.voice();
        rabbit.info();
    }
}
```

By introducing an abstract `Animal` class, we can reduce duplicate code and make it easier to manage common properties and behaviors among different animal types.