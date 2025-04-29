**Code Review: SWSGE1.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive types (double) for representing shapes' dimensions and area calculations instead of using more expressive domain-specific classes.
- Found in line no. - 6, 19, 20, 34, 35, 49
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy.
- Possible solution - Redefine the code to use specific classes for dimensions and areas. For example, create a `Radius`, `LengthWidth` and `BaseHeight` classes to encapsulate these properties.

```java
abstract class ShapeGood {
    abstract double calculateArea();
}

class CircleGood extends ShapeGood {
    private Radius radius;

    public CircleGood(Radius radius) {
        this.radius = radius;
    }

    @Override
    double calculateArea() {
        return Math.PI * radius.getValue() * radius.getValue();
    }
}

class RectangleGood extends ShapeGood {
    private LengthWidth dimensions;

    public RectangleGood(LengthWidth dimensions) {
        this.dimensions = dimensions;
    }

    @Override
    double calculateArea() {
        return dimensions.getLength() * dimensions.getWidth();
    }
}

class TriangleGood extends ShapeGood {
    private BaseHeight dimensions;

    public TriangleGood(BaseHeight dimensions) {
        this.dimensions = dimensions;
    }

    @Override
    double calculateArea() {
        return 0.5 * dimensions.getBase() * dimensions.getHeight();
    }
}

class SquareGood extends ShapeGood {
    private Side side;

    public SquareGood(Side side) {
        this.side = side;
    }

    @Override
    double calculateArea() {
        return side.getValue() * side.getValue();
    }
}

// Additional classes to encapsulate dimensions
class Radius {
    private double value;
    
    public Radius(double value) {
        this.value = value;
    }
    
    public double getValue() {
        return value;
    }
}

class LengthWidth {
    private double length;
    private double width;

    public LengthWidth(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }
}

class BaseHeight {
    private double base;
    private double height;

    public BaseHeight(double base, double height) {
        this.base = base;
        this.height = height;
    }

    public double getBase() {
        return base;
    }

    public double getHeight() {
        return height;
    }
}

class Side {
    private double value;

    public Side(double value) {
        this.value = value;
    }

    public double getValue() {
        return value;
    }
}

public class SWSGE1 {
    public static void main(String[] args) {
        ShapeGood circle = new CircleGood(new Radius(5));
        System.out.println("Area of circle: " + circle.calculateArea());
        ShapeGood rectangle = new RectangleGood(new LengthWidth(5, 10));
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        ShapeGood triangle = new TriangleGood(new BaseHeight(5, 10));
        System.out.println("Area of triangle: " + triangle.calculateArea());
        ShapeGood square = new SquareGood(new Side(5));
        System.out.println("Area of square: " + square.calculateArea());
    }
}
```