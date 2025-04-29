**Code Review: MMBE1.java**
  - Code smell no. - 1
  - Code smell name - Long Method
  - Code smell description - Methods that have grown to be too large and handle too much logic in one place, making them difficult to understand and maintain.
  - Found in line no. - 26-33, 49-53
  - Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
  - Possible solution - 
    ```java
    public void printAssignedTasks() {
        for(Map.Entry<FactoryWorkerBad, String> entry : assignedTasks.entrySet()) {
            printSingleAssignedTask(entry);
        }
    }

    private void printSingleAssignedTask(Map.Entry<FactoryWorkerBad, String> entry) {
        FactoryWorkerBad worker = entry.getKey();
        String task = entry.getValue();
        System.out.print("Worker: ");
        worker.getName();
        System.out.print("Task: " + task);
    }

    public void printFactoryDetails() {
        System.out.println("Supervisor Details: ");
        supervisor.printSupervisorDetails();
        printTasksAndRemaining();
    }

    private void printTasksAndRemaining() {
        System.out.println("Tasks remaining: ");
        supervisor.printAssignedTasks();
    }
    ```

  - Code smell no. - 2
  - Code smell name - Primitive Obsession
  - Code smell description - Using primitive data types to represent domain ideas, leading to code that requires extra validation and lacks expressiveness.
  - Found in line no. - 8, 62
  - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
  - Possible solution -
    ```java
    class PersonName {
        private String name;

        public PersonName(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }
    }

    class FactorySupervisorBad {
        private final PersonName name;
        private Map<FactoryWorkerBad, String> assignedTasks;
        private List<String> availableTasks;

        public FactorySupervisorBad(PersonName name, List<String> availableTasks) {
            this.name = name;
            this.availableTasks = availableTasks;
            this.assignedTasks = new HashMap<>();
        }

        // existing methods
    }

    class FactoryWorkerBad {
        private PersonName name;
        private List<String> tasks;
        private FactoryBad factory;

        public FactoryWorkerBad(PersonName name, FactoryBad factory) {
            this.name = name;
            this.factory = factory;
            this.tasks = new ArrayList<>();
        }

        public void getName() {
            System.out.println(name.getName());
        }

        // existing methods
    }
    ```

  - Code smell no. - 3
  - Code smell name - Feature Envy
  - Code smell description - A method that seems more interested in a class other than the one it actually is in.
  - Found in line no. - 72-75
  - Possible treatments - ['Move Method', 'Extract Method', 'Extract Method', 'Extract Method with Move Method']
  - Possible solution -
    ```java
    class FactoryWorkerBad {
        // existing fields

        public void getTask() {
            factory.assignTasksAndAddToWorker(this);
        }

        // existing methods
    }

    class FactoryBad {
        // existing fields and methods

        public void assignTasksAndAddToWorker(FactoryWorkerBad worker) {
            String task = assignTasks(worker);
            worker.addTask(task);
        }
    }
    ```

  - Code smell no. - 4
  - Code smell name - Inappropriate Intimacy
  - Code smell description - Classes that spend too much time delving into each other's private parts.
  - Found in line no. - 73
  - Possible treatments - ['Move Method & Move Field', 'Extract Class & Hide Delegate', 'Change Bidirectional Association to Unidirectional', 'Replace Delegation with Inheritance']
  - Possible solution -
    ```java
    class FactoryWorkerBad {
        // existing fields

        public void getTask() {
            String task = factory.requestTaskForWorker(this);
            tasks.add(task);
        }

        // existing methods
    }

    class FactoryBad {
        // existing fields and methods

        public String requestTaskForWorker(FactoryWorkerBad worker) {
            return supervisor.assignTask(worker);
        }
    }
    '''
