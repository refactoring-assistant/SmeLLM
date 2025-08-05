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