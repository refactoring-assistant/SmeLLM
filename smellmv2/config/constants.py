import os  # Import the os module

# Get the directory path of the current file
DEFAULT_PATH = os.path.dirname(__file__)

# Create the full path to the .env file in the same directory
ENV_PATH = os.path.join(DEFAULT_PATH, '.env')

JAVA_FILE_EXTENSIONS = ['.java']  # Define the Java file extension
TYPESCRIPT_FILE_EXTENSIONS = ['.ts', '.tsx']  # Define the TypeScript file extension

SUPPORTED_LANGUAGES = ['java', 'typescript']  # Define the supported languages

FOWLER_CODE_SMELLS = ['Long Method', 'Large Class', 'Primitive Obsession', 'Long Parameter List', 'Data Clumps', 
                      'Switch Statements', 'Temporary Field', 'Refused Bequest', 'Alternative Classes with Different Interfaces', 
                      'Divergent Change', 'Shotgun Surgery', 'Parallel Inheritance Hierarchies', 
                      'Comments', 'Duplicate Code', 'Lazy Class', 'Data Class', 'Dead Code', 'Speculative Generality',
                      'Feature Envy', 'Inappropriate Intimacy', 'Message Chains', 'Middle Man',
                      'Incomplete Library Class']  # Define the code smells

REPORT_FORMAT = '''
**Code Review: <Insert file name>**
    - Code smell no. - <index>
    - Code smell name - <Name of the code smell from the code smell list>
    - Code smell description - <Description of the code smell>
    - Found in line no. - <List of line numbers code smell was observed at. Line numbers will be given as (~number~), return a number normally.>
    - Possible solution - <A possible solution to the code smell shown by redefining the whole code file.>
'''

SYSTEM_PROMPT = f'''You are an expert code smell detector! You are always to the point and precise.
You will be given a code snippet and you have to identify all the code smells in it. Sometimes there might be no code smells.
You can identify the following code smells: {FOWLER_CODE_SMELLS}
The format of the report should be as follows:
{REPORT_FORMAT}
'''

USER_PROMPT = '''Generate a code smell report in markdown for the given code snippet:\n'''