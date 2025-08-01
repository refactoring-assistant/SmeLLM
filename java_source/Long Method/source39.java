class LawsOfMotion {
  double initialDisplacement;
  double initialVelocity;
  private final static double gravity = -9.8;

  public LawsOfMotion(double initialDisplacement, double initialVelocity) {
    this.initialDisplacement = initialDisplacement;
    this.initialVelocity = initialVelocity;
  }

  public void calculateAllMotion(int time, int mass) {
    System.out.println("Final velocity: " + calculateFinalVelocity(time));
    System.out.println("Displacement: " + calculateFinalDisplacement(time));
    System.out.println("Time to reach ground: " + calculateTimeToReachGround());
    System.out.println("Momentum: " + calculateMomentum(mass, time));
    System.out.println("Weight: " + calculateWeight(mass));
    System.out.println("Kinetic energy: " + calculateKineticEnergy(mass, time));
    System.out.println("Power: " + calculatePower(mass, time));
  }

  private double calculateFinalVelocity(int time) {
      return initialVelocity + gravity * time;
  }

  private double calculateFinalDisplacement(int time) {
      return initialDisplacement + initialVelocity * time + 0.5 * gravity * time * time;
  }

  private double calculateTimeToReachGround() {
      return (-initialVelocity - Math.sqrt(initialVelocity * initialVelocity - 2 * gravity * initialDisplacement)) / gravity;
  }

  private double calculateMomentum(int mass, int time) {
    return mass * calculateFinalVelocity(time);
  }

  private double calculateWeight(int mass) {
    return mass * gravity;
  }

  private double calculateKineticEnergy(int mass, int time) {
    return 0.5 * mass * calculateFinalVelocity(time) * calculateFinalVelocity(time);
  }

  private double calculatePower(int mass, int time) {
    return mass * gravity * calculateFinalVelocity(time);
  }

}
public class source39 {
  public static void main(String[] args) {
    LawsOfMotion lawsOfMotion = new LawsOfMotion(0, 0);
    lawsOfMotion.calculateAllMotion(10, 5);
  }
}
