**Code Review: DUPCGE1.java**
- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - A class that has too many responsibilities or has grown too large, making it hard to maintain.
- Found in line no. - 1
- Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
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
        balance += amount;
        printAccountDetails();
    }

    public void withdraw(double amount) {
        balance -= amount;
        printAccountDetails();
    }

    public void transfer(double amount, BankAccount otherAccount) {
        balance -= amount;
        otherAccount.balance += amount;
        printAccountDetails();
    }

    private void printAccountDetails() {
        System.out.println("Owner: " + owner);
        System.out.println("Account number: " + accountNumber);
        System.out.println("Balance: " + balance);
    }
}

class Bank {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount(1000, "John", "123456789");
        BankAccount account2 = new BankAccount(2000, "Jane", "987654321");

        account1.deposit(500);
        account1.withdraw(200);
        account1.transfer(100, account2);
    }
}
```
