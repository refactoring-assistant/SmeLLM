**Code Review: LZCGE1.java**
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - The code uses an explicit check for different operations (ADD, SUBTRACT) within a method, which can be replaced with a more polymorphic approach.
- Found in line no. - 39-43
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution - 
  ```java
  enum Operation {
      ADD {
          @Override
          public int apply(int a, int b) {
              return a + b;
          }
      },
      SUBTRACT {
          @Override
          public int apply(int a, int b) {
              return a - b;
          }
      };

      public abstract int apply(int a, int b);
  }

  class MatrixOperation {
      private final int [][]matrix1;
      private final int [][]matrix2;
      private final int [][]result;

      public MatrixOperation(int [][]matrix1, int [][]matrix2) {
          if (!canMatrixOperationBePerformed(matrix1, matrix2)) {
              throw new IllegalArgumentException("Matrix dimensions are not same");
          }
          this.matrix1 = matrix1;
          this.matrix2 = matrix2;
          result = new int[matrix1.length][matrix1[0].length];
      }

      public void addMatrices() {
          performOperation(Operation.ADD);
      }

      public void subtractMatrices() {
          performOperation(Operation.SUBTRACT);
      }

      public void printResult() {
          for (int i = 0; i < result.length; i++) {
              for (int j = 0; j < result[0].length; j++) {
                  System.out.print(result[i][j] + " ");
              }
              System.out.println();
          }
      }

      private void performOperation(Operation operation) {
          for (int i = 0; i < matrix1.length; i++) {
              for (int j = 0; j < matrix1[0].length; j++) {
                  result[i][j] = operation.apply(matrix1[i][j], matrix2[i][j]);
              }
          }
      }

      private boolean canMatrixOperationBePerformed(int [][]matrix1, int [][]matrix2) {
          return matrix1.length == matrix2.length && matrix1[0].length == matrix2[0].length;
      }
  }

  public class LZCGE1 {
      public static void main(String[] args) {
          int[][] matrix1 = {{1, 2}, {3, 4}};
          int[][] matrix2 = {{5, 6}, {7, 8}};
          MatrixOperation matrixOperation = new MatrixOperation(matrix1, matrix2);
          matrixOperation.addMatrices();
          System.out.println("Addition of matrices:");
          matrixOperation.printResult();
          System.out.println("Subtraction of matrices:");
          matrixOperation.subtractMatrices();
          matrixOperation.printResult();
      }
  }
  ```