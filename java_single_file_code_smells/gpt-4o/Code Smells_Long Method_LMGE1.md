**Code Review: LMGE1.java**
  - Code smell no. - 1
  - Code smell name - Switch Statements
  - Code smell description - The code uses a switch statement to determine the transaction status, which can lead to duplication or become error-prone when new cases need to be added.
  - Found in line no. - 155
  - Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', ' Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
  - Possible solution - Use polymorphism to handle transaction statuses and their corresponding print messages instead of using a switch case.

```java
interface TransactionStatusHandler {
    void printStatus();
}

class SuccessStatusHandler implements TransactionStatusHandler {
    @Override
    public void printStatus() {
        System.out.println("Transaction successful.");
    }
}

class FailureStatusHandler implements TransactionStatusHandler {
    @Override
    public void printStatus() {
        System.out.println("Transaction failed.");
    }
}

class PendingStatusHandler implements TransactionStatusHandler {
    @Override
    public void printStatus() {
        System.out.println("Transaction pending.");
    }
}

public class LMGE1 {
    public static void main(String[] args) {
        Date expiryDate = new Date();
        CardDetailsGood cardDetails = new CardDetailsGood("1234567890123456", "John Doe", expiryDate, 123);
        CreditCardGood card = new CreditCardGood(cardDetails);
        TransactionGood transactionSuccess = card.makeTransaction(1000, cardDetails, new Date());
        printTransactionStatus(transactionSuccess);
    }
  
    private static void printTransactionStatus(TransactionGood transaction) {
        TransactionStatusHandler handler = getStatusHandler(transaction.getStatus());
        handler.printStatus();
    }
  
    private static TransactionStatusHandler getStatusHandler(TransactionStatusGood status) {
        switch (status) {
            case SUCCESS:
                return new SuccessStatusHandler();
            case FAILURE:
                return new FailureStatusHandler();
            case PENDING:
                return new PendingStatusHandler();
            default:
                throw new IllegalArgumentException("Unknown status: " + status);
        }
    }
}
```

  - Code smell no. - 2
  - Code smell name - Primitive Obsession
  - Code smell description - The class `CardDetailsGood` uses multiple primitive fields which could be better represented as objects for clarity and encapsulation.
  - Found in line no. - 23, 24, 26
  - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', ' Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
  - Possible solution - Replace card number, holder name and CVV with more specific classes or objects.

```java
class CardNumber {
    private final String number;

    public CardNumber(String number) {
        this.number = number;
    }

    public String getNumber() {
        return number;
    }

    // Implement equals and hashCode methods based on number field
}

class CardHolder {
    private final String name;

    public CardHolder(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    // Implement equals and hashCode methods based on name field
}

class CVV {
    private final int cvv;

    public CVV(int cvv) {
        this.cvv = cvv;
    }

    public int getCVV() {
        return cvv;
    }

    // Implement equals and hashCode methods based on cvv field
}

class CardDetailsGood {
    private final CardNumber cardNumber;
    private final CardHolder cardHolder;
    private final Date expiryDate;
    private final CVV cvv;

    public CardDetailsGood(CardNumber cardNumber, CardHolder cardHolder, Date expiryDate, CVV cvv) {
        this.cardNumber = cardNumber;
        this.cardHolder = cardHolder;
        this.expiryDate = expiryDate;
        this.cvv = cvv;
    }

    public boolean equals(CardDetailsGood cardDetails) {
        return cardNumber.equals(cardDetails.cardNumber) && cardHolder.equals(cardDetails.cardHolder)
                && expiryDate.equals(cardDetails.expiryDate) && cvv.equals(cardDetails.cvv);
    }
}
```