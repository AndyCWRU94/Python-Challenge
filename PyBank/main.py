import os
import csv

csvpath = os.path.join('budget_data.csv')

month = []
profit = []


profloss = 0.00



#skip header so list includes only values

with open(csvpath) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    skipheader = next(csvreader)

    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
        profit = list(map(int, profit))
    print("Financial Analysis")
    print("-------------------------------------------")
    # The total number of months included in the dataset
    print("Total number of months: ")
    print(len(month))
    #The total net amount of "Profit/Losses" over the entire period
    print("Total net profit: ")
    totalamt = (sum(map(int, profit)))
    print("$" + str(totalamt))
    # The average change in "Profit/Losses" between months over the entire period
    print("Average change in profit between months:")
    numofrows = len(profit)
    average = totalamt/numofrows
    print("$"+str(round(average)))
    #The greatest increase in profits (date and amount) over the entire period
    print("Greatest increase in profits")
    differences = []
    for i in profit:
        new = i + (i - 1)
        differences.append(new)
    print("$"+str(max(differences)))
    #The greatest decrease in losses (date and amount) over the entire period
    print("Greatest decrease in profits:")
    print("$"+str(min(differences)))

