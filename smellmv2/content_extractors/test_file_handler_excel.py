import pandas as pd

class ExcelTestHandler:
    def __init__(self, file_path):
        """
        Initialize the ExcelImporter with the path to the Excel file.
        """
        self.file_path = file_path

    def import_test(self):
        """
        Import the Excel file and return a pandas DataFrame.
        """
        try:
            data_frame = pd.read_excel(self.file_path)
            return data_frame
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
        except pd.errors.EmptyDataError:
            print("Error: The Excel file is empty.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_test(self, save_data_frame, result_df, individual_code_smell_df):
        """
        Save the given DataFrame to the same Excel file.
        """
        try:
            with pd.ExcelWriter(self.file_path, engine='openpyxl', mode='w') as writer:
                save_data_frame.to_excel(writer, sheet_name="code_smells", index=False)
                result_df.to_excel(writer, sheet_name="results", index=False)
                individual_code_smell_df.to_excel(writer, sheet_name="individual_code_smells", index=False)
            print(f"DataFrame saved successfully to {self.file_path}")
        except Exception as e:
            print(f"An error occurred while saving to Excel: {e}")

# Example usage
if __name__ == "__main__":
    # Provide the path to your Excel file
    excel_path = "TEST.xlsx"
    
    # Create an instance of ExcelImporter
    excel_test_handler = ExcelTestHandler(excel_path)
    
    # Import the Excel file and get the DataFrame
    df = excel_test_handler.import_test()
    
    if df is not None:
        print("DataFrame imported successfully:")
        # print(df)
        print(df.columns)

    result_df = pd.DataFrame({
        "Column1": [1, 2, 3],
        "Column2": ["A", "B", "C"]
    })

    excel_test_handler.save_test(df, result_df)
    
