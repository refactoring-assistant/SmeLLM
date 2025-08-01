import static java.lang.Math.abs;

interface IAddress {
  void printAddress();
}

interface IBankAccount {
  void addDeposit(double money);
  void withdrawMoney(double money);
  void printBankDetails();
}

interface IPerson {
  void addAddress(IAddress address);
  void addBankAccount(IBankAccount bankAccount);
  void printPersonDetails();
}
class Address implements IAddress {
  private String street;
  private String city;
  private String state;
  private String zipcode;

  public Address() {
    this.street = "N/A";
    this.city = "N/A";
    this.state = "N/A";
    this.zipcode = "N/A";
  }
  public Address(String street, String city, String state, String zipcode) {
    this.street = street;
    this.city = city;
    this.state = state;
    this.zipcode = zipcode;
  }

  @Override
  public void printAddress() {
    System.out.println("Address: " + this.street + ", " + this.city + ", " + this.state + ", " + this.zipcode);
  }
}

class BankAccount implements IBankAccount {
  private String bankAccountNumber;
  private double bankAccountBalance;
  private String bankAccountType;

  public BankAccount() {
    this.bankAccountNumber = "N/A";
    this.bankAccountBalance = 0;
    this.bankAccountType = "N/A";
  }

  public BankAccount(String bankAccountNumber, String bankAccountType){
    this.bankAccountNumber = bankAccountNumber;
    this.bankAccountBalance = 0;
    this.bankAccountType = bankAccountType;
  }

  public void addDeposit(double money) {
    this.bankAccountBalance += abs(money);
  }

  public void withdrawMoney(double money) {
    this.bankAccountBalance -= abs(money);
  }

  public void printBankDetails() {
    System.out.println("Bank Account: " + this.bankAccountNumber + ", " + this.bankAccountType + ", " + this.bankAccountBalance);
  }
}

class Person implements IPerson {
  private String firstname;
  private String lastname;
  private IAddress address;
  private IBankAccount bankAccount;

  public Person(String firstname, String lastname) {
    this.firstname = firstname;
    this.lastname = lastname;
    address = new Address();
    bankAccount = new BankAccount();
  }

  public void addAddress(IAddress address) {
    this.address = address;
  }

  public void addBankAccount(IBankAccount bankAccount) {
    this.bankAccount = bankAccount;
  }

  public void printPersonDetails() {
    System.out.println("Name: " + this.firstname + " " + this.lastname);
    address.printAddress();
    bankAccount.printBankDetails();
  }
}

public class source29 {
  public static void main(String[] args) {
    IPerson person1 = new Person("John", "Doe");
    IAddress address1 = new Address("Street 1", "Boston", "MA", "02115");
    IBankAccount bankAccount1 = new BankAccount("123456789", "Checking");
    bankAccount1.addDeposit(1000);
    bankAccount1.withdrawMoney(100);
    person1.addAddress(address1);
    person1.addBankAccount(bankAccount1);
    person1.printPersonDetails();
  }
}

