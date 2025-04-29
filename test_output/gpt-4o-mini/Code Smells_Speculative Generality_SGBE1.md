**Code Review: SGBE1.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - A method is too long or complex, which makes it hard to understand and maintain.
- Found in line no. - 20, 26, 37
- Possible treatments - ['Extract Method', 'Decompose Conditional']
- Possible solution - 
```java
abstract class AccomodationBad {
    abstract double bookAccomodation(int numDays);
    abstract void printAccomodationDetails();
}

class HotelBad extends AccomodationBad {
    private final String name;
    private final String address;
    private final double perDayCost;
    private int numDaysStay;

    public HotelBad(String name, String address, double perDayCost) {
        this.name = name;
        this.address = address;
        this.perDayCost = perDayCost;
        this.numDaysStay = 0;
    }

    @Override
    public double bookAccomodation(int numDays) {
        numDaysStay = numDays;
        return calculateTotalStayCost();
    }

    @Override
    public void printAccomodationDetails() {
        if (numDaysStay == 0) {
            printNotBookedMessage();
            return;
        }
        printDetails();
    }

    private void printNotBookedMessage() {
        System.out.println("Accomodation not booked yet");
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

public class SGBE1 {
    public static void main(String[] args) {
        HotelBad hotel = new HotelBad("Hotel ABC", "123 Main St", 100);
        double totalCost = hotel.bookAccomodation(5);
        System.out.println("Total cost of accomodation: " + totalCost);
        hotel.printAccomodationDetails();
    }
}
```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - Usage of primitive data types to represent domain concepts instead of creating class types for those concepts.
- Found in line no. - 10
- Possible treatments - ['Replace Data Value with Object']
- Possible solution - 
```java
abstract class AccomodationBad {
    abstract double bookAccomodation(StayDuration stayDuration);
    abstract void printAccomodationDetails();
}

class StayDuration {
    private int numDays;

    public StayDuration(int numDays) {
        this.numDays = numDays;
    }

    public int getNumDays() {
        return numDays;
    }
}

class HotelBad extends AccomodationBad {
    private final String name;
    private final String address;
    private final double perDayCost;
    private StayDuration stayDuration;

    public HotelBad(String name, String address, double perDayCost) {
        this.name = name;
        this.address = address;
        this.perDayCost = perDayCost;
        this.stayDuration = new StayDuration(0);
    }

    @Override
    public double bookAccomodation(StayDuration stayDuration) {
        this.stayDuration = stayDuration;
        return calculateTotalStayCost();
    }

    @Override
    public void printAccomodationDetails() {
        if (stayDuration.getNumDays() == 0) {
            printNotBookedMessage();
            return;
        }
        printDetails();
    }

    private void printNotBookedMessage() {
        System.out.println("Accomodation not booked yet");
    }

    private void printDetails() {
        System.out.println("Hotel Name: " + name);
        System.out.println("Hotel Address: " + address);
        System.out.println("Total Cost: " + calculateTotalStayCost());
        System.out.println("Number of days stay: " + stayDuration.getNumDays());
    }

    private double calculateTotalStayCost() {
        return Math.round(stayDuration.getNumDays() * perDayCost);
    }
}

public class SGBE1 {
    public static void main(String[] args) {
        HotelBad hotel = new HotelBad("Hotel ABC", "123 Main St", 100);
        double totalCost = hotel.bookAccomodation(new StayDuration(5));
        System.out.println("Total cost of accomodation: " + totalCost);
        hotel.printAccomodationDetails();
    }
}
```