# Dependencies
import os
import csv

# Create output file name
file_output_name = "new_budget_data.txt"

budgetpath = os.path.join("..", "PyBank", "budget_data_1.csv")

#define lists
dates = []
revenues = []
revchanges = []

#define numeric values
totalmonths = 0
totalrevenue = 0
rev_change = 0
avg_rev_change = 0
greatest_inc_rev = 0
greatest_dec_rev = 0
greatest_inc_date = 0
greatest_dec_date = 0

with open(budgetpath, newline='') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    for row in budget:
        #calculate total dates
        if str(row[0]) != "Date":
            totalmonths = totalmonths + 1
            #create list of rows
            dates.append(str(row[0]))
        #calculate total revenue
        if str(row[1]) != "Revenue":
            totalrevenue = totalrevenue + int(row[1])
            #create list of revenues 
            revenues.append(int(row[1]))        
    #calculate average change in revenue  
    x = 0
    for i in range(len(revenues)-1):
        revchanges.append(revenues[x+1] - revenues[x])
        x = x + 1
    avg_rev_change =(sum(revchanges)/len(revchanges))
    #calculate greatest revenue change
    greatest_inc_rev = max(revchanges)
    # find date for greatest revenue increase
    x = 0
    for i in range(len(revenues)-1):
        if revenues[x+1] - revenues[x] == greatest_inc_rev:
            greatest_inc_date = dates[x+1]
        x = x +1
    #calculate greatest revenue decrease
    greatest_dec_rev = min(revchanges)
    #find date for greatest revenue decrease
    x = 0
    for i in range(len(revenues)-1):
        if revenues[x+1] - revenues[x] == greatest_dec_rev:
            greatest_dec_date = dates[x+1]
        x = x +1
        
# Print the financial data to terminal
print("Financial Analysis")
print("-" * 20)
print("Total Months: " + str(totalmonths))
print("Total Revenue: $" + str(totalrevenue))
print("Average Revenue Change: $" + str(avg_rev_change))
print("Greatest Increase in Revenue: " + str(greatest_inc_date) + " ($" + str(greatest_inc_rev) + ")")
print("Greatest Decrease in Revenue: " + str(greatest_dec_date) + " ($" + str(greatest_dec_rev) + ")")
 
 #print the financial data to text file
file = open("file_output_name.txt","w")

file.write("Financial Analysis\n")
file.write("-" * 20 + "\n")
file.write("Total Months: " + str(totalmonths) + "\n")
file.write("Total Revenue: $" + str(totalrevenue) + "\n")
file.write("Average Revenue Change: $" + str(avg_rev_change) + "\n")
file.write("Greatest Increase in Revenue: " + str(greatest_inc_date) + " ($" + str(greatest_inc_rev) + ")\n")
file.write("Greatest Decrease in Revenue: " + str(greatest_dec_date) + " ($" + str(greatest_dec_rev) + ")")