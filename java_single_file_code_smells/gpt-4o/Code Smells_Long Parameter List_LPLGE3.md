```markdown
**Code Review: LPLGE3.java**
   - Code smell no. - 1
   - Code smell name - Temporary Field
   - Code smell description - Temporary fields are instance variables that are only sometimes needed for objects. They may clutter the interface of a class.
   - Found in line no. - [29, 30, 31, 32]
   - Possible treatments - ['Extract Class or Replace Method with Method Object.', 'Introduce Null Object']
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

     class TriangleGood {
       private Coordinates2DGood point1;
       private Coordinates2DGood point2;
       private Coordinates2DGood point3;

       TriangleGood(Coordinates2DGood point1, Coordinates2DGood point2, Coordinates2DGood point3) {
         this.point1 = point1;
         this.point2 = point2;
         this.point3 = point3;
       }

       public double getPerimeter() {
         return point1.getDistance(point2) + point2.getDistance(point3) + point3.getDistance(point1);
       }

       public double getArea() {
         return calculateArea(point1.getDistance(point2), point2.getDistance(point3), point3.getDistance(point1));
       }

       private double calculateArea(double a, double b, double c) {
         double s = (a + b + c) / 2;
         return Math.sqrt(s * (s - a) * (s - b) * (s - c));
       }
     }

     public class LPLGE3 {
       public static void main(String[] args) {
         Coordinates2DGood point1 = new Coordinates2DGood(0, 0);
         Coordinates2DGood point2 = new Coordinates2DGood(0, 1);
         Coordinates2DGood point3 = new Coordinates2DGood(1, 0);
         TriangleGood triangle = new TriangleGood(point1, point2, point3);
         System.out.println("Perimeter: " + triangle.getPerimeter());
         System.out.println("Area: " + triangle.getArea());
       }
     }
     ```

   - Code smell no. - 2
   - Code smell name - Long Method
   - Code smell description - A method that has grown too large and takes on too many responsibilities may become hard to understand, test, and maintain.
   - Found in line no. - [28-34]
   - Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
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

     class TriangleGood {
       private Coordinates2DGood point1;
       private Coordinates2DGood point2;
       private Coordinates2DGood point3;

       TriangleGood(Coordinates2DGood point1, Coordinates2DGood point2, Coordinates2DGood point3) {
         this.point1 = point1;
         this.point2 = point2;
         this.point3 = point3;
       }

       public double getPerimeter() {
         return point1.getDistance(point2) + point2.getDistance(point3) + point3.getDistance(point1);
       }

       public double getArea() {
         return calculateArea(point1.getDistance(point2), point2.getDistance(point3), point3.getDistance(point1));
       }

       private double calculateArea(double a, double b, double c) {
         double s = calculateSemiPerimeter(a, b, c);
         return Math.sqrt(s * (s - a) * (s - b) * (s - c));
       }

       private double calculateSemiPerimeter(double a, double b, double c) {
         return (a + b + c) / 2;
       }
     }

     public class LPLGE3 {
       public static void main(String[] args) {
         Coordinates2DGood point1 = new Coordinates2DGood(0, 0);
         Coordinates2DGood point2 = new Coordinates2DGood(0, 1);
         Coordinates2DGood point3 = new Coordinates2DGood(1, 0);
         TriangleGood triangle = new TriangleGood(point1, point2, point3);
         System.out.println("Perimeter: " + triangle.getPerimeter());
         System.out.println("Area: " + triangle.getArea());
       }
     }
     ```
```