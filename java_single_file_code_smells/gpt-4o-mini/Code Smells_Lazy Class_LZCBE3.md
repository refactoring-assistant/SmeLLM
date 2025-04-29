```markdown
**Code Review: LZCBE3.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A class that is primarily a container for data without significant functionality, often leads to poor encapsulation and excessive exposure of its data.
- Found in line no. - 5, 6, 7, 15, 16
- Possible treatments - ['Encapsulate Field', 'Encapsulate Collection ', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
- Possible solution - 

```java
class RGB {
    private final int red;
    private final int green;
    private final int blue;

    public RGB(int red, int green, int blue) {
        this.red = red;
        this.green = green;
        this.blue = blue;
    }

    public double averageScale() {
        return (red + green + blue) / 3.0;
    }
    
    public int getRed() {
        return red;
    }

    public int getGreen() {
        return green;
    }

    public int getBlue() {
        return blue;
    }
}

public class LZCBE3 {
    public static void main(String[] args) {
        System.out.print("Hello world");
    }
}
```
```