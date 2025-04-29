**Code Review: DUPCGE1.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A class that has only fields and does not encapsulate behavior is often a data class. Here, the `BankAccountGood` class contains fields (balance, owner, accountNumber) but has minimal encapsulation of its functionality.
- Found in line no. - 1, 2, 3, 4
- Possible treatments - [Encapsulate Field, Move Method and Extract Method, Remove Setting Method and Hide Method]
- Possible solution - 
```java
class BankAccount {
    private double balance;
    private String owner;
    private String accountNumber;

    public BankAccount(double balance, String owner, String accountNumber) {
        this.balance = balance;
        this.owner = owner;
        this.accountNumber = accountNumber;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            printAccountDetails();
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            printAccountDetails();
        }
    }

    public void transfer(double amount, BankAccount otherAccount) {
        if (otherAccount != null && amount > 0 && amount <= balance) {
            balance -= amount;
            otherAccount.balance += amount;
            printAccountDetails();
            otherAccount.printAccountDetails();
        }
    }

    private void printAccountDetails() {
        System.out.println("Owner: " + owner);
        System.out.println("Account number: " + accountNumber);
        System.out.println("Balance: " + balance);
    }
}

public class DUPCGE1 {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount(1000, "John", "123456789");
        BankAccount account2 = new BankAccount(2000, "Jane", "987654321");

        account1.deposit(500);
        account1.withdraw(200);
        account1.transfer(100, account2);
    }
}
```