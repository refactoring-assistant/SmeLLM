```markdown
**Code Review: DCLSBE1.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A data class is an object that is primarily used to hold data with little or no behavior. It typically contains many fields and is often just a container for data.
- Found in line no. - 1, 2, 3
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
        System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
    }
}
```
```