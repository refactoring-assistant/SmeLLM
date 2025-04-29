```markdown
**Code Review: FEGE1.java**
    
    - Code smell no. - 1
    - Code smell name - Large Class
    - Code smell description - A class that has too many responsibilities, making it hard to understand, maintain, or change.
    - Found in line no. - [1, 25]
    - Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
    - Possible solution - 
    ```java
    class Coordinates2D {
        private int x;
        private int y;

        public Coordinates2D(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() { return x; }
        public int getY() { return y; }
        
        public int calculateDistance(Coordinates2D point) {
            return (int) Math.sqrt(Math.pow(x - point.getX(), 2) + Math.pow(y - point.getY(), 2));
        }

        public boolean sameX(Coordinates2D point) {
            return x == point.getX();
        }

        public boolean sameY(Coordinates2D point) {
            return y == point.getY();
        }
    }

    class Rectangle {
        private final int length;
        private final int breadth;

        public Rectangle(Coordinates2D [] points) throws IllegalArgumentException {
            checkPointsArraySize(points);
            checkRectangle(points);
            this.length = points[0].calculateDistance(points[1]);
            this.breadth = points[0].calculateDistance(points[3]);
        }

        public int calculateArea() {
            return length * breadth;
        }

        public int calculatePerimeter() {
            return 2 * (length + breadth);
        }

        private void checkPointsArraySize(Coordinates2D [] points) throws IllegalArgumentException {
            if (points.length != 4) {
                throw new IllegalArgumentException("Rectangle should have 4 points");
            }
        }

        private void checkRectangle(Coordinates2D [] points) throws IllegalArgumentException {
            if (!points[0].sameX(points[1]) || !points[0].sameY(points[3]) ||
                !points[1].sameY(points[2]) || !points[2].sameX(points[3])) {
                throw new IllegalArgumentException("Points do not form a rectangle");
            }
        }
    }

    public class FEGE1 {
        public static void main(String[] args) {
            Coordinates2D[] points = {new Coordinates2D(1, 1), new Coordinates2D(1, 3), 
                                       new Coordinates2D(3, 3), new Coordinates2D(3, 1)};
            Rectangle rectangle = new Rectangle(points);
            System.out.println("Area of rectangle: " + rectangle.calculateArea());
            System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
        }
    }
    ```

    - Code smell no. - 2
    - Code smell name - Primitive Obsession
    - Code smell description - The use of primitive data types to represent domain ideas, which can be better represented as objects.
    - Found in line no. - [26]
    - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
    - Possible solution - 
    ```java
    class Dimensions {
        private int length;
        private int breadth;

        public Dimensions(int length, int breadth) {
            this.length = length;
            this.breadth = breadth;
        }

        public int getLength() { return length; }
        public int getBreadth() { return breadth; }
    }

    // Update Rectangle class to use Dimensions
    class Rectangle {
        private final Dimensions dimensions;

        public Rectangle(Coordinates2D[] points) throws IllegalArgumentException {
            checkPointsArraySize(points);
            checkRectangle(points);
            this.dimensions = new Dimensions(
                points[0].calculateDistance(points[1]),
                points[0].calculateDistance(points[3])
            );
        }
        
        public int calculateArea() {
            return dimensions.getLength() * dimensions.getBreadth();
        }

        public int calculatePerimeter() {
            return 2 * (dimensions.getLength() + dimensions.getBreadth());
        }
    }
    ```

```