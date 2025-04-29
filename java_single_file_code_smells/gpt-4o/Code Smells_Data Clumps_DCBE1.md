**Code Review: DCBE1.java**

- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - A class contains many fields/methods that can make the class difficult to manage and understand, indicating it might be trying to do too much.
- Found in line no. - [3-66]
- Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
- Possible solution - Break down the `FlightBookingBad` class into smaller, more cohesive classes. For example, create separate classes for `CustomerDetails`, `FlightDetails`, and `BookingDetails` to encapsulate related fields and methods.

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - Using primitives to represent domain ideas like customers, airports, etc., which can lead to poor code organization and extensibility.
- Found in line no. - [4-13, 15-25]
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - Replace Strings representing customer and flight information with classes such as `Customer`, `Flight`, and `Location`.

- Code smell no. - 3
- Code smell name - Long Parameter List
- Code smell description - Methods have too many parameters, making them hard to read and prone to errors when calling.
- Found in line no. - [15, 28, 38, 46]
- Possible treatments - ['Replace Parameter with Method Call', 'Preserve Whole Object', 'Introduce Parameter Object']
- Possible solution - Create parameter objects like `CustomerDetails`, `FlightDetails`, and use these in method signatures to reduce the number of parameters.

- Code smell no. - 4
- Code smell name - Duplicate Code
- Code smell description - Similar or identical code present in multiple locations leading to higher maintenance efforts.
- Found in line no. - [30-41, 47-49]
- Possible treatments - ['Extract Method', 'Extract Method & Pull Up Field', 'Pull Up Constructor Body', 'Form Template Method', 'Substitute Algorithm', 'Extract Superclass', 'Extract ClassConsolidate Conditional Expression and use Extract Method', 'Consolidate Duplicate Conditional Fragments']
- Possible solution - Refactor validation logic into a separate method to avoid duplication in the `updateCustomerContactDetails`, `updateOriginDetails`, and `updateReturnOriginDetails` methods.

```java
import java.time.LocalDate;

class Customer {
    private String firstName;
    private String lastName;
    private String email;
    private String phoneNumber;

    // Constructor, getters, setters, and other customer-related methods
}

class Flight {
    private String flightNumber;
    private String origin;
    private String destination;
    private LocalDate departureDate;
    private LocalDate returnDate;

    // Constructor, getters, setters, and other flight-related methods
}

class BookingDetails {
    private Customer customer;
    private Flight flight;
    private String PNR;

    public BookingDetails(Customer customer, Flight flight, String PNR) {
        this.customer = customer;
        this.flight = flight;
        this.PNR = PNR;
    }

    private void validateCustomerDetails(String firstName, String lastName, String PNR) {
        if (!this.customer.getFirstName().equals(firstName) || !this.customer.getLastName().equals(lastName) || !this.PNR.equals(PNR)) {
            throw new IllegalArgumentException("Invalid customer details.");
        }
    }

    public void updateCustomerContactDetails(String firstName, String lastName, String PNR, String email, String phoneNumber) {
        validateCustomerDetails(firstName, lastName, PNR);
        customer.setEmail(email);
        customer.setPhoneNumber(phoneNumber);
    }

    public void updateFlightOrigin(String firstName, String lastName, String PNR, String origin, LocalDate departureDate) {
        validateCustomerDetails(firstName, lastName, PNR);
        flight.setOrigin(origin);
        flight.setDepartureDate(departureDate);
    }

    public void printBookingDetails() {
        System.out.println("Customer Name: " + customer.getFirstName() + " " + customer.getLastName());
        System.out.println("Customer Email: " + customer.getEmail());
        System.out.println("Customer Number: " + customer.getPhoneNumber());
        System.out.println("PNR: " + PNR);
        System.out.println("Flight Number: " + flight.getFlightNumber());
        System.out.println("Origin: " + flight.getOrigin());
        System.out.println("Departure Date: " + flight.getDepartureDate());
    }
}

public class DCBE1 {
    public static void main(String[] args) {
        LocalDate originDate = LocalDate.of(2025, 1, 1);
        LocalDate returnDate = LocalDate.of(2025, 1, 10);
        Customer customer = new Customer("John", "Doe", "email@mail.com", "1234567890");
        Flight flight = new Flight("AI123", "DEL", "BOM", originDate, returnDate);

        BookingDetails booking = new BookingDetails(customer, flight, "PNR123");

        try {
            booking.updateCustomerContactDetails("John", "Doe", "PNR123", "newemail@mail.com", "0987654321");
            booking.updateFlightOrigin("John", "Doe", "PNR123", "DEL", LocalDate.of(2025, 1, 2));
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

        booking.printBookingDetails();
    }
}
```