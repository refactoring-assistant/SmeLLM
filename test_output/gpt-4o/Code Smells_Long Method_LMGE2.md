**Code Review: LMGE2.java**
   - Code smell no. - 1
   - Code smell name - Long Method
   - Code smell description - A method is so long that it becomes difficult to understand and maintain. In this case, `calculateAllMotion` method performs too many tasks and has become lengthy.
   - Found in line no. - 11-19
   - Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
   - Possible solution - Break down the `calculateAllMotion` method into smaller methods, each handling one calculation and printing the result. This makes the code modular and easier to manage.
   
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
           printFinalVelocity(time);
           printFinalDisplacement(time);
           printTimeToReachGround();
           printMomentum(mass, time);
           printWeight(mass);
           printKineticEnergy(mass, time);
           printPower(mass, time);
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

       private void printFinalVelocity(int time) {
           System.out.println("Final velocity: " + calculateFinalVelocity(time));
       }

       private void printFinalDisplacement(int time) {
           System.out.println("Displacement: " + calculateFinalDisplacement(time));
       }

       private void printTimeToReachGround() {
           System.out.println("Time to reach ground: " + calculateTimeToReachGround());
       }

       private void printMomentum(int mass, int time) {
           System.out.println("Momentum: " + calculateMomentum(mass, time));
       }

       private void printWeight(int mass) {
           System.out.println("Weight: " + calculateWeight(mass));
       }

       private void printKineticEnergy(int mass, int time) {
           System.out.println("Kinetic energy: " + calculateKineticEnergy(mass, time));
       }

       private void printPower(int mass, int time) {
           System.out.println("Power: " + calculatePower(mass, time));
       }
   }

   public class LMGE2 {
       public static void main(String[] args) {
           LawsOfMotionGood lawsOfMotion = new LawsOfMotionGood(0, 0);
           lawsOfMotion.calculateAllMotion(10, 5);
       }
   }
   ```