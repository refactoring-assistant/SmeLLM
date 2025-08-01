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

public class source20 {
  public static void main(String[] args) {
    BankAccount account1 = new BankAccount(1000, "John", "123456789");
    BankAccount account2 = new BankAccount(2000, "Jane", "987654321");

    account1.deposit(500);
    account1.withdraw(200);
    account1.transfer(100, account2);
  }
}
