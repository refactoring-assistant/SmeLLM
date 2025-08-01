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

class CompareWeatherPatternsBad {
  public boolean isWeather1Greater(List<Integer> weather1List, List<Integer> weather2List) {
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

  public double averageAcross2Weathers(List<Integer> weather1List, List<Integer> weather2List) {
        int sumWeather = 0;
        for(int i = 0; i < weather1List.size(); i++) {
            sumWeather += weather1List.get(i);
            sumWeather += weather2List.get(i);
        }
        return (double) sumWeather / weather1List.size();
  }
}
public class source11 {
    public static void main(String[] args) {
          TwinCityWeatherSeries twinCityWeatherSeries = new TwinCityWeatherSeries();
            twinCityWeatherSeries.addWeather1Temp(10);
            twinCityWeatherSeries.addWeather1Temp(20);
            twinCityWeatherSeries.addWeather1Temp(30);
            twinCityWeatherSeries.addWeather2Temp(15);
            twinCityWeatherSeries.addWeather2Temp(25);
            twinCityWeatherSeries.addWeather2Temp(35);
            twinCityWeatherSeries.printEachCityWeather();
            CompareWeatherPatternsBad compareWeatherPatterns = new CompareWeatherPatternsBad();
            List<Integer> city1WeatherList = twinCityWeatherSeries.getCity1WeatherList();
            List<Integer> city2WeatherList = twinCityWeatherSeries.getCity2WeatherList();
            System.out.println("Is Weather 1 greater than Weather 2? " + compareWeatherPatterns.isWeather1Greater(city1WeatherList, city2WeatherList));
            System.out.println("Average across 2 weathers: " + compareWeatherPatterns.averageAcross2Weathers(city1WeatherList, city2WeatherList));
    }
}
