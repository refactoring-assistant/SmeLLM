```markdown
**Code Review: SWSBE1.java**

- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - The code uses a switch statement to determine behavior based on the 'shape' type. This approach can lead to inflexible and hard-to-maintain code.
- Found in line no. - 8
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', ' Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - A solution is to use polymorphism by creating separate classes for each shape, each implementing a common interface with a calculateArea method.

  ```java
  interface Shape {
      double calculateArea();
  }
  
  class Circle implements Shape {
      private double radius;
      
      public Circle(double radius) {
          this.radius = radius;
      }
      
      public double calculateArea() {
          return Math.PI * radius * radius;
      }
  }
  
  class Rectangle implements Shape {
      private double length, width;
      
      public Rectangle(double length, double width) {
          this.length = length;
          this.width = width;
      }
      
      public double calculateArea() {
          return length * width;
      }
  }

  class Triangle implements Shape {
      private double base, height;
      
      public Triangle(double base, double height) {
          this.base = base;
          this.height = height;
      }
      
      public double calculateArea() {
          return 0.5 * base * height;
      }
  }
  
  class Square implements Shape {
      private double side;
      
      public Square(double side) {
          this.side = side;
      }
      
      public double calculateArea() {
          return side * side;
      }
  }
  
  public class SWSBE1 {
      public static void main(String[] args) {
          Shape circle = new Circle(5);
          System.out.println("Area of circle: " + circle.calculateArea());
          
          Shape rectangle = new Rectangle(5, 10);
          System.out.println("Area of rectangle: " + rectangle.calculateArea());
          
          Shape triangle = new Triangle(5, 10);
          System.out.println("Area of triangle: " + triangle.calculateArea());
          
          Shape square = new Square(5);
          System.out.println("Area of square: " + square.calculateArea());
      }
  }
  ```
```
