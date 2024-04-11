import pandas as pd
import glob

# Get a list of all CSV files in a directory
csv_files = glob.glob('harth/*.csv')

for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Convert timestamp column to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Extract time portion from timestamp
    df['timestamp'] = df['timestamp'].dt.time

    # Write the modified DataFrame back to the same CSV file
    df.to_csv(csv_file, index=False)