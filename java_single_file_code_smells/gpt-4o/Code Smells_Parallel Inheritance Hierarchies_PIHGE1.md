**Code Review: PIHGE1.java**

- Code smell no. - 1
- Code smell name - Parallel Inheritance Hierarchies
- Code smell description - This smell occurs when related classes from two different hierarchies maintain parallel structures, leading to duplication and increased maintenance overhead.
- Found in line no. - [7, 25, 45]
- Possible treatments - Move Method & Move Field
- Possible solution - 
```java
interface VehicleGood {
    void createVehicle();
    void testFunctionality();
    void printVehicleInfo();
}

abstract class AbstractVehicle implements VehicleGood {
    private String model;
    private String engineType;
    protected String factoryName;

    public AbstractVehicle(String model, String engineType, String factory) {
        this.model = model;
        this.engineType = engineType;
        this.factoryName = factory;
    }

    public void printVehicleInfo() {
        System.out.println("Model: " + model + ", Engine Type: " + engineType);
    }
}

class Vehicle implements VehicleGood {
    private String model;
    private String engineType;
    private String factoryName;
    private String type;

    public Vehicle(String model, String engineType, String factoryName, String type) {
        this.model = model;
        this.engineType = engineType;
        this.factoryName = factoryName;
        this.type = type;
    }

    @Override
    public void createVehicle() {
        System.out.println(type + " created at " + factoryName);
    }

    @Override
    public void testFunctionality() {
        System.out.println(type + " tested at " + factoryName);
    }

    @Override
    public void printVehicleInfo() {
        System.out.println("Model: " + model + ", Engine Type: " + engineType);
    }
}

public class PIHGE1 {
    public static void main(String[] args) {
        VehicleGood car = new Vehicle("SUV", "Petrol", "Default SUV Factory", "Car");
        car.createVehicle();
        car.testFunctionality();
        car.printVehicleInfo();
        VehicleGood car2 = new Vehicle("SUV", "Petrol", "New Car Factory", "Car");
        car2.createVehicle();
        car2.testFunctionality();
        car2.printVehicleInfo();

        System.out.println();

        VehicleGood bike = new Vehicle("Mountain Bike", "Electric", "Default Mountain Bike Factory", "Bike");
        bike.createVehicle();
        bike.testFunctionality();
        bike.printVehicleInfo();
        VehicleGood bike2 = new Vehicle("Mountain Bike", "Electric", "New Bike Factory", "Bike");
        bike2.createVehicle();
        bike2.testFunctionality();
        bike2.printVehicleInfo();
    }
}
```