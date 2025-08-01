class BankAccount {
  private String accountNumber;
  private String accountType;
  private double balance;

  public BankAccount(String accountNumber, String accountType, double balance) {
    this.accountNumber = accountNumber;
    this.accountType = accountType;
    this.balance = balance;
  }

  public String getAccountDetails() {
    return "Account Number: " + this.accountNumber + ", Account Type: " + this.accountType + ", Balance: " + this.balance;
  }
}

class Address {
  private String street;
  private String city;
  private String state;
  private String zip;

  public Address(String street, String city, String state, String zip) {
    this.street = street;
    this.city = city;
    this.state = state;
    this.zip = zip;
  }

  public String getAddressDetails() {
    return "Address: " + this.street + ", " + this.city + ", " + this.state + ", " + this.zip;
  }
}

class Person {
  private String name;
  private int age;
  private Address address;
  private BankAccount bankAccount;

  public Person(String name, int age, Address address, BankAccount bankAccount) {
    this.name = name;
    this.age = age;
    this.address = address;
    this.bankAccount = bankAccount;
  }

  public String getPersonDetails() {
    return "Name: " + this.name + ", Age: " + this.age + ", " + this.address.getAddressDetails() + ", " + this.bankAccount.getAccountDetails();
  }
}

public class source43 {
  public static void main(String[] args) {
    Address address2 = new Address("123 Main St", "Springfield", "IL", "62701");
    BankAccount bankAccount2 = new BankAccount("123456789", "Checking", 1000.00);
    Person person2 = new Person("John", 30, address2, bankAccount2);
    System.out.println(person2.getPersonDetails());
  }
}