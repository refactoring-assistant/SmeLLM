import re
import os
from rapidfuzz import fuzz
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import config.constants as constants

class OutputSmellExtractor():
    def __init__(self, output_path, code_smells=None):
        self.output_path = output_path
        self.smell_data = code_smells

    def match_with_smell_list(self, extracted_smells, threshold=70):

        matched_smells = set()
        
        for smell in extracted_smells:
            best_match = None
            best_score = 0
            extracted_name = smell
            
            for fowler_smell in self.smell_data:
                score = fuzz.ratio(extracted_name.lower(), fowler_smell.lower())
                
                if score > best_score:
                    best_score = score
                    best_match = fowler_smell
            
            if best_score >= threshold:
                matched_smells.add(best_match)
            else:
                print(f"Warning: Could not match '{extracted_name}' with any Fowler smell above threshold.")
                
        return list(matched_smells)

    def process_documents(self):
        detected_code_smells = {}
        file_list = os.listdir(self.output_path)
        for file_name in file_list:
            print(f"Processing file: {file_name}")
            if file_name.endswith('.md'):
                file_path = os.path.join(self.output_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    # Comprehensive regex pattern to handle all variations:
                    # - Optional leading whitespace/indentation
                    # - Optional bold markers around "Code smell name" (**Code smell name** or Code smell name)
                    # - Both regular dash (-) and em dash (–)
                    # - Optional bold markers around the smell name itself
                    # - Captures the code smell name (stripping bold markers if present)
                    # Pattern breakdown:
                    # \s*-\s*                    : Optional whitespace, dash, optional whitespace
                    # \*?\*?Code smell name\*?\*? : "Code smell name" with optional ** on both sides
                    # \s*[–-]\s*                 : Separator (space, dash/em-dash, space)
                    # (?:                        : Non-capturing group for optional bold markers
                    #   \*\*([^*]+?)\*\*         : Bold name: **name**
                    #   |                        : OR
                    #   ([^\n]+?)                : Non-bold name (capture until newline)
                    # )
                    # (?=\s*\n|$)                : Lookahead for end of line
                    pattern = r'\s*-\s*\*?\*?Code smell name\*?\*?\s*[–-]\s*(?:\*\*([^*]+?)\*\*|([^\n]+?))(?=\s*\n|$)'
                    matches = re.findall(pattern, content, re.MULTILINE)
                    main_file_name = file_name.split('_')[-1]
                    # Extract from tuple (first group is bold, second is non-bold)
                    code_smells = []
                    for match in matches:
                        # match is a tuple: (bold_name, non_bold_name) - one will be empty
                        smell_name = match[0] if match[0] else match[1]
                        if smell_name.strip():
                            code_smells.append(smell_name.strip())

                    detected_code_smells[main_file_name] = self.match_with_smell_list(code_smells, threshold=70)
        return detected_code_smells
    

if __name__ == "__main__":
    
    # Path to your file
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../', 'java_single_file_code_smells/gpt-4o')
    smellExtractor = OutputSmellExtractor(output_path=folder_path, code_smells=constants.CODE_SMELLS)
    
    detected_code_smells = smellExtractor.process_documents()
    print(detected_code_smells)
    print("all matcher")
    print(len(detected_code_smells))
    # matched_smells = smellExtractor.match_with_smell_list(detected_code_smells, threshold=90)
    # print(matched_smells)