import os
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# Import constants - this already handles loading the code smells from JSON
import config.constants as constants

class OutputSmellExtractor:
    def __init__(self, directory_path, code_smells=None):
        """
        Initialize the OutputSmellExtractor with directory path and code smells.
        
        Args:
            directory_path: Path to directory containing .md files to analyze
            code_smells: List of code smells (optional, if not provided will use constants.CODE_SMELLS)
        """
        self.directory_path = directory_path
        
        # Use provided code smells or default to constants.CODE_SMELLS
        # constants.CODE_SMELLS is already loaded from the JSON file in constants.py
        self.code_smells = code_smells if code_smells else constants.CODE_SMELLS

    def find_code_smells_in_document(self, file_path):
        """
        Find code smells in a document.
        
        Args:
            file_path: Path to the document
            
        Returns:
            Set of detected code smells
        """
        detected_smells = set()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for smell in self.code_smells:
                    if re.search(rf'\b{re.escape(smell)}\b', content, re.IGNORECASE):
                        detected_smells.add(smell)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
        
        return detected_smells

    def process_documents(self):
        """
        Process all .md documents in the directory path.
        
        Returns:
            Dictionary mapping file names to detected code smells
        """
        results = {}
        try:
            for root, _, files in os.walk(self.directory_path):
                for file_name in files:
                    if file_name.endswith('.md'): 
                        file_path = os.path.join(root, file_name)
                        main_file_name = self.__main_file_match_rule(file_name)
                        print(f"Processing file: {file_name}")
                        detected_smells = list(self.find_code_smells_in_document(file_path))
                        results[main_file_name] = detected_smells
        except Exception as e:
            print(f"Error walking directory {self.directory_path}: {e}")
        
        return results

    def __main_file_match_rule(self, file_name):
        """
        Extract the main file name from the file name.
        
        Args:
            file_name: Name of the file
            
        Returns:
            Main file name
        """
        return file_name.split('_')[-1]

if __name__ == "__main__":
    # Path to the directory containing documents
    directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../', 'java_single_file_code_smells/gpt-4o')
    
    # Create an instance of OutputSmellExtractor
    # No need to pass the JSON path as constants.CODE_SMELLS is already loaded
    detector = OutputSmellExtractor(directory_path)
    
    # Process documents and get results
    detected_code_smells = detector.process_documents()
    
    # Print results
    print("Detected code smells by file:")
    for file_name, smells in detected_code_smells.items():
        print(f"{file_name}: {', '.join(smells) if smells else 'No code smells detected'}")
    
    print("\nDetection complete!")