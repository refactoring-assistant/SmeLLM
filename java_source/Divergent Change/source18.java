import java.util.Arrays;

enum LogType {
    INPUT, OUTPUT, DEFAULT
}

enum MatrixOperation {
    ADD, SUBTRACT, MULTIPLY
}

class PrintLogger {
    public void printMatrixResult(int[][] result, String operation, LogType logType) {
        switch (logType) {
            case INPUT:
                System.out.println("The input matrix is: " + Arrays.deepToString(result));
                break;
            case OUTPUT:
                System.out.println("The result of the operation " + operation + "  is: " + Arrays.deepToString(result));
                break;
            default:
                break;
        }
    }

}

class SquareMatrixOperations {
  private int matrix1[][];
  private int matrix2[][];
  private int result[][];
  private PrintLogger matrixLogger;

  public SquareMatrixOperations(int matrix1[][], int matrix2[][]) {
    this.matrix1 = matrix1;
    this.matrix2 = matrix2;
    this.result = new int[matrix1.length][matrix1[0].length];
    this.matrixLogger = new PrintLogger();
  }

  public int[][] add2Matrix() {
    perform_add_subtract(MatrixOperation.ADD);

    logResult("add");

    return result;

  }

  public int[][] subtract2Matrix() {
    perform_add_subtract(MatrixOperation.SUBTRACT);

    logResult("subtract");

    return result;
  }

  public int[][] multiply2Matrix() {
    performMultiplication();

    logResult("multiply");

    return result;
  }

  private void performMultiplication() {
    int row1 = matrix1.length;
    int col1 = matrix1[0].length;
    int col2 = matrix2[0].length;

    for (int i = 0; i < row1; i++) {
      for (int j = 0; j < col2; j++) {
        result[i][j] = 0;
        for (int k = 0; k < col1; k++) {
          result[i][j] += matrix1[i][k] * matrix2[k][j];
        }
      }
    }
  }

  private void perform_add_subtract(MatrixOperation operation) {
    for (int i = 0; i < matrix1.length; i++) {
      for (int j = 0; j < matrix1[0].length; j++) {
        switch (operation) {
          case ADD:
            result[i][j] = matrix1[i][j] + matrix2[i][j];
            break;
          case SUBTRACT:
            result[i][j] = matrix1[i][j] - matrix2[i][j];
            break;
          default:
            break;
        }
      }
    }
  }

  private void logResult(String operation) {
    matrixLogger.printMatrixResult(result, operation, LogType.OUTPUT);
  }

}

public class source18 {
  public static void main(String[] args) {
    int matrix1[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrix2[][] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};

    SquareMatrixOperations matrixOperations = new SquareMatrixOperations(matrix1, matrix2);
    matrixOperations.add2Matrix();
    matrixOperations.subtract2Matrix();
    matrixOperations.multiply2Matrix();
  }
}