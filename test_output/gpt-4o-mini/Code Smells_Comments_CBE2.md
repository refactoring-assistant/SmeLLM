```markdown
**Code Review: CBE2.java**
- Code smell no. - 1
- Code smell name - Long Method
- Code smell description - A method that is too long and could be simplified by breaking it into smaller methods.
- Found in line no. - 8, 12, 13, 14, 21
- Possible treatments - Extract Method, Decompose Conditional
- Possible solution:
```java
class MatrixBad {
    private final int[][] matrix;

    public MatrixBad(int[][] matrix) {
        this.matrix = matrix;
    }

    public void printDifferentMatrix() {
        System.out.println("Original Matrix:");
        printMatrix(matrix);
        int[][] transposedMatrix = createTransposedMatrix();
        System.out.println("Transposed Matrix:");
        printMatrix(transposedMatrix);
    }

    private int[][] createTransposedMatrix() {
        int[][] differentMatrix = new int[matrix[0].length][matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                differentMatrix[j][i] = matrix[i][j];
            }
        }
        return differentMatrix;
    }

    private void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}

public class CBE2 {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        MatrixBad matrixObj = new MatrixBad(matrix);
        matrixObj.printDifferentMatrix();
    }
}
```
```