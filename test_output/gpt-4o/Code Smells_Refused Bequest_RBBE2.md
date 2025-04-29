**Code Review: RBBE2.java**

- Code smell no. - 1
- Code smell name - Alternative Classes with Different Interfaces
- Code smell description - The `NotebookNotesBad` class does not support the `shareNotesAsPdf` method from the `NoteTakerBad` interface and throws an `UnsupportedOperationException`, which indicates classes implementing the same interface lack similar behavior.
- Found in line no. - 18, 25-27
- Possible treatments - ['Rename Method', 'Move Method, Add Parameter & Parameterize Method', 'Extract Superclass']
- Possible solution - One solution is to create an abstract class with the common functionalities shared by both devices and then have subclasses that enforce their specific implementations.

```java
interface NoteTaker {
    void writeNotes();
}

interface PdfSharable {
    void shareNotesAsPdf();
}

class IpadNotes implements NoteTaker, PdfSharable {
    @Override
    public void writeNotes() {
        System.out.println("Notes written on iPad.");
    }

    @Override
    public void shareNotesAsPdf() {
        System.out.println("Notes shared as PDF.");
    }
}

class NotebookNotes implements NoteTaker {
    @Override
    public void writeNotes() {
        System.out.println("Notes written on Notebook.");
    }
}

public class RBBE2 {
    public static void main(String[] args) {
      try {
        NoteTaker ipad = new IpadNotes();
        ipad.writeNotes();
        ((PdfSharable) ipad).shareNotesAsPdf();

        NoteTaker notebook = new NotebookNotes();
        notebook.writeNotes();
        // No shareNotesAsPdf method call for NotebookNotes as it isn't applicable
      }
      catch (UnsupportedOperationException e) {
        System.out.println(e.getMessage());
      }
    }
}
```

- Code smell no. - 2
- Code smell name - Refused Bequest
- Code smell description - The `NotebookNotesBad` class inherits all methods from the `NoteTakerBad` interface, but not all are applicable, as evident with `shareNotesAsPdf`.
- Found in line no. - 18, 25-27
- Possible treatments - ['Replace Inheritance with Delegation', 'Extract Superclass']
- Possible solution - Implement interfaces that are relevant for each implementation context, ensuring the class only implements methods that make sense for it.

**Possible solution is included in the solution provided for the first code smell.**