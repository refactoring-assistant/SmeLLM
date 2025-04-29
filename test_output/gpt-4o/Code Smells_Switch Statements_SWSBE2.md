**Code Review: SWSBE2.java**
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - Switch statements often lead to complex and hard-to-manage code as they grow, especially if they need to be modified frequently or if the cases involve complex logic. They can also hinder polymorphism.
- Found in line no. - 13
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - 

```java
enum RouteType {
    CAR, BIKE, WALK, BUS
}

interface Route {
    void calculateTimeToDestination();
}

class CarRoute implements Route {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by car: 30 minutes");
    }
}

class BikeRoute implements Route {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by bike: 45 minutes");
    }
}

class WalkRoute implements Route {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by walk: 2 hours");
    }
}

class BusRoute implements Route {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by bus: 1 hour");
    }
}

public class SWSBE2 {
    public static void main(String[] args) {
        Route carRoute = new CarRoute();
        carRoute.calculateTimeToDestination();

        Route bikeRoute = new BikeRoute();
        bikeRoute.calculateTimeToDestination();

        Route walkRoute = new WalkRoute();
        walkRoute.calculateTimeToDestination();

        Route busRoute = new BusRoute();
        busRoute.calculateTimeToDestination();
    }
}
```