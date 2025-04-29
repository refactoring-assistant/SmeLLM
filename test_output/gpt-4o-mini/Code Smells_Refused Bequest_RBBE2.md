```markdown
**Code Review: RBBE2.java**
    - Code smell no. - 1
    - Code smell name - Alternative Classes with Different Interfaces
    - Code smell description - Classes that implement the same interface expose methods that behave differently, leading to inconsistency.
    - Found in line no. - 26
    - Possible treatments - ['Rename Method', 'Move Method, Add Parameter & Parameterize Method', 'Extract Superclass']
    - Possible solution - 
    ```java
    interface NoteTaker {
        void writeNotes();
        void shareNotesAsPdf();
    }
    
    abstract class BaseNotes implements NoteTaker {
        @Override
        public abstract void writeNotes();
        
        @Override
        public void shareNotesAsPdf() {
            throw new UnsupportedOperationException("Sharing notes as PDF is not supported.");
        }
    }
    
    class IpadNotes extends BaseNotes {
        @Override
        public void writeNotes() {
            System.out.println("Notes written on iPad.");
        }
        
        @Override
        public void shareNotesAsPdf() {
            System.out.println("Notes shared as PDF.");
        }
    }
    
    class NotebookNotes extends BaseNotes {
        @Override
        public void writeNotes() {
            System.out.println("Notes written on Notebook.");
        }
    }
    
    public class RBBE2 {
        public static void main(String[] args) {
            NoteTaker ipad = new IpadNotes();
            ipad.writeNotes();
            ipad.shareNotesAsPdf();

            NoteTaker notebook = new NotebookNotes();
            notebook.writeNotes();
        }
    }
    ```
```