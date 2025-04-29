```markdown
**Code Review: SWSBE1.java**
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - The use of a switch statement to differentiate behavior based on the string value of shape makes the code harder to maintain and extend, as adding new shapes requires modifying the existing code.
- Found in line no. - [8]
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism']
- Possible solution - 
```java
abstract class Shape {
    abstract double calculateArea(int... dimensions);
}

class Circle extends Shape {
    double calculateArea(int... dimensions) {
        return Math.PI * dimensions[0] * dimensions[0];
    }
}

class Rectangle extends Shape {
    double calculateArea(int... dimensions) {
        return dimensions[0] * dimensions[1];
    }
}

class Triangle extends Shape {
    double calculateArea(int... dimensions) {
        return 0.5 * dimensions[0] * dimensions[1];
    }
}

class Square extends Shape {
    double calculateArea(int... dimensions) {
        return dimensions[0] * dimensions[0];
    }
}

public class SWSBE1 {
    public static void main(String[] args) {
        Shape circle = new Circle();
        System.out.println("Area of circle: " + circle.calculateArea(5));
        Shape rectangle = new Rectangle();
        System.out.println("Area of rectangle: " + rectangle.calculateArea(5, 10));
        Shape triangle = new Triangle();
        System.out.println("Area of triangle: " + triangle.calculateArea(5, 10));
        Shape square = new Square();
        System.out.println("Area of square: " + square.calculateArea(5));
    }
}
```
```