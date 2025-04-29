**Code Review: FEBE1.java**
    
- Code smell no. - 1
    - Code smell name - Primitive Obsession
    - Code smell description - The code is using primitive data types for coordinates and dimensions where more complex objects could be beneficial for clarity and functionality. 
    - Found in line no. - 2, 3, 15, 16
    - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
    - Possible solution - 
```java
class Coordinate {
    private final int x;
    private final int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() { return x; }
    public int getY() { return y; }
}

class Rectangle {
    private final Coordinate topLeft;
    private final int length;
    private final int breadth;

    public Rectangle(Coordinate topLeft, int length, int breadth) {
        this.topLeft = topLeft;
        this.length = length;
        this.breadth = breadth;
    }

    public int calculateArea() {
        return length * breadth;
    }

    public int calculatePerimeter() {
        return 2 * (length + breadth);
    }
}

public class FEBE1 {
    public static void main(String[] args) {
        Coordinate topLeft = new Coordinate(1, 1);
        int length = 2;
        int breadth = 2;
        Rectangle rectangle = new Rectangle(topLeft, length, breadth);
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
    }
}
```

- Code smell no. - 2
    - Code smell name - Primitive Obsession
    - Code smell description - The array `Coordinates2DBad[]` is used to represent a set of points, which can be encapsulated into a single Rectangle or geometric shape object to better capture their relationship and enforce rectangle-specific constraints.
    - Found in line no. - 18, 33, 39
    - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', ' Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
    - Possible solution - 
```java
class Rectangle {
    private final Coordinate topLeft;
    private final int length;
    private final int breadth;

    public Rectangle(Coordinate topLeft, int length, int breadth) {
        this.topLeft = topLeft;
        this.length = length;
        this.breadth = breadth;
    }

    public int calculateArea() {
        return length * breadth;
    }

    public int calculatePerimeter() {
        return 2 * (length + breadth);
    }
}

public class FEBE1 {
    public static void main(String[] args) {
        Coordinate topLeft = new Coordinate(1, 1);
        int length = 2;
        int breadth = 2;
        Rectangle rectangle = new Rectangle(topLeft, length, breadth);
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
    }
}
```

- Code smell no. - 3
    - Code smell name - Data Clumps
    - Code smell description - Frequent patterns of data grouping that could be combined into a single object for stronger cohesion and to prevent duplication of structure and logic.
    - Found in line no. - 18, 39, 46
    - Possible treatments - ['Extract Class', 'Introduce Parameter Object', 'Preserve Whole Object']
    - Possible solution - 
```java
class Coordinate {
    private final int x;
    private final int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() { return x; }
    public int getY() { return y; }
}

class Rectangle {
    private final Coordinate topLeft;
    private final Coordinate topRight;
    private final Coordinate bottomLeft;
    private final Coordinate bottomRight;

    public Rectangle(Coordinate topLeft, Coordinate topRight, Coordinate bottomLeft, Coordinate bottomRight) {
        checkRectangle(topLeft, topRight, bottomLeft, bottomRight);
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }

    private void checkRectangle(Coordinate topLeft, Coordinate topRight, Coordinate bottomLeft, Coordinate bottomRight) throws IllegalArgumentException {
        if(topLeft.getX() != bottomLeft.getX() || topRight.getY() != bottomRight.getY() ||
           topLeft.getY() != topRight.getY() || bottomLeft.getX() != bottomRight.getX()) {
            throw new IllegalArgumentException("Points do not form a rectangle");
        }
    }

    public int calculateArea() {
        int length = Math.abs(topRight.getX() - topLeft.getX());
        int breadth = Math.abs(bottomLeft.getY() - topLeft.getY());
        return length * breadth;
    }

    public int calculatePerimeter() {
        int length = Math.abs(topRight.getX() - topLeft.getX());
        int breadth = Math.abs(bottomLeft.getY() - topLeft.getY());
        return 2 * (length + breadth);
    }
}

public class FEBE1 {
    public static void main(String[] args) {
        Coordinate topLeft = new Coordinate(1, 1);
        Coordinate topRight = new Coordinate(1, 3);
        Coordinate bottomLeft = new Coordinate(3, 1);
        Coordinate bottomRight = new Coordinate(3, 3);
        Rectangle rectangle = new Rectangle(topLeft, topRight, bottomLeft, bottomRight);
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
    }
}
```