class Loan {
  private double principal;
  private double interestRate;
  private double term;
  private double interestAmount;
  private MonthlyInterestCalculator monthlyInterestCalculator;


  public Loan(double principal, double interestRate, double term) {
    this.principal = principal;
    this.interestRate = interestRate;
    this.term = term;
    this.interestAmount = 0;
    monthlyInterestCalculator = new MonthlyInterestCalculator();
  }

  public void calculateInterest() {
    if(term < 1) {
      monthlyInterestCalculator = new MonthlyInterestCalculator(interestRate, term);
      interestAmount = monthlyInterestCalculator.calculateInterestAmount(principal);
    }
    else {
      interestAmount = principal * interestRate * term;
    }
  }

  public double returnTotalAmount() {
    return principal + interestAmount;
  }
}

class MonthlyInterestCalculator {

  private double monthlyInterestRate;
  private int numMonths;
  public MonthlyInterestCalculator() {
    this.monthlyInterestRate = 0;
    this.numMonths = 0;
  }
  public MonthlyInterestCalculator(double interestRate, double term) {
    this.monthlyInterestRate = interestRate / 12;
    this.numMonths = (int)Math.ceil(term * 12);
  }

  public double calculateInterestAmount(double principal) {
    return principal * monthlyInterestRate * numMonths;
  }
}
public class source69 {
  public static void main(String[] args) {
    Loan loan = new Loan(1000, 0.1, 0.5);
    loan.calculateInterest();
    System.out.println("Total amount to be paid: " + loan.returnTotalAmount());
  }
}
