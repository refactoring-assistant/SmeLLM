class Loan {
  private double principal;
  private double interestRate;
  private double term;
  private double interestAmount;
  private double monthlyInterestRate;
  private int numMonths;

  public Loan(double principal, double interestRate, double term) {
      this.principal = principal;
      this.interestRate = interestRate;
      this.term = term;
      this.interestAmount = 0;
      this.monthlyInterestRate = interestRate / 12;
      this.numMonths = 12;
  }

    public void calculateInterest() {
      if(term < 1) {
        numMonths = (int)Math.ceil(term * 12);
        interestAmount = principal * monthlyInterestRate * numMonths;
      }
      else {
        interestAmount = principal * interestRate * term;
      }
    }

    public double returnTotalAmount() {
      return principal + interestAmount;
    }
}
public class source68 {
  public static void main(String[] args) {
    Loan loan = new Loan(1000, 0.1, 0.5);
    loan.calculateInterest();
    System.out.println("Total amount to be paid: " + loan.returnTotalAmount());
  }
}
