**Code Review: LZCBE2.java**
- Code smell no. - 1
- Code smell name - Inappropriate Intimacy
- Code smell description - Classes are too tightly coupled and one class is too dependent on another, leading to increased maintenance difficulty. 
- Found in line no. - 11, 12, 13, 16, 17
- Possible treatments - ['Move Method & Move Field', 'Extract Class & Hide Delegate', 'Change Bidirectional Association to Unidirectional', 'Replace Delegation with Inheritance']
- Possible solution:
```java
class Printer {
    private String userName;

    public Printer(String userName) {
        this.userName = userName;
    }

    public void printGreetings() {
        System.out.println("Hello, " + userName + "!");
    }
}

public class LZCBE2 {
    public static void main(String[] args) {
        Printer printer = new Printer("Alice");
        printer.printGreetings();
    }
}
```

- Code smell no. - 2
- Code smell name - Data Class
- Code smell description - A class that only contains fields and simple getters/setters and does not have significant behavior.
- Found in line no. - 1
- Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
- Possible solution:
```java
class User {
    private String userName;

    public User(String userName) {
        this.userName = userName;
    }

    public String getUserName() {
        return userName;
    }
}

class Printer {
    private User user;

    public Printer(User user) {
        this.user = user;
    }

    public void printGreetings() {
        System.out.println("Hello, " + user.getUserName() + "!");
    }
}

public class LZCBE2 {
    public static void main(String[] args) {
        User user = new User("Alice");
        Printer printer = new Printer(user);
        printer.printGreetings();
    }
}
```