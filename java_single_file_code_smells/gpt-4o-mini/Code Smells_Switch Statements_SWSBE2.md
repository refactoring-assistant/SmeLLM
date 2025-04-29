```markdown
**Code Review: SWSBE2.java**
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - The use of switch statements indicates that the code could be improved by using polymorphism instead, which enhances scalability and maintainability.
- Found in line no. - 13
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - 
```java
enum RouteType {
    CAR {
        @Override
        public void calculateRoute() {
            System.out.println("Time to destination by car: 30 minutes");
        }
    },
    BIKE {
        @Override
        public void calculateRoute() {
            System.out.println("Time to destination by bike: 45 minutes");
        }
    },
    WALK {
        @Override
        public void calculateRoute() {
            System.out.println("Time to destination by walk: 2 hours");
        }
    },
    BUS {
        @Override
        public void calculateRoute() {
            System.out.println("Time to destination by bus: 1 hour");
        }
    };

    public abstract void calculateRoute();
}

class UserRoute implements RouteBad {
    private RouteType routeType;

    @Override
    public void calculateTimeToDestination() {
        routeType.calculateRoute();
    }

    @Override
    public void setRouteType(RouteType routeType) {
        this.routeType = routeType;
    }
}

public class SWSBE2 {
    public static void main(String[] args) {
        RouteBad userRoute = new UserRoute();
        userRoute.setRouteType(RouteType.CAR);
        userRoute.calculateTimeToDestination();
        userRoute.setRouteType(RouteType.BIKE);
        userRoute.calculateTimeToDestination();
        userRoute.setRouteType(RouteType.WALK);
        userRoute.calculateTimeToDestination();
        userRoute.setRouteType(RouteType.BUS);
        userRoute.calculateTimeToDestination();
    }
}
```
```