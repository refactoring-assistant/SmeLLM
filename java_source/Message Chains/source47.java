import java.util.ArrayList;
import java.util.List;

class Address {
  private String street;
  private String city;
  private String zipCode;

  public Address(String street, String city, String zipCode) {
    this.street = street;
    this.city = city;
    this.zipCode = zipCode;
  }

  public String getAddress() {
    return street + ", " + city + ", " + zipCode;
  }
}

class Person {
  private String salutation;
  private String name;
  private Address address;

  public Person(String salutation, String name, Address address) {
    this.salutation = salutation;
    this.name = name;
    this.address = address;
  }

  public String getName() {
    return salutation + " " + name;
  }

  public String getAddress() {
    return address.getAddress();
  }
}

class Order {
  private Person person;
  private int orderNumber;
  private List<String> items;
  private String orderStatus;
  private double orderTotal;
  public Order(Person person, int orderNumber) {
    this.person = person;
    this.orderNumber = orderNumber;
    this.items = new ArrayList<String>();
    this.orderStatus = "Pending";
    this.orderTotal = 0;
  }

  public void addItem(String item) {
    orderTotal+=10;
    items.add(item);
  }

  public void placeOrder() {
    orderStatus = "Placed";
    System.out.println("Order placed successfully. Cost: " + orderTotal);
  }

  public void printOrderDetails() {
    System.out.println("Order Number: " + orderNumber);
    System.out.println("Order Status: " + orderStatus);
    System.out.println("Order Total: " + orderTotal);
    System.out.println("Items: ");
    for(String item : items) {
      System.out.println(item);
    }
    System.out.println("Person: " + person.getName());
    System.out.println("Address: " + person.getAddress());
  }
}

class OrderHistory {
  private List<Order> orders;

  public OrderHistory() {
    this.orders = new ArrayList<Order>();
  }

  public void addOrder(Order order) {
    orders.add(order);
  }

  public void printOrderHistory() {
    for(Order order : orders) {
      order.printOrderDetails();
    }
  }
}
public class source47 {
  public static void main(String[] args) {
    Address address = new Address("123 Main St", "Boston", "12345");
    Person person = new Person("Mr", "John Doe", address);
    Order order = new Order(person, 1);
    order.addItem("Item 1");
    order.addItem("Item 2");
    order.placeOrder();
    OrderHistory orderHistory = new OrderHistory();
    orderHistory.addOrder(order);
    orderHistory.printOrderHistory();
  }
}
