enum MouseDirection {
    UP("up"),
    DOWN("down"),
    LEFT("left"),
    RIGHT("right");

    private final String direction;

    MouseDirection(String direction) {
        this.direction = direction;
    }

    @Override
    public String toString() {
        return direction;
    }
}
class Computer {
    protected String brand;
    protected String model;
    protected Character key;

    protected MouseDirection mouseDirection;
    protected boolean switchedOn;

    public Computer(String brand, String model) {
        this.brand = brand;
        this.model = model;
        this.key = '\0';
        this.switchedOn = false;
    }
    public void printDetails(){
        System.out.println("Brand: " + brand + " Model: " + model);
    }
    public void switchOnOff() {
      System.out.println(switchedOn? turnOff() : turnOn());
    }
    public void clickKeyboard(Character clickedKey) {
      this.key = clickedKey;
      System.out.println("Clicked key: " + key);
    }
    public void moveMouse(MouseDirection direction) {
      this.mouseDirection = direction;
      System.out.println("Mouse moved to: " + mouseDirection.toString());
    }
    private String turnOn() {
      switchedOn = true;
      return "Turning on.";
    }
    private String turnOff() {
      switchedOn = false;
      return "Turning off.";
    }
}

class Mobile extends Computer {
    public Mobile(String brand, String model) {
        super(brand, model);
    }

    @Override
    public void clickKeyboard(Character clickedKey) {
        return;
    }
    @Override
    public void moveMouse(MouseDirection direction) {
      return;
    }
    public void clickScreen(Character clickedKey) {
        this.key = clickedKey;
        System.out.println("Clicked screen at: " + key);
    }
}
public class source56 {
  public static void main(String[] args) {
    Computer computer = new Computer("Dell", "Inspiron");
    computer.printDetails();
    computer.switchOnOff();
    computer.clickKeyboard('a');
    computer.moveMouse(MouseDirection.UP);
    computer.switchOnOff();
    System.out.println();
    Mobile mobile = new Mobile("Samsung", "Galaxy");
    mobile.printDetails();
    mobile.switchOnOff();
    mobile.clickScreen('c');
    mobile.switchOnOff();
  }
}
