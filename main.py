"""import pandas as pd
import glob

# Path to the directory containing the CSV files
directory_path = 'harth/*.csv'

# Get the list of CSV files in the directory
file_list = glob.glob(directory_path)

# Initialize an empty list to store DataFrames
dfs = []

# Iterate over each CSV file
for file in file_list:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)
    # Drop the index and unnamed columns if they exist
    df = df.drop(columns=['Unnamed: 0', 'index'], errors='ignore')
    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv('combined_data.csv', index=False)

# Count the number of rows
num_rows = len(combined_df)

print("Number of rows in the CSV file:", num_rows)
"""

"""import pandas as pd

df=pd.read_csv("combined_data.csv")

# Convert the 'timestamp' column to Unix timestamps (seconds since the epoch)
df['timestamp'] = pd.to_datetime(df['timestamp']).astype('int64')

print(df[:50])

"""

import pandas as pd
import glob

# Get a list of all CSV files in the directory
csv_files = glob.glob('harth/*.csv')

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through each CSV file, read it into a DataFrame, and append it to the list with a label
for i, csv_file in enumerate(csv_files):
    df = pd.read_csv(csv_file)
    df['person'] = f'CSV_{i+1}'  # Add a column indicating the source CSV
    df = df.drop(columns=['Unnamed: 0', 'index'], errors='ignore')
    dfs.append(df)

# Concatenate all DataFrames into one
concatenated_df = pd.concat(dfs, ignore_index=True)

# Write the concatenated DataFrame to a new CSV file
concatenated_df.to_csv('total_data.csv', index=False)
