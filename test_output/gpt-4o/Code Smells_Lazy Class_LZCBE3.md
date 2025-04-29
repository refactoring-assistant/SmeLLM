**Code Review: LZCBE3.java**
   - Code smell no. - 1
   - Code smell name - Data Class
   - Code smell description - A Data Class is a class that only has fields and provides accessors and possibly mutators, but no additional behavior.
   - Found in line no. - 4-18
   - Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
   - Possible solution - Encapsulate the fields and potentially add methods that manipulate the data of this class.

   ```java
   class RGBGood {
       private final int red;
       private final int green;
       private final int blue;

       public RGBGood(int red, int green, int blue) {
           this.red = red;
           this.green = green;
           this.blue = blue;
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

       public double averageScale() {
           return (red + green + blue) / 3.0;
       }
   }
   
   public class LZCBE3 {
       public static void main(String[] args) {
           System.out.print("Hello world");
       }
   }
   ```