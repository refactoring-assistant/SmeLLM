**Code Review: LMBE2.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - A method that contains too many lines of code, making it hard to understand and maintain.
- Found in line no. - 11
- Possible treatments - Extract Method
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
        calculateFinalVelocity(time);
        calculateDisplacement(time);
        calculateTimeToReachGround();
        calculateMomentum(mass, time);
        calculateWeight(mass);
        calculateKineticEnergy(mass);
        calculatePower(mass);
    }

    private void calculateFinalVelocity(int time) {
        double finalVelocity = initialVelocity + gravity * time;
        System.out.println("Final velocity: " + finalVelocity);
    }

    private void calculateDisplacement(int time) {
        double displacement = initialDisplacement + initialVelocity * time + 0.5 * gravity * time * time;
        System.out.println("Displacement: " + displacement);
    }

    private void calculateTimeToReachGround() {
        double timeToReachGround = (-initialVelocity - Math.sqrt(initialVelocity * initialVelocity - 2 * gravity * initialDisplacement)) / gravity;
        System.out.println("Time to reach ground: " + timeToReachGround);
    }

    private void calculateMomentum(int mass, int finalVelocity) {
        double momentum = mass * finalVelocity;
        System.out.println("Momentum: " + momentum);
    }

    private void calculateWeight(int mass) {
        double weight = mass * gravity;
        System.out.println("Weight: " + weight);
    }

    private void calculateKineticEnergy(int mass) {
        double kineticEnergy = 0.5 * mass * finalVelocity * finalVelocity;
        System.out.println("Kinetic energy: " + kineticEnergy);
    }
    
    private void calculatePower(int mass, int finalVelocity) {
        double power = mass * gravity * finalVelocity;
        System.out.println("Power: " + power);
    }
}
```