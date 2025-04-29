```markdown
**Code Review: MCGE1.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A class that has fields but lacks significant behavior beyond getters and setters.
- Found in line no. - 4, 20, 40, 77
- Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
- Possible solution - 
```java
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
        this.items = new ArrayList<>();
        this.orderStatus = "Pending";
        this.orderTotal = 0;
    }

    public void addItem(String item) {
        orderTotal += 10;
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
        System.out.println("Items: " + String.join(", ", items));
        System.out.println("Person: " + person.getName());
        System.out.println("Address: " + person.getAddress());
    }
}

class OrderHistory {
    private List<Order> orders;

    public OrderHistory() {
        this.orders = new ArrayList<>();
    }

    public void addOrder(Order order) {
        orders.add(order);
    }

    public void printOrderHistory() {
        for (Order order : orders) {
            order.printOrderDetails();
        }
    }
}

public class MCGE1 {
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
```