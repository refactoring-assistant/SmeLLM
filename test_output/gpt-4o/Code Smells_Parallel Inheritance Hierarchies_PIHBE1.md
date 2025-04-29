```markdown
**Code Review: PIHBE1.java**
    
- Code smell no. - 1
- Code smell name - Parallel Inheritance Hierarchies
- Code smell description - This smell occurs when changes in one hierarchy (e.g., `AbstractVehicleBad`, `CarBad`, `BikeBad`) necessitate mirror changes in another hierarchy (`AbstractVehicleFactoryBad`, `CarFactoryBad`, `BikeFactoryBad`).
- Found in line no. - 12, 33, 42, 73, 58, 91
- Possible treatments - ['Move Method & Move Field']
- Possible solution -
  
  ```java
  interface Vehicle {
      void createVehicle();
      void testVehicle();
      void printVehicleInfo();
  }
  
  class VehicleFactory {
      private String factoryName;
  
      public VehicleFactory(String name) {
          this.factoryName = name;
      }
  
      public void createVehicle(String type) {
          System.out.println(type + " created at " + factoryName);
      }
  
      public void testVehicle(String type) {
          System.out.println(type + " tested at " + factoryName);
      }
  }
  
  class Car implements Vehicle {
      private String model;
      private String engineType;
      private VehicleFactory factory;
  
      public Car(String model, String engineType, VehicleFactory factory) {
          this.model = model;
          this.engineType = engineType;
          this.factory = factory;
      }
  
      @Override
      public void createVehicle() {
          factory.createVehicle("Car");
      }
  
      @Override
      public void testVehicle() {
          factory.testVehicle("Car");
      }
  
      @Override
      public void printVehicleInfo() {
          System.out.println("Model: " + model + ", Engine Type: " + engineType);
      }
  
      public void setNewProductionFacility(VehicleFactory factory) {
          this.factory = factory;
      }
  }
  
  class Bike implements Vehicle {
      private String model;
      private String engineType;
      private VehicleFactory factory;
  
      public Bike(String model, String engineType, VehicleFactory factory) {
          this.model = model;
          this.engineType = engineType;
          this.factory = factory;
      }
  
      @Override
      public void createVehicle() {
          factory.createVehicle("Bike");
      }
  
      @Override
      public void testVehicle() {
          factory.testVehicle("Bike");
      }
  
      @Override
      public void printVehicleInfo() {
          System.out.println("Model: " + model + ", Engine Type: " + engineType);
      }
  
      public void setNewProductionFacility(VehicleFactory factory) {
          this.factory = factory;
      }
  }
  
  public class PIHBE1 {
      public static void main(String[] args) {
          VehicleFactory carFactory = new VehicleFactory("Default SUV Factory");
          Vehicle car = new Car("SUV", "Petrol", carFactory);
          car.createVehicle();
          car.testVehicle();
          car.printVehicleInfo();
          
          VehicleFactory newCarFactory = new VehicleFactory("New Car Factory");
          ((Car) car).setNewProductionFacility(newCarFactory);
          car.createVehicle();
          car.testVehicle();
          
          System.out.println();
  
          VehicleFactory bikeFactory = new VehicleFactory("Default Mountain Bike Factory");
          Vehicle bike = new Bike("Mountain Bike", "Electric", bikeFactory);
          bike.createVehicle();
          bike.testVehicle();
          bike.printVehicleInfo();
  
          VehicleFactory newBikeFactory = new VehicleFactory("New Bike Factory");
          ((Bike) bike).setNewProductionFacility(newBikeFactory);
          bike.createVehicle();
          bike.testVehicle();
      }
  }
  ```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - Use of strings to represent different types and factory management instead of using appropriate data structures or objects.
- Found in line no. - 13, 14, 34
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution -
 
  ```java
  class VehicleInfo {
      private String model;
      private String engineType;

      public VehicleInfo(String model, String engineType) {
          this.model = model;
          this.engineType = engineType;
      }

      public String getModel() {
          return model;
      }

      public String getEngineType() {
          return engineType;
      }
  }

  class VehicleFactory {
      // Factory logic remains similar with possible additions for VehicleInfo usage
  }

  class Car {
      private VehicleInfo info;
      private VehicleFactory factory;

      public Car(VehicleInfo info, VehicleFactory factory) {
          this.info = info;
          this.factory = factory;
      }

      // Methods using info.getModel() and info.getEngineType()
  }

  class Bike {
      private VehicleInfo info;
      private VehicleFactory factory;

      public Bike(VehicleInfo info, VehicleFactory factory) {
          this.info = info;
          this.factory = factory;
      }

      // Methods using info.getModel() and info.getEngineType()
  }
  ```

```
