**Code Review: LZCGE2.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A "Data Class" is a class that primarily stores data and has little or no behavior. It tends to have many fields with public accessors but lacks meaningful methods to manipulate the data.
- Found in line no. - 2, 3, 4, 6, 7
- Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
- Possible solution - 
```java
class PrintGreetingsGood {
    private String userName;

    public PrintGreetingsGood(String userName) {
        setUserName(userName);
    }

    public void setUserName(String userName) {
        if (userName != null && !userName.isEmpty()) {
            this.userName = userName;
        }
    }

    public String getUserName() {
        return userName;
    }

    public void printGreetings() {
        System.out.println("Hello, " + getUserName() + "!");
    }
}

public class LZCGE2 {
    public static void main(String[] args) {
        PrintGreetingsGood helloUser = new PrintGreetingsGood("Alice");
        helloUser.printGreetings();
    }
}
```