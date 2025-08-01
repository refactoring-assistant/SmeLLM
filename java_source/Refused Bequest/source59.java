interface NoteTaker {
  void writeNotes();
}

class IpadNotes implements NoteTaker {
  @Override
  public void writeNotes() {
    System.out.println("Notes written on iPad.");
  }

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
public class source59 {
  public static void main(String[] args) {
    NoteTaker ipad = new IpadNotes();
    ipad.writeNotes();
   ((IpadNotes) ipad).shareNotesAsPdf();

    NoteTaker notebook = new NotebookNotes();
    notebook.writeNotes();
  }
}
