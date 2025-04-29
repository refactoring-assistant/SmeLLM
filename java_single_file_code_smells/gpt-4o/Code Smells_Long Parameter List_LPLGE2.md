**Code Review: LPLGE2.java**

- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data types for `memberDiscount`, `stateTax`, `storeDiscount`, and `fees` instead of encapsulating these into more descriptive classes.
- Found in line no. - [~5~, ~6~, ~28~, ~29~]
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object']
- Possible solution: 
  ```java
  import java.util.HashMap;
  import java.util.Map;

  class Discount {
      private double discountValue;

      public Discount(double discountValue) {
          this.discountValue = discountValue;
      }

      public double getDiscountValue() {
          return discountValue;
      }
  }

  class StoreMemberPricingGood {
      private Discount memberDiscount;
      private double stateTax;

      public StoreMemberPricingGood(double stateTax) {
          this.memberDiscount = new Discount(0.05);
          this.stateTax = stateTax;
      }

      public double getMemberDiscount() {
          return memberDiscount.getDiscountValue();
      }

      public double getTax() {
          return stateTax;
      }

      public void printMemberDiscount() {
          System.out.println("Thank you for being a member.");
          System.out.println("Member Discount: " + memberDiscount.getDiscountValue());
          System.out.println("State Tax: " + stateTax);
      }
  }

  class StorePricingGood {
      private Discount storeDiscount;
      private double fees;
      private Map<String, Double> productPricePerQuantity;

      public StorePricingGood(Map<String, Double> productPricePerQuantity) {
          this.productPricePerQuantity = productPricePerQuantity;
          this.storeDiscount = new Discount(0.1);
          this.fees = 10;
      }

      public Map<String, Double> getProductPricePerQuantity() {
          return productPricePerQuantity;
      }

      public double getStoreDiscount() {
          return storeDiscount.getDiscountValue();
      }

      public double getFees() {
          return fees;
      }

      public void printProductTypesAndPrice() {
          for (Map.Entry<String, Double> entry : productPricePerQuantity.entrySet()) {
              System.out.println("Product: " + entry.getKey() + ", Price: " + entry.getValue());
          }
      }
  }

  class ShoppingCartGood {
      private Map<String, Integer> productsBought;
      private StorePricingGood storePricing;
      private StoreMemberPricingGood storeMemberPricing;

      public ShoppingCartGood(StorePricingGood storePricing, StoreMemberPricingGood storeMemberPricing) {
          this.productsBought = new HashMap<>();
          this.storePricing = storePricing;
          this.storeMemberPricing = storeMemberPricing;
      }

      public void addProduct(String product, int quantity) {
          productsBought.put(product, quantity);
      }

      public double calculateCartPrice() {
          Map<String, Double> priceList = storePricing.getProductPricePerQuantity();
          double storeDiscount = storePricing.getStoreDiscount();
          double memberDiscount = storeMemberPricing.getMemberDiscount();
          double tax = storeMemberPricing.getTax();
          double fees = storePricing.getFees();
          double totalPrice = 0;
          for (Map.Entry<String, Integer> entry : productsBought.entrySet()) {
              String product = entry.getKey();
              int quantity = entry.getValue();
              double price = priceList.get(product);
              totalPrice += price * quantity;
          }
          totalPrice = totalPrice * (1 - storeDiscount) * (1 - memberDiscount) * (1 + tax) + fees;
          return totalPrice;
      }
  }

  public class LPLGE2 {
      public static void main(String[] args) {
          Map<String, Double> productPricePerQuantity = Map.of("Apple", 1.0, "Banana", 0.5, "Orange", 1.5);
          StorePricingGood storePricing = new StorePricingGood(productPricePerQuantity);
          StoreMemberPricingGood storeMemberPricing = new StoreMemberPricingGood(0.1);
          storeMemberPricing.printMemberDiscount();
          storePricing.printProductTypesAndPrice();
          ShoppingCartGood shoppingCart = new ShoppingCartGood(storePricing, storeMemberPricing);
          shoppingCart.addProduct("Apple", 2);
          shoppingCart.addProduct("Banana", 3);
          shoppingCart.addProduct("Orange", 1);
          double totalPrice = shoppingCart.calculateCartPrice();
          System.out.println("Total Price: $" + totalPrice);
      }
  }
  ```