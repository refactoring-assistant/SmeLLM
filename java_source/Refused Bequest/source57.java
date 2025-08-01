interface NoteTaker {
    void writeNotes();
    void shareNotesAsPdf();
}

class IpadNotes implements NoteTaker {
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

    @Override
    public void shareNotesAsPdf() {
        throw new UnsupportedOperationException("Notebook does not support sharing notes as PDF.");
    }
}
public class source57 {
    public static void main(String[] args) {
      try {
        NoteTaker ipad = new IpadNotes();
        ipad.writeNotes();
        ipad.shareNotesAsPdf();

        NoteTaker notebook = new NotebookNotes();
        notebook.writeNotes();
        notebook.shareNotesAsPdf();
      }
      catch (UnsupportedOperationException e) {
        System.out.println(e.getMessage());
      }

    }
}
