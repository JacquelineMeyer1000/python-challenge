# import modules + set path for file
import os
import csv

Budgetdata_csv = os.path.join('Resources', 'budget_data.csv')

# open the csv file
with open(Budgetdata_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # set variables
    total_months = 0
    total_revenue = 0    
    prev_revenue = 0
    revenue_change = 0

    monthly_revenue_changes = []   
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999999]

    # loop through rows of data for outcomes:
    for rows in csvreader:
        
        # calculate total months
        total_months += 1 

        # calculate total revenue change
        total_revenue = total_revenue + int(rows[1]) 

        # calculate the average change from month to month over number of total changes
        revenue_change = float(rows[1])- prev_revenue
        prev_revenue = float(rows[1])
        monthly_revenue_changes += [revenue_change]       
        revenue_average = sum(monthly_revenue_changes) / len(monthly_revenue_changes)

        # calculate greatest increase in revenue
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = rows[0]

        # calculate decrease in revenue
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = rows[0]  

    # print statements
    print(f'Financial Analysis')
    print(f'-------------------------------------------')    
    print(f'Total Months: ' + str(total_months))
    print(f'Total Revenue: ' + '$' + str(total_revenue))
    print(f'Average Change: ' + '$' + str(round(sum(monthly_revenue_changes) / len(monthly_revenue_changes),2)))
    print(f'Greatest Increase: ' + str(greatest_increase[0]) + ' ($' +  str(greatest_increase[1]) + ')') 
    print(f'Greatest Decrease: ' + str(greatest_decrease[0]) + ' ($' +  str(greatest_decrease[1]) + ')')

# output statements to a text file
with open("output.txt", 'w') as file:
    file.write(f'Financial Analysis')
    file.write("\n")
    file.write(f'-------------------------------------------')
    file.write("\n")    
    file.write(f'Total Months: ' + str(total_months))
    file.write("\n")
    file.write(f'Total Revenue: ' + '$' + str(total_revenue))
    file.write("\n")
    file.write(f'Average Change: ' + '$' + str(round(sum(monthly_revenue_changes) / len(monthly_revenue_changes),2)))
    file.write("\n")
    file.write(f'Greatest Increase: ' + str(greatest_increase[0]) + ' ($' +  str(greatest_increase[1]) + ')')
    file.write("\n") 
    file.write(f'Greatest Decrease: ' + str(greatest_decrease[0]) + ' ($' +  str(greatest_decrease[1]) + ')')
    file.write("\n")
    file.close()

