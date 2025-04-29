**Code Review: CGE2.java**
- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The use of primitive data structures (in this case, a two-dimensional array) can make the code harder to read and maintain, and it may obscure the intent by not leveraging more expressive constructs.
- Found in line no. - 2, 4, 5, 16, 25, 26
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - Refactor to use a Matrix class that wraps the two-dimensional array, encapsulating the matrix operations within it.

```java
class Matrix {
    private final int[][] data;

    public Matrix(int[][] data) {
        this.data = data;
    }

    public void print() {
        for(int i = 0; i < data.length; i++) {
            for(int j = 0; j < data[0].length; j++) {
                System.out.print(data[i][j] + " ");
            }
            System.out.println();
        }
    }

    public Matrix transpose() {
        int[][] transposedData = new int[data[0].length][data.length];
        for(int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[0].length; j++) {
                transposedData[j][i] = data[i][j];
            }
        }
        return new Matrix(transposedData);
    }
    
    public void printTransposedMatrix() {
        System.out.println("Original Matrix:");
        print();
        System.out.println("Transposed Matrix:");
        transpose().print();
    }
}

public class CGE2 {
    public static void main(String[] args) {
        int[][] matrixData = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        Matrix matrix = new Matrix(matrixData);
        matrix.printTransposedMatrix();
    }
}
```