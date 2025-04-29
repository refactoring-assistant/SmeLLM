```markdown
**Code Review: LMGE2.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - A method that is too long and does multiple things, making it difficult to understand and maintain.
- Found in line no. - 11
- Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
- Possible solution - 
```java
public void calculateAllMotion(int time, int mass) {
    calculateAndPrintFinalVelocity(time);
    calculateAndPrintDisplacement(time);
    calculateAndPrintTimeToReachGround();
    calculateAndPrintMomentum(mass, time);
    calculateAndPrintWeight(mass);
    calculateAndPrintKineticEnergy(mass, time);
    calculateAndPrintPower(mass, time);
}

private void calculateAndPrintFinalVelocity(int time) {
    System.out.println("Final velocity: " + calculateFinalVelocity(time));
}

private void calculateAndPrintDisplacement(int time) {
    System.out.println("Displacement: " + calculateFinalDisplacement(time));
}

private void calculateAndPrintTimeToReachGround() {
    System.out.println("Time to reach ground: " + calculateTimeToReachGround());
}

private void calculateAndPrintMomentum(int mass, int time) {
    System.out.println("Momentum: " + calculateMomentum(mass, time));
}

private void calculateAndPrintWeight(int mass) {
    System.out.println("Weight: " + calculateWeight(mass));
}

private void calculateAndPrintKineticEnergy(int mass, int time) {
    System.out.println("Kinetic energy: " + calculateKineticEnergy(mass, time));
}

private void calculateAndPrintPower(int mass, int time) {
    System.out.println("Power: " + calculatePower(mass, time));
}
```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - Use of primitive types (like int) instead of small domain classes.
- Found in line no. - 11, 33, 37, 41, 45
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - 
```java
class MotionParameters {
    private int time;
    private int mass;
  
    public MotionParameters(int time, int mass) {
        this.time = time;
        this.mass = mass;
    }
  
    public int getTime() {
        return time;
    }
  
    public int getMass() {
        return mass;
    }
}

public void calculateAllMotion(MotionParameters parameters) {
    int time = parameters.getTime();
    int mass = parameters.getMass();
    // existing method implementation...
}

private double calculateMomentum(MotionParameters parameters) {
    return parameters.getMass() * calculateFinalVelocity(parameters.getTime());
}

private double calculateWeight(MotionParameters parameters) {
    return parameters.getMass() * gravity;
}

// Similarly modify methods using parameters
```

- Code smell no. - 3
- Code smell name - Data Clumps
- Code smell description - Groups of data that frequently appear together. 
- Found in line no. - 11, 33, 37, 41, 45
- Possible treatments - ['Extract Class', 'Introduce Parameter Object', 'Preserve Whole Object']
- Possible solution - See Primitive Obsession solutions, as both are closely related and can be resolved by the same refactoring.
```