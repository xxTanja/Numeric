import os
import csv

# Path to the folder containing the CSV files
path = 'C:/Users/tanja/Desktop/Stock_Data'

# Create a list of .csv files in folder: Stock_Data
files = os.listdir(path)
csv_files = [f for f in files if f.endswith('.csv')]


# Iterate through each CSV file in folder
for file in csv_files:
    # Open .csv files
    with open(os.path.join(path, file), 'r') as csv_file:
        # read .csv file
        reader = csv.reader(csv_file)
        # create list of rows from .csv
        data = list(reader)
        # create new list to store modified data
        new_data = []
        # Iterate through each row in the .csv
        for row in data:
            # Calculate % change between Close and Open price
            change = (float(row[4]) - float(row[1]))/float(row[1])
            # Add % change to row
            row.append(change)
            # Add modified row to new list
            new_data.append(row)
    # create new CSV file with the modified data
    with open(os.path.join(path, 'modified_' + file), 'w', newline='') as new_csv_file:
        # Write modified data to new CSV file
        writer = csv.writer(new_csv_file)
        writer.writerows(new_data)