import java.util.Arrays;

class SquareMatrixOperations {
  private int matrix1[][];
  private int matrix2[][];
  private int result[][];

  public SquareMatrixOperations(int matrix1[][], int matrix2[][]) {
    this.matrix1 = matrix1;
    this.matrix2 = matrix2;
    this.result = new int[matrix1.length][matrix1[0].length];
  }

    public int[][] add2Matrix() {
      perform_add_subtract("ADD");

        System.out.println("The result of the operation add is: " + Arrays.deepToString(result));

        return result;

    }

    public int[][] subtract2Matrix() {
      perform_add_subtract("SUBTRACT");

        System.out.println("The result of the operation subtract is: " + Arrays.deepToString(result));

        return result;
    }

  public int[][] multiply2Matrix() {
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

    System.out.println("The result of the operation multiply is: " + Arrays.deepToString(result));

    return result;
  }

  private void perform_add_subtract(String operation) {
    for (int i = 0; i < matrix1.length; i++) {
      for (int j = 0; j < matrix1[0].length; j++) {
        switch (operation) {
          case "ADD":
            result[i][j] = matrix1[i][j] + matrix2[i][j];
            break;
          case "SUBTRACT":
            result[i][j] = matrix1[i][j] - matrix2[i][j];
            break;
          default:
            break;
        }
      }
    }
  }

}

public class source17 {
    public static void main(String[] args) {
        int matrix1[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int matrix2[][] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};

        SquareMatrixOperations matrixOperations = new SquareMatrixOperations(matrix1, matrix2);
        matrixOperations.add2Matrix();
        matrixOperations.subtract2Matrix();
        matrixOperations.multiply2Matrix();
      }
}