class Lion {
    private String name;
    private int age;
    public Lion(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void lionVoice() {
        System.out.println("Roar");
    }
    public void lionInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

class Rabbit {
    private String name;
    private int age;
    public Rabbit(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void rabbitVoice() {
        System.out.println("Squeak");
    }
    public void rabbitInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}
public class source1 {
    public static void main(String[] args) {
        Lion lion = new Lion("Simba", 5);
        lion.lionVoice();
        lion.lionInfo();
        Rabbit rabbit = new Rabbit("Bunny", 2);
        rabbit.rabbitVoice();
        rabbit.rabbitInfo();
    }
}
