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

    // This is a method to calculate the total order amount.
    // It takes the number of items and the cost per item as input.
    // It calculates the total order amount by multiplying the number of items with the cost per item.
    public void solve(int numItems , double perItemCost) {
        // the order status must say 'confirmed' to calculate the order amount

        // the order amount requires the cost of all items, the discount, and the tax
        // the order amount is calculated after applying discount, which would be (orderAmount - orderAmount * discount)
        // the order amount is calculated after applying tax, which would be (orderAmount + orderAmount * tax)
        orderAmount = (numItems * perItemCost) * (1 - discount) * (1 + tax);
    }

    public void printOrderDetails() {
        System.out.println("Order ID: " + orderID);
        System.out.println("Order Name: " + orderName);
        System.out.println("Order Amount: " + Math.round(orderAmount));
        System.out.println("Order Status: " + orderStatus);
    }

}
public class source3 {
  public static void main(String[] args) {
    Order order = new Order(1, "Laptop", "confirmed");
    order.solve(2, 500);
    order.printOrderDetails();
  }
}
