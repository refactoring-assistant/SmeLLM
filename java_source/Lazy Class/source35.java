class PrintGreetings {
  private String userName;
  public PrintGreetings(String userName) {
    this.userName = userName;
  }
  public void printGreetings() {
    System.out.println("Hello, " + userName + "!");
  }
}
public class source35 {
    public static void main(String[] args) {
      PrintGreetings helloUser = new PrintGreetings("Alice");
      helloUser.printGreetings();
    }
}
