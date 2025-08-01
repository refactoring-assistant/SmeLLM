import java.time.LocalDate;

class FlightBooking {
  private String customerFirstName;
  private String customerLastName;
  private String customerEmail;
  private String customerNumber;
  private String PNR;
  private String flightNumber;
  private String origin;
  private String returnOrigin;
  private LocalDate originDate;
  private LocalDate returnOriginDate;

    public FlightBooking(String customerFirstName, String customerLastName, String customerEmail, String customerNumber, String PNR, String flightNumber, String origin, String returnOrigin, LocalDate originDate, LocalDate returnOriginDate) {
        this.customerFirstName = customerFirstName;
        this.customerLastName = customerLastName;
        this.customerEmail = customerEmail;
        this.customerNumber = customerNumber;
        this.PNR = PNR;
        this.flightNumber = flightNumber;
        this.origin = origin;
        this.returnOrigin = returnOrigin;
        this.originDate = originDate;
        this.returnOriginDate = returnOriginDate;
    }

    public void updateCustomerContactDetails(String customerFirstName, String customerLastName, String PNR, String customerEmail, String customerNumber) {

        if(!this.customerFirstName.equals(customerFirstName) || !this.customerLastName.equals(customerLastName) || !this.PNR.equals(PNR)) {
            throw new IllegalArgumentException("Cannot update contact. Customer details do not match.");
        }

        this.customerEmail = customerEmail;
        this.customerNumber = customerNumber;
    }

    public void updateOriginDetails(String customerFirstName, String customerLastName, String PNR, String origin, LocalDate originDate) {
        if(!this.customerFirstName.equals(customerFirstName) || !this.customerLastName.equals(customerLastName) || !this.PNR.equals(PNR)) {
          throw new IllegalArgumentException("Cannot update origin. Customer details do not match.");
        }
        this.origin = origin;
        this.originDate = originDate;
    }

    public void updateReturnOriginDetails(String customerFirstName, String customerLastName, String PNR, String returnOrigin, LocalDate returnOriginDate) {
        if(!this.customerFirstName.equals(customerFirstName) || !this.customerLastName.equals(customerLastName) || !this.PNR.equals(PNR)) {
          throw new IllegalArgumentException("Cannot update return. Customer details do not match.");
        }
        this.returnOrigin = returnOrigin;
        this.returnOriginDate = returnOriginDate;
    }

    public void printFlightDetails() {
        System.out.println("Customer Name: " + customerFirstName + " " + customerLastName);
        System.out.println("Customer Email: " + customerEmail);
        System.out.println("Customer Number: " + customerNumber);
        System.out.println("PNR: " + PNR);
        System.out.println("Flight Number: " + flightNumber);
        System.out.println("Origin: " + origin);
        System.out.println("Return Origin: " + returnOrigin);
        System.out.println("Origin Date: " + originDate);
        System.out.println("Return Origin Date: " + returnOriginDate);
    }

}

public class source10 {
  public static void main(String[] args) {
    LocalDate originDate = LocalDate.of(2025, 1, 1);
    LocalDate returnOriginDate = LocalDate.of(2025, 1, 10);
    LocalDate newOriginDate = LocalDate.of(2025, 1, 2);
    LocalDate newReturnOriginDate = LocalDate.of(2025, 1, 11);
    FlightBooking flightBooking = new FlightBooking("John", "Doe", "email@email.com", "1234567890", "PNR123", "AI123", "DEL", "BOM", originDate, returnOriginDate);
    try {
      flightBooking.updateCustomerContactDetails("John", "Doe", "PNR123", "email2@email.com" , "1234567890");
      flightBooking.updateOriginDetails("John", "Doe", "PNR123", "DEL", newOriginDate);
      flightBooking.updateReturnOriginDetails("John", "Doe", "PNR123", "BOM", newReturnOriginDate);;
    }
    catch (IllegalArgumentException e) {
      System.out.println(e.getMessage());
    }
    flightBooking.printFlightDetails();

  }
}