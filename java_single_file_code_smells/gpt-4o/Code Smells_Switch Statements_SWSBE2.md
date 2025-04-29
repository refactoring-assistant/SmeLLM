**Code Review: SWSBE2.java**
    
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - Switch statements can lead to complex and unmanageable code, especially when adding new cases. It often violates the Open/Closed Principle.
- Found in line no. - [13]
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - 

```java
enum RouteTypeBad {
    CAR, BIKE, WALK, BUS
}

interface RouteBad {
    void calculateTimeToDestination();
}

class CarRoute implements RouteBad {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by car: 30 minutes");
    }
}

class BikeRoute implements RouteBad {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by bike: 45 minutes");
    }
}

class WalkRoute implements RouteBad {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by walk: 2 hours");
    }
}

class BusRoute implements RouteBad {
    @Override
    public void calculateTimeToDestination() {
        System.out.println("Time to destination by bus: 1 hour");
    }
}

public class SWSBE2 {
    public static void main(String[] args) {
        RouteBad userRoute;

        userRoute = new CarRoute();
        userRoute.calculateTimeToDestination();

        userRoute = new BikeRoute();
        userRoute.calculateTimeToDestination();

        userRoute = new WalkRoute();
        userRoute.calculateTimeToDestination();

        userRoute = new BusRoute();
        userRoute.calculateTimeToDestination();
    }
}
```

This solution uses polymorphism to replace the switch statement, creating a class for each route type that implements the `RouteBad` interface, so that each route type knows how to calculate its time to destination.