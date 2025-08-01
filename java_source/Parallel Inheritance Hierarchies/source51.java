interface Vehicle {
  void createVehicle();
  void testFunctionality();
  void printVehicleInfo();
}

abstract class AbstractVehicle implements Vehicle {
    private String model;
    private String engineType;
    protected String factoryName;

    public AbstractVehicle(String model, String engineType, String factory) {
        this.model = model;
        this.engineType = engineType;
        this.factoryName = factory;
    }

    public void printVehicleInfo() {
        System.out.println("Model: " + model
                + ", Engine Type: " + engineType);
    }
}


class Car extends AbstractVehicle {


  public Car(String model, String engineType, String factory) {
    super(model, engineType, factory);

  }
  @Override
  public void createVehicle() {
    System.out.println("Car created at " + factoryName);
  }

  @Override
  public void testFunctionality() {
    System.out.println("Car tested at " + factoryName);
  }

}


class Bike extends AbstractVehicle {
  public Bike(String model, String engineType, String factory) {
    super(model, engineType, factory);
  }

  @Override
  public void createVehicle() {
    System.out.println("Bike created at " + factoryName);
  }

  @Override
  public void testFunctionality() {
    System.out.println("Bike tested at " + factoryName);
  }
}

public class source51 {
  public static void main(String[] args) {
    Vehicle car = new Car("SUV", "Petrol", "Default SUV Factory");
    car.createVehicle();
    car.testFunctionality();
    car.printVehicleInfo();
    Vehicle car2 = new Car("SUV", "Petrol", "New Car Factory");
    car2.createVehicle();
    car2.testFunctionality();
    car2.printVehicleInfo();

    System.out.println();

    Vehicle bike = new Bike("Mountain Bike", "Electric", "Default Mountain Bike Factory");
    bike.createVehicle();
    bike.testFunctionality();
    bike.printVehicleInfo();
    Vehicle bike2 = new Bike("Mountain Bike", "Electric", "New Bike Factory");
    bike2.createVehicle();
    bike2.testFunctionality();
    bike2.printVehicleInfo();
  }
}
