**Code Review: FEBE1.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A class that only contains data and lacks behavior, failing to encapsulate its fields properly.
- Found in line no. - 1, 14
- Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
- Possible solution - 
```java
class Coordinates2D {
    private final int x;
    private final int y;

    public Coordinates2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}

class Rectangle2D {
    private final Coordinates2D[] points;

    public Rectangle2D(Coordinates2D[] points) throws IllegalArgumentException {
        checkPointsArraySize(points);
        this.points = points; // encapsulating and allowing further processing within the class
    }

    public int calculateArea() {
        return calculateDistance(points[0], points[1]) * calculateDistance(points[0], points[3]);
    }

    public int calculatePerimeter() {
        return 2 * (calculateDistance(points[0], points[1]) + calculateDistance(points[0], points[3]));
    }

    private void checkPointsArraySize(Coordinates2D[] points) throws IllegalArgumentException {
        if(points.length != 4) {
            throw new IllegalArgumentException("Rectangle should have 4 points");
        }
    }

    private int calculateDistance(Coordinates2D point1, Coordinates2D point2) {
        return (int) Math.sqrt(Math.pow(point1.getX() - point2.getX(), 2) + Math.pow(point1.getY() - point2.getY(), 2));
    }
}
```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive types to represent domain concepts instead of using small classes, which can help in encapsulating related behavior and data.
- Found in line no. - 1, 14
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - 
```java
class Coordinates2D {
    private final int x;
    private final int y;

    public Coordinates2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}

class Rectangle2D {
    private Coordinates2D[] points;

    public Rectangle2D(Coordinates2D[] points) throws IllegalArgumentException {
        checkPointsArraySize(points);
        this.points = points;
    }

    public int calculateArea() {
        return calculateDistance(points[0], points[1]) * calculateDistance(points[0], points[3]);
    }

    public int calculatePerimeter() {
        return 2 * (calculateDistance(points[0], points[1]) + calculateDistance(points[0], points[3]));
    }

    private void checkPointsArraySize(Coordinates2D[] points) throws IllegalArgumentException {
        if(points.length != 4) {
            throw new IllegalArgumentException("Rectangle should have 4 points");
        }
    }

    private int calculateDistance(Coordinates2D point1, Coordinates2D point2) {
        return (int) Math.sqrt(Math.pow(point1.getX() - point2.getX(), 2) + Math.pow(point1.getY() - point2.getY(), 2));
    }
}
```