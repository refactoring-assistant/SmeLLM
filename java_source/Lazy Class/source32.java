class PrintGreetings {
    private String userName;
    public PrintGreetings(String userName) {
        this.userName = userName;
    }
    public void printGreetings() {
        System.out.println("Hello, " + userName + "!");
    }
}

class PrintHelloUser extends PrintGreetings {
    public PrintHelloUser(String userName) {
        super(userName);
    }

    public void printHelloUser() {
        printGreetings();
    }

}
public class source32 {
    public static void main(String[] args) {
      PrintHelloUser helloUser = new PrintHelloUser("Alice");
        helloUser.printHelloUser();
    }
}
