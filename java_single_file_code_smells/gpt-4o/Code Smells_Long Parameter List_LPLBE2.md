```markdown
**Code Review: LPLBE2.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data types for memberDiscount, stateTax, storeDiscount, and fees in the code rather than creating objects that better represent the concepts they encapsulate.
- Found in line no. -  (~5~), (~6~), (~28~), (~29~)
- Possible treatments - Replace Data Value with Object, Introduce Parameter Object or Preserve Whole Object, Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy.
- Possible solution - Creating classes or objects for discounts, tax and fees can improve code readability and maintainability.

- Code smell no. - 2
- Code smell name - Long Parameter List
- Code smell description - The `calculateCartPrice` method in `ShoppingCartBad` takes five parameters, which is considered excessive and can lead to errors and confusion.
- Found in line no. - (~70~)
- Possible treatments - Replace Parameter with Method Call, Preserve Whole Object, Introduce Parameter Object.
- Possible solution - Use objects to encapsulate parameters.

- Code smell no. - 3
- Code smell name - Data Clumps
- Code smell description - The recurring combination of `priceList`, `storeDiscount`, `memberDiscount`, `tax`, and `fees` suggests that these could be bundled into an object.
- Found in line no. - (~70~), (~94~)
- Possible treatments - Extract Class, Introduce Parameter Object, Preserve Whole Object.
- Possible solution - Create a PricingInfo class to pass data around.

**Revised Code Example:**

```java
import java.util.HashMap;
import java.util.Map;

class Discount {
    private double discount;

    public Discount(double discount) {
        this.discount = discount;
    }

    public double getValue() {
        return discount;
    }
}

class Tax {
    private double taxRate;

    public Tax(double taxRate) {
        this.taxRate = taxRate;
    }

    public double getRate() {
        return taxRate;
    }
}

class Fee {
    private double feeAmount;

    public Fee(double feeAmount) {
        this.feeAmount = feeAmount;
    }

    public double getAmount() {
        return feeAmount;
    }
}

class StoreMemberPricing {
    private Discount memberDiscount;
    private Tax stateTax;

    public StoreMemberPricing(Tax stateTax) {
        this.memberDiscount = new Discount(0.05);
        this.stateTax = stateTax;
    }

    public Discount getMemberDiscount() {
        return memberDiscount;
    }

    public Tax getStateTax() {
        return stateTax;
    }

    public void printMemberDiscount() {
        System.out.println("Thank you for being a member.");
        System.out.println("Member Discount: " + memberDiscount.getValue());
        System.out.println("State Tax: " + stateTax.getRate());
    }
}

class StorePricing {
    private Discount storeDiscount;
    private Fee fees;
    private Map<String, Double> productPricePerQuantity;

    public StorePricing(Map<String, Double> productPricePerQuantity) {
        this.productPricePerQuantity = productPricePerQuantity;
        this.storeDiscount = new Discount(0.1);
        this.fees = new Fee(10);
    }

    public Map<String, Double> getProductPricePerQuantity() {
        return productPricePerQuantity;
    }

    public Discount getStoreDiscount() {
        return storeDiscount;
    }

    public Fee getFees() {
        return fees;
    }

    public void printProductTypesAndPrice() {
        for (Map.Entry<String, Double> entry : productPricePerQuantity.entrySet()) {
            System.out.println("Product: " + entry.getKey() + ", Price: " + entry.getValue());
        }
    }
}

class PricingInfo {
    private Map<String, Double> priceList;
    private Discount storeDiscount;
    private Discount memberDiscount;
    private Tax tax;
    private Fee fees;

    public PricingInfo(Map<String, Double> priceList, Discount storeDiscount, Discount memberDiscount, Tax tax, Fee fees) {
        this.priceList = priceList;
        this.storeDiscount = storeDiscount;
        this.memberDiscount = memberDiscount;
        this.tax = tax;
        this.fees = fees;
    }

    public Map<String, Double> getPriceList() {
        return priceList;
    }

    public Discount getStoreDiscount() {
        return storeDiscount;
    }

    public Discount getMemberDiscount() {
        return memberDiscount;
    }

    public Tax getTax() {
        return tax;
    }

    public Fee getFees() {
        return fees;
    }
}

class ShoppingCart {
    private Map<String, Integer> productsBought;

    public ShoppingCart() {
        this.productsBought = new HashMap<>();
    }

    public void addProduct(String product, int quantity) {
        productsBought.put(product, quantity);
    }

    public double calculateCartPrice(PricingInfo pricingInfo) {
        double totalPrice = 0;
        for (Map.Entry<String, Integer> entry : productsBought.entrySet()) {
            String product = entry.getKey();
            int quantity = entry.getValue();
            double price = pricingInfo.getPriceList().get(product);
            totalPrice += price * quantity;
        }
        totalPrice = totalPrice * (1 - pricingInfo.getStoreDiscount().getValue())
                * (1 - pricingInfo.getMemberDiscount().getValue())
                * (1 + pricingInfo.getTax().getRate()) + pricingInfo.getFees().getAmount();
        return totalPrice;
    }
}

public class LPLBE2 {
    public static void main(String[] args) {
        Map<String, Double> productPricePerQuantity = Map.of("Apple", 1.0, "Banana", 0.5, "Orange", 1.5);
        StorePricing storePricing = new StorePricing(productPricePerQuantity);
        StoreMemberPricing storeMemberPricing = new StoreMemberPricing(new Tax(0.1));
        storeMemberPricing.printMemberDiscount();
        storePricing.printProductTypesAndPrice();
        ShoppingCart shoppingCart = new ShoppingCart();
        shoppingCart.addProduct("Apple", 2);
        shoppingCart.addProduct("Banana", 3);
        shoppingCart.addProduct("Orange", 1);
        PricingInfo pricingInfo = new PricingInfo(
                storePricing.getProductPricePerQuantity(),
                storePricing.getStoreDiscount(),
                storeMemberPricing.getMemberDiscount(),
                storeMemberPricing.getStateTax(),
                storePricing.getFees()
        );
        double totalPrice = shoppingCart.calculateCartPrice(pricingInfo);
        System.out.println("Total Price: $" + totalPrice);
    }
}
```
```