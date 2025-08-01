enum RouteType {
    CAR, BIKE, WALK, BUS
}
interface Route {
    void calculateTimeToDestination();
    void setRouteType(RouteType routeType);
}

class UserRoute implements Route {
    private RouteType routeType;
    @Override
    public void calculateTimeToDestination() {
        switch (routeType) {
            case CAR:
                calculateCarRoute();
                break;
            case BIKE:
                calculateBikeRoute();
                break;
            case WALK:
                calculateWalkRoute();
                break;
            case BUS:
                calculateBusRoute();
                break;
        }
    }

    @Override
    public void setRouteType(RouteType routeType) {
        this.routeType = routeType;
    }

    private void calculateCarRoute() {
        System.out.println("Time to destination by car: 30 minutes");
    }

    private void calculateBikeRoute() {
        System.out.println("Time to destination by bike: 45 minutes");
    }

    private void calculateWalkRoute() {
        System.out.println("Time to destination by walk: 2 hours");
    }

    private void calculateBusRoute() {
        System.out.println("Time to destination by bus: 1 hour");
    }
}

public class source65 {
    public static void main(String[] args) {
        Route userRoute = new UserRoute();
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
