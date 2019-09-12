import os
import csv

Months= [] # Stores month list
Profits = [] #Stores Profit list
Profit_delta =[] #Stores change in profit list
# 
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # Split the data on commas
    csvfileMain = csv.reader(csvfile, delimiter=',')
    header = next(csvfileMain)
    
    for i in csvfileMain:
        Months.append(i[0])
        Profits.append(int(i[1]))

number_of_months= len(Months) #total number of months in the dataset

total_profit = sum(Profits) # net total amount of profit or loss

#Creating a list for profit changes
for i in range(len(Profits)-1):
    TempChange = Profits[i+1]-Profits[i]
    Profit_delta.append(TempChange)

averageProfitDelta = sum(Profit_delta)/len(Profit_delta) #stores average profit delta

#greatest increase in profit
greatest_profit_increase = Profit_delta[0]
for i in range(len(Profit_delta)):
    if Profit_delta[i] > greatest_profit_increase:
        greatest_profit_increase = Profit_delta[i]
        greatest_profit_idate = Months[i+1]


#greatest decrease in profit
greatest_profit_decrease = Profit_delta[0]
for i in range(len(Profit_delta)):
    if Profit_delta[i] < greatest_profit_decrease:
        greatest_profit_decrease = Profit_delta[i]
        greatest_profit_ddate = Months[i+1]

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: {total_profit:,}")
print(f"Average Change: {averageProfitDelta:.2f}")
print(f"Greatest Increase in Profits: {greatest_profit_idate} ({greatest_profit_increase:,})")
print(f"Greatest Decrease in Profits: {greatest_profit_ddate} ({greatest_profit_decrease:,})")

#text file path
text_file = os.path.join('financial_analysis.txt')

with open(text_file, 'w') as text:
    text.write(f"Financial Analysis\n")
    text.write(f"---------------------------\n")
    text.write(f"Total Months: {number_of_months}\n")
    text.write(f"Total: ${total_profit:,}\n")
    text.write(f"Average Change: ${averageProfitDelta:.2f}\n")
    text.write(f"Greatest Increase in Profits: {greatest_profit_idate} (${greatest_profit_increase:,})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_profit_ddate} (${greatest_profit_decrease:,})\n")
