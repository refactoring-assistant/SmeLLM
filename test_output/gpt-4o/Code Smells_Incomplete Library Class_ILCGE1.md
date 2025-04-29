**Code Review: ILCGE1.java**

- Code smell no. - 1
- Code smell name - Primitive Obsession
- Code smell description - The code uses a primitive long to represent the number of milliseconds in a day. This is a classic problem often associated with Primitive Obsession, where instead of a primitive, an object or constant in a utility class could better represent the underlying concept.
- Found in line no. - 5
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', ' Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution:
```java
import java.util.Date;

class Duration {
    private static final long MILLIS_IN_DAY = 24 * 60 * 60 * 1000;

    public static long getMillisInDay() {
        return MILLIS_IN_DAY;
    }
}

class TrackDayGood {
    private Date defaultDay;

    public TrackDayGood(Date defaultDay) {
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
        return new Date(defaultDay.getTime() + days * Duration.getMillisInDay());
    }
}

public class ILCGE1 {
    public static void main(String[] args) {
        Date defaultDay = new Date();
        TrackDayGood trackDay = new TrackDayGood(defaultDay);
        trackDay.printDay();

        Date aheadDate = new Date(defaultDay.getTime() + Duration.getMillisInDay());
        System.out.println("Is given date next day: " + trackDay.isGivenDateNextDay(aheadDate));
        Date prevDate = new Date(defaultDay.getTime() - Duration.getMillisInDay());
        System.out.println("Is given date previous day: " + trackDay.isGivenDatePreviousDay(prevDate));

        trackDay.changeDayToNextDay();
        trackDay.printDay();
        trackDay.changeDayToPreviousDay();
        trackDay.printDay();
    }
}
```