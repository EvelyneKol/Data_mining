import pandas as pd
import matplotlib.pyplot as plt
import glob
import seaborn as sns  # Import seaborn for color palettes

# Get a list of all CSV files in a directory
csv_files = glob.glob('harth/*.csv')
# Define the labels dictionary
labels = {1: "walking", 2: "running", 3: "shuffling", 4: "stairs (ascending)",
          5: "stairs (descending)", 6: "standing", 7: "sitting", 8: "lying",
          13: "cycling (sit)", 14: "cycling (stand)", 130: "cycling (sit, inactive)", 140: "cycling (stand, inactive)"}
# Define a color palette with enough colors for the number of CSV files
colors = sns.color_palette('husl', len(csv_files))

# Iterate through each column
for column in ['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']:
    plt.figure(figsize=(12, 8))

    # Iterate through each CSV file
    for idx, csv_file in enumerate(csv_files):
        # Read the CSV file
        df = pd.read_csv(csv_file)
        median_df = df.groupby('label')[column].median()
        median_df = median_df.reset_index()  # Resetting the index to access the 'label' column
        median_df['label'] = median_df['label'].map(labels)
        median_df = median_df.sort_values(by='label')  # Sorting by label

        # Plot median values for the current column and CSV file
        plt.scatter(median_df['label'], median_df[column], color=colors[idx])

    # Add title, labels, and legend
    plt.title(f"Median Values for {column}")
    plt.xlabel('Label')
    plt.ylabel('Median Values')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()