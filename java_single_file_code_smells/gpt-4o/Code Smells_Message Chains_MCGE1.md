**Code Review: MCGE1.java**

- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - A method that has grown too big and is trying to accomplish too many tasks.
- Found in line no. - 64 to 74
- Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
- Possible solution:
  ```java
  class OrderGood {
      // ... existing code ...

      public void printOrderDetails() {
          printOrderInfo();
          printItems();
          printPersonDetails();
      }

      private void printOrderInfo() {
          System.out.println("Order Number: " + orderNumber);
          System.out.println("Order Status: " + orderStatus);
          System.out.println("Order Total: " + orderTotal);
      }

      private void printItems() {
          System.out.println("Items: ");
          for (String item : items) {
              System.out.println(item);
          }
      }

      private void printPersonDetails() {
          System.out.println("Person: " + person.getName());
          System.out.println("Address: " + person.getAddress());
      }
  }
  ```

No other code smells detected.