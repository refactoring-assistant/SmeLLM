**Code Review: DCGE1.java**
- Code smell no. - 1
- Code smell name - Long Parameter List
- Code smell description - Methods and constructors take many parameters, which can make them difficult to work with and understand.
- Found in line no. - [28, 52, 91]
- Possible treatments - ['Replace Parameter with Method Call', 'Preserve Whole Object', 'Introduce Parameter Object']
- Possible solution -
    - Create objects that encapsulate the parameters or use existing classes to reduce the number of parameters passed.

```java
import java.time.LocalDate;

class Contact {
    private String email;
    private String number;

    public Contact(String email, String number) {
        this.email = email;
        this.number = number;
    }

    public void update(Contact other) {
        this.email = other.email;
        this.number = other.number;
    }

    public void print() {
        System.out.println("Email: " + email);
        System.out.println("Number: " + number);
    }
}

class Customer {
    private String firstName;
    private String lastName;
    private Contact contact;

    public Customer(String firstName, String lastName, Contact contact) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.contact = contact;
    }

    public boolean verify(Customer other) {
        return this.firstName.equals(other.firstName) && this.lastName.equals(other.lastName);
    }

    public void updateContact(Contact other) {
        this.contact.update(other);
    }

    public void print() {
        System.out.println("Name: " + firstName + " " + lastName);
        contact.print();
    }
}

class BookingReference {
    private Customer customer;
    private String pnr;

    public BookingReference(Customer customer, String pnr) {
        this.customer = customer;
        this.pnr = pnr;
    }

    public boolean verify(BookingReference other) {
        return this.pnr.equals(other.pnr) && this.customer.verify(other.customer);
    }

    public void updateContact(Contact other) {
        this.customer.updateContact(other);
    }

    public void print() {
        customer.print();
        System.out.println("PNR: " + pnr);
    }
}

class TravelPlace {
    private String placeName;
    private LocalDate date;

    public TravelPlace(String placeName, LocalDate date) {
        this.placeName = placeName;
        this.date = date;
    }

    public void print() {
        System.out.println("Place: " + placeName);
        System.out.println("Date: " + date);
    }
}

class FlightBooking {
    private BookingReference booking;
    private String flightNumber;
    private TravelPlace origin;
    private TravelPlace returnPlace;

    public FlightBooking(BookingReference booking, String flightNumber, TravelPlace origin, TravelPlace returnPlace) {
        this.booking = booking;
        this.flightNumber = flightNumber;
        this.origin = origin;
        this.returnPlace = returnPlace;
    }

    public void updateContact(BookingReference bookingOther, Contact otherContact) {
        if (!verify(bookingOther)) {
            throw new IllegalArgumentException("Cannot update contact. Details do not match.");
        }
        booking.updateContact(otherContact);
    }

    public void updateOrigin(BookingReference bookingOther, TravelPlace newOrigin) {
        if (!verify(bookingOther)) {
            throw new IllegalArgumentException("Cannot update origin. Details do not match.");
        }
        this.origin = newOrigin;
    }

    public void updateReturn(BookingReference bookingOther, TravelPlace newReturn) {
        if (!verify(bookingOther)) {
            throw new IllegalArgumentException("Cannot update return. Details do not match.");
        }
        this.returnPlace = newReturn;
    }

    public void print() {
        booking.print();
        System.out.println("Flight Number: " + flightNumber);
        System.out.println("Origin: ");
        origin.print();
        System.out.println("Return: ");
        returnPlace.print();
    }

    private boolean verify(BookingReference other) {
        return this.booking.verify(other);
    }
}

public class DCGE1 {
    public static void main(String[] args) {
        LocalDate originDate = LocalDate.of(2025, 1, 1);
        LocalDate returnDate = LocalDate.of(2025, 1, 10);

        Contact contact1 = new Contact("email@email.com", "1234567890");
        Contact contact2 = new Contact("email2@email.com", "0987654321");

        Customer customer = new Customer("John", "Doe", contact1);

        BookingReference booking = new BookingReference(customer, "PNR123");

        TravelPlace origin = new TravelPlace("DEL", originDate);
        TravelPlace returnPlace = new TravelPlace("BOM", returnDate);

        FlightBooking flight = new FlightBooking(booking, "AI123", origin, returnPlace);

        try {
            flight.updateContact(booking, contact2);
            flight.updateOrigin(booking, new TravelPlace("DEL", LocalDate.of(2025, 1, 2)));
            flight.updateReturn(booking, new TravelPlace("BOM", LocalDate.of(2025, 1, 11)));
            flight.print();
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

This approach introduces small changes to effectively reduce parameter list lengths without altering the core functionality. It enhances readability and maintains simplicity in method invocation by encapsulating related data within objects.