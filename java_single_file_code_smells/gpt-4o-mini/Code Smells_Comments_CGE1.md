```markdown
**Code Review: CGE1.java**
- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - A class that has grown too large and is doing too much, making it difficult to understand and maintain.
- Found in line no. - 1
- Possible treatments - Extract Class, Extract Subclass, Extract Interface, Duplicate Observed Data.
- Possible solution - 
```java
class Order {
    private int orderID;
    private String orderName;
    private double orderAmount;
    private double discount;
    private double tax;
    private String orderStatus;

    public Order(int orderID, String orderName, String orderStatus) {
        this.orderID = orderID;
        this.orderName = orderName;
        this.discount = 0.15;
        this.tax = 0.1;
        this.orderStatus = orderStatus;
    }

    public void calculateOrderAmount(int numItems, double perItemCost) throws IllegalStateException {
        if (!orderStatus.equals("confirmed")) {
            throw new IllegalStateException("Order is not confirmed");
        }

        double totalCost = numItems * perItemCost;
        double percentageAfterDiscount = 1 - discount;
        double percentageAfterTax = 1 + tax;

        orderAmount = totalCost * percentageAfterDiscount * percentageAfterTax;
    }

    public void printOrderDetails() {
        System.out.println("Order ID: " + orderID);
        System.out.println("Order Name: " + orderName);
        System.out.println("Order Amount: " + Math.round(orderAmount));
        System.out.println("Order Status: " + orderStatus);
    }
}

public class CGE1 {
    public static void main(String[] args) {
        Order order = new Order(1, "Laptop", "confirmed");
        try {
            order.calculateOrderAmount(2, 500);
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
            return;
        }
        order.printOrderDetails();
    }
}
```

- Code smell no. - 2
- Code smell name - Data Class
- Code smell description - A class that only contains fields and accessors/mutators, lacking behavior.
- Found in line no. - 1
- Possible treatments - Encapsulate Field, Encapsulate Collection, Move Method and Extract Method, Remove Setting Method and Hide Method.
- Possible solution - 
```java
class Order {
    private int orderID;
    private String orderName;
    private double orderAmount;
    private double discount;
    private double tax;
    private String orderStatus;

    public Order(int orderID, String orderName, String orderStatus) {
        this.orderID = orderID;
        this.orderName = orderName;
        this.discount = 0.15;
        this.tax = 0.1;
        this.orderStatus = orderStatus;
    }

    public void calculateOrderAmount(int numItems, double perItemCost) throws IllegalStateException {
        if (!isConfirmed()) {
            throw new IllegalStateException("Order is not confirmed");
        }
        
        double totalCost = numItems * perItemCost;
        orderAmount = totalCost * getDiscountFactor() * getTaxFactor();
    }

    private boolean isConfirmed() {
        return orderStatus.equals("confirmed");
    }

    private double getDiscountFactor() {
        return 1 - discount;
    }

    private double getTaxFactor() {
        return 1 + tax;
    }

    public void printOrderDetails() {
        System.out.println("Order ID: " + orderID);
        System.out.println("Order Name: " + orderName);
        System.out.println("Order Amount: " + Math.round(orderAmount));
        System.out.println("Order Status: " + orderStatus);
    }
}
```
```