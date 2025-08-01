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

public class source45 {
  public static void main(String[] args) {
    Coordinates2D point1 = new Coordinates2D(0, 0);
    Coordinates2D point2 = new Coordinates2D(0, 1);
    Coordinates2D point3 = new Coordinates2D(1, 0);
    Triangle triangle = new Triangle(point1, point2, point3);
    System.out.println("Perimeter: " + triangle.getPerimeter());
    System.out.println("Area: " + triangle.getArea());
  }
}
