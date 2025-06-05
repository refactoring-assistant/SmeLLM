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
        "treatments": ["Introduce Foreign Method", "Introduce Local Extension"]
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
    - Possible treatments - <List of possible treatments that can be applied to the code with respect to the code smell.>
    - Possible solution - <A possible solution to the code smell shown by redefining the whole code file.>
'''

SYSTEM_PROMPT = f'''You are an expert code smell detector! You are always to the point and precise.
You will be given a code snippet and you have to identify all the code smells in it. Sometimes there might be no code smells.
You can identify the following code smells and provide treatments from the given list: {FOWLER_CODE_SMELLS}. Use the following 
template to generate the report: {REPORT_TEMPLATE}
'''

USER_PROMPT = '''Generate a code smell report in markdown for the given code snippet:\n'''