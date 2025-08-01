class Shape {
  private String shape;
  public Shape(String shape) {
    this.shape = shape;
  }

  public double calculateArea(int ... dimensions) {
    switch(shape) {
      case "circle":
        return Math.PI * dimensions[0] * dimensions[0];
      case "rectangle":
        return dimensions[0] * dimensions[1];
      case "triangle":
        return 0.5 * dimensions[0] * dimensions[1];
      case "square":
        return dimensions[0] * dimensions[0];
      default:
        return 0;
    }
  }
}

public class source64 {
    public static void main(String[] args) {
        Shape circle = new Shape("circle");
        System.out.println("Area of circle: " + circle.calculateArea(5));
        Shape rectangle = new Shape("rectangle");
        System.out.println("Area of rectangle: " + rectangle.calculateArea(5, 10));
        Shape triangle = new Shape("triangle");
        System.out.println("Area of triangle: " + triangle.calculateArea(5, 10));
        Shape square = new Shape("square");
        System.out.println("Area of square: " + square.calculateArea(5));
    }
}
