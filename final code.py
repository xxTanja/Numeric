import os
import csv

# path to folder
path = 'C:/Users/tanja/Documents/stock'

# create list of .csv files in folder
files = os.listdir(path)
csv_files = [f for f in files if f.endswith('.csv')]


# iterate through each CSV file
for file in csv_files:
    # open .csv files
    with open(os.path.join(path, file), 'r') as csv_file:
        # read .csv file
        reader = csv.reader(csv_file)
        # create list of rows from .csv
        data = list(reader)
        # create new list to store modified data
        new_data = []
        # iterate through each row in the .csv
        for row in data:
            # calculate % change between Close and Open price
            change = (float(row[4]) - float(row[1]))/float(row[1])
            # add % change to row
            row.append(change)
            # add modified row to new list
            new_data.append(row)
    # create new CSV file with the modified data
    with open(os.path.join(path, 'modified_' + file), 'w', newline='') as new_csv_file:
        # write modified data to new CSV file
        writer = csv.writer(new_csv_file)
        writer.writerows(new_data)