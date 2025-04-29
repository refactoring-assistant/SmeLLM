**Code Review: LZCBE2.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - Using a primitive type (String in this case) instead of an object to represent a concept (user name).
- Found in line no. - 2, 3
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - 

```java
class UserName {
    private String name;

    public UserName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

class PrintGreetingsBad {
    private UserName userName;

    public PrintGreetingsBad(UserName userName) {
        this.userName = userName;
    }

    public void printGreetings() {
        System.out.println("Hello, " + userName.getName() + "!");
    }
}

class PrintHelloUserBad extends PrintGreetingsBad {
    public PrintHelloUserBad(UserName userName) {
        super(userName);
    }

    public void printHelloUser() {
        printGreetings();
    }
}

public class LZCBE2 {
    public static void main(String[] args) {
        UserName userName = new UserName("Alice");
        PrintHelloUserBad helloUser = new PrintHelloUserBad(userName);
        helloUser.printHelloUser();
    }
}
```