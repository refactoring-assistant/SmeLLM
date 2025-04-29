**Code Review: FEBE1.java**
   - Code smell no. - 1
   - Code smell name - Data Clumps
   - Code smell description - The same group of data, specifically the `Coordinates2DBad` array of points, is being passed around through multiple methods, indicating a relationship that might better be represented as a class.
   - Found in line no. - [18, 19, 20, 33, 39]
   - Possible treatments - ['Extract Class', 'Introduce Parameter Object', 'Preserve Whole Object']
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

class Rectangle {
    private final Coordinates2D topLeft;
    private final Coordinates2D topRight;
    private final Coordinates2D bottomLeft;
    private final Coordinates2D bottomRight;
    private final int length;
    private final int breadth;

    public Rectangle(Coordinates2D topLeft, Coordinates2D topRight, Coordinates2D bottomLeft, Coordinates2D bottomRight) {
        checkRectangle(topLeft, topRight, bottomLeft, bottomRight);
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
        this.length = calculateDistance(topLeft, topRight);
        this.breadth = calculateDistance(topLeft, bottomLeft);
    }

    public int calculateArea() {
        return length * breadth;
    }

    public int calculatePerimeter() {
        return 2 * (length + breadth);
    }

    private void checkRectangle(Coordinates2D topLeft, Coordinates2D topRight, Coordinates2D bottomLeft, Coordinates2D bottomRight) {
        if (topLeft.getX() != bottomLeft.getX() || topLeft.getY() != topRight.getY() ||
            topRight.getY() != bottomRight.getY() || bottomRight.getX() != bottomLeft.getX()) {
            throw new IllegalArgumentException("Points do not form a rectangle");
        }
    }

    private int calculateDistance(Coordinates2D point1, Coordinates2D point2) {
        return (int) Math.sqrt(Math.pow(point1.getX() - point2.getX(), 2) + Math.pow(point1.getY() - point2.getY(), 2));
    }
}

public class FEBE1 {
    public static void main(String[] args) {
        Coordinates2D topLeft = new Coordinates2D(1, 3);
        Coordinates2D topRight = new Coordinates2D(3, 3);
        Coordinates2D bottomLeft = new Coordinates2D(1, 1);
        Coordinates2D bottomRight = new Coordinates2D(3, 1);
        
        Rectangle rectangle = new Rectangle(topLeft, topRight, bottomLeft, bottomRight);
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
    }
}
```

   - Code smell no. - 2
   - Code smell name - Primitive Obsession
   - Code smell description - The use of primitive data types `int x` and `int y` for coordinates rather than encapsulating them within a more expressive object like a coordinate class.
   - Found in line no. - [2, 3, 5, 6, 7]
   - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class', 'Replace Type Code with Subclasses', 'Replace Type Code with State/Strategy', 'Replace Array with Object']
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

class Rectangle {
    private final Coordinates2D topLeft;
    private final Coordinates2D topRight;
    private final Coordinates2D bottomLeft;
    private final Coordinates2D bottomRight;
    private final int length;
    private final int breadth;

    public Rectangle(Coordinates2D topLeft, Coordinates2D topRight, Coordinates2D bottomLeft, Coordinates2D bottomRight) {
        checkRectangle(topLeft, topRight, bottomLeft, bottomRight);
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
        this.length = calculateDistance(topLeft, topRight);
        this.breadth = calculateDistance(topLeft, bottomLeft);
    }

    public int calculateArea() {
        return length * breadth;
    }

    public int calculatePerimeter() {
        return 2 * (length + breadth);
    }

    private void checkRectangle(Coordinates2D topLeft, Coordinates2D topRight, Coordinates2D bottomLeft, Coordinates2D bottomRight) {
        if (topLeft.getX() != bottomLeft.getX() || topLeft.getY() != topRight.getY() ||
            topRight.getY() != bottomRight.getY() || bottomRight.getX() != bottomLeft.getX()) {
            throw new IllegalArgumentException("Points do not form a rectangle");
        }
    }

    private int calculateDistance(Coordinates2D point1, Coordinates2D point2) {
        return (int) Math.sqrt(Math.pow(point1.getX() - point2.getX(), 2) + Math.pow(point1.getY() - point2.getY(), 2));
    }
}

public class FEBE1 {
    public static void main(String[] args) {
        Coordinates2D topLeft = new Coordinates2D(1, 3);
        Coordinates2D topRight = new Coordinates2D(3, 3);
        Coordinates2D bottomLeft = new Coordinates2D(1, 1);
        Coordinates2D bottomRight = new Coordinates2D(3, 1);
        
        Rectangle rectangle = new Rectangle(topLeft, topRight, bottomLeft, bottomRight);
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
    }
}
```
