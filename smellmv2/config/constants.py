import os  # Import the os module
import json

# Get the directory path of the current file
CONFIG_DEFAULT_PATH = os.path.dirname(__file__)

# Create the full path to the .env file in the same directory
ENV_PATH = os.path.join(CONFIG_DEFAULT_PATH, '.env')

MODELS_LIST = os.path.join(CONFIG_DEFAULT_PATH, 'models_list.json')
CODE_SMELL_LIST = os.path.join(CONFIG_DEFAULT_PATH, 'code_smell_list.json')

def extract_code_smell_list(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        code_smells = json.load(file)
        # Extract the "name" field from each object
        code_smell_names = [smell["name"] for smell in code_smells]
    return {"code_smell_names": code_smell_names, "code_smell_names_and_treatments": code_smells}

CODE_SMELL_DATA = extract_code_smell_list(CODE_SMELL_LIST)
CODE_SMELLS_WITH_TREATMENTS = CODE_SMELL_DATA["code_smell_names_and_treatments"]
CODE_SMELLS = CODE_SMELL_DATA["code_smell_names"]


JAVA_FILE_EXTENSIONS = ['.java']  # Define the Java file extension
TYPESCRIPT_FILE_EXTENSIONS = ['.ts', '.tsx']  # Define the TypeScript file extension

SUPPORTED_LANGUAGES = ['java', 'typescript']  # Define the supported languages


#have to replace this with CODE_SMELLS_WITH_TREATMENTS and check if it works
FOWLER_CODE_SMELLS = [
    {
        "name": "Long Method",
        "treatments": ["Extract Method", "Replace Temp with Query, Introduce Parameter Object or Preserve Whole Object", "Decompose Conditional"]
    },
    {
        "name": "Large Class",
        "treatments": ["Extract Class", "Extract Subclass", "Extract Interface", "Duplicate Observed Data"]
    },
    {
        "name": "Primitive Obsession",
        "treatments": ["Replace Data Value with Object", "Introduce Parameter Object or Preserve Whole Object",
                        " Replace Type Code with Class, Replace Type Code with Subclasses or Replace Type Code with State/Strategy", 
                        "Replace Array with Object"]
    },
    {
        "name": "Long Parameter List",
        "treatments": ["Replace Parameter with Method Call", "Preserve Whole Object", "Introduce Parameter Object"]
    },
    {
        "name": "Data Clumps",
        "treatments": ["Extract Class", "Introduce Parameter Object", "Preserve Whole Object"]
    },
    {
        "name": "Switch Statements",
        "treatments": ["Extract Method & then Move Method", "Replace Type Code with Subclasses or Replace Type Code with State/Strategy", 
                       " Replace Conditional with Polymorphism", "Replace Parameter with Explicit Methods", "Introduce Null Object"]
    },
    {
        "name": "Temporary Field",
        "treatments": ["Extract Class or Replace Method with Method Object.", "Introduce Null Object"]
    },
    {
        "name": "Refused Bequest",
        "treatments": ["Replace Inheritance with Delegation", "Extract Superclass"]
    },
    {
        "name": "Alternative Classes with Different Interfaces",
        "treatments": ["Rename Method", "Move Method, Add Parameter & Parameterize Method", "Extract Superclass"]
    },
    {
        "name": "Divergent Change",
        "treatments": ["Extract Class", "Extract Superclass & Extract Subclass"]
    },
    {
        "name": "Shotgun Surgery",
        "treatments": ["Move Method & Move Field", "Inline Class"]
    },
    {
        "name": "Parallel Inheritance Hierarchies",
        "treatments": ["Move Method & Move Field"]
    },
    {
        "name": "Comments",
        "treatments": ["Extract Variable", "Extract Method", "Rename Method", "Introduce Assertion"]
    },
    {
        "name": "Duplicate Code",
        "treatments": ["Extract Method", "Extract Method & Pull Up Field", "Pull Up Constructor Body",
                       "Form Template Method", "Substitute Algorithm", "Extract Superclass", "Extract Class"
                       "Consolidate Conditional Expression and use Extract Method", "Consolidate Duplicate Conditional Fragments"]
    },
    {
        "name": "Lazy Class",
        "treatments": ["Inline Class", "Collapse Hierarchy"]
    }, 
    {
        "name": "Data Class",
        "treatments": ["Encapsulate Field", "Encapsulate Collection ", "Move Method and Extract Method", "Remove Setting Method and Hide Method"]
    },
    {
        "name": "Dead Code",
        "treatments": ["Remove Unused Code", "Inline Class or Collapse Hierarchy", "Remove Parameter"]
    },
    {
        "name": "Speculative Generality",
        "treatments": ["Collapse Hierarchy", "Inline Class", "Inline Method", "Remove Parameter"]
    },
    {
        "name": "Feature Envy",
        "treatments": ["Move Method", "Extract Method", "Extract Method", "Extract Method with Move Method"]
    },
    {
        "name": "Inappropriate Intimacy",
        "treatments": ["Move Method & Move Field", "Extract Class & Hide Delegate", 
                       "Change Bidirectional Association to Unidirectional", " Replace Delegation with Inheritance"]
    },
    {
        "name": "Message Chains",
        "treatments": ["Hide Delegate", "Extract Method & Move Method"]
    },
    {
        "name": "Middle Man",
        "treatments": ["Remove Middle Man"]
    },
    {
        "name": "Incomplete Library Class",
    }
]


CODE_SMELLS = [
    "Long Method",
    "Primitive Obsession",
    "Data Clumps",
    "Large Class",
    "Long Parameter List",
    "Alternative Classes With Different Interfaces",
    "Refused Bequest",
    "Temporary Field",
    "Switch Statements",
    "Divergent Change",
    "Parallel Inheritance Hierarchies",
    "Shotgun Surgery",
    "Comments",
    "Data Class",
    "Lazy Class",
    "Duplicate Code",
    "Dead Code",
    "Speculative Generality",
    "Feature Envy",
    "Incomplete Library Class",
    "Inappropriate Intimacy",
    "Middle Man",
    "Message Chains"
]


CODE_SMELLS_WITH_DESCRIPTION = [
    {
        "name": "Long Method",
        "description": "A method is too long (usually above 10-20 lines) and violates the single responsibility principle"
    },
    {
        "name": "Large Class",
        "description": "A class is too long and violates the single responsibility principle" 
    },
    {
        "name": "Primitive Obsession",
        "description": "Use of primitives instead of small objects for simple tasks (such as currency, ranges, special strings for phone numbers, etc.)" 
    },
    {
        "name": "Long Parameter List",
        "description": "More than three or four parameters for a method" 
    },
    {
        "name": "Data Clumps",
        "description": "Repeated use of identical groups of variables" 
    },
    {
        "name": "Switch Statements",
        "description": "Complex switch operator or sequence of if statements" 
    },
    {
        "name": "Temporary Field",
        "description": "Temporary fields get their values only under certain circumstances. Outside of these circumstances, they're empty" 
    },
    {
        "name": "Refused Bequest",
        "description": "If a subclass uses only some of the methods and properties inherited from its parents. The unneeded methods may simply go unused or be redefined and give off exceptions" 
    },
    {
        "name": "Alternative Classes with Different Interfaces",
        "description": "Two classes perform identical functions but have different method names" 
    },
    {
        "name": "Divergent Change",
        "description": "Having to change many unrelated methods when you make changes to a class" 
    },
    {
        "name": "Shotgun Surgery",
        "description": "Making any modifications requires that you make many small changes to many different classes" 
    },
    {
        "name": "Parallel Inheritance Hierarchies",
        "description": "Creation of a subclass for a class leads to the needing to create a subclass for another class" 
    },
    {
        "name": "Comments",
        "description": "A method is filled with explanatory comments" 
    },
    {
        "name": "Duplicate Code",
        "description": "Two code fragments look almost identical" 
    },
    {
        "name": "Lazy Class",
        "description": "If a class doesn't do much, it can be categorized as a Lazy Class" 
    }, 
    {
        "name": "Data Class",
        "description": "A data class refers to a class that contains only fields and crude methods for accessing them (getters and setters). These are simply containers for data used by other classes. These classes don't contain any additional functionality and can't independently operate on the data that they own" 
    },
    {
        "name": "Dead Code",
        "description": "A variable, parameter, field, method or class is no longer used (usually because it's obsolete)" 
    },
    {
        "name": "Speculative Generality",
        "description": "There's an unused class, method, field or parameter" 
    },
    {
        "name": "Feature Envy",
        "description": "A method accesses the data of another object more than its own data" 
    },
    {
        "name": "Inappropriate Intimacy",
        "description": "One class uses the internal fields and methods of another class" 
    },
    {
        "name": "Message Chains",
        "description": "In code you see a series of calls resembling $a->b()->c()->d()" 
    },
    {
        "name": "Middle Man",
        "description": "A class performs only one action that is delegating work to another class and does nothing else" 
    },
    {
        "name": "Incomplete Library Class",
        "description": "Having to augment a library to suit the users need repeatedly" 
    }
]

EXCEL_CODE_SMELLS_LIST = [
        'Bloaters', 'Long Method', 'Large Class', 'Primitive Obsession', 'Long Parameter List', 'Data Clumps',
        'Object-Orientation Abusers', 'Switch Statements', 'Temporary Field', 'Refused Bequest',
        'Alternative Classes with Different Interfaces', 'Change Preventers', 'Divergent Change', 'Shotgun Surgery',
        'Parallel Inheritance Hierarchies', 'Dispensables', 'Comments', 'Duplicate Code', 'Lazy Class', 'Data Class',
        'Dead Code', 'Speculative Generality', 'Couplers', 'Feature Envy', 'Inappropriate Intimacy',
        'Message Chains', 'Middle Man', 'Other Smells', 'Incomplete Library Class', 'Totals', 'No Smell Intended'
    ]


EXCEL_MAIN_CODE_SMELL_LIST = [
    {'Bloaters': ['Long Method', 'Large Class', 'Primitive Obsession', 'Long Parameter List', 'Data Clumps']},
    {'Object-Orientation Abusers': ['Switch Statements', 'Temporary Field', 'Refused Bequest', 'Alternative Classes with Different Interfaces']},
    {'Change Preventers': ['Divergent Change', 'Shotgun Surgery', 'Parallel Inheritance Hierarchies']},
    {'Dispensables': ['Comments', 'Duplicate Code', 'Lazy Class', 'Data Class', 'Dead Code', 'Speculative Generality']},
    {'Couplers': ['Feature Envy', 'Inappropriate Intimacy', 'Message Chains', 'Middle Man']},
    {'Other Smells': ['Incomplete Library Class']},
]



REPORT_EXTENSION = '.md'

REPORT_TEMPLATE = '''
**Code Review: <Insert file name>**
    - Code smell no. - <index>
    - Code smell name - <Name of the code smell from the code smell list>
    - Code smell description - <Description of the code smell>
    - Found in line no. - <List of line numbers code smell was observed at. Line numbers will be given as (~number~), return a number normally.>
'''

SIMPLE_REPORT_TEMPLATE = '''
Code smell - <Name of code smell from the code smell list>
Found in line - <List of line numbers the code smell was observed at. Line numbers will be given as (~number~), return a number normally.>
'''

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

USER_PROMPT = '''Find the code smell in this file:\n'''

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