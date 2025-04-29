**Code Review: LMBE2.java**

- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - This code smell occurs when a method is too long, making it difficult to understand and maintain.
- Found in line no. - [11-25]
- Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
- Possible solution - 
  ```java
  class LawsOfMotionBad {
      double initialDisplacement;
      double initialVelocity;
      private final static double gravity = -9.8;

      public LawsOfMotionBad(double initialDisplacement, double initialVelocity) {
          this.initialDisplacement = initialDisplacement;
          this.initialVelocity = initialVelocity;
      }

      public void calculateAllMotion(int time, int mass) {
          System.out.println("Final velocity: " + calculateFinalVelocity(time));
          System.out.println("Displacement: " + calculateDisplacement(time));
          System.out.println("Time to reach ground: " + calculateTimeToReachGround());
          System.out.println("Momentum: " + calculateMomentum(mass, calculateFinalVelocity(time)));
          System.out.println("Weight: " + calculateWeight(mass));
          System.out.println("Kinetic energy: " + calculateKineticEnergy(mass, calculateFinalVelocity(time)));
          System.out.println("Power: " + calculatePower(mass, calculateFinalVelocity(time)));
      }

      private double calculateFinalVelocity(int time) {
          return initialVelocity + gravity * time;
      }

      private double calculateDisplacement(int time) {
          return initialDisplacement + initialVelocity * time + 0.5 * gravity * time * time;
      }

      private double calculateTimeToReachGround() {
          return (-initialVelocity - Math.sqrt(initialVelocity * initialVelocity - 2 * gravity * initialDisplacement)) / gravity;
      }

      private double calculateMomentum(int mass, double finalVelocity) {
          return mass * finalVelocity;
      }

      private double calculateWeight(int mass) {
          return mass * gravity;
      }

      private double calculateKineticEnergy(int mass, double finalVelocity) {
          return 0.5 * mass * finalVelocity * finalVelocity;
      }

      private double calculatePower(int mass, double finalVelocity) {
          return mass * gravity * finalVelocity;
      }
  }

  public class LMBE2 {
      public static void main(String[] args) {
          LawsOfMotionBad lawsOfMotion = new LawsOfMotionBad(0, 0);
          lawsOfMotion.calculateAllMotion(10, 5);
      }
  }
  ```