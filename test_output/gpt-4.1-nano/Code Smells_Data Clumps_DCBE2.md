**Code Review: DCBE2.java**

- Code smell no. - 1
- Code smell name - Large Class
- Code smell description - The class `DCBE2` contains multiple responsibilities, including managing weather data, printing data, and comparing weather patterns, which makes it complex and difficult to maintain.
- Found in line no. - 62-78
- Possible treatments - Extract Class, Extract Subclass
- Possible solution - Separate weather data management, printing, and comparison functionalities into dedicated classes such as `WeatherData`, `WeatherPrinter`, and `WeatherComparator`.