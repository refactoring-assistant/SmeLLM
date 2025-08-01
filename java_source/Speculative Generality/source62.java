abstract class Accomodation {
  abstract double bookAccomodation(int numDays);
  abstract void printAccomodationDetails();
}

class Hotel extends Accomodation {
 private final String name;
 private final String address;
 private final double perDayCost;
 private int numDaysStay;

    public Hotel(String name, String address, double perDayCost) {
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
     if(numDaysStay == 0) {
        System.out.println("Accomodation not booked yet");
        return;
     }
       System.out.println("Hotel Name: " + name);
       System.out.println("Hotel Address: " + address);
       System.out.println("Total Cost: " + calculateTotalStayCost());
       System.out.println("Number of days stay: " + numDaysStay);
    }

    private double calculateTotalStayCost() {
        return Math.round(numDaysStay * perDayCost);
    }
}
public class source62 {
 public static void main(String[] args) {
  Hotel hotel = new Hotel("Hotel ABC", "123 Main St", 100);
    double totalCost = hotel.bookAccomodation(5);
    System.out.println("Total cost of accomodation: " + totalCost);
    hotel.printAccomodationDetails();
 }
}
