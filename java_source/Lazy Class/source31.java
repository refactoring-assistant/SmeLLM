enum Operation {
  ADD, SUBTRACT
}
class MatrixOperationValidator {
    public boolean canMatrixOperationBePerformed(int [][]matrix1, int [][]matrix2) {
      return matrix1.length == matrix2.length && matrix1[0].length == matrix2[0].length;
    }
}
class MatrixOperation {
  private final int [][]matrix1;
  private final int [][]matrix2;
  private final int [][]result;

  public MatrixOperation(int [][]matrix1, int [][]matrix2) throws IllegalArgumentException {
    MatrixOperationValidator validator = new MatrixOperationValidator();
      if(!validator.canMatrixOperationBePerformed(matrix1, matrix2)) {
          throw new IllegalArgumentException("Matrix dimensions are not same");
      }
      this.matrix1 = matrix1;
      this.matrix2 = matrix2;
      result = new int[matrix1.length][matrix1[0].length];
  }

  public void addMatrices() {
    performAddSubtractOperation(Operation.ADD);
  }

  public void subtractMatrices() {
    performAddSubtractOperation(Operation.SUBTRACT);
  }

  public void printResult() {
      for(int i = 0; i < result.length; i++) {
          for(int j = 0; j < result[0].length; j++) {
              System.out.print(result[i][j] + " ");
          }
          System.out.println();
      }
  }

  private void performAddSubtractOperation(Operation operation) {
    for(int i = 0; i < matrix1.length; i++) {
      for(int j = 0; j < matrix1[0].length; j++) {
        if(operation.equals(Operation.ADD)) {
          result[i][j] = matrix1[i][j] + matrix2[i][j];
        } else if(operation.equals(Operation.SUBTRACT)) {
          result[i][j] = matrix1[i][j] - matrix2[i][j];
        }
      }
    }
  }
}
public class source31 {
  public static void main(String[] args) {
    int [][]matrix1 = {{1, 2}, {3, 4}};
    int [][]matrix2 = {{5, 6}, {7, 8}};
    MatrixOperation matrixOperation = new MatrixOperation(matrix1, matrix2);
    matrixOperation.addMatrices();
    System.out.println("Addition of matrices:");
    matrixOperation.printResult();
    System.out.println("Subtraction of matrices:");
    matrixOperation.subtractMatrices();
    matrixOperation.printResult();
  }
}
