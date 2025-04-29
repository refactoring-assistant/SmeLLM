**Code Review: PIHBE1.java**
    
- Code smell no. - 1
- Code smell name - Parallel Inheritance Hierarchies
- Code smell description - There are parallel class hierarchies where for each subclass of one hierarchy (e.g., `AbstractVehicleBad`), there is a corresponding subclass in another hierarchy (e.g., `AbstractVehicleFactoryBad`).
- Found in line no. - 12, 33, 42, 58, 73, 91.
- Possible treatments - Move Method & Move Field
- Possible solution - In order to eliminate parallel inheritance hierarchies, we can refactor the related classes and introduce an association between the `Vehicle` and `VehicleFactory` rather than having parallel hierarchies. This can be achieved by consolidating the logic concerning creation and testing of vehicles into more cohesive structures.
  
```java
class Vehicle {
    private String model;
    private String engineType;
    private VehicleFactory factory;

    public Vehicle(String model, String engineType, VehicleFactory factory) {
        this.model = model;
        this.engineType = engineType;
        this.factory = factory;
    }

    public void printVehicleInfo() {
        System.out.println("Model: " + model + ", Engine Type: " + engineType);
    }

    public void createVehicle() {
        factory.createVehicle(model);
    }

    public void testFunctionality() {
        factory.testFunctionality(model);
    }

    public void setNewProductionFacility(VehicleFactory factory) {
        this.factory = factory;
    }
}

class VehicleFactory {
    private String factoryName;

    public VehicleFactory(String factoryName) {
        this.factoryName = factoryName;
    }

    public void createVehicle(String model) {
        System.out.println(model + " created at " + factoryName);
    }

    public void testFunctionality(String model) {
        System.out.println(model + " tested at " + factoryName);
    }
}

public class PIHBE1 {
    public static void main(String[] args) {
        Vehicle car = new Vehicle("SUV", "Petrol", new VehicleFactory("Default Car Factory"));
        car.createVehicle();
        car.testFunctionality();
        car.printVehicleInfo();

        VehicleFactory newCarFactory = new VehicleFactory("New Car Factory");
        car.setNewProductionFacility(newCarFactory);
        car.createVehicle();
        car.testFunctionality();

        System.out.println();

        Vehicle bike = new Vehicle("Mountain Bike", "Electric", new VehicleFactory("Default Bike Factory"));
        bike.createVehicle();
        bike.testFunctionality();
        bike.printVehicleInfo();

        VehicleFactory newBikeFactory = new VehicleFactory("New Bike Factory");
        bike.setNewProductionFacility(newBikeFactory);
        bike.createVehicle();
        bike.testFunctionality();
    }
}
```

This approach simplifies the code structure and avoids the unnecessary parallel class hierarchy.