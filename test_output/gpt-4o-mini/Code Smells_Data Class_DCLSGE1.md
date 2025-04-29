```markdown
**Code Review: DCLSGE1.java**
    - Code smell no. - 1
    - Code smell name - Data Class
    - Code smell description - A Data Class is a class that has only data fields and methods to access that data without any real business logic. In this case, the RectangleGood class holds the dimensions of a rectangle and provides only basic calculations, suggesting a lack of behavior and business logic.
    - Found in line no. - 1, 2, 3, 4, 5, 6, 8, 11, 14
    - Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
    - Possible solution - 
```java
class Rectangle {
    private final double height;
    private final double width;

    public Rectangle(double height, double width) {
        this.height = height;
        this.width = width;
    }

    public double getPerimeter() {
        return calculatePerimeter();
    }

    public double getArea() {
        return calculateArea();
    }

    private double calculatePerimeter() {
        return 2 * (height + width);
    }

    private double calculateArea() {
        return height * width;
    }
}

public class DCLSGE1 {
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle(5, 10);
        double perimeter = rectangle.getPerimeter();
        System.out.println("Perimeter of rectangle: " + perimeter);
        double area = rectangle.getArea();
        System.out.println("Area of rectangle: " + area);
    }
}
``` 
```