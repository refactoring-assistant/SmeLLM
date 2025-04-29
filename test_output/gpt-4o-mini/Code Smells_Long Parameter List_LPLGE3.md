```markdown
**Code Review: LPLGE3.java**
- Code smell no. - 1
- Code smell name - Data Clumps
- Code smell description - Data clumps occur when multiple variables are always passed together and can be grouped into a single object.
- Found in line no. - 14, 15, 16
- Possible treatments - Extract Class, Introduce Parameter Object, Preserve Whole Object
- Possible solution - 
```java
class Coordinates2DGood {
  private double x;
  private double y;

  Coordinates2DGood(double x, double y) {
    this.x = x;
    this.y = y;
  }

  public double getDistance(Coordinates2DGood other) {
    return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
  }
}

class Triangle {
  private Coordinates2DGood[] points;

  Triangle(Coordinates2DGood point1, Coordinates2DGood point2, Coordinates2DGood point3) {
    this.points = new Coordinates2DGood[]{point1, point2, point3};
  }

  public double getPerimeter() {
    return points[0].getDistance(points[1]) + points[1].getDistance(points[2]) + points[2].getDistance(points[0]);
  }

  public double getArea() {
    double a = points[0].getDistance(points[1]);
    double b = points[1].getDistance(points[2]);
    double c = points[2].getDistance(points[0]);
    double s = (a + b + c) / 2;
    return Math.sqrt(s * (s - a) * (s - b) * (s - c));
  }
}

public class LPLGE3 {
  public static void main(String[] args) {
    Coordinates2DGood point1 = new Coordinates2DGood(0, 0);
    Coordinates2DGood point2 = new Coordinates2DGood(0, 1);
    Coordinates2DGood point3 = new Coordinates2DGood(1, 0);
    Triangle triangle = new Triangle(point1, point2, point3);
    System.out.println("Perimeter: " + triangle.getPerimeter());
    System.out.println("Area: " + triangle.getArea());
  }
}
```
```