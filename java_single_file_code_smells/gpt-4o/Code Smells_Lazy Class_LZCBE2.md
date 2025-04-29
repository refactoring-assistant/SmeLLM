**Code Review: LZCBE2.java**
- Code smell no. - 1
- Code smell name - Refused Bequest
- Code smell description - PrintHelloUserBad inherits from PrintGreetingsBad, but it doesn't override or extend the functionality significantly, merely using the methods from the superclass. This is typically considered a Refused Bequest because the subclass does not utilize the inherited methods to their full potential or explicitly differ in behavior.
- Found in line no. - 11
- Possible treatments - Replace Inheritance with Delegation, Extract Superclass
- Possible solution - Use delegation to have PrintHelloUser utilize PrintGreetings rather than extend it.

```java
class PrintGreetings {
    private String userName;
    
    public PrintGreetings(String userName) {
        this.userName = userName;
    }
    
    public void printGreetings() {
        System.out.println("Hello, " + userName + "!");
    }
}

class PrintHelloUser {
    private PrintGreetings printGreetings;
    
    public PrintHelloUser(String userName) {
        this.printGreetings = new PrintGreetings(userName);
    }
    
    public void printHelloUser() {
        printGreetings.printGreetings();
    }
}

public class LZCBE2 {
    public static void main(String[] args) {
        PrintHelloUser helloUser = new PrintHelloUser("Alice");
        helloUser.printHelloUser();
    }
}
```