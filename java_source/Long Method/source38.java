
import java.util.ArrayDeque;
import java.util.Date;
import java.util.Deque;

enum Status {
  ACTIVE,
  INACTIVE
}

enum Standing {
  GOOD,
  BAD
}

enum TransactionStatus {
  SUCCESS,
  FAILURE,
  PENDING
}

class CardDetails {
    private final String cardNumber;
    private final String cardHolder;
    private final Date expiryDate;
    private final int cvv;

    public CardDetails(String cardNumber, String cardHolder, Date expiryDate, int cvv) {
        this.cardNumber = cardNumber;
        this.cardHolder = cardHolder;
        this.expiryDate = expiryDate;
        this.cvv = cvv;
    }

    public boolean equals(CardDetails cardDetails) {
        return cardNumber.equals(cardDetails.cardNumber) && cardHolder.equals(cardDetails.cardHolder) && expiryDate.equals(cardDetails.expiryDate) && cvv == cardDetails.cvv;
    }
}

class Transaction {
  private String txnId;
  private float amount;
  private Date date;
  private TransactionStatus status;

  public Transaction(String txnId, float amount, Date date) {
    this.txnId = txnId;
    this.amount = amount;
    this.date = date;
    this.status = TransactionStatus.PENDING;
  }

  public void updateStatus(TransactionStatus status) {
    this.status = status;
  }

  public TransactionStatus getStatus() {
    return this.status;
  }

  public  void printTransactionDetails() {
    System.out.println("TransactionBad ID: " + txnId);
    System.out.println("Amount: " + amount);
    System.out.println("Date: " + date);
    System.out.println("Status: " + status);
}
}

class CreditCard {
  private CardDetails cardDetails;
  private float creditLimit;
  private float availableBalance;
  private Status status;
  private Standing standing;
  private Deque<Transaction> txnHistory;

  public CreditCard(CardDetails cardDetails) {
    this.cardDetails = cardDetails;
    this.creditLimit = 10000f;
    this.availableBalance = 10000f;
    this.status = Status.ACTIVE;
    this.standing = Standing.GOOD;
    txnHistory = new ArrayDeque<>();
  }

  public Transaction makeTransaction(float amount, CardDetails cardDetails, Date transactionDate) {
    String txnId = "TXN" + (int) (Math.random() * 1000);
    Transaction txn = new Transaction(txnId, amount, transactionDate);
    TransactionStatus transactionStatus = checkTransactionValidity(amount, cardDetails);

    if(transactionStatus == TransactionStatus.SUCCESS) {
      performTransaction(amount);
    }

    txn.updateStatus(transactionStatus);
    txnHistory.push(txn);
    return txn;
  }

  private void performTransaction(float amount) {
    availableBalance -= amount;
    System.out.println("Transaction successful. Available balance: " + availableBalance);
  }

  private TransactionStatus checkTransactionValidity(float amount, CardDetails cardDetails) {
    if(!verifyCardDetails(cardDetails) || !checkAccountStandingAndStatus() || !checkTransactionAmountWithinLimit(amount)) {
      return TransactionStatus.FAILURE;
    }
    return TransactionStatus.SUCCESS;
  }

  private boolean verifyCardDetails(CardDetails cardDetails) {
    if(!cardDetails.equals(this.cardDetails)) {
      System.out.println("Invalid card details. Please check and try again.");
        return false;
    }
    return true;
  }

  private boolean checkAccountStandingAndStatus() {
    if(status == Status.INACTIVE) {
      System.out.println("Card is inactive. Please contact customer service.");
      return false;
    }
    if(standing == Standing.BAD) {
      System.out.println("Card is in bad standing. Please contact customer service.");
      return false;
    }
    return true;
  }

  private boolean checkTransactionAmountWithinLimit(float amount) {
    if(amount > creditLimit) {
      System.out.println("Transaction amount exceeds credit limit. Please try again.");
      return false;
    }
    if(amount > availableBalance) {
      System.out.println("Transaction amount exceeds available balance. Please try again.");
      return false;
    }
    return true;
  }
}

public class source38 {
  public static void main(String[] args) {
    Date expiryDate = new Date();
    CardDetails cardDetails = new CardDetails("1234567890123456", "John Doe", expiryDate, 123);
    CreditCard card = new CreditCard(cardDetails);
    Transaction transactionSuccess = card.makeTransaction(1000, cardDetails, new Date());
    printTransactionStatus(transactionSuccess);
  }

  private static void printTransactionStatus(Transaction transaction) {
    switch (transaction.getStatus()) {
      case SUCCESS:
        System.out.println("TransactionBad successful.");
        break;
      case FAILURE:
        System.out.println("TransactionBad failed.");
        break;
      case PENDING:
        System.out.println("TransactionBad pending.");
        break;
    }
  }
}
