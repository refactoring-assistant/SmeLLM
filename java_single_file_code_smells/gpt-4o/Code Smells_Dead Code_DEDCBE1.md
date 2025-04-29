
**Code Review: DEDCBE1.java**
    
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data types (e.g., doubles for gravity, initial velocity, time, etc.) instead of small classes that better abstract these entities.
- Found in line no. - 2, 3, 4, 8, 9, 10, 11
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - Convert these primitives into objects that encapsulate the data and behavior related to them.

```java
class PhysicsParameter {
    private double value;

    public PhysicsParameter(double value) {
        this.value = value;
    }

    public double getValue() {
        return value;
    }
}

class PhysicsEngine {
    private PhysicsParameter gravity;
    private PhysicsParameter initialVelocity;
    private PhysicsParameter time;
    private PhysicsParameter finalVelocity;

    public PhysicsEngine(PhysicsParameter gravity, PhysicsParameter initialVelocity, PhysicsParameter time) {
        this.gravity = gravity;
        this.initialVelocity = initialVelocity;
        this.time = time;
        this.finalVelocity = new PhysicsParameter(-1);
    }

    public void calculateDistance() {
        double distance = initialVelocity.getValue() * time.getValue() 
                + 0.5 * gravity.getValue() * time.getValue() * time.getValue();
    }

    public void calculateFinalVelocity() {
        finalVelocity = new PhysicsParameter(initialVelocity.getValue() + gravity.getValue() * time.getValue());
    }

    public void printPhysicsParameters() {
        System.out.println("Gravity: " + gravity.getValue());
        System.out.println("Initial Velocity: " + initialVelocity.getValue());
        System.out.println("Time: " + time.getValue());
        System.out.println("Final Velocity: " + finalVelocity.getValue());
    }
}

public class DEDCBE1 {
    public static void main(String[] args) {
        PhysicsParameter gravity = new PhysicsParameter(9.8);
        PhysicsParameter initialVelocity = new PhysicsParameter(10);
        PhysicsParameter time = new PhysicsParameter(2);

        PhysicsEngine physicsEngine = new PhysicsEngine(gravity, initialVelocity, time);
        physicsEngine.calculateFinalVelocity();
        physicsEngine.printPhysicsParameters();
    }
}
```

- Code smell no. - 2
- Code smell name - Temporary Field
- Code smell description - The `distance` variable in the `PhysicsEngineBad` class is initialized but never used outside its method.
- Found in line no. - 5, 14, 16 
- Possible treatments - ['Extract Class or Replace Method with Method Object.', 'Introduce Null Object']
- Possible solution - Remove the field `distance` since it's not needed as a class member; it's a method-local temporary value.

```java
class PhysicsEngine {
    private PhysicsParameter gravity;
    private PhysicsParameter initialVelocity;
    private PhysicsParameter time;
    private PhysicsParameter finalVelocity;

    public PhysicsEngine(PhysicsParameter gravity, PhysicsParameter initialVelocity, PhysicsParameter time) {
        this.gravity = gravity;
        this.initialVelocity = initialVelocity;
        this.time = time;
        this.finalVelocity = new PhysicsParameter(-1);
    }

    public double calculateDistance() {
        return initialVelocity.getValue() * time.getValue() 
               + 0.5 * gravity.getValue() * time.getValue() * time.getValue();
    }

    public void calculateFinalVelocity() {
        finalVelocity = new PhysicsParameter(initialVelocity.getValue() + gravity.getValue() * time.getValue());
    }

    public void printPhysicsParameters() {
        System.out.println("Gravity: " + gravity.getValue());
        System.out.println("Initial Velocity: " + initialVelocity.getValue());
        System.out.println("Time: " + time.getValue());
        System.out.println("Final Velocity: " + finalVelocity.getValue());
    }
}

public class DEDCBE1 {
    public static void main(String[] args) {
        PhysicsParameter gravity = new PhysicsParameter(9.8);
        PhysicsParameter initialVelocity = new PhysicsParameter(10);
        PhysicsParameter time = new PhysicsParameter(2);

        PhysicsEngine physicsEngine = new PhysicsEngine(gravity, initialVelocity, time);
        physicsEngine.calculateFinalVelocity();
        physicsEngine.printPhysicsParameters();
    }
}
```

- Code smell no. - 3
- Code smell name - Long Method
- Code smell description - Multiple responsibilities within single methods, like performing calculations and displaying results separately.
- Found in line no. - 23-28
- Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
- Possible solution - Method extraction, separate the logic for each display line.

```java
public void printPhysicsParameters() {
    printGravity();
    printInitialVelocity();
    printTime();
    printFinalVelocity();
}

private void printGravity() {
    System.out.println("Gravity: " + gravity.getValue());
}

private void printInitialVelocity() {
    System.out.println("Initial Velocity: " + initialVelocity.getValue());
}

private void printTime() {
    System.out.println("Time: " + time.getValue());
}

private void printFinalVelocity() {
    System.out.println("Final Velocity: " + finalVelocity.getValue());
}
```