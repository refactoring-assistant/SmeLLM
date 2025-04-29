**Code Review: DVCHGE1.java**
    
- Code smell no. - 1
- Code smell name - Switch Statements
- Code smell description - A switch statement is used to control the flow of logic based on different `logType` values, which can signify that the class might be prone to frequent changes or additions when new types are added.
- Found in line no. - 13-22, 83-92
- Possible treatments - ['Extract Method & then Move Method', 'Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Conditional with Polymorphism', 'Replace Parameter with Explicit Methods', 'Introduce Null Object']
- Possible solution:
```java
import java.util.Arrays;

abstract class LogStrategy {
    public abstract void log(int[][] result, String operation);
}

class InputLogStrategy extends LogStrategy {
    @Override
    public void log(int[][] result, String operation) {
        System.out.println("The input matrix is: " + Arrays.deepToString(result));
    }
}

class OutputLogStrategy extends LogStrategy {
    @Override
    public void log(int[][] result, String operation) {
        System.out.println("The result of the operation " + operation + " is: " + Arrays.deepToString(result));
    }
}

class NullLogStrategy extends LogStrategy {
    @Override
    public void log(int[][] result, String operation) {
        // Do nothing
    }
}

enum LogType {
    INPUT, OUTPUT, DEFAULT
}

enum MatrixOperation {
    ADD, SUBTRACT, MULTIPLY
}

class PrintLoggerGood {
    public void printMatrixResult(int[][] result, String operation, LogStrategy logStrategy) {
        logStrategy.log(result, operation);
    }
}

class SquareMatrixOperationsGood {
    private int matrix1[][];
    private int matrix2[][];
    private int result[][];
    private PrintLoggerGood matrixLogger;

    public SquareMatrixOperationsGood(int matrix1[][], int matrix2[][]) {
        this.matrix1 = matrix1;
        this.matrix2 = matrix2;
        this.result = new int[matrix1.length][matrix1[0].length];
        this.matrixLogger = new PrintLoggerGood();
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
                if (operation == MatrixOperation.ADD) {
                    result[i][j] = matrix1[i][j] + matrix2[i][j];
                } else if (operation == MatrixOperation.SUBTRACT) {
                    result[i][j] = matrix1[i][j] - matrix2[i][j];
                }
            }
        }
    }

    private void logResult(String operation) {
        matrixLogger.printMatrixResult(result, operation, new OutputLogStrategy());
    }
}

public class DVCHGE1 {
    public static void main(String[] args) {
        int matrix1[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int matrix2[][] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};

        SquareMatrixOperationsGood matrixOperations = new SquareMatrixOperationsGood(matrix1, matrix2);
        matrixOperations.add2Matrix();
        matrixOperations.subtract2Matrix();
        matrixOperations.multiply2Matrix();
    }
}
```