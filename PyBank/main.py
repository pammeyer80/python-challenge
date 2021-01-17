import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')


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

        month = str(row[0])
        current_value = int(row[1])

        counter += 1
        total += current_value
        
        if counter == 1:
            starting_value = current_value
        elif counter > 1:
            profit_change = current_value - previous_value
            profit_change_total += profit_change

        if profit_change >= greatest_increase:
            greatest_increase_month = month
            greatest_increase = profit_change
        
        if profit_change <= greatest_decrease:
            greatest_decrease_month = month
            greatest_decrease = profit_change

        previous_value = current_value
        

average_change = profit_change_total/(counter-1)


print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {counter}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")