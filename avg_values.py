import csv
import matplotlib.pyplot as plt
import numpy as np
import os

# Function to read and process all CSV files in a directory
def process_all_csvs(directory, labels):
    # Dictionary to store sum and count of values for each activity
    activity_values = {activity: [0] * 6 for activity in labels.values()}
    activity_counts = {activity: 0 for activity in labels.values()}

    # Iterate over each CSV file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            process_csv(file_path, labels, activity_values, activity_counts)

    # Calculate average values for each activity
    activity_average_values = {}
    for activity, sum_values in activity_values.items():
        count = activity_counts[activity]
        if count != 0:
            average_values = [x / count for x in sum_values]
            activity_average_values[activity] = average_values

    # Plotting
    num_activities = len(activity_average_values)
    num_cols = 3
    num_rows = (num_activities + num_cols - 1) // num_cols
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 10))
    axs = axs.flatten()
    for i, (activity, avg_values) in enumerate(activity_average_values.items()):
        xpoints = np.arange(len(avg_values))  # Adjusted to the length of average values
        axs[i].bar(xpoints, avg_values, width=0.4)  # Plot slim bars
        axs[i].set_xticks(xpoints)
        axs[i].set_xticklabels(['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z'], rotation=45, ha='right')  # Adjusted to sensor names
        axs[i].set_xlabel('Sensor')
        axs[i].set_ylabel('Average Values')
        axs[i].set_title(f'Average Values for {activity}')

    # Hide unused subplots
    for j in range(num_activities, num_rows * num_cols):
        fig.delaxes(axs[j])

    plt.tight_layout()
    plt.show()

# Function to read and process a single CSV file
def process_csv(file_path, labels, activity_values, activity_counts):
    # Open the file in read mode
    with open(file_path, 'r', newline='') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csvfile)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            label = int(row['label'])  # Assuming 'label' is the column name for the activity label
            values = [float(row[column]) for column in ['back_x', 'back_y', 'back_z', 'thigh_x', 'thigh_y', 'thigh_z']]
            activity = labels.get(label, f'Unknown activity ({label})')

            # Update activity_values dictionary
            activity_values[activity] = [x + y for x, y in zip(activity_values[activity], values)]
            activity_counts[activity] += 1

# Path to the directory containing the CSV files
directory = 'harth'

# Define the labels dictionary
labels = {1: "Walking", 2: "Running", 3: "Shuffling", 4: "Stairs (ascending)",
          5: "Stairs (descending)", 6: "Standing", 7: "Sitting", 8: "Lying",
          13: "Cycling (sit)", 14: "Cycling (stand)", 130: "Cycling (sit, inactive)", 140: "Cycling (stand, inactive)"}

# Process all CSV files in the directory
process_all_csvs(directory, labels)
