```markdown
**Code Review: CBE1.java**
   - Code smell no. - 1
   - Code smell name - Comments
   - Code smell description - The code contains comments that can be avoided by giving meaningful names to variables and methods. Instead of adding comments, the clarity should be achieved through code structure.
   - Found in line no. - 17, 18, 19, 21, 23, 24, 25
   - Possible treatments - ['Extract Variable', 'Extract Method', 'Rename Method', 'Introduce Assertion']
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

         public void calculateTotalOrderAmount(int numItems, double perItemCost) {
             if ("confirmed".equals(orderStatus)) {
                 double initialAmount = numItems * perItemCost;
                 double discountAmount = initialAmount * discount;
                 double taxAmount = initialAmount * tax;
                 orderAmount = (initialAmount - discountAmount + taxAmount);
             }
         }

         public void printOrderDetails() {
             System.out.println("Order ID: " + orderID);
             System.out.println("Order Name: " + orderName);
             System.out.println("Order Amount: " + Math.round(orderAmount));
             System.out.println("Order Status: " + orderStatus);
         }
     }

     public class CBE1 {
         public static void main(String[] args) {
             Order order = new Order(1, "Laptop", "confirmed");
             order.calculateTotalOrderAmount(2, 500);
             order.printOrderDetails();
         }
     }
     ```

   - Code smell no. - 2
   - Code smell name - Long Method
   - Code smell description - The `solve` method is doing multiple tasks including calculating discounts and taxes, which makes it lengthy and difficult to maintain.
   - Found in line no. - 20-26
   - Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
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

         public void calculateTotalOrderAmount(int numItems, double perItemCost) {
             if ("confirmed".equals(orderStatus)) {
                 double initialAmount = calculateInitialAmount(numItems, perItemCost);
                 double discountedAmount = applyDiscount(initialAmount);
                 orderAmount = applyTax(discountedAmount);
             }
         }

         private double calculateInitialAmount(int numItems, double perItemCost) {
             return numItems * perItemCost;
         }

         private double applyDiscount(double amount) {
             return amount * (1 - discount);
         }

         private double applyTax(double amount) {
             return amount * (1 + tax);
         }

         public void printOrderDetails() {
             System.out.println("Order ID: " + orderID);
             System.out.println("Order Name: " + orderName);
             System.out.println("Order Amount: " + Math.round(orderAmount));
             System.out.println("Order Status: " + orderStatus);
         }
     }

     public class CBE1 {
         public static void main(String[] args) {
             Order order = new Order(1, "Laptop", "confirmed");
             order.calculateTotalOrderAmount(2, 500);
             order.printOrderDetails();
         }
     }
     ```
```
