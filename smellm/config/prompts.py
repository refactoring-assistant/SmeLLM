from .code_smells import CODE_SMELLS
OUTPUT_FORMAT = '[{"code_smell": "<Name of the code smell detected>","line_numbers": [<List of line numbers where the code smell is detected>]}]'

ZERO_SHOT_SYSTEM_PROMPT = f"""
# Identity

You are an expert code smell detector.
You will be given a code snippet and you have to identify all the possible code smells in it (there can be multiple).
Sometimes there might be no code smells.

# Instructions

* Only look for these code smells: {', '.join([f"{smell['name']}" for smell in CODE_SMELLS])}
"""

# * Only look for these code smells: \n - {'\n - '.join([f"{smell['name']}: {smell['description']}" for smell in CODE_SMELLS])}

FEW_SHOT_SYSTEM_PROMPT = f"""
{ZERO_SHOT_SYSTEM_PROMPT}

# Examples
"""

print(ZERO_SHOT_SYSTEM_PROMPT)