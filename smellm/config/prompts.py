from code_smells import CODE_SMELLS_WITH_DESCRIPTION
from report import REPORT_TEMPLATE

# SYSTEM_PROMPT = f'''You are an expert code smell detector! You are always to the point and precise.
# You will be given a code snippet and you have to identify all the code smells in it. Sometimes there might be no code smells.
# You can identify the following code smells and provide treatments from the given list: {FOWLER_CODE_SMELLS}. Use the following 
# template to generate the report: {REPORT_TEMPLATE}
# '''

SYSTEM_PROMPT = f'''You are a code smell detector. You are always given a file of code in Java. You have to go through the code and detect code smells using their given descriptions
to find them as listed in the code smell list given to you and return a message in the report format given to you.

In the code file given to you, there may or may not be a code smell. If a code smell exists in the file, it is in the code smell list.

Code smell list: """
{CODE_SMELLS_WITH_DESCRIPTION}
"""
Report format: """
{REPORT_TEMPLATE}
"""
'''

# ZERO SHOT PROMPT
ZS_USER_PROMPT = '''Find code smells given in the code below'''

# FEW SHOT PROMPT

FS_USER_PROMPT = '''

Find code smells given in the code to you.

Below are 2 examples of code files with the correct code smells identified in them.
You need to look at the 3rd code file and find the code smell in it.

Code 1:

enum ConnectionState {
    CONNECTED,
    FAILURE,
    NOTCONNECTED
}

class MongoDBConnector {
    private ConnectionState state;

    public MongoDBConnector() {
        this.state = ConnectionState.NOTCONNECTED;
    }

    public boolean isCredentialsValid(int port, String host, String username, String password) {
        if (port < 0 || port > 65535) {
            throw new IllegalArgumentException("Port is invalid");
        }

        if (!host.startsWith("http")) {
            throw new IllegalArgumentException("Host is invalid");
        }

        return true;
    }

    public boolean testConnection(int port, String host, String username, String password) {
        if (Math.random() > 0.1) {
            System.out.println("Connection to: " + host + ":" + port + "/" + username + "&" + password + "successful");
            return true;
        } else {
            System.out.println("Connection to: " + host + ":" + port + "/" + username + "&" + password + "failed");
            return false;
        }
    }

    public void connectToDatabase(int port, String host, String username, String password)
            throws IllegalArgumentException {
        if (!isCredentialsValid(port, host, username, password)) {
            this.state = ConnectionState.FAILURE;
            throw new IllegalArgumentException("Invalid database credentials");
        }

        System.out.println("Testing connection...");

        if (!testConnection(port, host, username, password)) {
            this.state = ConnectionState.FAILURE;
            throw new IllegalArgumentException(
                    "Failed trying to connect to database: " + host + ":" + port + "/" + username + "&" + password);
        }

        System.out
                .println("Connection to database estabilished: " + host + ":" + port + "/" + username + "&" + password);
        this.state = ConnectionState.CONNECTED;
    }

    public String getCurrentState() {
        return "State: " + this.state;
    }
}

public class DCBE1 {
    public static void main(String[] args) {
        MongoDBConnector mongodb = new MongoDBConnector();
        mongodb.connectToDatabase(27017, "http://localhost", "yash", "fn023uc");
    }
}

Code smells identified: 
- Data Clumps (lines 2-5)

Code 2:

import java.util.HashMap;
import java.util.Map;

class Product {
    private String name;
    private String type;
    private int stock;

    public Product(String name, String type, int stock) {
        this.name = name;
        this.type = type;
        this.stock = stock;
    }

    public int getStock() {
        return this.stock;
    }

    public void reduceStock() {
        this.stock -= 1;
    }

    public void showDetails(int id) {
        System.out.println("Name: " + this.name);
        System.out.println("Type: " + this.type);
        System.out.println("Stock: " + this.stock);
    }
}

class ProductManager {
    Map<Integer, ProductHandler> products;

    public ProductManager() {
        this.products = new HashMap<>();
    }

    public void addProduct(int id, ProductHandler product) {
        products.put(id, product);
    }

    public void removeProduct(int id) {
        products.remove(id);
    }

    public void showTotalStock() {
        int totalStock = 0;
        for (Map.Entry<Integer, ProductHandler> product : products.entrySet()) {
            totalStock += product.getValue().getStock();
        }
        System.out.println("Total Stock of all Products: " + totalStock);
    }

}

class ProductHandler {
    private Product product;
    private String name;
    private int id;

    public ProductHandler(Product product, String name, int id) {
        this.product = product;
        this.name = name;
        this.id = id;
    }

    public int getStock() {
        return product.getStock();
    }

    public void printDetails() {
        System.out.println("Name: " + this.name + "\nId: " + this.id);
    }
    

}

public class MMBE1 {

    public static void main(String[] args) {
        Product redsoxcap = new Product("Baseball Cap", "Hat", 10);
        ProductHandler redsoxcapHandler = new ProductHandler(redsoxcap, "CapHandler", 123);
        Product stanley = new Product("Stanley Cup", "Mug", 15);
        ProductHandler stanleyHandler = new ProductHandler(stanley, "MugHandler", 234);
        ProductManager pm = new ProductManager();
        pm.addProduct(1, redsoxcapHandler);
        pm.addProduct(2, stanleyHandler);
        pm.showTotalStock();
        redsoxcap.reduceStock();
        pm.showTotalStock();
    }

}

Code smells identified: 
- Middle Man (lines 55-66)
- Data Class (line 55-66)

Code 3:

'''

# CHAIN OF THOUGHT PROMPT

COT_USER_PROMPT = '''
Find code smells given in the code to you.

Below are 2 examples of code files with the correct code smells identified in them.
You need to look at the 3rd code file and find the code smell in it.

Code 1:

enum ConnectionState {
    CONNECTED,
    FAILURE,
    NOTCONNECTED
}

class MongoDBConnector {
    private ConnectionState state;

    public MongoDBConnector() {
        this.state = ConnectionState.NOTCONNECTED;
    }

    public boolean isCredentialsValid(int port, String host, String username, String password) {
        if (port < 0 || port > 65535) {
            throw new IllegalArgumentException("Port is invalid");
        }

        if (!host.startsWith("http")) {
            throw new IllegalArgumentException("Host is invalid");
        }

        return true;
    }

    public boolean testConnection(int port, String host, String username, String password) {
        if (Math.random() > 0.1) {
            System.out.println("Connection to: " + host + ":" + port + "/" + username + "&" + password + "successful");
            return true;
        } else {
            System.out.println("Connection to: " + host + ":" + port + "/" + username + "&" + password + "failed");
            return false;
        }
    }

    public void connectToDatabase(int port, String host, String username, String password)
            throws IllegalArgumentException {
        if (!isCredentialsValid(port, host, username, password)) {
            this.state = ConnectionState.FAILURE;
            throw new IllegalArgumentException("Invalid database credentials");
        }

        System.out.println("Testing connection...");

        if (!testConnection(port, host, username, password)) {
            this.state = ConnectionState.FAILURE;
            throw new IllegalArgumentException(
                    "Failed trying to connect to database: " + host + ":" + port + "/" + username + "&" + password);
        }

        System.out
                .println("Connection to database estabilished: " + host + ":" + port + "/" + username + "&" + password);
        this.state = ConnectionState.CONNECTED;
    }

    public String getCurrentState() {
        return "State: " + this.state;
    }
}

public class DCBE1 {
    public static void main(String[] args) {
        MongoDBConnector mongodb = new MongoDBConnector();
        mongodb.connectToDatabase(27017, "http://localhost", "yash", "fn023uc");
    }
}

Code smells identified: 
- Data Clumps (lines 2-5) 
    Reason for code smell 'Data Clumps': Code contain identical groups of variables in parameters or fields and are reused throughout.

Code 2:

import java.util.HashMap;
import java.util.Map;

class Product {
    private String name;
    private String type;
    private int stock;

    public Product(String name, String type, int stock) {
        this.name = name;
        this.type = type;
        this.stock = stock;
    }

    public int getStock() {
        return this.stock;
    }

    public void reduceStock() {
        this.stock -= 1;
    }

    public void showDetails(int id) {
        System.out.println("Name: " + this.name);
        System.out.println("Type: " + this.type);
        System.out.println("Stock: " + this.stock);
    }
}

class ProductManager {
    Map<Integer, ProductHandler> products;

    public ProductManager() {
        this.products = new HashMap<>();
    }

    public void addProduct(int id, ProductHandler product) {
        products.put(id, product);
    }

    public void removeProduct(int id) {
        products.remove(id);
    }

    public void showTotalStock() {
        int totalStock = 0;
        for (Map.Entry<Integer, ProductHandler> product : products.entrySet()) {
            totalStock += product.getValue().getStock();
        }
        System.out.println("Total Stock of all Products: " + totalStock);
    }

}

class ProductHandler {
    private Product product;
    private String name;
    private int id;

    public ProductHandler(Product product, String name, int id) {
        this.product = product;
        this.name = name;
        this.id = id;
    }

    public int getStock() {
        return product.getStock();
    }

    public void printDetails() {
        System.out.println("Name: " + this.name + "\nId: " + this.id);
    }
    

}

public class MMBE1 {

    public static void main(String[] args) {
        Product redsoxcap = new Product("Baseball Cap", "Hat", 10);
        ProductHandler redsoxcapHandler = new ProductHandler(redsoxcap, "CapHandler", 123);
        Product stanley = new Product("Stanley Cup", "Mug", 15);
        ProductHandler stanleyHandler = new ProductHandler(stanley, "MugHandler", 234);
        ProductManager pm = new ProductManager();
        pm.addProduct(1, redsoxcapHandler);
        pm.addProduct(2, stanleyHandler);
        pm.showTotalStock();
        redsoxcap.reduceStock();
        pm.showTotalStock();
    }

}

Code smells identified: 
- Middle Man (lines 55-66)
    Reason for code smell 'Middle Man': A class performs only one action, delegating work to another class
- Data Class (line 55-66)
    Reason for code smell 'Data Class': A class only holds a constructor, fields and their getters and setters and absolutely nothing else.

Code 3:


'''