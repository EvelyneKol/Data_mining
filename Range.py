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

# Initialize dictionaries to store minimum and maximum values for each label and each column
min_values = {}
max_values = {}

# Iterate through each CSV file
for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Group by label and calculate the range of values for each column
    range_df = df.groupby('label').agg({'back_x': ['min', 'max'],
                                        'back_y': ['min', 'max'],
                                        'back_z': ['min', 'max'],
                                        'thigh_x': ['min', 'max'],
                                        'thigh_y': ['min', 'max'],
                                        'thigh_z': ['min', 'max']})

    # Update the dictionaries with the new minimum and maximum values
    for label in range_df.index:
        label_name = labels[label]  # Map numeric label to activity name
        if label_name not in min_values:
            min_values[label_name] = {}
            max_values[label_name] = {}
        for column in range_df.columns.levels[0]:
            if column not in min_values[label_name]:
                min_values[label_name][column] = range_df.loc[label, (column, 'min')]
                max_values[label_name][column] = range_df.loc[label, (column, 'max')]
            else:
                min_values[label_name][column] = min(min_values[label_name][column], range_df.loc[label, (column, 'min')])
                max_values[label_name][column] = max(max_values[label_name][column], range_df.loc[label, (column, 'max')])

# Plot the range of values for each label and each column
fig, ax = plt.subplots(figsize=(12, 8))

y_labels = list(min_values.keys())
y_ticks = np.arange(len(y_labels))

for label_idx, label in enumerate(y_labels):
    for column in ['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']:
        min_val = min_values[label][column]
        max_val = max_values[label][column]
        ax.barh(label_idx, max_val - min_val, left=min_val, color='skyblue')

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)
ax.set_xlabel('Range')
ax.set_ylabel('Activity')
ax.set_title('Range of values for each activity')

plt.grid(True)
plt.tight_layout()
plt.show()
