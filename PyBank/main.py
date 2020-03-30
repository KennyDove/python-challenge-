#Financial record analaysis
#Pull the file into the document
import os
#what will be analyzed
import csv
#create a path to the document which will be used to run the code
csvpath = os.path.join("..", "PyBank","budget_data.csv")
#I need to declare variables and leave openings for calculations
totmonths = 0
period_growth = 0
profit_loss = 0
variation = 0
monthly_change = 0
profit = []
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = 0
greatest_decrease_date = 0
#Read through the csv
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
#skips the header
    header = next(reader)
#using the file I need to create funcitons to run on the data
    print("Here is the data you're looking for:")
    for row in reader:
        totmonths += 1
        period_growth += int(row[1])
#average change is the variation between each month
#I need to go from month to month then find the difference between one them
        variation = int(row[1]) - monthly_change
        monthly_change = int(row[1])
        profit.append(variation)
#Then take that number and divide it by the total number of months
        avg_change = (monthly_change / totmonths)
#Greatest increase and decrease. The greatest change in both a positive and negative diretion Thankfully because the data was small enough to scan the min and max contain the highest and lowest profit change. So for this dataset I know the min and max values are also the greatest change. Using the previous function I can just min and max that.
        greatest_increase = max(profit)
        
        greatest_decrease = min(profit)
#Now I need to referance the index in order to pull the date from the minimum and maximum.
        greatest_increase_date = profit.index(greatest_increase)
        greatest_decrease_date = profit.index(greatest_decrease)
print("Financial analysis")
print("-------------------------------------------")
print("Total months:",totmonths)
print("Total Growth: $",period_growth)
print("Average change per month",avg_change)
print("Greatest increase in profit was on index", greatest_increase_date,"for $", greatest_increase)
print("Greatest decrease in profet was on index",greatest_decrease_date,"for $", greatest_decrease)
#export to .txt file
#open a txt file
f = open("PyBank.txt","w+")
print("Financial analysis", file=f)
print("-------------------------------------------", file=f)
print("Total months:",totmonths, file=f)
print("Total Growth: $",period_growth, file=f)
print("Average change per month",avg_change, file=f)
print("Greatest increase in profit was on index", greatest_increase_date,"for $", greatest_increase, file=f)
print("Greatest decrease in profet was on index",greatest_decrease_date,"for $", greatest_decrease, file=f)
