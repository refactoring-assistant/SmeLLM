**Code Review: FEBE1.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A class whose only purpose is to hold data and has little or no behavior.
- Found in line no. - 1
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
    
    public double distanceTo(Coordinates2D other) {
        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
    }
}

class Rectangle {
    private final int length;
    private final int breadth;

    public Rectangle(Coordinates2D[] points) throws IllegalArgumentException {
        checkPointsArraySize(points);
        checkRectangle(points);
        this.length = (int) points[0].distanceTo(points[1]);
        this.breadth = (int) points[0].distanceTo(points[3]);
    }

    public int calculateArea() {
        return length * breadth;
    }

    public int calculatePerimeter() {
        return 2 * (length + breadth);
    }

    private void checkPointsArraySize(Coordinates2D[] points) throws IllegalArgumentException {
        if(points.length != 4) {
            throw new IllegalArgumentException("Rectangle should have 4 points");
        }
    }

    private void checkRectangle(Coordinates2D[] points) throws IllegalArgumentException {
        if(points[0].getX() != points[1].getX() || points[0].getY() != points[3].getY() ||
           points[1].getY() != points[2].getY() || points[2].getX() != points[3].getX()) {
            throw new IllegalArgumentException("Points do not form a rectangle");
        }
    }
}

public class FEBE1 {
    public static void main(String[] args) {
        Coordinates2D[] points = {
            new Coordinates2D(1, 1), 
            new Coordinates2D(1, 3), 
            new Coordinates2D(3, 3), 
            new Coordinates2D(3, 1)
        };
        Rectangle rectangle = new Rectangle(points);
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
    }
}
```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data types to represent domain ideas instead of using small classes.
- Found in line no. - 1, 14
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - The solution above combines the Coordinates and Rectangle classes to use more meaningful object representations instead of primitive types and arrays.