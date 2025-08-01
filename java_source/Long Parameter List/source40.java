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

class PersonBad {
    private String name;
    private int age;
    private Address address;
    private BankAccount bankAccount;

    public PersonBad(String name, int age, String street, String city, String state, String zip, String accountNumber, String accountType, double balance) {
        this.name = name;
        this.age = age;
        this.address = new Address(street, city, state, zip);
        this.bankAccount = new BankAccount(accountNumber, accountType, balance);
    }

    public String getPersonDetails() {
        return "Name: " + this.name + ", Age: " + this.age + ", " + this.address.getAddressDetails() + ", " + this.bankAccount.getAccountDetails();
    }
}

public class source40 {
    public static void main(String[] args) {
        PersonBad person1 = new PersonBad("John", 30, "123 Main St", "Springfield", "IL", "62701", "123456789", "Checking", 1000);
        System.out.println(person1.getPersonDetails());
    }
}