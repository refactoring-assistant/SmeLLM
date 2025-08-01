class Coordinates2D {
  private int x;
  private int y;

  public Coordinates2D(int x, int y) {
    this.x = x;
    this.y = y;
  }

  public int getX() { return x; }
  public int getY() { return y; }
  public int calculateDistance(Coordinates2D point) {
    return (int) Math.sqrt(Math.pow(x - point.getX(), 2) + Math.pow(y - point.getY(), 2));
  }

  public boolean sameX(Coordinates2D point) {
    return x == point.getX();
  }

  public boolean sameY(Coordinates2D point) {
      return y == point.getY();
  }
}

class Rectangle2DSpace {
  private final int length;
  private final int breadth;

  public Rectangle2DSpace(Coordinates2D [] points) throws IllegalArgumentException {
    checkPointsArraySize(points);
    checkRectangle(points);
    this.length = points[0].calculateDistance(points[1]);
    this.breadth = points[0].calculateDistance(points[3]);
  }

  public int calculateArea() {
    return length * breadth;
  }

  public int calculatePerimeter() {
    return 2 * (length + breadth);
  }

  private void checkPointsArraySize(Coordinates2D [] points) throws IllegalArgumentException {
    if(points.length != 4) {
      throw new IllegalArgumentException("Rectangle should have 4 points");
    }
  }

  private void checkRectangle(Coordinates2D [] points) throws IllegalArgumentException {
    if(!points[0].sameX(points[1])  || !points[0].sameY(points[3])  ||
            !points[1].sameY(points[2]) || !points[2].sameX(points[3]) ) {
      throw new IllegalArgumentException("Points do not form a rectangle");
    }
  }


}
public class source22 {
  public static void main(String[] args) {
    Coordinates2D [] points = {new Coordinates2D(1, 1), new Coordinates2D(1, 3), new Coordinates2D(3, 3), new Coordinates2D(3, 1)};
    Rectangle2DSpace rectangle = new Rectangle2DSpace(points);
    System.out.println("Area of rectangle: " + rectangle.calculateArea());
    System.out.println("Perimeter of rectangle: " + rectangle.calculatePerimeter());
  }
}
