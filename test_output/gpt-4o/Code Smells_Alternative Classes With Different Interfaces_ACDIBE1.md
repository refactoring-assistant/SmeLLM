**Code Review: ACDIBE1.java**
    
- Code smell no. - 1
- Code smell name - Duplicate Code
- Code smell description - The `LionBad` and `RabbitBad` classes have similar code structures, specifically the duplication of fields and methods.
- Found in line no. - [2, 3, 4-14] and [18, 19, 20-30]
- Possible treatments - ['Extract Method', 'Extract Method & Pull Up Field', 'Pull Up Constructor Body', 'Form Template Method', 'Substitute Algorithm', 'Extract Superclass', 'Extract ClassConsolidate Conditional Expression and use Extract Method', 'Consolidate Duplicate Conditional Fragments']
- Possible solution - Refactor the code to extract a superclass `Animal`, which will encapsulate the common fields and methods (`name`, `age`, `lionInfo()/rabbitInfo()`), and then have `LionBad` and `RabbitBad` extend `Animal`.

```java
abstract class Animal {
    private String name;
    private int age;
    
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void animalInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
    
    public abstract void makeVoice();
}

class Lion extends Animal {
    public Lion(String name, int age) {
        super(name, age);
    }
    
    @Override
    public void makeVoice() {
        System.out.println("Roar");
    }
}

class Rabbit extends Animal {
    public Rabbit(String name, int age) {
        super(name, age);
    }
    
    @Override
    public void makeVoice() {
        System.out.println("Squeak");
    }
}

public class ACDIBE1 {
    public static void main(String[] args) {
        Lion lion = new Lion("Simba", 5);
        lion.makeVoice();
        lion.animalInfo();
        Rabbit rabbit = new Rabbit("Bunny", 2);
        rabbit.makeVoice();
        rabbit.animalInfo();
    }
}
```

This refactor reduces duplication by leveraging inheritance to extract shared properties and methods into a superclass, resulting in a cleaner and more maintainable design.