/**
 * This class will be used to represent an RGB color.
 */
class RGB {
  private final int red;
  private final int green;
  private final int blue;

  public RGB(int red, int green, int blue) {
      this.red = red;
      this.green = green;
      this.blue = blue;
  }

  public double averageScale() {
      return (red + green + blue) / 3.0;
  }
}
public class source33 {
    public static void main(String[] args) {
        System.out.print("Hello world");
    }
}
