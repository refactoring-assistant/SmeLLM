```markdown
**Code Review: LMBE2.java**
    - Code smell no. - 1
    - Code smell name - Long Method
    - Code smell description - The method `calculateAllMotion` is excessively long, performing multiple calculations in sequence which makes it hard to read and maintain.
    - Found in line no. - [11, 12, 13, 14, 16, 18, 20, 22, 24]
    - Possible treatments - [Extract Method, Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object, Decompose Conditional]
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
            System.out.println("Momentum: " + calculateMomentum(mass, time));
            System.out.println("Weight: " + calculateWeight(mass));
            System.out.println("Kinetic energy: " + calculateKineticEnergy(mass, time));
            System.out.println("Power: " + calculatePower(mass, time));
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

        private double calculateMomentum(int mass, int time) {
            return mass * calculateFinalVelocity(time);
        }

        private double calculateWeight(int mass) {
            return mass * gravity;
        }

        private double calculateKineticEnergy(int mass, int time) {
            double finalVelocity = calculateFinalVelocity(time);
            return 0.5 * mass * finalVelocity * finalVelocity;
        }

        private double calculatePower(int mass, int time) {
            return mass * gravity * calculateFinalVelocity(time);
        }
    }

    public class LMBE2 {
        public static void main(String[] args) {
            LawsOfMotionBad lawsOfMotion = new LawsOfMotionBad(0, 0);
            lawsOfMotion.calculateAllMotion(10, 5);
        }
    }
    ```

    - Code smell no. - 2
    - Code smell name - Large Class
    - Code smell description - The `LawsOfMotionBad` class is potentially too large as it contains multiple behaviors related to motion calculations.
    - Found in line no. - [1, 2, 3, 4, 6-26]
    - Possible treatments - [Extract Class, Extract Subclass, Extract Interface, Duplicate Observed Data]
    - Possible solution - 
    ```java
    class MotionCalculator {
        private double initialDisplacement;
        private double initialVelocity;
        private final static double gravity = -9.8;

        MotionCalculator(double initialDisplacement, double initialVelocity) {
            this.initialDisplacement = initialDisplacement;
            this.initialVelocity = initialVelocity;
        }

        double calculateFinalVelocity(double time) {
            return initialVelocity + gravity * time;
        }

        double calculateDisplacement(double time) {
            return initialDisplacement + initialVelocity * time + 0.5 * gravity * time * time;
        }

        double calculateTimeToReachGround() {
            return (-initialVelocity - Math.sqrt(initialVelocity * initialVelocity - 2 * gravity * initialDisplacement)) / gravity;
        }
    }

    class LawsOfMotion {
        private MotionCalculator calculator;

        public LawsOfMotion(double initialDisplacement, double initialVelocity) {
            calculator = new MotionCalculator(initialDisplacement, initialVelocity);
        }

        public void calculateAllMotion(int time, int mass) {
            System.out.println("Final velocity: " + calculator.calculateFinalVelocity(time));
            System.out.println("Displacement: " + calculator.calculateDisplacement(time));
            System.out.println("Time to reach ground: " + calculator.calculateTimeToReachGround());
            System.out.println("Momentum: " + mass * calculator.calculateFinalVelocity(time));
            System.out.println("Weight: " + mass * MotionCalculator.gravity);
            System.out.println("Kinetic energy: " + 0.5 * mass * Math.pow(calculator.calculateFinalVelocity(time), 2));
            System.out.println("Power: " + mass * MotionCalculator.gravity * calculator.calculateFinalVelocity(time));
        }
    }

    public class LMBE2 {
        public static void main(String[] args) {
            LawsOfMotion lawsOfMotion = new LawsOfMotion(0, 0);
            lawsOfMotion.calculateAllMotion(10, 5);
        }
    }
    ```
```