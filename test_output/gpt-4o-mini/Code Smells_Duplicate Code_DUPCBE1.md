**Code Review: DUPCBE1.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - Methods that are excessively long and do more than one thing, which makes them hard to understand and maintain.
- Found in line no. - 12, 19, 26
- Possible treatments - Extract Method
- Possible solution - 
```java
class BankAccountBad {
    private double balance;
    private String owner;
    private String accountNumber;

    public BankAccountBad(double balance, String owner, String accountNumber) {
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

    public void transfer(double amount, BankAccountBad otherAccount) {
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

public class DUPCBE1 {
    public static void main(String[] args) {
        BankAccountBad account1 = new BankAccountBad(1000, "John", "123456789");
        BankAccountBad account2 = new BankAccountBad(2000, "Jane", "987654321");

        account1.deposit(500);
        account1.withdraw(200);
        account1.transfer(100, account2);
    }
}
```

- Code smell no. - 2
- Code smell name - Long Parameter List
- Code smell description - A method with too many parameters increases complexity and reduces readability.
- Found in line no. - 26
- Possible treatments - Introduce Parameter Object
- Possible solution - 
```java
class BankAccountBad {
    private double balance;
    private String owner;
    private String accountNumber;

    public BankAccountBad(double balance, String owner, String accountNumber) {
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

    public void transfer(TransferDetails details) {
        balance -= details.amount;
        details.otherAccount.balance += details.amount;
        printAccountDetails();
    }

    private void printAccountDetails() {
        System.out.println("Owner: " + owner);
        System.out.println("Account number: " + accountNumber);
        System.out.println("Balance: " + balance);
    }
}

class TransferDetails {
    double amount;
    BankAccountBad otherAccount;

    public TransferDetails(double amount, BankAccountBad otherAccount) {
        this.amount = amount;
        this.otherAccount = otherAccount;
    }
}

public class DUPCBE1 {
    public static void main(String[] args) {
        BankAccountBad account1 = new BankAccountBad(1000, "John", "123456789");
        BankAccountBad account2 = new BankAccountBad(2000, "Jane", "987654321");

        account1.deposit(500);
        account1.withdraw(200);
        account1.transfer(new TransferDetails(100, account2));
    }
}
```