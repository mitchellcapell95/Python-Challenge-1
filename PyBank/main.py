import os

import csv

csvpath = "budget_data.csv"


# PyBank Part I - Count of total months in the P/L analysis

counter = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)

    for row in csvreader:
        counter += 1

print("Total Months: " + str(counter))


# PyBank Part II - Total P/L over all months in the analysis

total_profit_or_loss = 0
  

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)
    
    for row in csvreader:
        int_profit_or_loss = int(row[1])
        total_profit_or_loss += int_profit_or_loss

print("Total Profit/Loss: " + str(total_profit_or_loss))


# PyBank Part III - Average P/L change over the entire analysis period

rows = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)

    for row in csvreader:
        rows.append(int(row[1]))
        
list_of_changes = []

    
for i in range(0,len(rows) - 1):
    list_of_changes.append((rows[i+1] - rows[i]))
    
total_change = 0

for num in list_of_changes:
    total_change += num

avg_change = round(total_change / len(list_of_changes),2)

print("Average Change: " + str(avg_change))
    
       

# PyBank Part IV & Part V - Greatest Increase in Profits and Greatest Decrease in Profits


maximum_change = list_of_changes[0]

for num in list_of_changes:
    if num > maximum_change:
        maximum_change = num

greatest_dec = list_of_changes[0]

for num in list_of_changes:
    if num < greatest_dec:
        greatest_dec = num

dates = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)

    for row in csvreader:
        dates.append(str(row[0]))

dates.pop(0)
        
dates_and_changes = zip(list_of_changes, dates)

dates_and_changes = list(dates_and_changes)

for i,j in dates_and_changes:
    if i == maximum_change:
        max_change_date = j

for i,j in dates_and_changes:
    if i == greatest_dec:
        greatest_dec_date = j

print("Greatest Increase in Profits: " + max_change_date + " " + "($" + str(maximum_change) + ")")
print("Greatest Decrease in Profits: " + greatest_dec_date + " " + "($" + str(greatest_dec) + ")")


text_file = open("budget_results.txt", "w")
text_file.write("Total Months: " + str(counter) + "\n")
text_file.write("Total Profit/Loss: " + str(total_profit_or_loss) + "\n")
text_file.write("Average Change: " + str(avg_change) + "\n")
text_file.write("Greatest Increase in Profits: " + max_change_date + " " + "($" + str(maximum_change) + ")" + "\n")
text_file.write("Greatest Decrease in Profits: " + greatest_dec_date + " " + "($" + str(greatest_dec) + ")" + "\n")
