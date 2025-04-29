**Code Review: RBGE1.java**

- Code smell no. - 1
- Code smell name - Inappropriate Intimacy
- Code smell description - The `MobileGood` class shows inappropriate intimacy with the `ComputerGood` class by inheriting its behavior through delegation instead of having its distinct characteristics.
- Found in line no. - [53-71]
- Possible treatments - Extract Class & Hide Delegate, Move Method & Move Field, Change Bidirectional Association to Unidirectional, Replace Delegation with Inheritance.
- Possible solution - Consider redefining the `MobileGood` class to independently handle its own logic or consider direct inheritance from shared functionality if appropriate.

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - The use of a `Character` type to represent single key or screen clicks might indicate a primitive obsession, particularly in managing input keys.
- Found in line no. - [21, 55, 35-37, 67-69]
- Possible treatments - Replace Data Value with Object, Replace Type Code with Class, Replace Array with Object.
- Possible solution - Introduce a dedicated class, such as `KeyPress`, to encapsulate the concept of a key or screen click.

```java
enum MouseDirectionGood {
  UP("up"),
  DOWN("down"),
  LEFT("left"),
  RIGHT("right");

  private final String direction;

  MouseDirectionGood(String direction) {
    this.direction = direction;
  }

  @Override
  public String toString() {
    return direction;
  }
}

class ComputerGood {
  private String brand;
  private String model;
  private KeyPress keyPress;
  private boolean switchedOn;
  MouseDirectionGood mouseDirection;

  public ComputerGood(String brand, String model) {
    this.brand = brand;
    this.model = model;
    this.keyPress = new KeyPress('\0');
  }

  public void printDetails(){
    System.out.println("Brand: " + brand + " Model: " + model);
  }

  public void switchOnOff() {
    System.out.println(switchedOn ? turnOff() : turnOn());
  }

  public void clickKeyboard(KeyPress clickedKey) {
    this.keyPress = clickedKey;
    System.out.println("Clicked key: " + keyPress);
  }

  public void moveMouse(MouseDirectionGood direction) {
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

class MobileGood {
  private ComputerGood computer;

  public MobileGood(String brand, String model) {
    computer = new ComputerGood(brand, model);
  }

  public void switchOnOff() {
    computer.switchOnOff();
  }

  public void printDetails() {
    computer.printDetails();
  }

  public void clickScreen(KeyPress clickedKey) {
    System.out.println("Clicked screen at: " + clickedKey);
  }
}

class KeyPress {
  private final char key;

  public KeyPress(char key) {
    this.key = key;
  }

  @Override
  public String toString() {
    return String.valueOf(key);
  }
}

public class RBGE1 {
  public static void main(String[] args) {
    ComputerGood computer = new ComputerGood("Dell", "Inspiron");
    computer.printDetails();
    computer.switchOnOff();
    computer.clickKeyboard(new KeyPress('a'));
    computer.moveMouse(MouseDirectionGood.UP);
    computer.switchOnOff();
    System.out.println();
    MobileGood mobile = new MobileGood("Samsung", "Galaxy");
    mobile.printDetails();
    mobile.switchOnOff();
    mobile.clickScreen(new KeyPress('c'));
    mobile.switchOnOff();
  }
}
```
