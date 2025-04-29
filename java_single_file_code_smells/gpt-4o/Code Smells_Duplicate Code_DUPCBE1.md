**Code Review: DUPCBE1.java**

- Code smell no. - 1
  - Code smell name - Duplicate Code
  - Code smell description - The code for printing the account information (owner, account number, and balance) is repeated in multiple methods: `deposit`, `withdraw`, and `transfer`.
  - Found in line no. - [14-16, 21-23, 29-31]
  - Possible treatments - Extract Method, Extract Method & Pull Up Field, Consolidate Duplicate Conditional Fragments.
  - Possible solution:
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
            printAccountInfo();
        }

        public void withdraw(double amount) {
            balance -= amount;
            printAccountInfo();
        }

        public void transfer(double amount, BankAccountBad otherAccount) {
            balance -= amount;
            otherAccount.balance += amount;
            printAccountInfo();
        }

        private void printAccountInfo() {
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