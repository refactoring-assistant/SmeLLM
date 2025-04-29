```markdown
**Code Review: SGBE1.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The code uses primitive data types for representing complex entities (e.g., accommodation details).
- Found in line no. - 12, 13, 14
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - Create a class to encapsulate accommodation properties such as name, address, and per day cost.

```java
abstract class Accomodation {
    abstract double bookAccomodation(int numDays);
    abstract void printAccomodationDetails();
}

class Hotel {
    private final String name;
    private final String address;
    private final double perDayCost;

    public Hotel(String name, String address, double perDayCost) {
        this.name = name;
        this.address = address;
        this.perDayCost = perDayCost;
    }

    public String getName() { return name; }
    public String getAddress() { return address; }
    public double getPerDayCost() { return perDayCost; }
}

class HotelBooking extends Accomodation {
    private Hotel hotel;
    private int numDaysStay;

    public HotelBooking(Hotel hotel) {
        this.hotel = hotel;
        this.numDaysStay = 0;
    }

    @Override
    public double bookAccomodation(int numDays) {
        numDaysStay = numDays;
        return calculateTotalStayCost();
    }

    @Override
    public void printAccomodationDetails() {
        if(numDaysStay == 0) {
            System.out.println("Accomodation not booked yet");
            return;
        }
        System.out.println("Hotel Name: " + hotel.getName());
        System.out.println("Hotel Address: " + hotel.getAddress());
        System.out.println("Total Cost: " + calculateTotalStayCost());
        System.out.println("Number of days stay: " + numDaysStay);
    }

    private double calculateTotalStayCost() {
        return Math.round(numDaysStay * hotel.getPerDayCost());
    }
}

public class SGBE1 {
    public static void main(String[] args) {
        Hotel hotel = new Hotel("Hotel ABC", "123 Main St", 100);
        HotelBooking booking = new HotelBooking(hotel);
        double totalCost = booking.bookAccomodation(5);
        System.out.println("Total cost of accomodation: " + totalCost);
        booking.printAccomodationDetails();
    }
}
```
```
