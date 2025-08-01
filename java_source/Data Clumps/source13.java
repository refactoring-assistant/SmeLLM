import java.time.LocalDate;

class Contact {
  private String customerEmail;
  private String customerNumber;

  public Contact(String customerEmail, String customerNumber) {
    this.customerEmail = customerEmail;
    this.customerNumber = customerNumber;
  }

  public void updateContactDetails(Contact contactOther) {
    this.customerEmail = contactOther.customerEmail;
    this.customerNumber = contactOther.customerNumber;
  }

  public void printContactDetails() {
    System.out.println("Customer Email: " + customerEmail);
    System.out.println("Customer Number: " + customerNumber);
  }
}

class Customer {
    private String customerFirstName;
    private String customerLastName;
    private Contact contact;

    public Customer(String customerFirstName, String customerLastName, Contact contact) {
        this.customerFirstName = customerFirstName;
        this.customerLastName = customerLastName;
        this.contact = contact;
    }

    public boolean verifyCustomerName(Customer customerOther) {
        return this.customerFirstName.equals(customerOther.customerFirstName) && this.customerLastName.equals(customerOther.customerLastName);
    }

    public void updateContactDetails(Contact contactOther) {
        this.contact.updateContactDetails(contactOther);
    }

    public void printCustomerDetails() {
        System.out.println("Customer Name: " + customerFirstName + " " + customerLastName);
        contact.printContactDetails();
    }
}
class BookingReference {
  private Customer customer;

  private String PNR;

  public BookingReference(Customer customer, String PNR) {
      this.customer = customer;
      this.PNR = PNR;
  }

  public boolean verifyBooking(BookingReference bookingDetails) {
      return this.PNR.equals(bookingDetails.PNR) && this.customer.verifyCustomerName(bookingDetails.customer);
  }

  public void updateContactDetails(Contact contactOther) {
    this.customer.updateContactDetails(contactOther);
  }

  public void printBookingDetails() {
    customer.printCustomerDetails();
    System.out.println("PNR: " + PNR);
  }
}
class TravelPlace {
  private String placeName;
  private LocalDate flightDate;

  public TravelPlace(String placeName, LocalDate flightDate) {
    this.placeName = placeName;
    this.flightDate = flightDate;
  }

  public void printTravelDetails() {
    System.out.println("Place Name: " + placeName);
    System.out.println("Flight Date: " + flightDate);
  }
}

class FlightBooking {
  private BookingReference bookingDetails;
  private String flightNumber;
  private TravelPlace origin;
  private TravelPlace returnOrigin;

  public FlightBooking(BookingReference bookingDetails, String flightNumber, TravelPlace origin, TravelPlace returnOrigin) {
    this.bookingDetails = bookingDetails;
    this.flightNumber = flightNumber;
    this.origin = origin;
    this.returnOrigin = returnOrigin;
  }

  public void updateCustomerContactDetails(BookingReference bookingOther, Contact contactOther) {

    if(!verifyBookingReference(bookingOther)) {
      throw new IllegalArgumentException("Cannot update contact. Customer details do not match.");
    }

    bookingDetails.updateContactDetails(contactOther);
  }

  public void updateOriginDetails(BookingReference bookingOther, TravelPlace originOther) {
    if(!verifyBookingReference(bookingOther)) {
      throw new IllegalArgumentException("Cannot update origin. Customer details do not match.");
    }

    this.origin = originOther;
  }

  public void updateReturnOriginDetails(BookingReference bookingOther, TravelPlace returnOriginOther) {
    if(!verifyBookingReference(bookingOther)) {
      throw new IllegalArgumentException("Cannot update return. Customer details do not match.");
    }
    this.returnOrigin = returnOriginOther;
  }

  public void printFlightDetails() {
    bookingDetails.printBookingDetails();
    System.out.println("Flight Number: " + flightNumber);
    System.out.println("Origin Details:");
    origin.printTravelDetails();
    System.out.println("Return Details:");
    returnOrigin.printTravelDetails();
  }

  private boolean verifyBookingReference(BookingReference bookingOther) {
    return this.bookingDetails.verifyBooking(bookingOther);
  }
}
public class source13 {
  public static void main(String[] args) {
    LocalDate originDate = LocalDate.of(2025, 1, 1);
    LocalDate returnOriginDate = LocalDate.of(2025, 1, 10);
    LocalDate newOriginDate = LocalDate.of(2025, 1, 2);
    LocalDate newReturnOriginDate = LocalDate.of(2025, 1, 11);
    Contact contact1 = new Contact("email@email.com", "1234567890");
    Contact contact2 = new Contact("email2@email.com", "1234567890");
    Customer customer = new Customer("John", "Doe", contact1);
    BookingReference booking = new BookingReference(customer, "PNR123");
    TravelPlace origin1 = new TravelPlace("DEL", originDate);
    TravelPlace returnOrigin1 = new TravelPlace("BOM", returnOriginDate);
    TravelPlace origin2 = new TravelPlace("DEL", newOriginDate);
    TravelPlace returnOrigin2 = new TravelPlace("BOM", newReturnOriginDate);
    FlightBooking flightBooking = new FlightBooking(booking, "AI123", origin1, returnOrigin1);

    try {
      flightBooking.updateCustomerContactDetails(booking, contact2);
      flightBooking.updateOriginDetails(booking, origin2);
      flightBooking.updateReturnOriginDetails(booking, returnOrigin2);
      flightBooking.printFlightDetails();
    } catch (IllegalArgumentException e) {
      System.out.println(e.getMessage());
    }
  }
}
