**Code Review: DCLSBE1.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A data class is a class that contains only fields and crude methods to access them (getters and setters). It does not contain any functionality, often leading to poor encapsulation and violation of object-oriented principles.
- Found in line no. - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]
- Possible treatments - ['Encapsulate Field', 'Encapsulate Collection ', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
- Possible solution:
  ```java
  class Rectangle {
      private double height;
      private double width;
    
      public Rectangle(double height, double width) {
          this.height = height;
          this.width = width;
      }
    
      public double getHeight() {
          return height;
      }
    
      public double getWidth() {
          return width;
      }
    
      public double calculatePerimeter() {
          return 2 * (height + width);
      }
    
      public double calculateArea() {
          return height * width;
      }
  }
  
  public class DCLSBE1 {
      public static void main(String[] args) {
          Rectangle rectangle = new Rectangle(5, 10);
          double perimeter = rectangle.calculatePerimeter();
          System.out.println("Perimeter of rectangle: " + perimeter);
          double area = rectangle.calculateArea();
          System.out.println("Area of rectangle: " + area);
      }
  }
  ```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data types instead of small classes for simple tasks such as currency, ranges, or special strings. This often leads to duplication of code and loss of domain specificity.
- Found in line no. - [2, 3]
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution:
  In this specific case, the primitive obsession is addressed by encapsulating the logic of perimeter and area calculations within the Rectangle class, which reduces the need for direct manipulation of primitives. See previous solution for the changes incorporated.