# This is a Python Script that read the test result excel sheet from SmeLLM tool end-to-end
# This script will calculate the 4 metrics and show the relevant sets from one excel result sheet
# e.g.
# True-Postive: headcount, {actual code smells that are TP}
# False-Postive: headcount, {actual code smells that are FP}
# False-Negative: headcount, {actual code smells that are FN}
# True-Negative: headcount, {actual code smells that are TN}

from global_constants import Global_Constants
import os
import pandas as pd
import ast
from datetime import datetime

# constant
class Set_Constant:
    excel_path = "TEST-3-merged-claude-sonnet-4-5-output-2025-10-26-19-31-41.xlsx"
    EXPECTED_CODE_SMELLS = "Expected Code Smells"
    DETECTED_CODE_SMELLS = "Detected Code Smells"

    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path)
    else:
        print("File not found. Please check the filename and location.")
        exit()
    # peek data frame shape and column information
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("The information for columns are as follows: ", end="\n")
    print(df.columns.to_list())  


class Metric:
    @staticmethod
    def parse_excel_cell_to_set(cell):
        '''
        This function parses one excel cell to a set.
        '''

        if isinstance(cell, str) and cell.strip():
            try:
                parsed = ast.literal_eval(cell)
                return set(parsed) if isinstance(parsed, list) else set()
            except (ValueError, SyntaxError):
                return set()
        return set()

    @staticmethod
    def produce_sets_for_excel_test_sheet(data_frame):
        '''
        This function produces both expected code smells and detected code smells as sets.
        Writes results to markdown file in output_set_manipulation folder.
        '''
        # define two sets for each file
        expected_code_smells_set_per_file = [Metric.parse_excel_cell_to_set(item) for item in Set_Constant.df[Set_Constant.EXPECTED_CODE_SMELLS]]
        detected_code_smells_set_per_file = [Metric.parse_excel_cell_to_set(item) for item in Set_Constant.df[Set_Constant.DETECTED_CODE_SMELLS]]

        # Collect all results for markdown output
        results = []
        for i in range(len(Set_Constant.df)):
            file_name = Set_Constant.df.iloc[i, 0]
            expected_code_smells_set = expected_code_smells_set_per_file[i]
            detected_code_smells_set = detected_code_smells_set_per_file[i]
            
            # Print to console
            print(f"\n*** Row {i+1}: {file_name} ***")
            print(f"Expected: {expected_code_smells_set}")
            print(f"Detected: {detected_code_smells_set}", end="\n\n")
            
            # Calculate metrics and print to console
            metrics = Metric.calculate_four_metrics_and_related_code_smells(expected_code_smells_set, detected_code_smells_set)
            
            # Store results for markdown
            results.append({
                'row': i + 1,
                'file_name': file_name,
                'expected_set': expected_code_smells_set,
                'detected_set': detected_code_smells_set,
                'metrics': metrics
            })
        
        # Write all results to markdown file
        Metric.write_results_to_markdown(results)

    @staticmethod
    def calculate_four_metrics_and_related_code_smells(expected_set, actual_set):
        '''
        This function is to calculate the 4 metrics and demonstrate the relevant sets.
        '''
        true_positive = expected_set & actual_set
        false_positive = actual_set - expected_set
        false_negative = expected_set - actual_set
        true_negative = Global_Constants.ALL_CODE_SMELLS - expected_set - actual_set

        # Print to console
        print(f"True_Positive: {len(true_positive)}, {true_positive}", end="\n\n")
        print(f"False_Positive: {len(false_positive)}, {false_positive}", end="\n\n")
        print(f"False_Negative: {len(false_negative)}, {false_negative}", end="\n\n")
        print(f"True_Negative: {len(true_negative)}, {true_negative}", end="\n\n")
        
        return {
            "True_Positive": (len(true_positive), true_positive),
            "False_Positive": (len(false_positive), false_positive),
            "False_Negative": (len(false_negative), false_negative),
            "True_Negative": (len(true_negative), true_negative)
        }
    
    @staticmethod
    def write_results_to_markdown(results):
        '''
        Consolidates all markdown generation and writes results to a markdown file.
        '''
        # Create output directory if it doesn't exist
        output_dir = "output_set_manipulation"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate output filename based on excel file name and timestamp
        excel_basename = os.path.splitext(os.path.basename(Set_Constant.excel_path))[0]
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"{excel_basename}_{timestamp}.md"
        output_path = os.path.join(output_dir, output_filename)
        
        # Build markdown content
        markdown_content = []
        
        # Header section
        markdown_content.append("# Code Smell Analysis Results\n\n")
        markdown_content.append(f"**Source File:** `{Set_Constant.excel_path}`\n\n")
        markdown_content.append(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        markdown_content.append(f"**Total Files Analyzed:** {len(results)}\n\n")
        markdown_content.append(f"**DataFrame Shape:** {Set_Constant.df.shape[0]} rows × {Set_Constant.df.shape[1]} columns\n\n")
        markdown_content.append("---\n\n")
        
        # Results section for each row
        for result in results:
            file_name = result['file_name']
            expected_set = result['expected_set']
            detected_set = result['detected_set']
            metrics = result['metrics']
            
            # Row header
            markdown_content.append(f"## Row {result['row']}: {file_name}\n\n")
            
            # Expected and Detected sets
            markdown_content.append(f"**Expected Code Smells:** `{sorted(expected_set) if expected_set else '{}'}`\n\n")
            markdown_content.append(f"**Detected Code Smells:** `{sorted(detected_set) if detected_set else '{}'}`\n\n")
            
            # Metrics table
            markdown_content.append("### Metrics\n\n")
            markdown_content.append("| Metric | Count | Code Smells |\n")
            markdown_content.append("|--------|-------|-------------|\n")
            
            tp_count, tp_set = metrics["True_Positive"]
            fp_count, fp_set = metrics["False_Positive"]
            fn_count, fn_set = metrics["False_Negative"]
            tn_count, tn_set = metrics["True_Negative"]
            
            markdown_content.append(f"| **True Positive** | {tp_count} | `{sorted(tp_set) if tp_set else '{}'}` |\n")
            markdown_content.append(f"| **False Positive** | {fp_count} | `{sorted(fp_set) if fp_set else '{}'}` |\n")
            markdown_content.append(f"| **False Negative** | {fn_count} | `{sorted(fn_set) if fn_set else '{}'}` |\n")
            markdown_content.append(f"| **True Negative** | {tn_count} | `{sorted(tn_set) if tn_set else '{}'}` |\n\n")
            markdown_content.append("---\n\n")
        
        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"\n{'='*60}")
        print(f"Results saved to: {output_path}")
        print(f"{'='*60}\n")

def main():

    Metric.produce_sets_for_excel_test_sheet(Set_Constant.df)

if __name__ == "__main__":
    main()



  