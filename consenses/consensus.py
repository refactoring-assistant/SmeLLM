# This Python script will sythesize test results from different LLMs 
# and conduct the consensus analysis among the different LLMs on the 4 metrics
# given the pre-test excel sheets are the same

from global_constants import Global_Constants
from set_manipulation import Metric
import pandas as pd
import os
from datetime import datetime

class Consensus_Constant:
    EXPECTED_CODE_SMELLS = "Expected Code Smells"
    DETECTED_CODE_SMELLS = "Detected Code Smells"
    
    # configuration: { LLM_name: excel_file_path }
    RUNNER_CONFIG = {
        # closed 
        "GPT-5": "TEST-3-merged-gpt-5-output-2025-10-27-19-35-41.xlsx",
        "Claude Sonnet 4.5": "TEST-3-merged-claude-sonnet-4-5-output-2025-10-26-19-31-41.xlsx",

        # open-sourced
        # "Qwen3-Next-80B-A3B-Thinking": "TEST-3-merged-Qwen3-Next-80B-A3B-Thinking-output-2025-11-18-12-01-24.xlsx",
        "DeepSeek-R1": "TEST-3-merged-DeepSeek-R1-0528-output-2025-11-17-16-20-46.xlsx",

        "Meta-Llama-3.1-405B-Instruct-Turbo": "TEST-3-merged-Meta-Llama-3.1-405B-Instruct-Turbo-output-2025-11-17-19-27-16.xlsx",
        "gemma-3n-E4B-it": "TEST-3-merged-gemma-3n-E4B-it-output-2025-11-18-14-08-32.xlsx",
    }
    
    runner_names = list(RUNNER_CONFIG.keys())
    excel_files = list(RUNNER_CONFIG.values())
    dfs = {}
    
    for runner_name, file_path in RUNNER_CONFIG.items():
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            dfs[runner_name] = df
            print(f"Loaded: {runner_name}")
            print(f"File: {file_path}")
            print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
            print(f"Columns: {df.columns.to_list()}")
        else:
            print(f"ERROR: File not found for {runner_name}")
            print(f"Expected path: {file_path}")
            exit(1)
    
    print(f"{len(dfs)} LLM test results have been loaded.")

class Consensus_Computation:
    def __init__(self, excel_files):
        '''
        Initialize by reading all excel files and extracting expected_set and actual_sets.
        For each row (Java file), expected_set is the same across all excel files,
        but actual_sets differ across different LLM results.
        '''
        self.excel_files = excel_files
        self.dataframes = {}
        
        # Read all excel files
        for excel_file in excel_files:
            if os.path.exists(excel_file):
                df = pd.read_excel(excel_file)
                self.dataframes[excel_file] = df
            else:
                print(f"ERROR: File not found: {excel_file}")
                exit(1)
        
        # Verify all dataframes have the same number of rows
        row_counts = [len(df) for df in self.dataframes.values()]
        if len(set(row_counts)) > 1:
            print(f"ERROR: Excel files have different numbers of rows: {row_counts}")
            exit(1)
        
        self.num_rows = row_counts[0] if row_counts else 0
        
        # Extract expected_set and actual_sets for each row
        # expected_set is the same across all files (we'll use the first file's expected)
        # actual_sets will be a list of sets, one from each excel file
        self.expected_sets_per_row = []
        self.actual_sets_per_row = []
        self.file_names = []
        
        # Get file name column (first column)
        first_df = list(self.dataframes.values())[0]
        file_name_column = first_df.columns[0]
        
        for i in range(self.num_rows):
            # Get expected_set from first file (should be same across all)
            first_df = list(self.dataframes.values())[0]
            expected_cell = first_df[Consensus_Constant.EXPECTED_CODE_SMELLS].iloc[i]
            expected_set = Metric.parse_excel_cell_to_set(expected_cell)
            self.expected_sets_per_row.append(expected_set)
            
            # Get actual_sets from all files
            actual_sets = []
            for excel_file, df in self.dataframes.items():
                actual_cell = df[Consensus_Constant.DETECTED_CODE_SMELLS].iloc[i]
                actual_set = Metric.parse_excel_cell_to_set(actual_cell)
                actual_sets.append(actual_set)
            self.actual_sets_per_row.append(actual_sets)
            
            # Get file name
            file_name = first_df[file_name_column].iloc[i]
            self.file_names.append(file_name)
    
    def compute_collective_metrics_for_all_rows(self):
        '''
        For each Java file (row), compute the 4 collective metrics and print to console.
        Also collects results for markdown output.
        '''
        print("\n" + "="*70)
        print("Consensus Analysis: Collective Metrics Across All LLMs")
        print("="*70 + "\n")
        
        # Collect results for markdown output
        results = []
        
        for i in range(self.num_rows):
            file_name = self.file_names[i]
            expected_set = self.expected_sets_per_row[i]
            actual_sets = self.actual_sets_per_row[i]
            
            print(f"\n{'='*70}")
            print(f"Row {i+1}: {file_name}")
            print(f"{'='*70}")
            print(f"Expected Code Smells: {sorted(expected_set) if expected_set else '{}'}")
            print(f"Number of LLM results: {len(actual_sets)}")
            for idx, actual_set in enumerate(actual_sets):
                print(f"  LLM {idx+1} Detected: {sorted(actual_set) if actual_set else '{}'}")
            print()
            
            # Compute collective metrics
            tp_count, tp_set = Consensus_Computation.collective_true_positive_set(expected_set, actual_sets)
            fp_count, fp_set = Consensus_Computation.collective_false_positive_set(expected_set, actual_sets)
            fn_count, fn_set = Consensus_Computation.collective_false_negative(expected_set, actual_sets)
            tn_count, tn_set = Consensus_Computation.collective_true_negative(expected_set, actual_sets)
            
            print(f"Collective True Positive: {tp_count}, {sorted(tp_set) if tp_set else '{}'}")
            print(f"Collective False Positive: {fp_count}, {sorted(fp_set) if fp_set else '{}'}")
            print(f"Collective False Negative: {fn_count}, {sorted(fn_set) if fn_set else '{}'}")
            print(f"Collective True Negative: {tn_count}, {sorted(tn_set) if tn_set else '{}'}")
            print()
            
            # Store results for markdown
            results.append({
                'row': i + 1,
                'file_name': file_name,
                'expected_set': expected_set,
                'actual_sets': actual_sets,
                'metrics': {
                    'True_Positive': (tp_count, tp_set),
                    'False_Positive': (fp_count, fp_set),
                    'False_Negative': (fn_count, fn_set),
                    'True_Negative': (tn_count, tn_set)
                }
            })
        
        # Write results to markdown file
        self.write_results_to_markdown(results)
    
    def write_results_to_markdown(self, results):
        '''
        Writes consensus analysis results to a markdown file in output_consensus folder.
        '''
        # Create output directory if it doesn't exist
        output_dir = "output_consensus"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate output filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"consensus_analysis_{timestamp}.md"
        output_path = os.path.join(output_dir, output_filename)
        
        # Build markdown content
        markdown_content = []
        
        # Header section
        markdown_content.append("# Consensus Analysis: Collective Metrics Across All LLMs\n\n")
        markdown_content.append(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        markdown_content.append(f"**Number of LLMs Analyzed:** {len(self.excel_files)}\n\n")
        markdown_content.append(f"**Total Files Analyzed:** {len(results)}\n\n")
        
        # Source files section
        markdown_content.append("## Source Files\n\n")
        for idx, excel_file in enumerate(self.excel_files, 1):
            markdown_content.append(f"{idx}. `{excel_file}`\n")
        markdown_content.append("\n---\n\n")
        
        # Results section for each row
        for result in results:
            file_name = result['file_name']
            expected_set = result['expected_set']
            actual_sets = result['actual_sets']
            metrics = result['metrics']
            
            # Row header
            markdown_content.append(f"## Row {result['row']}: {file_name}\n\n")
            
            # Expected Code Smells
            markdown_content.append(f"**Expected Code Smells:** `{sorted(expected_set) if expected_set else '{}'}`\n\n")
            
            # Detected Code Smells from each LLM
            markdown_content.append("### Detected Code Smells by LLM\n\n")
            for idx, actual_set in enumerate(actual_sets, 1):
                llm_name = Consensus_Constant.runner_names[idx - 1] if idx <= len(Consensus_Constant.runner_names) else f"LLM {idx}"
                markdown_content.append(f"**{llm_name}:** `{sorted(actual_set) if actual_set else '{}'}`\n\n")
            
            # Collective Metrics table
            markdown_content.append("### Collective Metrics\n\n")
            markdown_content.append("| Metric | Count | Code Smells |\n")
            markdown_content.append("|--------|-------|-------------|\n")
            
            tp_count, tp_set = metrics["True_Positive"]
            fp_count, fp_set = metrics["False_Positive"]
            fn_count, fn_set = metrics["False_Negative"]
            tn_count, tn_set = metrics["True_Negative"]
            
            markdown_content.append(f"| **Collective True Positive** | {tp_count} | `{sorted(tp_set) if tp_set else '{}'}` |\n")
            markdown_content.append(f"| **Collective False Positive** | {fp_count} | `{sorted(fp_set) if fp_set else '{}'}` |\n")
            markdown_content.append(f"| **Collective False Negative** | {fn_count} | `{sorted(fn_set) if fn_set else '{}'}` |\n")
            markdown_content.append(f"| **Collective True Negative** | {tn_count} | `{sorted(tn_set) if tn_set else '{}'}` |\n\n")
            markdown_content.append("---\n\n")
        
        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"\n{'='*70}")
        print(f"Results saved to: {output_path}")
        print(f"{'='*70}\n")
    
    def write_collective_metrics_to_excel(self, output_excel_path="TEST-3-merged-preprompt.xlsx"):
        '''
        Writes collective metrics to an Excel file with the same structure as the input files.
        The output file should have File Name and Expected Code Smells columns,
        plus columns for collective metrics.
        '''
        # Read the template/preprompt Excel file
        if not os.path.exists(output_excel_path):
            print(f"ERROR: Output template file not found: {output_excel_path}")
            print("Creating new file from first input file structure...")
            # Use first dataframe as template
            template_df = list(self.dataframes.values())[0].copy()
            output_df = pd.DataFrame({
                'File Name': template_df.iloc[:, 0],
                'Expected Code Smells': template_df[Consensus_Constant.EXPECTED_CODE_SMELLS]
            })
        else:
            output_df = pd.read_excel(output_excel_path)
        
        # Verify that file names match and align rows
        first_df = list(self.dataframes.values())[0]
        file_name_column = first_df.columns[0]
        input_file_names = first_df[file_name_column].tolist()
        output_file_names = output_df['File Name'].tolist()
        
        if input_file_names != output_file_names:
            print(f"WARNING: File names don't match exactly. Aligning to input file order.")
            # Create a new dataframe with input file names as reference
            aligned_df = pd.DataFrame({'File Name': input_file_names})
            # Merge with output_df to preserve Expected Code Smells if they match
            aligned_df = aligned_df.merge(
                output_df[['File Name', 'Expected Code Smells']], 
                on='File Name', 
                how='left'
            )
            # If Expected Code Smells is missing, get it from input (preserve original format)
            if aligned_df['Expected Code Smells'].isna().any():
                for idx, file_name in enumerate(input_file_names):
                    if pd.isna(aligned_df.loc[idx, 'Expected Code Smells']):
                        # Get from the first input dataframe to preserve format
                        matching_row = first_df[first_df[file_name_column] == file_name]
                        if not matching_row.empty:
                            aligned_df.loc[idx, 'Expected Code Smells'] = matching_row[Consensus_Constant.EXPECTED_CODE_SMELLS].iloc[0]
            output_df = aligned_df
        
        # Prepare columns for collective metrics
        collective_tp_counts = []
        collective_tp_sets = []
        collective_fp_counts = []
        collective_fp_sets = []
        collective_fn_counts = []
        collective_fn_sets = []
        collective_tn_counts = []
        collective_tn_sets = []
        
        # Calculate collective metrics for each row
        for i in range(self.num_rows):
            expected_set = self.expected_sets_per_row[i]
            actual_sets = self.actual_sets_per_row[i]
            
            # Compute collective metrics
            tp_count, tp_set = Consensus_Computation.collective_true_positive_set(expected_set, actual_sets)
            fp_count, fp_set = Consensus_Computation.collective_false_positive_set(expected_set, actual_sets)
            fn_count, fn_set = Consensus_Computation.collective_false_negative(expected_set, actual_sets)
            tn_count, tn_set = Consensus_Computation.collective_true_negative(expected_set, actual_sets)
            
            # Store results (format as lists to match Excel format)
            collective_tp_counts.append(tp_count)
            collective_tp_sets.append(sorted(list(tp_set)) if tp_set else [])
            collective_fp_counts.append(fp_count)
            collective_fp_sets.append(sorted(list(fp_set)) if fp_set else [])
            collective_fn_counts.append(fn_count)
            collective_fn_sets.append(sorted(list(fn_set)) if fn_set else [])
            collective_tn_counts.append(tn_count)
            collective_tn_sets.append(sorted(list(tn_set)) if tn_set else [])
        
        # Add collective metrics columns to output dataframe
        # Format sets as strings matching the Excel format (list representation)
        output_df['Collective True Positive Count'] = collective_tp_counts
        output_df['Collective True Positive'] = collective_tp_sets
        output_df['Collective False Positive Count'] = collective_fp_counts
        output_df['Collective False Positive'] = collective_fp_sets
        output_df['Collective False Negative Count'] = collective_fn_counts
        output_df['Collective False Negative'] = collective_fn_sets
        output_df['Collective True Negative Count'] = collective_tn_counts
        output_df['Collective True Negative'] = collective_tn_sets
        
        # Write to Excel file
        output_df.to_excel(output_excel_path, index=False, engine='openpyxl')
        
        print(f"\n{'='*70}")
        print(f"Collective metrics written to: {output_excel_path}")
        print(f"Total rows: {len(output_df)}")
        print(f"Columns: {', '.join(output_df.columns.tolist())}")
        print(f"{'='*70}\n")
    
    
    @staticmethod
    def collective_true_positive_set(expected_set, actual_sets):
        '''
        This function purely calculates the collective true positive set among all test results.
        '''
        if not expected_set or not actual_sets:
            return 0, set()

        true_positive_sets = [ set.intersection(actual_set, expected_set) for actual_set in actual_sets ]
        colletive_true_positive_set = set.intersection(*true_positive_sets) 
        return len(colletive_true_positive_set), colletive_true_positive_set
    

    @staticmethod
    def collective_false_positive_set(expected_set, actual_sets):
        '''
        This function purely calculates the collective false positive set among all test results.
        Returns: (count, set)
        '''
        if not expected_set or not actual_sets:
            return 0, set()

        false_positive_sets = [actual_set - expected_set for actual_set in actual_sets]
        if not false_positive_sets:
            return 0, set()
        collective_false_positive_set = set.intersection(*false_positive_sets)
        return len(collective_false_positive_set), collective_false_positive_set
    

    @staticmethod
    def collective_true_negative(expected_set, actual_sets):
        '''
        This function purely calculates the collective true negative set among all test results.
        Returns: (count, set)
        '''
        if not expected_set or not actual_sets:
            return 0, set()
        
        true_negative_sets = [Global_Constants.ALL_CODE_SMELLS - expected_set - actual_set for actual_set in actual_sets]
        if not true_negative_sets:
            return 0, set()
        collective_true_negative_set = set.intersection(*true_negative_sets)
        return len(collective_true_negative_set), collective_true_negative_set
    

    @staticmethod
    def collective_false_negative(expected_set, actual_sets):
        '''
        This function purely calculates the collective false negative set among all test results.
        Returns: (count, set)
        '''
        if not expected_set or not actual_sets:
            return 0, set()
        
        false_negative_sets = [expected_set - actual_set for actual_set in actual_sets]
        if not false_negative_sets:
            return 0, set()
        collective_false_negative_set = set.intersection(*false_negative_sets)
        return len(collective_false_negative_set), collective_false_negative_set


def main():
    """Main function to run consensus analysis"""
    consensus = Consensus_Computation(Consensus_Constant.excel_files)
    consensus.compute_collective_metrics_for_all_rows()
    consensus.write_collective_metrics_to_excel("TEST-3-merged-preprompt.xlsx")

if __name__ == "__main__":
    main()
