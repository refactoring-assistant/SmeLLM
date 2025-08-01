interface Vehicle {
    VehicleFactory initiateProduction();
    void setNewProductionFacility(VehicleFactory factory);
    void printVehicleInfo();
}

interface VehicleFactory {
  void createVehicle();
  void testFunctionality();
}

abstract class AbstractVehicle implements Vehicle {
    private String model;
    private String engineType;
    protected VehicleFactory factory;

    public AbstractVehicle(String model, String engineType) {
        this.model = model;
        this.engineType = engineType;
    }
    @Override
    public VehicleFactory initiateProduction() {
      return this.factory;
    }


    public void printVehicleInfo() {
        System.out.println("Model: " + model
                + ", Engine Type: " + engineType);
    }
}

abstract class AbstractVehicleFactory implements VehicleFactory {
    protected String factoryName;
    public AbstractVehicleFactory(String name) {
        this.factoryName = name;
    }


}

class Car extends AbstractVehicle {

    public Car(String model, String engineType) {
        super(model, engineType);
        this.factory = new CarFactoryBad("Default " + model + " Factory");
    }

    @Override
    public void setNewProductionFacility(VehicleFactory factory) {
      if (factory instanceof CarFactoryBad) {
        this.factory = factory;
      }
    }

}

class CarFactoryBad extends AbstractVehicleFactory {
    public CarFactoryBad(String name) {
        super(name);
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

    public Bike(String model, String engineType) {
      super(model, engineType);
      this.factory = new BikeFactory("Default " + model + " Factory");
    }



    @Override
    public void setNewProductionFacility(VehicleFactory factory) {
      if(factory instanceof BikeFactory) {
        this.factory = factory;
      }

    }
}

class BikeFactory extends AbstractVehicleFactory {
    public BikeFactory(String name) {
        super(name);
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
public class source50 {
  public static void main(String[] args) {
    Vehicle car = new Car("SUV", "Petrol");
    VehicleFactory carFactory = car.initiateProduction();
    carFactory.createVehicle();
    carFactory.testFunctionality();
    car.printVehicleInfo();
    CarFactoryBad newCarFactory = new CarFactoryBad("New Car Factory");
    car.setNewProductionFacility(newCarFactory);
    newCarFactory.createVehicle();
    newCarFactory.testFunctionality();

    System.out.println();

    Vehicle bike = new Bike("Mountain Bike", "Electric");
    VehicleFactory bikeFactory = bike.initiateProduction();
    bikeFactory.createVehicle();
    bikeFactory.testFunctionality();
    bike.printVehicleInfo();
    BikeFactory newBikeFactory = new BikeFactory("New Bike Factory");
    bike.setNewProductionFacility(newBikeFactory);
    newBikeFactory.createVehicle();
    newBikeFactory.testFunctionality();
  }
}
