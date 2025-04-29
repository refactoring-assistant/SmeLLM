**Code Review: CGE1.java**
  - Code smell no. - 1
  - Code smell name - Data Class
  - Code smell description - A Data Class is one that contains fields and possibly some getter/setter methods, but it doesn't have any complex functionality or behaviors associated with the data it holds.
  - Found in line no. - 1 to 36
  - Possible treatments - ['Encapsulate Field', 'Encapsulate Collection ', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
  - Possible solution - 
    ```java
    class OrderGood {
      private int orderID;
      private String orderName;
      private double orderAmount;
      private double discount;
      private double tax;
      private String orderStatus;

      public OrderGood(int orderID, String orderName, String orderStatus) {
        this.orderID = orderID;
        this.orderName = orderName;
        setDiscount(0.15);
        setTax(0.1);
        this.orderStatus = orderStatus;
      }
      
      public double getDiscount() {
        return discount;
      }

      private void setDiscount(double discount) {
        this.discount = discount;
      }

      public double getTax() {
        return tax;
      }

      private void setTax(double tax) {
        this.tax = tax;
      }

      public void calculateOrderAmount(int numItems, double perItemCost) throws IllegalStateException {
        if (!isOrderConfirmed()) {
          throw new IllegalStateException("Order is not confirmed");
        }
        orderAmount = computeTotalAmount(numItems, perItemCost);
      }

      private boolean isOrderConfirmed() {
        return "confirmed".equals(orderStatus);
      }

      private double computeTotalAmount(int numItems, double perItemCost) {
        double totalCost = numItems * perItemCost;
        double percentageAfterDiscount = 1 - getDiscount();
        double percentageAfterTax = 1 + getTax();
        return totalCost * percentageAfterDiscount * percentageAfterTax;
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
        OrderGood order = new OrderGood(1, "Laptop", "confirmed");
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