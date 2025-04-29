**Code Review: DCLSBE1.java**
   - Code smell no. - 1
   - Code smell name - Data Class
   - Code smell description - A class that is used to store data fields but lacks complex functionality, with data fields accessed directly by external classes, often lacks encapsulation.
   - Found in line no. - 1-17
   - Possible treatments - ['Encapsulate Field', 'Encapsulate Collection ', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
   - Possible solution - 
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
   - Code smell description - The urge to use primitive data types to represent more complex entities, resulting in unclear code.
   - Found in line no. - 2-3, 28-30
   - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
   - Possible solution - (The suggested solution for the Data Class code smell already addresses this by using encapsulation and adding methods to the `Rectangle` class.)