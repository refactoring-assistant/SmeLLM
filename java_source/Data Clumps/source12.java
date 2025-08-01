interface ILoanValuesBad {
  void printLoanDetails();
}

abstract class AbstractLoanValues implements ILoanValuesBad {
    protected double principal;
    protected double rate;
    protected double time;
    protected double interest;

    public AbstractLoanValues(double principal, double rate, double time) {
        this.principal = principal;
        this.rate = rate;
        this.time = time;
        this.interest = calculateInterest();
    }

    public void printLoanDetails() {
        System.out.println("Principal: " + this.principal);
        System.out.println("Rate: " + this.rate);
        System.out.println("Time: " + this.time);
        System.out.println("Interest: " + this.interest);
    }

    protected abstract double calculateInterest();
}
class SimpleLoanValuesBad extends AbstractLoanValues {

  public SimpleLoanValuesBad(double principal, double rate, double time) {
    super(principal, rate, time);
  }

  @Override
    protected double calculateInterest() {
      InterestCalculatorBad interestCalculator = new InterestCalculatorBad();
      return interestCalculator.calculateSimpleInterest(principal, rate, time);
    }
}

class CompoundLoanValuesBad extends AbstractLoanValues {

  public CompoundLoanValuesBad(double principal, double rate, double time) {
    super(principal, rate, time);
  }

  @Override
    protected double calculateInterest() {
      InterestCalculatorBad interestCalculator = new InterestCalculatorBad();
      return interestCalculator.calculateCompoundInterest(principal, rate, time);
    }
}
class InterestCalculatorBad {
  public double calculateSimpleInterest(double principal, double rate, double time) {
    return (principal * rate * time) / 100;
  }

  public double calculateCompoundInterest(double principal, double rate, double time) {
    return principal * Math.pow(1 + rate / 100, time) - principal;
  }
}
public class source12 {
    public static void main(String[] args) {
        ILoanValuesBad simpleLoan = new SimpleLoanValuesBad(1000, 5, 2);
        simpleLoan.printLoanDetails();

        ILoanValuesBad compoundLoan = new CompoundLoanValuesBad(1000, 5, 2);
        compoundLoan.printLoanDetails();
    }
}
