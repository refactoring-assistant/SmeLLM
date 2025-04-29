**Code Review: RBBE1.java**

- Code smell no. - 1
- Code smell name - Refused Bequest
- Code smell description - The `MobileBad` class inherits from `ComputerBad` but does not utilize all inherited behavior (e.g., `clickKeyboard`, `moveMouse` methods), undermining the intended purpose of inheritance.
- Found in line no. - 56-73
- Possible treatments - ['Replace Inheritance with Delegation', 'Extract Superclass']
- Possible solution - 
  ```java
  enum MouseDirectionBad {
      UP("up"), DOWN("down"), LEFT("left"), RIGHT("right");

      private final String direction;

      MouseDirectionBad(String direction) {
          this.direction = direction;
      }

      @Override
      public String toString() {
          return direction;
      }
  }

  class Device {
      protected String brand;
      protected String model;
      protected boolean switchedOn;

      public Device(String brand, String model) {
          this.brand = brand;
          this.model = model;
          this.switchedOn = false;
      }

      public void printDetails() {
          System.out.println("Brand: " + brand + " Model: " + model);
      }

      public void switchOnOff() {
          System.out.println(switchedOn ? turnOff() : turnOn());
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

  class ComputerBad extends Device {
      protected Character key;
      protected MouseDirectionBad mouseDirection;

      public ComputerBad(String brand, String model) {
          super(brand, model);
          this.key = '\0';
      }

      public void clickKeyboard(Character clickedKey) {
          this.key = clickedKey;
          System.out.println("Clicked key: " + key);
      }

      public void moveMouse(MouseDirectionBad direction) {
          this.mouseDirection = direction;
          System.out.println("Mouse moved to: " + mouseDirection.toString());
      }
  }

  class MobileBad {
      private final Device device;
      private Character key;

      public MobileBad(String brand, String model) {
          this.device = new Device(brand, model);
      }

      public void printDetails() {
          device.printDetails();
      }

      public void switchOnOff() {
          device.switchOnOff();
      }

      public void clickScreen(Character clickedKey) {
          this.key = clickedKey;
          System.out.println("Clicked screen at: " + key);
      }
  }

  public class RBBE1 {
      public static void main(String[] args) {
          ComputerBad computer = new ComputerBad("Dell", "Inspiron");
          computer.printDetails();
          computer.switchOnOff();
          computer.clickKeyboard('a');
          computer.moveMouse(MouseDirectionBad.UP);
          computer.switchOnOff();
          System.out.println();
          MobileBad mobile = new MobileBad("Samsung", "Galaxy");
          mobile.printDetails();
          mobile.switchOnOff();
          mobile.clickScreen('c');
          mobile.switchOnOff();
      }
  }
  ```