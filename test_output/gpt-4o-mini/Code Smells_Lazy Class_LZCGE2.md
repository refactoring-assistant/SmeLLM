```markdown
**Code Review: LZCGE2.java**
   - Code smell no. - 1
   - Code smell name - Data Class
   - Code smell description - A data class is a class that contains only fields and gets/sets methods with little behavior. This code snippet shows a class that primarily stores data, lacking significant behavior or operations on that data.
   - Found in line no. - 1, 2, 3, 4, 6, 7, 8
   - Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
   - Possible solution - 
```java
class Greeting {
    private String userName;

    public Greeting(String userName) {
        this.userName = userName;
    }

    public void printGreeting() {
        generateMessage();
    }

    private String generateMessage() {
        return "Hello, " + userName + "!";
    }
}

public class LZCGE2 {
    public static void main(String[] args) {
        Greeting helloUser = new Greeting("Alice");
        System.out.println(helloUser.printGreeting());
    }
}
```
```