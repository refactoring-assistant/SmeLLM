**Code Review: MMGE1.java**

- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - Methods that have grown too long can be hard to understand and maintain. They may do more than one responsibility.
- Found in line no. - 26-34
- Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
- Possible solution - Break down the `printAssignedTasks` method into smaller, more manageable methods:

```java
class FactorySupervisorGood {
  private final String name;
  private Map<FactoryWorkerGood, String> assignedTasks;
  private List<String> availableTasks;

  public FactorySupervisorGood(String name, List<String> availableTasks) {
    this.name = name;
    this.availableTasks = availableTasks;
    this.assignedTasks = new HashMap<>();
  }

  public String assignTask(FactoryWorkerGood worker) {
    Random random = new Random();
    int randomTaskIndex = random.nextInt(availableTasks.size());
    String task = availableTasks.get(randomTaskIndex);
    assignedTasks.put(worker, task);
    return task;
  }

  public void printAssignedTasks() {
    assignedTasks.forEach(this::printWorkerTask);
  }

  private void printWorkerTask(FactoryWorkerGood worker, String task) {
    System.out.print("Worker: ");
    worker.getName();
    System.out.print("Task: " + task);
  }

  public void printSupervisorDetails() {
    System.out.println("Name: " + name);
  }
}

class FactoryWorkerGood {
  private String name;
  private List<String> tasks;
  private FactorySupervisorGood supervisor;

  public FactoryWorkerGood(String name, FactorySupervisorGood supervisor) {
    this.name = name;
    this.supervisor = supervisor;
    this.tasks = new ArrayList<>();
  }

  public void getTask() {
    String task = supervisor.assignTask(this);
    tasks.add(task);
  }

  public void printTasks() {
    for (String task : tasks) {
      System.out.println("Task: " + task);
    }
  }

  public void getName() {
    System.out.println(name);
  }
}

public class MMGE1 {
  public static void main(String[] args) {
    FactorySupervisorGood supervisor = new FactorySupervisorGood("John Doe", List.of("Task 1", "Task 2", "Task 3"));
    FactoryWorkerGood worker = new FactoryWorkerGood("Jane Doe", supervisor);
    worker.getTask();
    System.out.println("Tasks assigned to worker: ");
    worker.printTasks();
    System.out.println("Factory details: ");
    System.out.println("Supervisor details: ");
    supervisor.printSupervisorDetails();
    System.out.println("Tasks remaining: ");
    supervisor.printAssignedTasks();
  }
}
```