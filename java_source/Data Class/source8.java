class Rectangle {
  private double height;
  private double width;
  public void setHeight(double height) {
    this.height = height;
  }
  public void setWidth(double width) {
    this.width = width;
  }
  public double getHeight() {
    return height;
  }

  public double getWidth() {
    return width;
  }
}

public class source8 {
  private static double calculateRectanglePerimeter(Rectangle rectangle) {
    return 2*(rectangle.getHeight() + rectangle.getWidth());
  }

  private static double calculateRectangleArea(Rectangle rectangle) {
    return rectangle.getHeight() * rectangle.getWidth();
  }
  public static void main(String[] args) {
    Rectangle rectangle = new Rectangle();
    rectangle.setHeight(5);
    rectangle.setWidth(10);
    double perimeter = calculateRectanglePerimeter(rectangle);
    System.out.println("Perimeter of rectangle: " + perimeter);
    double area = calculateRectangleArea(rectangle);
    System.out.println("Area of rectangle: " + area);
  }
}
