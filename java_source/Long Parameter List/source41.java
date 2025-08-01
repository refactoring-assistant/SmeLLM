import java.util.HashMap;
import java.util.Map;

class StoreMemberPricing {
    private double memberDiscount;
    private double stateTax;

    public StoreMemberPricing(double stateTax) {
        this.memberDiscount = 0.05;
        this.stateTax = stateTax;
    }

    public double getMemberDiscount() {
        return memberDiscount;
    }

    public double getTax() {
        return stateTax;
    }

    public void printMemberDiscount() {
        System.out.println("Thank you for being a member.");
        System.out.println("Member Discount: " + memberDiscount);
        System.out.println("State Tax: " + stateTax);
    }
}
class StorePricing {
    private double storeDiscount;
    private double fees;
    private Map<String, Double> productPricePerQuantity;

    public StorePricing(Map<String, Double> productPricePerQuantity) {
        this.productPricePerQuantity = productPricePerQuantity;
        this.storeDiscount = 0.1;
        this.fees = 10;
    }

    public Map<String, Double> getProductPricePerQuantity() {
        return productPricePerQuantity;
    }

    public double getStoreDiscount() {
        return storeDiscount;
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
class ShoppingCart {

    private Map<String, Integer> productsBought;

    public ShoppingCart() {
        this.productsBought = new HashMap<>();
    }

    public void addProduct(String product, int quantity) {
        productsBought.put(product, quantity);
    }

    public double calculateCartPrice(Map<String, Double> priceList, double storeDiscount, double memberDiscount, double tax, double fees) {
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
public class source41 {
    public static void main(String[] args) {
        Map<String, Double> productPricePerQuantity = Map.of("Apple", 1.0, "Banana", 0.5, "Orange", 1.5);
        StorePricing storePricing = new StorePricing(productPricePerQuantity);
        StoreMemberPricing storeMemberPricing = new StoreMemberPricing(0.1);
        storeMemberPricing.printMemberDiscount();
        storePricing.printProductTypesAndPrice();
        ShoppingCart shoppingCart = new ShoppingCart();
        shoppingCart.addProduct("Apple", 2);
        shoppingCart.addProduct("Banana", 3);
        shoppingCart.addProduct("Orange", 1);
        double totalPrice = shoppingCart.calculateCartPrice(storePricing.getProductPricePerQuantity(), storePricing.getStoreDiscount(), storeMemberPricing.getMemberDiscount(), storeMemberPricing.getTax(), storePricing.getFees());
        System.out.println("Total Price: $" + totalPrice);
    }
}
