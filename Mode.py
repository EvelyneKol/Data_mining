import os
import pandas as pd
import matplotlib.pyplot as plt

# Directory containing the CSV files
directory = 'harth'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Iterate over each CSV file
for file in csv_files:
    # Read the CSV file
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)

    # Group by 'label' column and compute the mode for each group
    modes = df.groupby('label')[['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']].apply(lambda x: x.mode().iloc[0])

    # Plot scatter graph
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    for i, col in enumerate(['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']):
        ax = axs[i//3, i%3]
        ax.scatter(modes.index, modes[col])
        ax.set_title(col)
        ax.set_xlabel('Label')
        ax.set_ylabel('Mode')

    fig.suptitle(f"Scatter plot of modes for {file}", y=1.02)
    plt.tight_layout()
    plt.show()
