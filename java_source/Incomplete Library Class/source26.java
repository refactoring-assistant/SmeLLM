import java.util.Date;

class TrackDay {
  private Date defaultDay;
  private static final long MILLIS_IN_DAY = 24 * 60 * 60 * 1000;
  public TrackDay(Date defaultDay) {
    this.defaultDay = defaultDay;
  }

  public void changeDayToNextDay() {
    defaultDay = changeDay(1);
  }

  public void changeDayToPreviousDay() {
    defaultDay = changeDay(-1);
  }

  public boolean isGivenDateNextDay(Date givenDate) {
    Date nextDay = changeDay(1);
    return nextDay.compareTo(givenDate) == 0;
  }

  public boolean isGivenDatePreviousDay(Date givenDate) {
    Date prevDay = changeDay(-1);
    return prevDay.compareTo(givenDate) == 0;
  }

  public void printDay() {
    System.out.println("Day: " + defaultDay.toString());
  }

  private Date changeDay(int days) {
    return new Date(defaultDay.getTime() + days * MILLIS_IN_DAY);
  }
}
public class source26 {
  public static void main(String[] args) {
    Date defaultDay = new Date();
    TrackDay trackDay = new TrackDay(defaultDay);
    trackDay.printDay();

    Date aheadDate = new Date(defaultDay.getTime() + 24 * 60 * 60 * 1000);
    System.out.println("Is given date next day: " + trackDay.isGivenDateNextDay(aheadDate));
    Date prevDate = new Date(defaultDay.getTime() - 24 * 60 * 60 * 1000);
    System.out.println("Is given date previous day: " + trackDay.isGivenDatePreviousDay(prevDate));

    trackDay.changeDayToNextDay();
    trackDay.printDay();
    trackDay.changeDayToPreviousDay();
    trackDay.printDay();
  }
}
