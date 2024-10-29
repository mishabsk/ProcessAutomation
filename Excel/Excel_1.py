import pandas as pd
from docx import Document

def print_all_sheets_data(file_path, nan_replacement=''):
    # Read all sheets into a dictionary of DataFrames
    all_sheets_df = pd.read_excel(file_path, sheet_name=None)
    
    # Loop through each sheet
    for sheet_name, df in all_sheets_df.items():
        print(f"Sheet: {sheet_name}")
        df=df.fillna(nan_replacement)
        print(df)  # Print the entire DataFram
        print("\n----------------------------------\n")

    return df

# Example usage
file_path = r"C:\Users\abhasker1\Downloads\EmilyTeohProject\ExcelData_Important\1.1 Anglo_PolicyData.xlsx"
print_all_sheets_data(file_path)
