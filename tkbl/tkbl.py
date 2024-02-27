import pandas as pd
import json
import os

# Path to the data directory
#data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# Load the CSV files into DataFrames
df_SFTool = pd.read_csv(os.path.join(data_dir, 'SFTool_uniformat.csv'))
df_ESTCP = pd.read_csv(os.path.join(data_dir, 'ESTCP_uniformat.csv'))

# Merge the two DataFrames into one, replacing NaN values with an empty string
df = pd.concat([df_SFTool, df_ESTCP], ignore_index=True).fillna('')

def filter_by_uniformat_code(uniformat_code):
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