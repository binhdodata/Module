import os
import csv

# Set the path to the budget_data.csv file
budget_file = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')

# Initialize variables to store the results
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
changes = []
greatest_increase = {"date": None, "amount": 0}
greatest_decrease = {"date": None, "amount": 0}

# Open the budget_data.csv file
with open(budget_file, 'r') as csvfile:

    budget_data_reader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvfile)
    # Loop through the rows in the budget_data.csv file
    for row in budget_data_reader:
        # Increment the total number of months
        total_months += 1
        
        # Add the profit/loss for the current row to the total profit/loss
        total_profit_losses += int(row[1])
        
        # Calculate the change from the previous profit/loss, if applicable
        if previous_profit_loss is not None:
            change = int(row[1]) - previous_profit_loss
            changes.append(change)
            
            # Check if the current change is the greatest increase or decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change
        
        # Set the current profit/loss as the previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])
    
    # Calculate the average change
    average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")