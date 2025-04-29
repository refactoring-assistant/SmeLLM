```markdown
**Code Review: MMBE1.java**
  
  - Code smell no. - 1
  - Code smell name - Long Method
  - Code smell description - A method that is too long and does too much can be hard to understand and maintain.
  - Found in line no. - 18
  - Possible treatments - Extract Method
  - Possible solution - 
    ```java
    public String assignTask(FactoryWorkerBad worker) {
        String task = getRandomTask();
        assignedTasks.put(worker, task);
        return task;
    }

    private String getRandomTask() {
        Random random = new Random();
        int randomTaskIndex = random.nextInt(availableTasks.size());
        return availableTasks.get(randomTaskIndex);
    }
    ```

  - Code smell no. - 2
  - Code smell name - Data Class
  - Code smell description - A class that is primarily used to hold data with little or no behavior.
  - Found in line no. - 8 (FactoryWorkerBad)
  - Possible treatments - Encapsulate Field, Move Method and Extract Method
  - Possible solution - 
    ```java
    class FactoryWorkerBad {
        private String name;
        private List<String> tasks = new ArrayList<>();
        private FactoryBad factory;

        public FactoryWorkerBad(String name, FactoryBad factory) {
            this.name = name;
            this.factory = factory;
        }

        public void getTask() {
            String task = factory.assignTasks(this);
            tasks.add(task);
        }

        public void printTasks() {
            for (String task : tasks) {
                System.out.println("Task: " + task);
            }
        }

        public String getName() {
            return name;
        }
    }
    ```

  - Code smell no. - 3
  - Code smell name - Message Chains
  - Code smell description - A situation where multiple method calls are chained together, which may indicate poor encapsulation.
  - Found in line no. - 31 (worker.getName())
  - Possible treatments - Hide Delegate
  - Possible solution - 
    ```java
    class FactoryWorkerBad {
        ...
        public String getName() {
            return name;
        }
        ...
    }

    // Update printAssignedTasks to use the getName method:
    public void printAssignedTasks() {
        for (Map.Entry<FactoryWorkerBad, String> entry : assignedTasks.entrySet()) {
            FactoryWorkerBad worker = entry.getKey();
            String task = entry.getValue();
            System.out.print("Worker: " + worker.getName());
            System.out.println("Task: " + task);
        }
    }
    ```
```