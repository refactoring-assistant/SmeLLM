import java.util.Map;
import java.util.List;
import java.util.HashMap;
import java.util.Random;
import java.util.ArrayList;

class FactorySupervisor{
  private final String name;
  private Map<FactoryWorker, String> assignedTasks;
  private List<String> availableTasks;

  public FactorySupervisor(String name, List<String> availableTasks) {
      this.name = name;
      this.availableTasks = availableTasks;
      this.assignedTasks = new HashMap<>();
  }

  public String assignTask(FactoryWorker worker) {
      Random random = new Random();
      int randomTaskIndex = random.nextInt(availableTasks.size());
      String task = availableTasks.get(randomTaskIndex);
      assignedTasks.put(worker, task);
      return task;
  }

  public void printAssignedTasks() {
      for(Map.Entry<FactoryWorker, String> entry : assignedTasks.entrySet()) {
          FactoryWorker worker = entry.getKey();
          String task = entry.getValue();
          System.out.print("Worker: ");
          worker.getName();
          System.out.print("Task: " + task);
      }
  }


  public void printSupervisorDetails() {
      System.out.println("Name: " + name);
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

    public String assignTasks(FactoryWorker worker) {
      return supervisor.assignTask(worker);
    }
}

class FactoryWorker {
    private String name;
    private List<String> tasks;
    private Factory factory;

    public FactoryWorker(String name, Factory factory) {
        this.name = name;
        this.factory = factory;
        this.tasks = new ArrayList<>();
    }

    public void getTask() {
        String task = factory.assignTasks(this);
        tasks.add(task);
    }

    public void printTasks() {
        for(String task : tasks) {
            System.out.println("Task: " + task);
        }
    }
    public void getName() {
        System.out.println(name);
    }
}
public class source48 {
  public static void main(String[] args) {
    FactorySupervisor supervisor = new FactorySupervisor("John Doe", List.of("Task 1", "Task 2", "Task 3"));
    Factory factory = new Factory(supervisor);
    FactoryWorker worker = new FactoryWorker("Jane Doe", factory);
    worker.getTask();
    System.out.println("Tasks assigned to worker: ");
    worker.printTasks();
    System.out.println("Factory details: ");
    factory.printFactoryDetails();
  }
}
