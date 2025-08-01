/**
 * This class represents a user address.
 **/
class UserAddress {
  // Variables are final so that they can be initialized only once
  private final String street;
  private final String city;
  private final String state;

  public UserAddress(String street, String city, String state) {
      this.street = street;
      this.city = city;
      this.state = state;
  }

  // Code to print the address of the user in a predefined format
  public void printFormattedAddress() {
    System.out.println("The address of this user is " + street + ", " + city + ", " + state);
  }
}
public class source5 {
    public static void main(String[] args) {
        UserAddress userAddress = new UserAddress("1234", "New York City", "NY");
        userAddress.printFormattedAddress();
    }
}
