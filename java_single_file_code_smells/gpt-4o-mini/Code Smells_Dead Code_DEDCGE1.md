```markdown
**Code Review: DEDCGE1.java**
- Code smell no. - 1
- Code smell name - Data Class
- Code smell description - A class that serves primarily to hold data with little or no behavior.
- Found in line no. - 1
- Possible treatments - ['Encapsulate Field', 'Encapsulate Collection', 'Move Method and Extract Method', 'Remove Setting Method and Hide Method']
- Possible solution - 
```java
class PhysicsEngine {
    private double gravity;
    private double initialVelocity;
    private double time;
    private double finalVelocity;

    public PhysicsEngine(double velocity, double time) {
        this.gravity = 9.8;
        this.initialVelocity = velocity;
        this.time = time;
        this.finalVelocity = -1;
    }

    public double calculateFinalVelocity() {
        finalVelocity = initialVelocity + gravity * time;
        return finalVelocity;
    }

    public void displayPhysicsParameters() {
        System.out.printf("Gravity: %.2f%n", gravity);
        System.out.printf("Initial Velocity: %.2f%n", initialVelocity);
        System.out.printf("Time: %.2f%n", time);
        System.out.printf("Final Velocity: %.2f%n", calculateFinalVelocity());
    }
}

public class DEDCGE1 {
    public static void main(String[] args) {
        PhysicsEngine physicsEngine = new PhysicsEngine(10, 2);
        physicsEngine.displayPhysicsParameters();
    }
}
```
```