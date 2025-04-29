**Code Review: PIHGE1.java**
- Code smell no. - 1
- Code smell name - Duplicate Code
- Code smell description - The `main` method instantiates multiple `CarGood` and `BikeGood` objects with similar logic and prints their details, resulting in code duplication.
- Found in line no. -  63-70, 74-81
- Possible treatments - ['Extract Method', 'Extract Method & Pull Up Field', 'Pull Up Constructor Body', 'Form Template Method', 'Substitute Algorithm', 'Extract Superclass', 'Extract ClassConsolidate Conditional Expression and use Extract Method', 'Consolidate Duplicate Conditional Fragments']
- Possible solution - Refactor the common logic into separate methods to avoid duplication. For instance:

```java
public class PIHGE1 {
    public static void main(String[] args) {
        printVehicleDetails(new CarGood("SUV", "Petrol", "Default SUV Factory"));
        printVehicleDetails(new CarGood("SUV", "Petrol", "New Car Factory"));
        
        System.out.println();
        
        printVehicleDetails(new BikeGood("Mountain Bike", "Electric", "Default Mountain Bike Factory"));
        printVehicleDetails(new BikeGood("Mountain Bike", "Electric", "New Bike Factory"));
    }
    
    private static void printVehicleDetails(VehicleGood vehicle) {
        vehicle.createVehicle();
        vehicle.testFunctionality();
        vehicle.printVehicleInfo();
    }
}
```

This refactoring reduces duplication and makes the code more maintainable.