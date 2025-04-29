```markdown
**Code Review: LMBE2.java**
- Code smell no. - 1
    - Code smell name - Long Method
    - Code smell description - A method that has grown too long can be hard to understand and maintain. It tries to do too many things without dividing responsibilities into smaller methods.
    - Found in line no. - [11-26]
    - Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
    - Possible solution - Break down the `calculateAllMotion` method into several smaller methods, each handling a specific calculation. This can be done by extracting each calculation into its own method and calling them within `calculateAllMotion`.

- Code smell no. - 2
    - Code smell name - Primitive Obsession
    - Code smell description - Overusing primitives for things that could be encapsulated as objects, which leads to duplicated code and less flexibility.
    - Found in line no. - [2, 3, 12, 14, 16, 18, 20, 22, 24]
    - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', ' Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
    - Possible solution - Consider introducing a `PhysicsParameters` object to encapsulate `initialDisplacement`, `initialVelocity`, and other calculated properties, which would reduce duplication and enhance readability.

- Code smell no. - 3
    - Code smell name - Data Clumps
    - Code smell description - When a group of variables are found together in multiple places, they are likely related and should be encapsulated.
    - Found in line no. - [2, 3, 6-8, 12, 18-22]
    - Possible treatments - ['Extract Class', 'Introduce Parameter Object', 'Preserve Whole Object']
    - Possible solution - Extract a class that encapsulates related data, such as a `MotionData` class to hold properties like `initialDisplacement`, `initialVelocity`, and perhaps combine it with a `MassProperties` for `mass` and `gravity`.

Here's a possible improved solution restructuring the code:

```java
class LawsOfMotion {
    private double initialDisplacement;
    private double initialVelocity;
    private double mass;
    private static final double gravity = -9.8;

    public LawsOfMotion(double initialDisplacement, double initialVelocity, double mass) {
        this.initialDisplacement = initialDisplacement;
        this.initialVelocity = initialVelocity;
        this.mass = mass;
    }

    public void calculateAllMotion(int time) {
        double finalVelocity = calculateFinalVelocity(time);
        display("Final velocity", finalVelocity);
        double displacement = calculateDisplacement(time);
        display("Displacement", displacement);
        double timeToReachGround = calculateTimeToReachGround();
        display("Time to reach ground", timeToReachGround);
        double momentum = calculateMomentum(finalVelocity);
        display("Momentum", momentum);
        double weight = calculateWeight();
        display("Weight", weight);
        double kineticEnergy = calculateKineticEnergy(finalVelocity);
        display("Kinetic energy", kineticEnergy);
        double power = calculatePower(finalVelocity);
        display("Power", power);
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

    private double calculateMomentum(double finalVelocity) {
        return mass * finalVelocity;
    }
    
    private double calculateWeight() {
        return mass * gravity;
    }

    private double calculateKineticEnergy(double finalVelocity) {
        return 0.5 * mass * finalVelocity * finalVelocity;
    }

    private double calculatePower(double finalVelocity) {
        return mass * gravity * finalVelocity;
    }

    private void display(String parameter, double value) {
        System.out.println(parameter + ": " + value);
    }
}

public class LMBE2 {
    public static void main(String[] args) {
        LawsOfMotion lawsOfMotion = new LawsOfMotion(0, 0, 5);
        lawsOfMotion.calculateAllMotion(10);
    }
}
```
```