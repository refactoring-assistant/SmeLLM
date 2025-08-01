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

class Lion extends AbstractAnimal implements Animal {
    public Lion(String name, int age) {
        super(name, age);
    }

    @Override
    public void animalVoice() {
        System.out.println("Roar");
    }
}

class Rabbit extends AbstractAnimal implements Animal {
    public Rabbit(String name, int age) {
        super(name, age);
    }

    @Override
    public void animalVoice() {
        System.out.println("Squeak");
    }
}
public class source2 {
  public static void main(String[] args) {
    Animal lion = new Lion("Simba", 5);
    lion.animalVoice();
    lion.animalInfo();
    Animal rabbit = new Rabbit("Bunny", 2);
    rabbit.animalVoice();
    rabbit.animalInfo();
  }
}
