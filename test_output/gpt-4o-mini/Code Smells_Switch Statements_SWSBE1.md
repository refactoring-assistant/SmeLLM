```markdown
**Code Review: SWSBE1.java**
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - The use of a switch statement to handle different shapes in calculating areas creates a type code situation where any additional shape will require modifying the existing code structure.
- Found in line no. - [8]
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - 
```java
abstract class Shape {
    public abstract double calculateArea(int... dimensions);
}

class Circle extends Shape {
    public double calculateArea(int... dimensions) {
        return Math.PI * dimensions[0] * dimensions[0];
    }
}

class Rectangle extends Shape {
    public double calculateArea(int... dimensions) {
        return dimensions[0] * dimensions[1];
    }
}

class Triangle extends Shape {
    public double calculateArea(int... dimensions) {
        return 0.5 * dimensions[0] * dimensions[1];
    }
}

class Square extends Shape {
    public double calculateArea(int... dimensions) {
        return dimensions[0] * dimensions[0];
    }
}

class ShapeFactory {
    public static Shape createShape(String shapeType) {
        switch (shapeType.toLowerCase()) {
            case "circle": return new Circle();
            case "rectangle": return new Rectangle();
            case "triangle": return new Triangle();
            case "square": return new Square();
            default: throw new IllegalArgumentException("Unknown shape type");
        }
    }
}

public class SWSBE1 {
    public static void main(String[] args) {
        Shape circle = ShapeFactory.createShape("circle");
        System.out.println("Area of circle: " + circle.calculateArea(5));
        
        Shape rectangle = ShapeFactory.createShape("rectangle");
        System.out.println("Area of rectangle: " + rectangle.calculateArea(5, 10));
        
        Shape triangle = ShapeFactory.createShape("triangle");
        System.out.println("Area of triangle: " + triangle.calculateArea(5, 10));
        
        Shape square = ShapeFactory.createShape("square");
        System.out.println("Area of square: " + square.calculateArea(5));
    }
}
```
```