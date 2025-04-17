import os
import sys
import pandas as pd
import ast

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import config.constants as constants
from content_extractors.output_smell_details_extractor import OutputSmellExtractor
from content_extractors.test_file_handler_excel import ExcelTestHandler

class TestOutput:
    def __init__(self, output_dir_path, test_file_path):
        if output_dir_path is None:
            print('Output directory path is None. Please provide a valid output directory path.')
        if test_file_path is None:
            print('Test file path is None. Please provide a valid test file path.')
        self.code_smell_extractor = OutputSmellExtractor(output_dir_path, constants.CODE_SMELLS)
        self.test_file_handler = ExcelTestHandler(test_file_path)
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0
    
    def test(self):
        # Test the output of the code smell extractor
        detected_code_smells = self.code_smell_extractor.process_documents()
        detected_df = self.__convert_smell_to_df(detected_code_smells)
        dataframe = self.test_file_handler.import_test()
        merged_df = self.__merge_dataframes(dataframe, detected_df)
        merged_df['True Positives'] = merged_df.apply(self.__count_tp, axis=1)
        merged_df['False Positives'] = merged_df.apply(self.__count_fp, axis=1)
        merged_df['False Negatives'] = merged_df.apply(self.__count_fn, axis=1)
        merged_df['True Negatives'] = merged_df.apply(self.__count_tn, axis=1)
        self.tp = sum(merged_df['True Positives'])
        self.fp = sum(merged_df['False Positives'])
        self.fn = sum(merged_df['False Negatives'])
        self.tn = sum(merged_df['True Negatives'])
        self.test_file_handler.save_test(merged_df, self.__calculate_conf_matrix_vals())
        print("Test completed successfully.")
        
    def __convert_smell_to_df(self, detected_code_smells):
        # Convert the detected code smells to a DataFrame
        data = []
        for file_name, smells in detected_code_smells.items():
            main_file = file_name.split('.')[0]
            data.append({"File Name": main_file, "Detected Code Smells": smells})
        return pd.DataFrame(data)
    
    def __merge_dataframes(self, df1, df2):
        # Merge two DataFrames on 'File Name' column
        try:
            merged_df = pd.merge(df1, df2, on='File Name', how='inner')
            merged_df['Expected Code Smells'] = merged_df['Expected Code Smells'].apply(self.__format_row_smell)
            merged_df['Detected Code Smells'] = merged_df['Detected Code Smells'].apply(self.__format_row_smell)
            return merged_df
        except KeyError as e:
            print(f"KeyError: {e}. Please check the column names in the DataFrames.")
            return exit(1)
    
    def __calculate_conf_matrix_vals(self):
        precision = self.tp/(self.tp + self.fp) if (self.tp + self.fp) > 0 else 0
        recall = self.tp/(self.tp + self.fn) if (self.tp + self.fn) > 0 else 0

        result_df = pd.DataFrame({
            "Metric": ["True Positives", "False Positives", "False Negatives", "True Negatives", "Precision", "Recall"],
            "Value": [self.tp, self.fp, self.fn, self.tn, precision, recall]
        })

        
        return result_df
        
    def __count_tp(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']
        
        # Find intersection
        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            return len(set(expected_smells).intersection(set(detected_smells)))
        else:
            return 0
        
    def __count_fp(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']
        
        # Find false positives using set subtraction
        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            return len(set(detected_smells) - set(expected_smells))
        else:
            return 0
        
    def __count_fn(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']
        
        # Find false positives using set subtraction
        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            return len(set(expected_smells) - set(detected_smells))
        else:
            return 0
        
    def __count_tn(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']

        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            if len(expected_smells) == 0 and len(detected_smells) == 0:
                return 1
        return 0
            
        
    def __format_row_smell(self, row_smell):
        if isinstance(row_smell, str):
            try:
                row_smell = ast.literal_eval(row_smell)
            except (ValueError, SyntaxError):
                row_smell = [s.strip() for s in row_smell.strip('[]').split(',')]
        return row_smell


if __name__ == "__main__":
    # Path to the directory containing documents
    output_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../', 'java_single_file_code_smells/gpt-4o-mini')
    
    # Path to the test file (if needed)
    test_file_path = 'TEST-4o-mini.xlsx'
    
    # Create an instance of TestOutput
    test_output = TestOutput(output_dir_path, test_file_path)
    
    # Run the test
    test_output.test()