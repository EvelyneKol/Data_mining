import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

# Get a list of all CSV files in a directory
csv_files = glob.glob('harth/*.csv')

# Define the labels dictionary
labels = {1: "walking", 2: "running", 3: "shuffling", 4: "stairs (ascending)",
          5: "stairs (descending)", 6: "standing", 7: "sitting", 8: "lying",
          13: "cycling (sit)", 14: "cycling (stand)", 130: "cycling (sit, inactive)", 140: "cycling (stand, inactive)"}

# Initialize a dictionary to store variance values for each activity
variance_values = {activity: {column: [] for column in ['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']} for activity in labels.values()}

# Iterate through each CSV file
for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Group by label and calculate the variance of values for each activity
    for label, activity_name in labels.items():
        activity_df = df[df['label'] == label]
        if not activity_df.empty:
            for column in ['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']:
                variance_values[activity_name][column].append(activity_df[column].var())

# Plot the variance of each value for each activity
for activity_name in labels.values():
    if any(len(variance_values[activity_name][column]) > 0 for column in ['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']):
        fig, ax = plt.subplots(figsize=(12, 8))

        x_values = np.arange(len(['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']))
        y_values = [np.mean(variance_values[activity_name][column]) if variance_values[activity_name][column] else 0 for column in ['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']]

        ax.bar(x_values, y_values, color='skyblue')
        ax.set_xticks(x_values)
        ax.set_xticklabels(['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z'])
        ax.set_xlabel('Sensor Value')
        ax.set_ylabel('Variance')
        ax.set_title(f'Variance of each sensor value for {activity_name}')

        plt.grid(True)
        plt.tight_layout()
        plt.show()
