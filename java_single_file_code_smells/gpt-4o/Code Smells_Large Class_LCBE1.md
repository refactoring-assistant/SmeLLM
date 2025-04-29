**Code Review: LCBE1.java**

- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - The `PersonBad` class is handling various responsibilities such as storing personal information, address details, and bank account information, leading to a class with too many functions and responsibilities.
- Found in line no. - [~3~ to ~52~]
- Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
- Possible solution:
  ```java
  class Person {
      private String firstname;
      private String lastname;
  
      public Person(String firstname, String lastname) {
          this.firstname = firstname;
          this.lastname = lastname;
      }
  
      public String getFullName() {
          return firstname + " " + lastname;
      }
  }

  class Address {
      private String street;
      private String city;
      private String state;
      private String zipcode;

      public Address(String street, String city, String state, String zipcode) {
          this.street = street;
          this.city = city;
          this.state = state;
          this.zipcode = zipcode;
      }

      @Override
      public String toString() {
          return street + ", " + city + ", " + state + ", " + zipcode;
      }
  }

  class BankAccount {
      private String accountNumber;
      private String accountType;
      private double balance;

      public BankAccount(String accountNumber, String accountType) {
          this.accountNumber = accountNumber;
          this.accountType = accountType;
          this.balance = 0;
      }

      public void deposit(double money) {
          this.balance += Math.abs(money);
      }

      public void withdraw(double money) {
          this.balance -= Math.abs(money);
      }

      @Override
      public String toString() {
          return accountNumber + ", " + accountType + ", " + balance;
      }
  }

  public class LCBE1 {
      public static void main(String[] args) {
          Person person1 = new Person("John", "Doe");
          Address address1 = new Address("Street 1", "Boston", "MA", "02115");
          BankAccount bankAccount1 = new BankAccount("123456789", "Checking");
  
          bankAccount1.deposit(1000);
          bankAccount1.withdraw(100);
  
          System.out.println("Name: " + person1.getFullName());
          System.out.println("Address: " + address1.toString());
          System.out.println("Bank Account: " + bankAccount1.toString());
      }
  }
  ```

- Code smell no. - 2
- Code smell name - Data Clumps
- Code smell description - Frequent occurrences of groups of data that appear together repeatedly, such as address components and bank account details.
- Found in line no. - [~6~ to ~9~, ~10~ to ~12~, ~26~ to ~30~, ~33~ to ~36~]
- Possible treatments - ['Extract Class', 'Introduce Parameter Object', 'Preserve Whole Object']
- Possible solution:
  - Already addressed with the solution provided for the "Large Class" code smell by extracting `Address` and `BankAccount` classes. 

No further code smells were detected in the provided code.