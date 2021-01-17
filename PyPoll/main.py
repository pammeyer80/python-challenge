import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Specify the file to write summary data to
output_data = os.path.join("analysis", "election_results.txt")

#create function to print candidate stats
def print_candidate_stats(name, votes, total_votes):
    percent_of_votes = (votes/total_votes)*100
    print(f"{name}: {percent_of_votes:.3f}% ({votes})")

#Initialize variables
total_votes = 0
candidates = {}

with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Skip header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        #calculate total votes
        total_votes += 1
        candidate_name = str(row[2])

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

        

header = f"Election Results"
break_line = f"---------------------------"
total_line = f"Total Votes: {total_votes}"

print(header)
print(break_line)
print(total_line)
print(break_line)
for candidate in candidates:
    print_candidate_stats(candidate, candidates[candidate], total_votes)
    # winner = candidate
    #     if 
print(break_line)