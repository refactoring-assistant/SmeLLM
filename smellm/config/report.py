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
