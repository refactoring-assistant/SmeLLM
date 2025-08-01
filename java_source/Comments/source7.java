class Matrix {
  private final int[][] matrix;

  public Matrix(int[][] matrix) {
    this.matrix = matrix;
  }

  public void printDifferentMatrix() {
    System.out.println("Original Matrix:");
    printMatrix(matrix);

    System.out.println("Transposed Matrix:");
    printMatrix(transposeMatrix());
  }

  private void printMatrix(int[][] matrix) {
    for(int i = 0; i < matrix.length; i++) {
      for(int j = 0; j < matrix[0].length; j++) {
        System.out.print(matrix[i][j] + " ");
      }
      System.out.println();
    }
  }

  private int [][] transposeMatrix() {
    int[][] transpose = new int[matrix[0].length][matrix.length];
    for(int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[0].length; j++) {
        transpose[j][i] = matrix[i][j];
      }
    }
    return transpose;
  }
}

public class source7 {
  public static void main(String[] args) {
    int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    Matrix matrixObj = new Matrix(matrix);
    matrixObj.printDifferentMatrix();
  }
}
