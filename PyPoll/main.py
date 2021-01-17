import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Specify the file to write summary data to
output_data = os.path.join("analysis", "election_results.txt")

#Initialize variables
total_votes = 0

with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Skip header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_votes += 1


header = f"Election Results"
break_line = f"---------------------------"
total_line = f"Total Votes: {total_votes}"

print(header)
print(break_line)
print(total_line)
print(break_line)