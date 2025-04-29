**Code Review: LZCBE2.java**
   - Code smell no. - 1
   - Code smell name - Refused Bequest
   - Code smell description - A subclass inherits methods and data that it does not need or use, which violates the Liskov Substitution Principle and implies a poor design.
   - Found in line no. - 11
   - Possible treatments - ['Replace Inheritance with Delegation', 'Extract Superclass']
   - Possible solution - 
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
