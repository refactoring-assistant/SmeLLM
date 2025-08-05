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

CODE_SMELLS_WITH_TREATMENTS = [
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
