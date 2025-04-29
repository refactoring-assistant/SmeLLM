**Code Review: ACDIGE1.java**
- Code smell no. - 1
- Code smell name - Refused Bequest
- Code smell description - Refused Bequest occurs when a class inherits a parent class but does not use or need the inherited functionality. This might indicate that inheritance is being misused and the subclass does not naturally extend the superclass behavior.
- Found in line no. - 22, 33
- Possible treatments - ['Replace Inheritance with Delegation', 'Extract Superclass']
- Possible solution - 
```java
interface Animal {
    void animalVoice();
    void animalInfo();
}

class AnimalDetails {
    private String name;
    private int age;

    public AnimalDetails(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void animalInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

class LionGood implements Animal {
    private AnimalDetails details;

    public LionGood(String name, int age) {
        this.details = new AnimalDetails(name, age);
    }

    @Override
    public void animalVoice() {
        System.out.println("Roar");
    }

    @Override
    public void animalInfo() {
        details.animalInfo();
    }
}

class RabbitGood implements Animal {
    private AnimalDetails details;

    public RabbitGood(String name, int age) {
        this.details = new AnimalDetails(name, age);
    }

    @Override
    public void animalVoice() {
        System.out.println("Squeak");
    }

    @Override
    public void animalInfo() {
        details.animalInfo();
    }
}

public class ACDIGE1 {
    public static void main(String[] args) {
        Animal lion = new LionGood("Simba", 5);
        lion.animalVoice();
        lion.animalInfo();
        Animal rabbit = new RabbitGood("Bunny", 2);
        rabbit.animalVoice();
        rabbit.animalInfo();
    }
}
```
