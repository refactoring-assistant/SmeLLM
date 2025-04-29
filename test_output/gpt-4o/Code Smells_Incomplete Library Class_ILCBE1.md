**Code Review: ILCBE1.java**
  - Code smell no. - 1
  - Code smell name - Primitive Obsession
  - Code smell description - The use of primitive data types or basic classes like `Date` for complex operations or calculations can signify a primitive obsession. In this snippet, `Date` is directly accessed and manipulated for calculations, which can be encapsulated for clarity and reusability.
  - Found in line no. - 4, 11, 15, 19, 24
  - Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', ' Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
  - Possible solution - 
    ```java
    import java.time.LocalDate;

    class TrackDay {
        private LocalDate defaultDay;
        private static final int DAYS_IN_DAY = 1;

        public TrackDay(LocalDate defaultDay) {
            this.defaultDay = defaultDay;
        }

        public void changeDayToNextDay() {
            defaultDay = defaultDay.plusDays(DAYS_IN_DAY);
        }

        public void changeDayToPreviousDay() {
            defaultDay = defaultDay.minusDays(DAYS_IN_DAY);
        }

        public boolean isGivenDateNextDay(LocalDate givenDate) {
            LocalDate nextDay = defaultDay.plusDays(DAYS_IN_DAY);
            return nextDay.equals(givenDate);
        }

        public boolean isGivenDatePreviousDay(LocalDate givenDate) {
            LocalDate prevDay = defaultDay.minusDays(DAYS_IN_DAY);
            return prevDay.equals(givenDate);
        }

        public void printDay() {
            System.out.println("Day: " + defaultDay.toString());
        }
    }

    public class ILCBE1 {
        public static void main(String[] args) {
            LocalDate defaultDay = LocalDate.now();
            TrackDay trackDay = new TrackDay(defaultDay);
            trackDay.printDay();

            LocalDate aheadDate = defaultDay.plusDays(1);
            System.out.println("Is given date next day: " + trackDay.isGivenDateNextDay(aheadDate));
            LocalDate prevDate = defaultDay.minusDays(1);
            System.out.println("Is given date previous day: " + trackDay.isGivenDatePreviousDay(prevDate));

            trackDay.changeDayToNextDay();
            trackDay.printDay();
            trackDay.changeDayToPreviousDay();
            trackDay.printDay();
        }
    }
    ```