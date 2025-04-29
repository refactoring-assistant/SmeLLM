**Code Review: SGGE1.java**

- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - The `printAccomodationDetails` method performs several operations, including a conditional check and multiple print statements, making it longer and harder to maintain.
- Found in line no. - [19-28]
- Possible treatments - ['Extract Method', 'Decompose Conditional']
- Possible solution - Refactor the `printAccomodationDetails` method to move some of its operations to separate methods, thereby reducing its length and improving maintainability.

```java
class HotelGood {
    private final String name;
    private final String address;
    private final double perDayCost;
    private int numDaysStay;

    public HotelGood(String name, String address, double perDayCost) {
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
        if (accomodationNotBooked()) {
            printNotBookedMessage();
        } else {
            printDetails();
        }
    }

    private void printNotBookedMessage() {
        System.out.println("Accommodation not booked yet");
    }

    private boolean accomodationNotBooked() {
        return numDaysStay == 0;
    }

    private void printDetails() {
        System.out.println("Hotel Name: " + name);
        System.out.println("Hotel Address: " + address);
        System.out.println("Total Cost: " + calculateTotalStayCost());
        System.out.println("Number of days stay: " + numDaysStay);
    }

    private double calculateTotalStayCost() {
        return Math.round(numDaysStay * perDayCost);
    }
}

public class SGGE1 {
    public static void main(String[] args) {
        HotelGood hotel = new HotelGood("Hotel ABC", "123 Main St", 100);
        double totalCost = hotel.bookAccomodation(5);
        System.out.println("Total cost of accommodation: " + totalCost);
        hotel.printAccomodationDetails();
    }
}
```

In this solution, the `printAccomodationDetails` method was decomposed into smaller methods to handle different parts of its functionality, specifically for checking if the accommodation was booked and printing the respective message or details.