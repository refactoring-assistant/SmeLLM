**Code Review: LMGE2.java**
    
  - Code smell no. - 1
  - Code smell name - Long Method
  - Code smell description - The method `calculateAllMotion` contains many print statements, making it longer and performing many actions. This can make the code hard to read and maintain.
  - Found in line no. - [11]
  - Possible treatments - ["Extract Method", "Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object", "Decompose Conditional"]
  - Possible solution - 
    ```java
    class LawsOfMotionGood {
      double initialDisplacement;
      double initialVelocity;
      private final static double gravity = -9.8;

      public LawsOfMotionGood(double initialDisplacement, double initialVelocity) {
        this.initialDisplacement = initialDisplacement;
        this.initialVelocity = initialVelocity;
      }

      public void calculateAllMotion(int time, int mass) {
        double finalVelocity = calculateFinalVelocity(time);
        double displacement = calculateFinalDisplacement(time);
        double timeToReachGround = calculateTimeToReachGround();
        double momentum = calculateMomentum(mass, time);
        double weight = calculateWeight(mass);
        double kineticEnergy = calculateKineticEnergy(mass, time);
        double power = calculatePower(mass, time);

        printCalculatedResults(finalVelocity, displacement, timeToReachGround, momentum, weight, kineticEnergy, power);
      }
      
      private void printCalculatedResults(double finalVelocity, double displacement, double timeToReachGround, double momentum, double weight, double kineticEnergy, double power) {
          System.out.println("Final velocity: " + finalVelocity);
          System.out.println("Displacement: " + displacement);
          System.out.println("Time to reach ground: " + timeToReachGround);
          System.out.println("Momentum: " + momentum);
          System.out.println("Weight: " + weight);
          System.out.println("Kinetic energy: " + kineticEnergy);
          System.out.println("Power: " + power);
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
    public class LMGE2 {
      public static void main(String[] args) {
        LawsOfMotionGood lawsOfMotion = new LawsOfMotionGood(0, 0);
        lawsOfMotion.calculateAllMotion(10, 5);
      }
    }
    ```
