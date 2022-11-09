# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")


# Initialize variables
total_amount = 0
month_count = 0
greatest_inc = 0
greatest_inc_date = ""
greatest_dec = 0
greatest_dec_date = ""
change = 0
average_change = 0

# Initialize list of changes
change_list = []

#Open the csv file as an object
with open(csvpath, newline='') as csvfile:


    # Pass in the csv file to the csv.reader() function
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row.  next reads the first line and then bypasses it.. 
    header = next(csvreader)

    #Append the column 'Change' to the header
    header.append("Change")

    #Read each row of data after the header
    for row in csvreader:
        
        #calculate change by comparing current Profit/Losses value against previous rows Profit/Losses that is still contained in varaible ProfitLosses
        if month_count >= 1:
            change = (int(row[1]) - ProfitLosses)  
        
        row.append(change)
        change_list.append(change)

        # Set the 'Date', 'ProfitLosses', 'Change' variables
        Date = row[0]
        ProfitLosses = int(row[1])

        # capture greatest increase or greatest decrease of ProfitLosses
        if greatest_dec == 0 and greatest_inc == 0:
            greatest_dec = change
            greatest_inc = change
        elif greatest_inc < change:
            greatest_inc = change
            greatest_inc_date = Date
        elif greatest_dec > change:
            greatest_dec = change
            greatest_dec_date = Date

        # Track and update totals
        month_count += 1
        total_amount += ProfitLosses
            
#functional to calculate average of a list subtract
def Average(list_avg):
    avg = sum(list_avg) / (len(list_avg)-1)
    return avg

#calculate average change
average_change = round(Average(change_list), 2)

#print results to terminal
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_amount}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_inc_date} ${greatest_inc}")
print(f"Greatest Decrease in Profits: {greatest_dec_date} ${greatest_dec}")


# Open a file given the output path and print results
with open("Financial_Analysis.txt", 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${total_amount}\n")
    file.write(f"Average  Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc_date} ${greatest_inc}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec_date} ${greatest_dec}\n")
