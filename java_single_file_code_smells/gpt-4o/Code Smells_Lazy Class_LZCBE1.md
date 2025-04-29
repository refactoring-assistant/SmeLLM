**Code Review: LZCBE1.java**

- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - The method `performAddSubtractOperation` uses a sequential if-else statement to apply different operations based on an enum `OperationBad`, resembling a switch statement that lacks extensibility and flexibility.
- Found in line no. - [44, 46]
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', ' Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - 
  ```java
  interface Operation {
      int apply(int a, int b);
  }

  class AddOperation implements Operation {
      public int apply(int a, int b) {
          return a + b;
      }
  }

  class SubtractOperation implements Operation {
      public int apply(int a, int b) {
          return a - b;
      }
  }

  class MatrixOperationValidator {
      public boolean canMatrixOperationBePerformed(int [][]matrix1, int [][]matrix2) {
          return matrix1.length == matrix2.length && matrix1[0].length == matrix2[0].length;
      }
  }

  class MatrixOperation {
      private final int[][] matrix1;
      private final int[][] matrix2;
      private final int[][] result;

      public MatrixOperation(int [][]matrix1, int [][]matrix2) throws IllegalArgumentException {
          MatrixOperationValidator validator = new MatrixOperationValidator();
          if (!validator.canMatrixOperationBePerformed(matrix1, matrix2)) {
              throw new IllegalArgumentException("Matrix dimensions are not same");
          }
          this.matrix1 = matrix1;
          this.matrix2 = matrix2;
          this.result = new int[matrix1.length][matrix1[0].length];
      }

      public void performOperation(Operation operation) {
          for (int i = 0; i < matrix1.length; i++) {
              for (int j = 0; j < matrix1[0].length; j++) {
                  result[i][j] = operation.apply(matrix1[i][j], matrix2[i][j]);
              }
          }
      }

      public void printResult() {
          for (int[] row : result) {
              for (int value : row) {
                  System.out.print(value + " ");
              }
              System.out.println();
          }
      }
  }

  public class LZCBE1 {
      public static void main(String[] args) {
          int [][]matrix1 = {{1, 2}, {3, 4}};
          int [][]matrix2 = {{5, 6}, {7, 8}};
          MatrixOperation matrixOperation = new MatrixOperation(matrix1, matrix2);

          Operation add = new AddOperation();
          matrixOperation.performOperation(add);
          System.out.println("Addition of matrices:");
          matrixOperation.printResult();

          Operation subtract = new SubtractOperation();
          matrixOperation.performOperation(subtract);
          System.out.println("Subtraction of matrices:");
          matrixOperation.printResult();
      }
  }
  ```