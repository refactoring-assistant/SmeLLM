**Code Review: MCBE1.java**

- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - Using primitive data types to represent complex entities such as street, city, and zipCode for an address, and for grouping person related information like salutation, name, and address.
- Found in line no. - 5, 6, 7, 21, 22, 23
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy, Replace Array with Object
- Possible solution - 
  ```java
  class Address {
      private final String street;
      private final String city;
      private final String zipCode;

      public Address(String street, String city, String zipCode) {
          this.street = street;
          this.city = city;
          this.zipCode = zipCode;
      }

      public String fullAddress() {
          return street + ", " + city + ", " + zipCode;
      }
  }

  class Person {
      private final String salutation;
      private final String name;
      private final Address address;

      public Person(String salutation, String name, Address address) {
          this.salutation = salutation;
          this.name = name;
          this.address = address;
      }

      public String fullName() {
          return salutation + " " + name;
      }

      public Address getAddress() {
          return address;
      }
  }

  class Order {
      private final Person person;
      private final int orderNumber;
      private final List<String> items;
      private String orderStatus;
      private double orderTotal;

      public Order(Person person, int orderNumber) {
          this.person = person;
          this.orderNumber = orderNumber;
          this.items = new ArrayList<>();
          this.orderStatus = "Pending";
          this.orderTotal = 0;
      }

      public Person getPerson() {
          return person;
      }

      public void addItem(String item) {
          orderTotal += 10; // Assuming each item costs 10 for simplicity
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
          items.forEach(System.out::println);
      }
  }

  class OrderHistory {
      private final List<Order> orders;

      public OrderHistory() {
          this.orders = new ArrayList<>();
      }

      public void addOrder(Order order) {
          orders.add(order);
      }

      public void printOrderHistory() {
          for (Order order : orders) {
              order.printOrderDetails();
              System.out.println("Person: " + order.getPerson().fullName());
              System.out.println("Address: " + order.getPerson().getAddress().fullAddress());
          }
      }
  }

  public class MCBE1 {
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
  ```

- Code smell no. - 2
- Code smell name - Long Method
- Code smell description - Methods with too many lines of code and complex logic that can be decomposed for better readability and maintainability.
- Found in line no. - 68-76, 90-95
- Possible treatments - Extract Method, Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object, Decompose Conditional
- Possible solution -
  ```java
  class Order {
      //... existing code ...

      public void printOrderDetails() {
          System.out.println("Order Number: " + orderNumber);
          System.out.println("Order Status: " + orderStatus);
          System.out.println("Order Total: " + orderTotal);
          printItems();
      }

      private void printItems() {
          System.out.println("Items: ");
          items.forEach(System.out::println);
      }
  }

  class OrderHistory {
      //... existing code ...

      public void printOrderHistory() {
          for (Order order : orders) {
              order.printOrderDetails();
              printPersonDetails(order.getPerson());
          }
      }

      private void printPersonDetails(Person person) {
          System.out.println("Person: " + person.fullName());
          System.out.println("Address: " + person.getAddress().fullAddress());
      }
  }
  ```