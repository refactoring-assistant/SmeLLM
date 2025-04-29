```markdown
**Code Review: DCBE1.java**
    
- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - The `FlightBookingBad` class contains a large number of fields and methods, indicating that it may have too many responsibilities.
- Found in line no. - 3
- Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
- Possible solution - Break down the `FlightBookingBad` class into smaller classes to encapsulate logic related to customer details and flight details separately.

- Code smell no. - 2
- Code smell name - Long Parameter List
- Code smell description - Methods like `FlightBookingBad` constructor and update methods have a long list of parameters which makes it difficult to understand and refactor.
- Found in line no. - 15, 28, 38, 46
- Possible treatments - ['Replace Parameter with Method Call', 'Preserve Whole Object', 'Introduce Parameter Object']
- Possible solution - Use objects to encapsulate parameters or utilize setter methods to reduce parameter list.

- Code smell no. - 3
- Code smell name - Data Clumps
- Code smell description - Repeated use of customer details parameters (`customerFirstName`, `customerLastName`, `customerEmail`, `customerNumber`, `PNR`) indicates that these are likely to be grouped together.
- Found in line no. - 15, 28, 38, 46
- Possible treatments - ['Extract Class', 'Introduce Parameter Object', 'Preserve Whole Object']
- Possible solution - Encapsulate customer-related data into a separate class named `Customer` and use instances of this class in the `FlightBookingBad` class.

- Code smell no. - 4
- Code smell name - Duplicate Code
- Code smell description - Similar logic is repeated in several update methods regarding parameter checking with `if` condition.
- Found in line no. - 30, 39, 47
- Possible treatments - ['Extract Method', 'Extract Method & Pull Up Field', 'Pull Up Constructor Body', 'Form Template Method', 'Substitute Algorithm', 'Extract Superclass', 'Extract ClassConsolidate Conditional Expression and use Extract Method', 'Consolidate Duplicate Conditional Fragments']
- Possible solution - Create a private method to confirm matching customer identification parameters and use it within each of the update methods to remove redundancy.

```java
import java.time.LocalDate;

class Customer {
    private String firstName;
    private String lastName;
    private String email;
    private String number;
    private String PNR;

    public Customer(String firstName, String lastName, String email, String number, String PNR) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.number = number;
        this.PNR = PNR;
    }

    public boolean matches(String firstName, String lastName, String PNR) {
        return this.firstName.equals(firstName) && this.lastName.equals(lastName) && this.PNR.equals(PNR);
    }

    public void updateContacts(String email, String number) {
        this.email = email;
        this.number = number;
    }

    public void printDetails() {
        System.out.println("Customer Name: " + firstName + " " + lastName);
        System.out.println("Customer Email: " + email);
        System.out.println("Customer Number: " + number);
        System.out.println("PNR: " + PNR);
    }
}

class FlightInfo {
    private String flightNumber;
    private String origin;
    private String returnOrigin;
    private LocalDate originDate;
    private LocalDate returnOriginDate;

    public FlightInfo(String flightNumber, String origin, String returnOrigin, LocalDate originDate, LocalDate returnOriginDate) {
        this.flightNumber = flightNumber;
        this.origin = origin;
        this.returnOrigin = returnOrigin;
        this.originDate = originDate;
        this.returnOriginDate = returnOriginDate;
    }

    public void updateOrigin(String origin, LocalDate originDate) {
        this.origin = origin;
        this.originDate = originDate;
    }

    public void updateReturnOrigin(String returnOrigin, LocalDate returnOriginDate) {
        this.returnOrigin = returnOrigin;
        this.returnOriginDate = returnOriginDate;
    }

    public void printFlightDetails() {
        System.out.println("Flight Number: " + flightNumber);
        System.out.println("Origin: " + origin);
        System.out.println("Return Origin: " + returnOrigin);
        System.out.println("Origin Date: " + originDate);
        System.out.println("Return Origin Date: " + returnOriginDate);
    }
}

class FlightBooking {
    private Customer customer;
    private FlightInfo flightInfo;

    public FlightBooking(Customer customer, FlightInfo flightInfo) {
        this.customer = customer;
        this.flightInfo = flightInfo;
    }

    public void updateCustomerContactDetails(String firstName, String lastName, String PNR, String email, String number) {
        if (!customer.matches(firstName, lastName, PNR)) {
            throw new IllegalArgumentException("Cannot update contact. Customer details do not match.");
        }
        customer.updateContacts(email, number);
    }

    public void updateOriginDetails(String firstName, String lastName, String PNR, String origin, LocalDate originDate) {
        if (!customer.matches(firstName, lastName, PNR)) {
            throw new IllegalArgumentException("Cannot update origin. Customer details do not match.");
        }
        flightInfo.updateOrigin(origin, originDate);
    }

    public void updateReturnOriginDetails(String firstName, String lastName, String PNR, String returnOrigin, LocalDate returnOriginDate) {
        if (!customer.matches(firstName, lastName, PNR)) {
            throw new IllegalArgumentException("Cannot update return. Customer details do not match.");
        }
        flightInfo.updateReturnOrigin(returnOrigin, returnOriginDate);
    }

    public void printFlightDetails() {
        customer.printDetails();
        flightInfo.printFlightDetails();
    }
}

public class DCBE1 {
    public static void main(String[] args) {
        LocalDate originDate = LocalDate.of(2025, 1, 1);
        LocalDate returnOriginDate = LocalDate.of(2025, 1, 10);
        LocalDate newOriginDate = LocalDate.of(2025, 1, 2);
        LocalDate newReturnOriginDate = LocalDate.of(2025, 1, 11);

        Customer customer = new Customer("John", "Doe", "email@email.com", "1234567890", "PNR123");
        FlightInfo flightInfo = new FlightInfo("AI123", "DEL", "BOM", originDate, returnOriginDate);
        FlightBooking flightBooking = new FlightBooking(customer, flightInfo);

        try {
            flightBooking.updateCustomerContactDetails("John", "Doe", "PNR123", "email2@email.com", "1234567890");
            flightBooking.updateOriginDetails("John", "Doe", "PNR123", "DEL", newOriginDate);
            flightBooking.updateReturnOriginDetails("John", "Doe", "PNR123", "BOM", newReturnOriginDate);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        flightBooking.printFlightDetails();
    }
}
```
```