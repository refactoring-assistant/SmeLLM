import java.util.ArrayList;
import java.util.List;
class TwinCityWeatherSeries {
  private List<Integer> weather1;
  private List<Integer> weather2;

  public TwinCityWeatherSeries() {
    this.weather1 = new ArrayList<>();
    this.weather2 = new ArrayList<>();
  }

  public void addWeather1Temp(int number) {
    weather1.add(number);
  }

  public void addWeather2Temp(int number) {
    weather2.add(number);
  }

  public void printEachCityWeather() {
    System.out.println("Weather City 1: ");
    for (int number : weather1) {
      System.out.println(number);
    }
    System.out.println("Weather City 2: ");
    for (int number : weather2) {
      System.out.println(number);
    }
  }

  public List<Integer> getCity1WeatherList() {
    return weather1;
  }

  public List<Integer> getCity2WeatherList() {
    return weather2;
  }
}

class CompareWeatherPatterns {
  public boolean isWeather1Greater(TwinCityWeatherSeries twinCityWeatherSeries) {
    List<Integer> weather1List = twinCityWeatherSeries.getCity1WeatherList();
    List<Integer> weather2List = twinCityWeatherSeries.getCity2WeatherList();
    int sumWeather1 = 0;
    int sumWeather2 = 0;
    for (int weather1 : weather1List) {
      sumWeather1 += weather1;
    }
    for (int weather2 : weather2List) {
      sumWeather2 += weather2;
    }
    return sumWeather1 > sumWeather2;
  }

  public double averageAcross2Weathers(TwinCityWeatherSeries twinCityWeatherSeries) {
    List<Integer> weather1List = twinCityWeatherSeries.getCity1WeatherList();
    List<Integer> weather2List = twinCityWeatherSeries.getCity2WeatherList();
    int sumWeather = 0;
    for(int i = 0; i < weather1List.size(); i++) {
      sumWeather += weather1List.get(i);
      sumWeather += weather2List.get(i);
    }
    return (double) sumWeather / weather1List.size();
  }
}
public class source14 {
  public static void main(String[] args) {
    TwinCityWeatherSeries twinCityWeatherSeries = new TwinCityWeatherSeries();
    twinCityWeatherSeries.addWeather1Temp(10);
    twinCityWeatherSeries.addWeather1Temp(20);
    twinCityWeatherSeries.addWeather1Temp(30);
    twinCityWeatherSeries.addWeather2Temp(15);
    twinCityWeatherSeries.addWeather2Temp(25);
    twinCityWeatherSeries.addWeather2Temp(35);
    twinCityWeatherSeries.printEachCityWeather();
    CompareWeatherPatterns compareWeatherPatterns = new CompareWeatherPatterns();
    System.out.println("Is Weather 1 greater than Weather 2? " + compareWeatherPatterns.isWeather1Greater(twinCityWeatherSeries));
    System.out.println("Average across 2 weathers: " + compareWeatherPatterns.averageAcross2Weathers(twinCityWeatherSeries));
  }
}
