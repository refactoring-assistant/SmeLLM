```markdown
**Code Review: SWSGE2.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - Methods that exceed a certain length, making them harder to read and maintain.
- Found in line no. - 7, 28, 21, 43
- Possible treatments - Extract Method
- Possible solution - Refactor each `calculateTimeToDestination` method to extract the logging functionality into a separate method.

```java
class CarRouteStrategy implements RouteStrategy {
    @Override
    public void calculateTimeToDestination() {
        logTime("car", 30);
    }

    private void logTime(String mode, int time) {
        System.out.println("Time to destination by " + mode + ": " + time + " minutes");
    }
}
```

- Code smell no. - 2
- Code smell name - Duplicate Code
- Code smell description - Code that is repeated in multiple locations, which can lead to inconsistency and difficulty in maintenance.
- Found in line no. - 8, 15, 22, 29
- Possible treatments - Extract Method, Extract Class
- Possible solution - Create a common `logTime` method in the interface or a utility class that each route strategy can use to avoid code duplication.

```java
private void logTime(String mode, int time) {
    System.out.println("Time to destination by " + mode + ": " + time + " minutes");
}
```
```