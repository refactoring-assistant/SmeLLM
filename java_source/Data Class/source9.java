class Rectangle {
  private final double height;
  private final double width;
  public Rectangle(double height, double width) {
    this.height = height;
    this.width = width;
  }
  public double getPerimeter() {
    return 2 * (height + width);
  }
  public double getArea() {
      return height * width;
  }
}
public class source9 {
  public static void main(String[] args) {
    Rectangle rectangle = new Rectangle(5, 10);
    double perimeter = rectangle.getPerimeter();
    System.out.println("Perimeter of rectangle: " + perimeter);
    double area = rectangle.getArea();
    System.out.println("Area of rectangle: " + area);
  }
}
