class LawsOfMotion {
  double initialDisplacement;
  double initialVelocity;
  private final static double gravity = -9.8;

  public LawsOfMotion(double initialDisplacement, double initialVelocity) {
      this.initialDisplacement = initialDisplacement;
      this.initialVelocity = initialVelocity;
  }

  public void calculateAllMotion(int time, int mass) {
    double finalVelocity = initialVelocity + gravity * time;
    System.out.println("Final velocity: " + finalVelocity);
    double displacement = initialDisplacement + initialVelocity * time + 0.5 * gravity * time * time;
    System.out.println("Displacement: " + displacement);
    double timeToReachGround = (-initialVelocity - Math.sqrt(initialVelocity * initialVelocity - 2 * gravity * initialDisplacement)) / gravity;
    System.out.println("Time to reach ground: " + timeToReachGround);
    double momentum = mass * finalVelocity;
    System.out.println("Momentum: " + momentum);
    double weight = mass * gravity;
    System.out.println("Weight: " + weight);
    double kineticEnergy = 0.5 * mass * finalVelocity * finalVelocity;
    System.out.println("Kinetic energy: " + kineticEnergy);
    double power = mass * gravity * finalVelocity;
    System.out.println("Power: " + power);
  }

}
public class source37 {
    public static void main(String[] args) {
        LawsOfMotion lawsOfMotion = new LawsOfMotion(0, 0);
        lawsOfMotion.calculateAllMotion(10, 5);
    }
}
