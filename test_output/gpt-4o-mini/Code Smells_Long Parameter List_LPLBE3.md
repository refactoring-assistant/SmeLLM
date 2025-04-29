**Code Review: LPLBE3.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data types (double) to represent coordinates (x, y) is an example of primitive obsession, where the code relies heavily on primitive values instead of encapsulating them in a meaningful object.
- Found in line no. - 4, 18
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - 
```java
class Coordinates2D {
    private double x;
    private double y;

    Coordinates2D(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getDistance(Coordinates2D other) {
        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
    }
}

class Triangle {
    private Coordinates2D point1;
    private Coordinates2D point2;
    private Coordinates2D point3;

    Triangle(Coordinates2D point1, Coordinates2D point2, Coordinates2D point3) {
        this.point1 = point1;
        this.point2 = point2;
        this.point3 = point3;
    }

    public double getPerimeter() {
        return point1.getDistance(point2) + point2.getDistance(point3) + point3.getDistance(point1);
    }

    public double getArea() {
        double a = point1.getDistance(point2);
        double b = point2.getDistance(point3);
        double c = point3.getDistance(point1);
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}

public class LPLBE3 {
    public static void main(String[] args) {
        Triangle triangle = new Triangle(new Coordinates2D(0, 0), new Coordinates2D(0, 1), new Coordinates2D(1, 0));
        System.out.println("Perimeter: " + triangle.getPerimeter());
        System.out.println("Area: " + triangle.getArea());
    }
}
```