import json
import os

import pandas as pd

# Path to the data directory
#data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# Load the CSV files into DataFrames
df_SFTool = pd.read_csv(os.path.join(data_dir, 'SFTool_uniformat.csv'))
df_ESTCP = pd.read_csv(os.path.join(data_dir, 'ESTCP_uniformat.csv'))
df_BSYNC = pd.read_csv(os.path.join(data_dir, 'building-sync-eem.csv'))
df_FedBPS = pd.read_csv(os.path.join(data_dir, 'federal-bps.csv'))
df_BPS_A1 = pd.read_csv(os.path.join(data_dir, 'Table_A1_Federal_BPS.csv'), encoding='ISO-8859-1')
df_BPS_A2 = pd.read_csv(os.path.join(data_dir, 'Table_A2_Federal_BPS.csv'), encoding='ISO-8859-1')

# Merge the two DataFrames into one, replacing NaN values with an empty string
df = pd.concat([df_SFTool, df_ESTCP], ignore_index=True).fillna('')

def bsync_by_uniformat_code(uniformat_code):
    """
    Looks up rows in the DataFrame df that match the given uniformat_code.
    For a 6-digit uniformat_code, it uses only the letter and the first 4 digits for matching.

    Parameters:
    - uniformat_code (str): The uniformat code to look up.

    Returns:
    - list[dict]: An array of dictionaries, each representing a matching row in JSON format.
    """
    # Adjust the uniformat_code for 6 digits to use only the letter and the first 4 digits
    if len(uniformat_code) <= 5:
        # Filter the DataFrame for rows that match the uniformat_code
        matching_rows = df_BSYNC[df_BSYNC['uni_code_manual'].fillna('').str.startswith(uniformat_code)]
    else:
        # Filter the DataFrame for rows that match the uniformat_code
        matching_rows = df_BSYNC[df_BSYNC['lvl4_uni_code'].fillna('').str.startswith(uniformat_code)]

    # Convert matching rows to a list of dictionaries (JSON format)
    return matching_rows.to_dict('records')

def federal_bps_by_uniformat_code(uniformat_code):
    """
    Looks up rows in the DataFrame df that match the given uniformat_code.

    Parameters:
    - uniformat_code (str): The uniformat code to look up.

    Returns:
    - list[dict]: An array of dictionaries, each representing a matching row in JSON format.
    """

    # Filter the DataFrame for rows that match the uniformat_code
    matching_rows = df_FedBPS[df_FedBPS['preexisting-uniformat'].fillna('').str.startswith(uniformat_code)]

    # Convert matching rows to a list of dictionaries (JSON format)
    return matching_rows.to_dict('records')

def bps_a1_by_uniformat_code(uniformat_code):
    """
    Filters a DataFrame for entries matching a specific UniFormat code.

    This function takes a UniFormat code as input, validates its presence in the DataFrame,
    and returns a JSON string containing all records from the DataFrame where the 'preexisting-uniformat'
    column matches the provided UniFormat code. The output JSON is formatted with indentation for readability.

    Parameters:
    uniformat_code (str): The UniFormat code to filter the DataFrame by.

    Returns:
    str: A JSON formatted string containing the filtered records. If the specified column
    is not found, or if any other error occurs, it returns a JSON string with an error message.
    """
    try:
        # Ensure the input is a string and strip whitespace
        uniformat_code = str(uniformat_code).strip()
        print("uniformat_code:", uniformat_code)
        # Check if 'preexisting-uniformat' column exists
        if 'preexisting-uniformat' not in df_BPS_A1.columns:
            return json.dumps({"error": "Column 'uniformat code' not found in DataFrame."}, indent=4)
        
        # Strip whitespace from 'uniformat code' column for accurate comparison
        df_BPS_A1['preexisting-uniformat'] = df_BPS_A1['preexisting-uniformat'].str.strip()
        
        # Filter the DataFrame where 'uniformat code' column matches the input value
        filtered_df = df_BPS_A1[df_BPS_A1['preexisting-uniformat'] == uniformat_code].copy()
        
        # Convert the filtered DataFrame to JSON with indentation for better readability
        result_json = json.loads(filtered_df.to_json(orient='records'))
        result_pretty_json = json.dumps(result_json, indent=4)
        
        return result_pretty_json
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

def bps_a2_by_uniformat_code(uniformat_code):
    """
    Filters a DataFrame for entries matching a specific UniFormat code.
    
    This function takes a UniFormat code as input, validates its presence in the DataFrame,
    and returns a JSON string containing all records from the DataFrame where the 'preexisting-uniformat'
    column matches the provided UniFormat code. The output JSON is formatted with indentation for readability.
    
    Parameters:
    uniformat_code (str): The UniFormat code to filter the DataFrame by.
    
    Returns:
    str: A JSON formatted string containing the filtered records. If the specified column
    is not found, or if any other error occurs, it returns a JSON string with an error message.
    """
    try:
        # Ensure the input is a string and strip whitespace
        uniformat_code = str(uniformat_code).strip()
        print("uniformat_code:", uniformat_code)
        # Check if 'preexisting-uniformat' column exists
        if 'preexisting-uniformat' not in df_BPS_A2.columns:
            return json.dumps({"error": "Column 'uniformat code' not found in DataFrame."}, indent=4)
        
        # Strip whitespace from 'uniformat code' column for accurate comparison
        df_BPS_A2['preexisting-uniformat'] = df_BPS_A2['preexisting-uniformat'].str.strip()
        
        # Filter the DataFrame where 'uniformat code' column matches the input value
        filtered_df = df_BPS_A2[df_BPS_A2['preexisting-uniformat'] == uniformat_code].copy()
        
        # Convert the filtered DataFrame to JSON with indentation for better readability
        result_json = json.loads(filtered_df.to_json(orient='records'))
        result_pretty_json = json.dumps(result_json, indent=4)
        
        return result_pretty_json
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)      
    
def filter_by_uniformat_code(uniformat_code):
    """
    Filters rows in a DataFrame based on a provided uniformat code. This function expects a global DataFrame 'df'
    to be defined outside this function. It checks if the 'uniformat code' column exists in 'df', strips whitespace
    from the uniformat code in both the input and the DataFrame, and filters the DataFrame for rows that match
    the provided uniformat code. It then attempts to make URLs in the 'url' column clickable (this part is commented out)
    and returns the filtered DataFrame as a pretty-printed JSON string.

    Parameters:
    - uniformat_code (str): The uniformat code used for filtering.

    Returns:
    - str: A JSON string representing the filtered rows. If an error occurs, a JSON string with an error message is returned.
    """
    try:
        # Ensure the input is a string and strip whitespace
        uniformat_code = str(uniformat_code).strip()
        
        # Check if 'uniformat code' column exists
        if 'uniformat code' not in df.columns:
            return json.dumps({"error": "Column 'uniformat code' not found in DataFrame."}, indent=4)
        
        # Strip whitespace from 'uniformat code' column for accurate comparison
        df['uniformat code'] = df['uniformat code'].str.strip()
        
        # Filter the DataFrame where 'uniformat code' column matches the input value
        filtered_df = df[df['uniformat code'] == uniformat_code].copy()
        
        # Update URLs in the DataFrame to be clickable links using .loc to avoid the warning
        #filtered_df.loc[:, 'url'] = filtered_df['url'].apply(lambda x: f"<a href='{x}'>{x}</a>")
        
        # Convert the filtered DataFrame to JSON with indentation for better readability
        result_json = json.loads(filtered_df.to_json(orient='records'))
        result_pretty_json = json.dumps(result_json, indent=4)
        
        return result_pretty_json
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)
