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

  public void calculateOrderAmount(int numItems , double perItemCost) throws IllegalStateException {
    if(!orderStatus.equals("confirmed")) {
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
public class source6 {
  public static void main(String[] args) {
    Order order = new Order(1, "Laptop", "confirmed");
    try {
      order.calculateOrderAmount(2, 500);
    } catch(IllegalStateException e) {
      System.out.println(e.getMessage());
      return;
    }
    order.printOrderDetails();
  }
}
