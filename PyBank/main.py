import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Loop through the data
    for row in csvreader:

        print(row)
