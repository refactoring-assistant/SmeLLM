```markdown
**Code Review: CGE2.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - A long method becomes difficult to understand and maintain. It can benefit from being broken down into smaller methods to improve readability and organization.
- Found in line no. - 8, 12, 14
- Possible treatments - ['Extract Method']
- Possible solution - 
```java
class MatrixGood {
    private final int[][] matrix;

    public MatrixGood(int[][] matrix) {
        this.matrix = matrix;
    }

    public void printDifferentMatrix() {
        printOriginalMatrix();
        printTransposedMatrix();
    }

    private void printOriginalMatrix() {
        System.out.println("Original Matrix:");
        printMatrix(matrix);
    }

    private void printTransposedMatrix() {
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

public class CGE2 {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        MatrixGood matrixObj = new MatrixGood(matrix);
        matrixObj.printDifferentMatrix();
    }
}
```
```