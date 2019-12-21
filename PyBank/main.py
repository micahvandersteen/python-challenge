"""
Author: 
    Micah Vandersteen
Purpose: 
    This script is meant to analyze a csv file containing months and
    profit/losses for each month. It is to find the number of months 
    in the data set, the net profit of the data set, the average change
    between every month in the data set, as well as find the greatest
    increase/decrease in profit alongside the corresponding month. 
    It prints the results to the terminal as well as exports the 
    results to a .txt file.
"""
# pyBank
# IMPORT RELEVANT MODULES ====================================================
import os
import csv

# REFERENCE FILE PATH ========================================================
pyBank_csv_path = ("/Users/micahvandersteen/Desktop/python-challenge/Resources/03-Python_Homework_PyBank_Resources_budget_data.csv")

# READ IN .CSV FILE ==========================================================
with open(pyBank_csv_path, newline = '') as pyBank_csvfile:

    # CAST VARIABLE FOR CSV READER ===========================================
    pyBank_csv_reader = csv.reader(pyBank_csvfile, delimiter = ',')

    # DEALING WITH THE HEADER ROW ============================
    next(pyBank_csv_reader)

    # INITIALIZING DESIRED VARIABLES ==================================================
    number_of_months = 0
    net_profit = 0
    average_change = 0 
    i = 0 
    changes = []
    change = 0
    csv_values = []
    csv_dates = []

    # INITIALIZING LOOP TO FIND DESIRED VARIABLES 
    for row in pyBank_csv_reader:

        # appends dollar values to list object for finding change
        csv_values.append(int(row[1]))
        csv_dates.append(str(row[0]))

        # finds total number of months
        number_of_months += 1

        # finds net profit
        net_profit += float(row[1])

    # initializes loop on values list to find list of change 
    # between each value
    for i in range(len(csv_values)-1):
        change = csv_values[i+1] - csv_values[i]
        changes.append(change)

    # calculates average change
    average_change = round(( sum(changes) / len(changes) ), 2)

    # finds greatest increase
    greatest_increase = max(changes)

    # finds greatest loss 
    greatest_decrease = min(changes)

    # finds index of greatest increase occurance, adds one to 
    # account for 
    # the fact that the changes list is one less than the
    # csv length
    greatest_increase_index = 0
    for i in range(len(changes)):
        if changes[i] == greatest_increase:
            greatest_increase_index = i + 1
    
    # finds date greatest increase
    date_greatest_inc = csv_dates[greatest_increase_index]

    # finds index of greatest loss, adds one to account for 
    # the fact that the changes list is one less than the
    # csv length
    greatest_loss_index = 0
    for i in range(len(changes)):
        if changes[i] == greatest_decrease:
            greatest_loss_index = i + 1

    # finds date greatest loss
    date_greatest_dec = csv_dates[greatest_loss_index]

    # print out desired variables that have been found to terminal
    print()
    print()
    print("---------FINANCIAL ANALYSIS------------------")
    print(f"The number of months in this data set: {number_of_months}")
    print(f"The net profit is: {net_profit}")
    print(f"The average change over each month is: {average_change}")
    print(f"The greatest increase in profits was: {greatest_increase}, on {date_greatest_inc}")
    print(f"The greatest decrease in profits was: {greatest_decrease}, on {date_greatest_dec}")
    print()
    print()

    # writing results to .txt file
    file = open("financial_analysis.txt", "w")
    file.write("---------FINANCIAL ANALYSIS------------------\n")
    file.write(f"The number of months in this data set: {number_of_months}\n" )
    file.write(f"The net profit is: {net_profit}\n")
    file.write(f"The average change over each month is: {average_change}\n")
    file.write(f"The greatest increase in profits was: {greatest_increase}, on {date_greatest_inc}\n")
    file.write(f"The greatest decrease in profits was: {greatest_decrease}, on {date_greatest_dec}\n")
    file.close()
    

