import os
import sys
import pandas as pd
import ast
import re

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
        tp_data = merged_df.apply(self.__count_tp, axis=1)
        fp_data = merged_df.apply(self.__count_fp, axis=1)
        fn_data = merged_df.apply(self.__count_fn, axis=1)
        tn_data = merged_df.apply(self.__count_tn, axis=1)
        matrix_data = {
            'True Positives': tp_data,
            'False Positives': fp_data,
            'False Negatives': fn_data,
            'True Negatives': tn_data
        }
        merged_df['True Positives'] = tp_data.apply(lambda x: x['count'])
        merged_df['False Positives'] = fp_data.apply(lambda x: x['count'])
        merged_df['False Negatives'] =  fn_data.apply(lambda x: x['count'])
        merged_df['True Negatives'] = tn_data.apply(lambda x: x['count'])
        self.tp = sum(merged_df['True Positives'])
        self.fp = sum(merged_df['False Positives'])
        self.fn = sum(merged_df['False Negatives'])
        self.tn = sum(merged_df['True Negatives'])
        self.test_file_handler.save_test(merged_df, self.__calculate_conf_matrix_vals(), self.__calculate_individual_smell_counts(matrix_data, merged_df))
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
    
    def __calculate_individual_smell_counts(self, matrix_data, evaluation_data):
        individual_code_smell_data = {
            'Code Smells': constants.EXCEL_CODE_SMELLS_LIST,
            'Expected': [0] * len(constants.EXCEL_CODE_SMELLS_LIST),
            'Detected Accurately': [0] * len(constants.EXCEL_CODE_SMELLS_LIST),
            'Detected Falsely': [0] * len(constants.EXCEL_CODE_SMELLS_LIST),
            'Not Detected': [0] * len(constants.EXCEL_CODE_SMELLS_LIST)
        }

        individual_df = pd.DataFrame(individual_code_smell_data)

        correctly_detected = matrix_data['True Positives'].apply(lambda x: x['code_smells'])
        falsely_detected = matrix_data['False Positives'].apply(lambda x: x['code_smells'])
        not_detected = matrix_data['False Negatives'].apply(lambda x: x['code_smells'])
        total_not_expected = evaluation_data.apply(
            lambda row: 1 if (
                isinstance(row['Expected Code Smells'], list) and len(row['Expected Code Smells']) == 0 
            ) else 0,
            axis=1
        ).sum()

        metrics_data = {
            'Correctly Detected': correctly_detected,
            'Falsely Detected': falsely_detected,
            'Not Detected': not_detected,
            'Total Not Expected': total_not_expected
        }

        individual_df = self.__get_individual_counts(individual_df, metrics_data)
        individual_df = self.__count_main_classes(individual_df)
        individual_df.loc[individual_df['Code Smells'] == 'No Smell Intended', 'Detected Accurately'] = sum(evaluation_data['True Negatives'])
        individual_df.loc[individual_df['Code Smells'] == 'No Smell Intended', 'Expected'] = metrics_data['Total Not Expected']
        individual_df.loc[individual_df['Code Smells'] == 'No Smell Intended', 'Not Detected'] = metrics_data['Total Not Expected'] - sum(evaluation_data['True Negatives'])

        return individual_df
            
    def __count_tp(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']

        tp_data = {'code_smells': [], 'count': 0}
        
        # Find intersection
        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            code_smells_intersection = set(expected_smells).intersection(set(detected_smells))
            tp_data['code_smells'] = code_smells_intersection
            tp_data['count'] = len(code_smells_intersection)

        return tp_data
        
    def __count_fp(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']
        
        fp_data = {'code_smells': [], 'count': 0}
        # Find false positives using set subtraction
        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            code_smells_difference = set(detected_smells) - set(expected_smells)
            fp_data['code_smells'] = code_smells_difference
            fp_data['count'] = len(code_smells_difference)
            
        return fp_data
          
        
    def __count_fn(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']

        fn_data = {'code_smells': [], 'count': 0}
        
        # Find false positives using set subtraction
        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            code_smells_difference = set(expected_smells) - set(detected_smells)
            fn_data['code_smells'] = code_smells_difference
            fn_data['count'] = len(code_smells_difference)
        
        return fn_data
        
    def __count_tn(self, row):
        expected_smells = row['Expected Code Smells']
        detected_smells = row['Detected Code Smells']

        tn_data = {'code_smells': [], 'count': 0}

        if isinstance(expected_smells, list) and isinstance(detected_smells, list):
            if len(expected_smells) == 0 and len(detected_smells) == 0:
                tn_data['count'] = 1
        return tn_data
            
        
    def __format_row_smell(self, row_smell):
        if isinstance(row_smell, str):
            try:
                row_smell = ast.literal_eval(row_smell)
            except (ValueError, SyntaxError):
                # Split the string and clean each element
                row_smell = [self.__clean_string(s.strip()) for s in row_smell.strip('[]').strip("'").strip('"').split(',')]
        
        # If we have a list, clean each element in the list
        if isinstance(row_smell, list):
            row_smell = [self.__clean_string(s) if isinstance(s, str) else s for s in row_smell]
                
        return row_smell

    def __clean_string(self, text):
            # Keep only alphanumeric characters and spaces
            return re.sub(r'[^a-zA-Z0-9 ]', '', text)
    
    def __get_individual_counts(self, individual_df, metrics_data):
        correctly_detected = metrics_data['Correctly Detected']
        falsely_detected = metrics_data['Falsely Detected']  
        not_detected = metrics_data['Not Detected']

        # count = 0
        for index, row in individual_df.iterrows():
            code_smell = row['Code Smells']
            
            # Count correctly detected
            individual_df.at[index, 'Detected Accurately'] = sum(code_smell in smells for smells in correctly_detected)
            
            # Count falsely detected
            individual_df.at[index, 'Detected Falsely'] = sum(code_smell in smells for smells in falsely_detected)
            
            # Count not detected
            individual_df.at[index, 'Not Detected'] = sum(code_smell in smells for smells in not_detected)

            # for smells in falsely_detected:
            #     if code_smell in smells:
            #         print(f"Code smell {code_smell} falsely detected in: {smells}")
            #         count += 1

            # Expected count
            individual_df.at[index, 'Expected'] = individual_df.at[index, 'Detected Accurately'] + individual_df.at[index, 'Not Detected']
        
        return individual_df
    
    def __count_main_classes(self, individual_df):
        df_detect_accurate = 0
        df_detect_falsely = 0
        df_not_detected = 0
        df_expected = 0
        
        for main_class in constants.EXCEL_MAIN_CODE_SMELL_LIST:
            detected_accurately_count = 0
            falsely_detected_count = 0
            not_detected_count = 0
            total_expected = 0
            for class_name, sub_smells in main_class.items():
                
                for smell in sub_smells:
                    detected_accurately_count += individual_df[individual_df['Code Smells'] == smell]['Detected Accurately'].sum()
                    falsely_detected_count += individual_df[individual_df['Code Smells'] == smell]['Detected Falsely'].sum()
                    not_detected_count += individual_df[individual_df['Code Smells'] == smell]['Not Detected'].sum()
                    total_expected += individual_df[individual_df['Code Smells'] == smell]['Expected'].sum()
                
                individual_df.loc[individual_df['Code Smells'] == class_name, 'Detected Accurately'] = detected_accurately_count
                individual_df.loc[individual_df['Code Smells'] == class_name, 'Detected Falsely'] = falsely_detected_count
                individual_df.loc[individual_df['Code Smells'] == class_name, 'Not Detected'] = not_detected_count
                individual_df.loc[individual_df['Code Smells'] == class_name, 'Expected'] = total_expected
            
            df_detect_accurate += detected_accurately_count
            df_detect_falsely += falsely_detected_count
            df_not_detected += not_detected_count
            df_expected += total_expected
        
        individual_df.loc[individual_df['Code Smells'] == 'Totals', 'Detected Accurately'] = df_detect_accurate
        individual_df.loc[individual_df['Code Smells'] == 'Totals', 'Detected Falsely'] = df_detect_falsely
        individual_df.loc[individual_df['Code Smells'] == 'Totals', 'Not Detected'] = df_not_detected
        individual_df.loc[individual_df['Code Smells'] == 'Totals', 'Expected'] = df_expected
        print(f"Updated Totals: {individual_df.loc[individual_df['Code Smells'] == 'Totals']}")
        return individual_df


if __name__ == "__main__":
    # Path to the directory containing documents
    output_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../', 'java_single_file_code_smells/gpt-4o-mini')
    
    # Path to the test file (if needed)
    test_file_path = 'TEST-4o-mini-trial.xlsx'
    
    # Create an instance of TestOutput
    test_output = TestOutput(output_dir_path, test_file_path)
    
    # Run the test
    test_output.test()