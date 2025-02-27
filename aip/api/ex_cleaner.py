import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from category_encoders import TargetEncoder, WOEEncoder

def excel_to_dataframe(file_path, sheet_name=0):
    
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Successfully loaded data from {file_path}")
        print(f"DataFrame shape: {df.shape} (rows, columns)")
        print(f"Columns: {df.columns.tolist()}")
        
        return df
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    
def get_excel_columns(file_path, sheet_name=0):

    try:
        df_header = pd.read_excel(file_path, sheet_name=sheet_name, nrows=0)
        columns = df_header.columns.tolist()
        print(f"Found {len(columns)} columns in {file_path}, sheet '{sheet_name}'")
        return columns
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None