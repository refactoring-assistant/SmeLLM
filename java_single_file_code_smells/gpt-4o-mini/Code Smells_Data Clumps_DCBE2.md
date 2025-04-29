**Code Review: DCBE2.java**
- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - A class that is too large and does too much, which makes it harder to maintain and understand.
- Found in line no. - 3, 40
- Possible treatments - ['Extract Class', 'Extract Subclass', 'Extract Interface', 'Duplicate Observed Data']
- Possible solution - 
```java
class TwinCityWeather {
    private List<Integer> weatherData;

    public TwinCityWeather() {
        this.weatherData = new ArrayList<>();
    }

    public void addTemperature(int temperature) {
        weatherData.add(temperature);
    }

    public List<Integer> getWeatherData() {
        return weatherData;
    }

    public void printWeather() {
        for (int temperature : weatherData) {
            System.out.println(temperature);
        }
    }
}

class CompareWeatherPatterns {
    public boolean isWeather1Greater(TwinCityWeather weather1, TwinCityWeather weather2) {
        return weather1.getWeatherData().stream().mapToInt(Integer::intValue).sum() > 
               weather2.getWeatherData().stream().mapToInt(Integer::intValue).sum();
    }

    public double averageAcross2Weathers(TwinCityWeather weather1, TwinCityWeather weather2) {
        int sumWeather = 0;
        List<Integer> weather1List = weather1.getWeatherData();
        List<Integer> weather2List = weather2.getWeatherData();
        
        for (int i = 0; i < weather1List.size(); i++) {
            sumWeather += weather1List.get(i);
            sumWeather += weather2List.get(i);
        }
        return (double) sumWeather / weather1List.size();
    }
}

public class DCBE2 {
    public static void main(String[] args) {
        TwinCityWeather city1Weather = new TwinCityWeather();
        city1Weather.addTemperature(10);
        city1Weather.addTemperature(20);
        city1Weather.addTemperature(30);

        TwinCityWeather city2Weather = new TwinCityWeather();
        city2Weather.addTemperature(15);
        city2Weather.addTemperature(25);
        city2Weather.addTemperature(35);

        System.out.println("Weather City 1: ");
        city1Weather.printWeather();
        System.out.println("Weather City 2: ");
        city2Weather.printWeather();
        
        CompareWeatherPatterns compareWeatherPatterns = new CompareWeatherPatterns();
        System.out.println("Is Weather 1 greater than Weather 2? " + compareWeatherPatterns.isWeather1Greater(city1Weather, city2Weather));
        System.out.println("Average across 2 weathers: " + compareWeatherPatterns.averageAcross2Weathers(city1Weather, city2Weather));
    }
}
```

- Code smell no. - 2
- Code smell name - Primitive Obsession
- Code smell description - Using primitive data types to represent domain ideas instead of using small classes that encapsulate the relevant behavior and data.
- Found in line no. - 4, 5, 12, 16
- Possible treatments - ['Replace Data Value with Object', 'Introduce Parameter Object or Preserve Whole Object', 'Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy', 'Replace Array with Object']
- Possible solution - 
```java
class Temperature {
    private final int value;

    public Temperature(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}

class TwinCityWeather {
    private List<Temperature> weatherData;

    ...
    
    public void addTemperature(Temperature temperature) {
        weatherData.add(temperature);
    }

    ...
}

// Usage in main method
city1Weather.addTemperature(new Temperature(10));
city1Weather.addTemperature(new Temperature(20));
city1Weather.addTemperature(new Temperature(30));
```

- Code smell no. - 3
- Code smell name - Duplicate Code
- Code smell description - Code that is duplicated in more than one place, making maintenance difficult and error-prone as one instance requires changes across all instances.
- Found in line no. - 12, 16, 64, 68
- Possible treatments - ['Extract Method', 'Extract Method & Pull Up Field', 'Pull Up Constructor Body', 'Form Template Method', 'Substitute Algorithm', 'Extract Superclass', 'Extract ClassConsolidate Conditional Expression and use Extract Method', 'Consolidate Duplicate Conditional Fragments']
- Possible solution - 
```java
class TwinCityWeather {
    ...

    public void addWeather(int city, int temperature) {
        if (city == 1) {
            weather1.add(new Temperature(temperature));
        } else if (city == 2) {
            weather2.add(new Temperature(temperature));
        }
    }
    
    ...
}

// Usage in main method
twinCityWeatherSeries.addWeather(1, 10);
twinCityWeatherSeries.addWeather(1, 20);
twinCityWeatherSeries.addWeather(1, 30);
twinCityWeatherSeries.addWeather(2, 15);
twinCityWeatherSeries.addWeather(2, 25);
twinCityWeatherSeries.addWeather(2, 35);
```

- Code smell no. - 4
- Code smell name - Long Method
- Code smell description - A method that is excessively long and does too much in a single method scope.
- Found in line no. - 20, 53
- Possible treatments - ['Extract Method', 'Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object', 'Decompose Conditional']
- Possible solution - 
```java
public void printWeather(TwinCityWeather weather) {
    System.out.println("Weather Data: ");
    for (Temperature temp : weather.getWeatherData()) {
        System.out.println(temp);
    }
}

public void printEachCityWeather() {
    printWeather(city1Weather);
    printWeather(city2Weather);
}

public double averageAcross2Weathers(TwinCityWeather weather1, TwinCityWeather weather2) {
    return calculateAverage(weather1) + calculateAverage(weather2);
}

private double calculateAverage(TwinCityWeather weather) {
    ...
}
```
