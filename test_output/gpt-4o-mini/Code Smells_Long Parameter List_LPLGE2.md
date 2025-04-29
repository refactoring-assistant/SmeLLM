```markdown
**Code Review: LPLGE2.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - This method is too long and handles multiple tasks that could be separated.
- Found in line no. - 72-86
- Possible treatments - Extract Method, Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object, Decompose Conditional
- Possible solution - 
  ```java
  public double calculateCartPrice() {
      Map<String, Double> priceList = storePricing.getProductPricePerQuantity();
      double totalPrice = calculateTotalPrice(priceList);
      totalPrice = applyDiscountsAndFees(totalPrice);
      return totalPrice;
  }

  private double calculateTotalPrice(Map<String, Double> priceList) {
      double totalPrice = 0;
      for (Map.Entry<String, Integer> entry : productsBought.entrySet()) {
          String product = entry.getKey();
          int quantity = entry.getValue();
          double price = priceList.get(product);
          totalPrice += price * quantity;
      }
      return totalPrice;
  }

  private double applyDiscountsAndFees(double totalPrice) {
      double storeDiscount = storePricing.getStoreDiscount();
      double memberDiscount = storeMemberPricing.getMemberDiscount();
      double tax = storeMemberPricing.getTax();
      double fees = storePricing.getFees();
      return totalPrice * (1 - storeDiscount) * (1 - memberDiscount) * (1 + tax) + fees;
  }
  ```

- Code smell no. - 2
- Code smell name - Data Clumps
- Code smell description - Similar data structures are being used for different classes, which could be combined into a single class.
- Found in line no. - 5-6, 28-29
- Possible treatments - Extract Class, Introduce Parameter Object, Preserve Whole Object
- Possible solution - 
  ```java
  class PricingDetails {
      private double discount;
      private double taxOrFees;

      public PricingDetails(double discount, double taxOrFees) {
          this.discount = discount;
          this.taxOrFees = taxOrFees;
      }

      public double getDiscount() {
          return discount;
      }

      public double getTaxOrFees() {
          return taxOrFees;
      }
  }

  class StoreMemberPricingGood {
      private PricingDetails pricingDetails;

      public StoreMemberPricingGood(double stateTax) {
          this.pricingDetails = new PricingDetails(0.05, stateTax);
      }

      public double getMemberDiscount() {
          return pricingDetails.getDiscount();
      }

      public double getTax() {
          return pricingDetails.getTaxOrFees();
      }
  }

  class StorePricingGood {
      private PricingDetails pricingDetails;
      private Map<String, Double> productPricePerQuantity;

      public StorePricingGood(Map<String, Double> productPricePerQuantity) {
          this.productPricePerQuantity = productPricePerQuantity;
          this.pricingDetails = new PricingDetails(0.1, 10);
      }

      public double getStoreDiscount() {
          return pricingDetails.getDiscount();
      }

      public double getFees() {
          return pricingDetails.getTaxOrFees();
      }
  }
  ```

- Code smell no. - 3
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data types (double) for critical domain data can be improved.
- Found in line no. - 5-6, 28-29
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Array with Object
- Possible solution - Similar to the Data Clumps solution above, encapsulating discount and fees in a `PricingDetails` class streamlines usage and enhances the clarity of the code.
```