import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Specify the file to write summary data to
output_analysis = os.path.join("analysis", "budget_analysis.txt")

# Initialize variables
counter = 0
total = 0
profit_change = 0
profit_change_total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
previous_value = 0

with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Skip header row
    next(csvreader)

    # Loop through the data
    for row in csvreader:

        # get current row month and profit/loss value
        month = str(row[0])
        current_value = int(row[1])

        # increment row counter
        counter += 1

        # increment total profit/loss value
        total += current_value
        
        # identify if this is the first row
        if counter == 1:
            # get first row profit/loss value
            starting_value = current_value

        # if this is not the first row of data
        elif counter > 1:
            # get profit change between this row and previous
            profit_change = current_value - previous_value

            # increment total profit loss change value
            profit_change_total += profit_change

        # if the current profit change is greater than the greatest increase in profit/loss
        if profit_change >= greatest_increase:
            # get the month
            greatest_increase_month = month
            # get the greatest value increase
            greatest_increase = profit_change
        
        # if the current profit change is less than the greatest decrease in profit/loss
        if profit_change <= greatest_decrease:
            # get the month
            greatest_decrease_month = month
            # get the greatest value decrease
            greatest_decrease = profit_change

        # retain the profit/loss value of current row to compare to next row
        previous_value = current_value
        
# calculate the average change of profit/loss over the entire period
average_change = profit_change_total/(counter-1)


#get summary table data
header = (f"Financial Analysis")
break_line = (f"-----------------------------")
total_months = (f"Total Months: {counter}")
total_line = (f"Total: ${total}")
average_change_line = (f"Average Change: ${average_change:.2f}")
greatest_increase_line = (f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
greatest_decrease_line = (f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# print summary analysis table to terminal
print(header)
print(break_line)
print(total_months)
print(total_line)
print(average_change_line)
print(greatest_increase_line)
print(greatest_decrease_line)


# create or open if already exists output file budget_analysis.txt 
with open(output_analysis, 'w', newline='') as txtfile:

    # write summary analysis table to output file 
    txtfile.write(header + "\n")
    txtfile.write(break_line + "\n")
    txtfile.write(total_months + "\n")
    txtfile.write(total_line + "\n")
    txtfile.write(average_change_line + "\n")
    txtfile.write(greatest_increase_line + "\n")
    txtfile.write(greatest_decrease_line + "\n")

    txtfile.close()
