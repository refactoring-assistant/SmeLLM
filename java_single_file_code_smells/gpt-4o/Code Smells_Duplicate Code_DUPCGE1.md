**Code Review: DUPCGE1.java**

- Code smell no. - 1
- Code smell name - Duplicate Code
- Code smell description - The code contains repeated calls to `printAccountDetails()` in the `deposit`, `withdraw`, and `transfer` methods, which exhibit duplicate logic.
- Found in line no. - [14, 19, 25]
- Possible treatments - ['Extract Method', 'Extract Method & Pull Up Field', 'Pull Up Constructor Body', 'Form Template Method', 'Substitute Algorithm', 'Extract Superclass', 'Extract ClassConsolidate Conditional Expression and use Extract Method', 'Consolidate Duplicate Conditional Fragments']
- Possible solution - To reduce the duplicate code, consolidate the repeated call to `printAccountDetails()` by incorporating it into a new method or adjusting the logic, and call this new method in each bank transaction.

**Redefined Code:**

```java
class BankAccountGood {
  private double balance;
  private String owner;
  private String accountNumber;

  public BankAccountGood(double balance, String owner, String accountNumber) {
    this.balance = balance;
    this.owner = owner;
    this.accountNumber = accountNumber;
  }

  public void deposit(double amount) {
    balance += amount;
    transactionComplete();
  }

  public void withdraw(double amount) {
    balance -= amount;
    transactionComplete();
  }

  public void transfer(double amount, BankAccountGood otherAccount) {
    balance -= amount;
    otherAccount.balance += amount;
    transactionComplete();
  }

  private void transactionComplete() {
    printAccountDetails();
  }

  private void printAccountDetails() {
    System.out.println("Owner: " + owner);
    System.out.println("Account number: " + accountNumber);
    System.out.println("Balance: " + balance);
  }
}

public class DUPCGE1 {
  public static void main(String[] args) {
    BankAccountGood account1 = new BankAccountGood(1000, "John", "123456789");
    BankAccountGood account2 = new BankAccountGood(2000, "Jane", "987654321");

    account1.deposit(500);
    account1.withdraw(200);
    account1.transfer(100, account2);
  }
}
```
