```markdown
**Code Review: CGE1.java**
- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - A class that has grown too large and has too many responsibilities.
- Found in line no. - ~1~
- Possible treatments - Extract Class, Extract Subclass, Extract Interface, Duplicate Observed Data.
- Possible solution - 
```java
class Order {
    private int orderID;
    private String orderName;
    private double orderAmount;

    public Order(int orderID, String orderName) {
        this.orderID = orderID;
        this.orderName = orderName;
    }

    public void setOrderAmount(double orderAmount) {
        this.orderAmount = orderAmount;
    }

    public void printOrderDetails() {
        System.out.println("Order ID: " + orderID);
        System.out.println("Order Name: " + orderName);
        System.out.println("Order Amount: " + Math.round(orderAmount));
    }
}

class OrderGood {
    private Order order;
    private double discount;
    private double tax;
    private String orderStatus;

    public OrderGood(int orderID, String orderName, String orderStatus) {
        this.order = new Order(orderID, orderName);
        this.discount = 0.15;
        this.tax = 0.1;
        this.orderStatus = orderStatus;
    }

    public void calculateOrderAmount(int numItems , double perItemCost) throws IllegalStateException {
        if(!orderStatus.equals("confirmed")) {
            throw new IllegalStateException("Order is not confirmed");
        }

        double totalCost = numItems * perItemCost;
        double percentageAfterDiscount = 1 - discount;
        double percentageAfterTax = 1 + tax;

        order.setOrderAmount(totalCost * percentageAfterDiscount * percentageAfterTax);
    }

    public void printOrderDetails() {
        order.printOrderDetails();
    }
}

public class CGE1 {
    public static void main(String[] args) {
        OrderGood order = new OrderGood(1, "Laptop", "confirmed");
        try {
            order.calculateOrderAmount(2, 500);
        } catch(IllegalStateException e) {
            System.out.println(e.getMessage());
            return;
        }
        order.printOrderDetails();
    }
}
```
- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - Using primitive data types to represent concepts instead of encapsulating them in objects.
- Found in line no. - ~2~, ~3~, ~4~, ~12~, ~13~, ~7~
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy.
- Possible solution - 
```java
class OrderStatus {
    private String status;

    public OrderStatus(String status) {
        this.status = status;
    }

    public boolean isConfirmed() {
        return "confirmed".equals(status);
    }
}

class Order {
    private int orderID;
    private String orderName;
    private double orderAmount;

    public Order(int orderID, String orderName) {
        this.orderID = orderID;
        this.orderName = orderName;
    }
    
    // Other methods as before
}

class OrderGood {
    private Order order;
    private double discount;
    private double tax;
    private OrderStatus orderStatus;

    public OrderGood(int orderID, String orderName, String orderStatus) {
        this.order = new Order(orderID, orderName);
        this.discount = 0.15;
        this.tax = 0.1;
        this.orderStatus = new OrderStatus(orderStatus);
    }

    public void calculateOrderAmount(int numItems , double perItemCost) throws IllegalStateException {
        if(!orderStatus.isConfirmed()) {
            throw new IllegalStateException("Order is not confirmed");
        }

        // Remaining method as before
    }
}
```
```