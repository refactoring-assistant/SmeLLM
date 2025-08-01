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
  private String brand;
  private String model;
  private Character key;
  private boolean switchedOn;
  MouseDirection mouseDirection;
  public Computer(String brand, String model) {
    this.brand = brand;
    this.model = model;
    this.key = '\0';
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

class Mobile {
  private Computer computer;
  private Character key;
  public Mobile(String brand, String model) {
    computer = new Computer(brand, model);
  }

  public void switchOnOff() {
    computer.switchOnOff();
  }

  public void printDetails() {
    computer.printDetails();
  }
  public void clickScreen(Character clickedKey) {
    this.key = clickedKey;
    System.out.println("Clicked screen at: " + key);
  }
}
public class source58 {
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
