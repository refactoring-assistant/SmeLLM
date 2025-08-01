interface RouteStrategy {
  void calculateTimeToDestination();
}

class CarRouteStrategy implements RouteStrategy {
  @Override
  public void calculateTimeToDestination() {
    System.out.println("Time to destination by car: 30 minutes");
  }
}

class BikeRouteStrategy implements RouteStrategy {
  @Override
  public void calculateTimeToDestination() {
    System.out.println("Time to destination by bike: 45 minutes");
  }
}

class WalkRouteStrategy implements RouteStrategy {
  @Override
  public void calculateTimeToDestination() {
    System.out.println("Time to destination by walk: 2 hours");
  }
}

class BusRouteStrategy implements RouteStrategy {
  @Override
  public void calculateTimeToDestination() {
    System.out.println("Time to destination by bus: 1 hour");
  }
}

interface Route {
  void calculateTimeToDestination();
  void setRouteType(RouteStrategy routeStrategy);
}

class UserRoute implements Route {
  private RouteStrategy routeStrategy;

  @Override
  public void calculateTimeToDestination() {
    routeStrategy.calculateTimeToDestination();
  }

  @Override
  public void setRouteType(RouteStrategy routeStrategy) {
    this.routeStrategy = routeStrategy;
  }

}

public class source67 {
  public static void main(String[] args) {
    Route userRoute = new UserRoute();
    userRoute.setRouteType(new CarRouteStrategy());
    userRoute.calculateTimeToDestination();
    userRoute.setRouteType(new BikeRouteStrategy());
    userRoute.calculateTimeToDestination();
    userRoute.setRouteType(new WalkRouteStrategy());
    userRoute.calculateTimeToDestination();
    userRoute.setRouteType(new BusRouteStrategy());
    userRoute.calculateTimeToDestination();
  }
}
