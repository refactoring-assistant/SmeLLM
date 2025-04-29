```markdown
**Code Review: LZCBE3.java**
    - Code smell no. - 1
    - Code smell name - Data Class
    - Code smell description - A Data Class is a class that primarily holds data without offering significant behavior or functionality. It typically contains fields and accessor methods but lacks meaningful methods that utilize those fields.
    - Found in line no. - 4, 5, 6, 7, 9, 13, 15, 16
    - Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
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

        @Override
        public String toString() {
            return String.format("RGB(%d, %d, %d)", red, green, blue);
        }
    }

    public class LZCBE3 {
        public static void main(String[] args) {
            RGB color = new RGB(255, 0, 0); // Example instantiation
            System.out.println(color);
            System.out.print("Average scale: " + color.averageScale());
        }
    }
    ```
```