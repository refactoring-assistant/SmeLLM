import os  # Import the os module

# Get the directory path of the current file
DEFAULT_PATH = os.path.dirname(__file__)

# Create the full path to the .env file in the same directory
ENV_PATH = os.path.join(DEFAULT_PATH, '.env')

JAVA_FILE_EXTENSION = '.java'  # Define the Java file extension
TYPESCRIPT_FILE_EXTENSION = '.ts'  # Define the TypeScript file extension
TYPESCRIPT_JSX_FILE_EXTENSION = '.tsx'  # Define the TypeScript JSX file extension