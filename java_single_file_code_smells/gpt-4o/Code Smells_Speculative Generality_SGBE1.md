**Code Review: SGBE1.java**
  - Code smell no. - 1
  - Code smell name - Long Method
  - Code smell description - A method that is too long can be hard to understand and maintain. It is often a sign that a class is trying to do too much.
  - Found in line no. - [26-35]
  - Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
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
            if(numDaysStay == 0) {
                System.out.println("Accomodation not booked yet");
                return;
            }
            printFormattedDetails();
        }

        private void printFormattedDetails() {
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
  - Code smell description - This occurs when you are using primitives for particular purposes without creating a dedicated data structure or class.
  - Found in line no. - [7, 8, 9, 10]
  - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', ' Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
  - Possible solution - 
    ```java
    abstract class AccomodationBad {
        abstract double bookAccomodation(int numDays);
        abstract void printAccomodationDetails();
    }

    class HotelDetails {
        private final String name;
        private final String address;
        private final double perDayCost;
        
        public HotelDetails(String name, String address, double perDayCost) {
            this.name = name;
            this.address = address;
            this.perDayCost = perDayCost;
        }

        public String getName() {
            return name;
        }

        public String getAddress() {
            return address;
        }

        public double getPerDayCost() {
            return perDayCost;
        }
    }

    class HotelBad extends AccomodationBad {
        private final HotelDetails details;
        private int numDaysStay;

        public HotelBad(HotelDetails details) {
            this.details = details;
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
            printFormattedDetails();
        }

        private void printFormattedDetails() {
            System.out.println("Hotel Name: " + details.getName());
            System.out.println("Hotel Address: " + details.getAddress());
            System.out.println("Total Cost: " + calculateTotalStayCost());
            System.out.println("Number of days stay: " + numDaysStay);
        }

        private double calculateTotalStayCost() {
            return Math.round(numDaysStay * details.getPerDayCost());
        }
    }

    public class SGBE1 {
        public static void main(String[] args) {
            HotelDetails hotelDetails = new HotelDetails("Hotel ABC", "123 Main St", 100);
            HotelBad hotel = new HotelBad(hotelDetails);
            double totalCost = hotel.bookAccomodation(5);
            System.out.println("Total cost of accomodation: " + totalCost);
            hotel.printAccomodationDetails();
        }
    }
    ```