class Coordinates2D {
  private double x;
  private double y;
  Coordinates2D(double x, double y) {
    this.x = x;
    this.y = y;
  }

  public double getDistance(Coordinates2D other) {
    return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
  }
}
class Triangle {
  private Coordinates2D point1;
  private Coordinates2D point2;
  private Coordinates2D point3;

  Triangle(double x1, double y1, double x2, double y2, double x3, double y3) {
    this.point1 = new Coordinates2D(x1, y1);
    this.point2 = new Coordinates2D(x2, y2);
    this.point3 = new Coordinates2D(x3, y3);
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

public class source42 {
  public static void main(String[] args) {
    Triangle triangle = new Triangle(0, 0, 0, 1, 1, 0);
    System.out.println("Perimeter: " + triangle.getPerimeter());
    System.out.println("Area: " + triangle.getArea());
  }
}
