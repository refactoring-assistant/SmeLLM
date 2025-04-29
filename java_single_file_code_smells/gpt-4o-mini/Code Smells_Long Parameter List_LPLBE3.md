**Code Review: LPLBE3.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - Using primitive data types (double) to represent concepts that could be encapsulated in a type (like a 2D point).
- Found in line no. - 4, 18
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object']
- Possible solution - 
```java
class Point {
    private double x;
    private double y;

    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getDistance(Point other) {
        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
    }
}

class Triangle {
    private Point point1;
    private Point point2;
    private Point point3;

    Triangle(Point point1, Point point2, Point point3) {
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
        Point p1 = new Point(0, 0);
        Point p2 = new Point(0, 1);
        Point p3 = new Point(1, 0);
        Triangle triangle = new Triangle(p1, p2, p3);
        System.out.println("Perimeter: " + triangle.getPerimeter());
        System.out.println("Area: " + triangle.getArea());
    }
}
```