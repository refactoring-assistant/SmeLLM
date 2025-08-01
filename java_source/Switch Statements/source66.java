abstract class Shape {
    abstract double calculateArea();
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double calculateArea() {
        return Math.PI * radius * radius;
    }
}

class Rectangle extends Shape {
    private double length;
    private double breadth;

    public Rectangle(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    @Override
    double calculateArea() {
        return length * breadth;
    }
}

class Triangle extends Shape {
    private double base;
    private double height;

    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    @Override
    double calculateArea() {
        return 0.5 * base * height;
    }
}

class Square extends Shape {
    private double side;

    public Square(double side) {
        this.side = side;
    }

    @Override
    double calculateArea() {
        return side * side;
    }
}
public class source66 {
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
