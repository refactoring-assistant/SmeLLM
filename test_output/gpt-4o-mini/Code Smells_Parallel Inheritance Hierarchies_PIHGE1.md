```markdown
**Code Review: PIHGE1.java**
- Code smell no. - 1
- Code smell name - Duplicate Code
- Code smell description - The code has several duplicate method implementations across the `CarGood` and `BikeGood` classes, specifically the `createVehicle` and `testFunctionality` methods that share similar logic.
- Found in line no. - ~33~, ~38~, ~51~, ~56~
- Possible treatments - Extract Method, Extract Method & Pull Up Field
- Possible solution - 
```java
abstract class AbstractVehicle implements VehicleGood {
    //...
    public void createVehicle(String vehicleType) {
        System.out.println(vehicleType + " created at " + factoryName);
    }

    public void testFunctionality(String vehicleType) {
        System.out.println(vehicleType + " tested at " + factoryName);
    }
}

class CarGood extends AbstractVehicle {
    @Override
    public void createVehicle() {
        super.createVehicle("Car");
    }

    @Override
    public void testFunctionality() {
        super.testFunctionality("Car");
    }
}

class BikeGood extends AbstractVehicle {
    @Override
    public void createVehicle() {
        super.createVehicle("Bike");
    }

    @Override
    public void testFunctionality() {
        super.testFunctionality("Bike");
    }
}
```
```