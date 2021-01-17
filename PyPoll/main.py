import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# write election result data to election_results.tx
output_election_results = os.path.join("analysis", "election_results.txt")

#create function to print candidate stats
def get_candidate_stats(name, votes, total_votes):
    percent_of_votes = (votes/total_votes)*100
    stats = (f"{name}: {percent_of_votes:.3f}% ({votes})")
    return stats

# initialize variables
total_votes = 0
candidates = {}
winner_votes = 0

with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Skip header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        #calculate total votes
        total_votes += 1

        # identify candidate name
        candidate_name = str(row[2])

        # if candidate is in the candidates dictionary
        if candidate_name in candidates:
            # add a vote
            candidates[candidate_name] += 1
        else:
            # otherwise add candidate to dictionary
            candidates[candidate_name] = 1

        
# get election result summary data
header = f"Election Results"
break_line = f"---------------------------"
total_line = f"Total Votes: {total_votes}"

# print election result summary data
print(header)
print(break_line)
print(total_line)
print(break_line)

# print election result candidate statistics
for candidate in candidates:
    votes = candidates[candidate]

    # get candidate statistics to print
    print(get_candidate_stats(candidate, votes, total_votes))
    
    # identify winner by vote counts
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
        winner_line = f"Winner: {winner}"

# print election result winner 
print(break_line)
print(winner_line)
print(break_line)

# create or open if already exists output file budget_analysis.txt 
with open(output_election_results, 'w', newline='') as txtfile:

    # write election results to output file 
    txtfile.write(header + "\n")
    txtfile.write(break_line + "\n")
    txtfile.write(total_line + "\n")
    txtfile.write(break_line + "\n")

    # get candidate statistics to write to output file
    for candidate in candidates:
        votes = candidates[candidate]
        txtfile.write(get_candidate_stats(candidate, votes, total_votes) + "\n")
   
    # write election result winner to output file
    txtfile.write(break_line + "\n")
    txtfile.write(winner_line + "\n")
    txtfile.write(break_line)

    txtfile.close()