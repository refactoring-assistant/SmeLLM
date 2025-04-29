**Code Review: MMBE1.java**

- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - Usage of primitive data types or basic types, such as strings for tasks and names, instead of custom objects.
- Found in line no. - [8, 9, 10, 12, 14, 18, 21, 28, 29, 31, 32, 38, 42, 43, 45, 49-53, 61, 62, 63, 65, 66, 68, 69, 72, 74, 78, 82, 83]
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Array with Object']
- Possible solution - 
  ```java
  import java.util.Map;
  import java.util.List;
  import java.util.HashMap;
  import java.util.Random;
  import java.util.ArrayList;

  class Task {
      private String description;

      public Task(String description) {
          this.description = description;
      }

      public String getDescription() {
          return description;
      }
  }

  class Name {
      private String fullName;

      public Name(String fullName) {
          this.fullName = fullName;
      }

      public String getFullName() {
          return fullName;
      }
  }

  class FactorySupervisor {
      private final Name name;
      private Map<FactoryWorker, Task> assignedTasks;
      private List<Task> availableTasks;

      public FactorySupervisor(Name name, List<Task> availableTasks) {
          this.name = name;
          this.availableTasks = availableTasks;
          this.assignedTasks = new HashMap<>();
      }

      public Task assignTask(FactoryWorker worker) {
          Random random = new Random();
          int randomTaskIndex = random.nextInt(availableTasks.size());
          Task task = availableTasks.get(randomTaskIndex);
          assignedTasks.put(worker, task);
          return task;
      }

      public void printAssignedTasks() {
          for (Map.Entry<FactoryWorker, Task> entry : assignedTasks.entrySet()) {
              FactoryWorker worker = entry.getKey();
              Task task = entry.getValue();
              System.out.print("Worker: ");
              worker.getName();
              System.out.print("Task: " + task.getDescription());
          }
      }

      public void printSupervisorDetails() {
          System.out.println("Name: " + name.getFullName());
      }
  }

  class Factory {
      private FactorySupervisor supervisor;

      public Factory(FactorySupervisor supervisor) {
          this.supervisor = supervisor;
      }

      public void printFactoryDetails() {
          System.out.println("Supervisor Details: ");
          supervisor.printSupervisorDetails();
          System.out.println("Tasks remaining: ");
          supervisor.printAssignedTasks();
      }

      public Task assignTasks(FactoryWorker worker) {
          return supervisor.assignTask(worker);
      }
  }

  class FactoryWorker {
      private Name name;
      private List<Task> tasks;
      private Factory factory;

      public FactoryWorker(Name name, Factory factory) {
          this.name = name;
          this.factory = factory;
          this.tasks = new ArrayList<>();
      }

      public void getTask() {
          Task task = factory.assignTasks(this);
          tasks.add(task);
      }

      public void printTasks() {
          for(Task task : tasks) {
              System.out.println("Task: " + task.getDescription());
          }
      }

      public void getName() {
          System.out.println(name.getFullName());
      }
  }

  public class MMBE1 {
      public static void main(String[] args) {
          FactorySupervisor supervisor = new FactorySupervisor(new Name("John Doe"), List.of(new Task("Task 1"), new Task("Task 2"), new Task("Task 3")));
          Factory factory = new Factory(supervisor);
          FactoryWorker worker = new FactoryWorker(new Name("Jane Doe"), factory);
          worker.getTask();
          System.out.println("Tasks assigned to worker: ");
          worker.printTasks();
          System.out.println("Factory details: ");
          factory.printFactoryDetails();
      }
  }
  ```

- Code smell no. - 2
- Code smell name - Feature Envy
- Code smell description - A method seems more interested in a class other than the one it is actually in.
- Found in line no. - [49-54]
- Possible treatments - ['Move Method', 'Extract Method', 'Extract Method with Move Method']
- Possible solution - Move the `printFactoryDetails` method to the `FactorySupervisor` class and extract methods where needed to improve encapsulation and reduce dependency on external classes.