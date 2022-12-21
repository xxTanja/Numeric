# Solution

import os
import csv

# Path to the folder containing the CSV files
path = 'C:/Users/User/Desktop/Stock_Data'

# Create a list of all the CSV files in the folder
files = os.listdir(path)
csv_files = [f for f in files if f.endswith('.csv')]

# Iterate through each CSV file in the folder
for file in csv_files:
    # Open the CSV file
    with open(os.path.join(path, file), 'r') as csv_file:
        # Read the CSV file
        reader = csv.reader(csv_file)
        # Create a list of all the rows in the CSV file
        data = list(reader)
        # Create a new list to store the modified data
        new_data = []
        # Iterate through each row in the CSV file
        for row in data:
            # Calculate the percentage change between Close and Open price
            change = (float(row[4]) - float(row[1]))/float(row[1])
            # Add the percentage change to the row
            row.append(change)
            # Add the modified row to the new list
            new_data.append(row)
    # Create a new CSV file with the modified data
    with open(os.path.join(path, 'modified_' + file), 'w', newline='') as new_csv_file:
        # Write the modified data to the new CSV file
        writer = csv.writer(new_csv_file)
        writer.writerows(new_data)