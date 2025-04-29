**Code Review: SGGE1.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The code uses primitives for attributes like `name`, `address`, and `perDayCost` which can lead to less maintainable code when additional functionality or validation is added to these attributes in the future.
- Found in line no. - 2, 3, 4
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', ' Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - Create separate classes for `Name`, `Address`, and `Cost` to encapsulate these primitives.

**Redefined Code:**
```java
class HotelGood {
    private final HotelName name;
    private final Address address;
    private final Cost perDayCost;
    private int numDaysStay;

    public HotelGood(HotelName name, Address address, Cost perDayCost) {
        this.name = name;
        this.address = address;
        this.perDayCost = perDayCost;
        this.numDaysStay = 0;
    }

    public double bookAccomodation(int numDays) {
        numDaysStay = numDays;
        return calculateTotalStayCost();
    }

    public void printAccomodationDetails() {
        if(numDaysStay == 0) {
            System.out.println("Accomodation not booked yet");
            return;
        }
        System.out.println("Hotel Name: " + name.getValue());
        System.out.println("Hotel Address: " + address.getValue());
        System.out.println("Total Cost: " + calculateTotalStayCost());
        System.out.println("Number of days stay: " + numDaysStay);
    }

    private double calculateTotalStayCost() {
        return Math.round(numDaysStay * perDayCost.getValue());
    }
}

class HotelName {
    private final String value;

    public HotelName(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }
}

class Address {
    private final String value;

    public Address(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }
}

class Cost {
    private final double value;

    public Cost(double value) {
        this.value = value;
    }

    public double getValue() {
        return value;
    }
}

public class SGGE1 {
    public static void main(String[] args) {
        HotelName hotelName = new HotelName("Hotel ABC");
        Address address = new Address("123 Main St");
        Cost cost = new Cost(100);
        
        HotelGood hotel = new HotelGood(hotelName, address, cost);
        double totalCost = hotel.bookAccomodation(5);
        System.out.println("Total cost of accomodation: " + totalCost);
        hotel.printAccomodationDetails();
    }
}
```