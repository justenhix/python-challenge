import os
import csv

#open the csv file

csvpath = os.path.join("..", "Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    csv_header = next(csvreader)
    print(f"csv_header: {csv_header}")
    #for row in csvreader:
       #print(row)

    # define the variables
    def financial_analysis(budget_data):
        date = str(budget_data[0])
        profitlosses = int(budget_data[1])
    profitlosses = []
    date = []

    for rows in csvreader:
        date.append(rows[0])
        profitlosses.append(int(rows[1]))
        
    print ('Financial Analysis__________________________________')
    # total number of months in dataset
    total_months = len(date)
    print(f'Total Months: {total_months}')
    
    # net total amount of profit/losses over the entire period
    nettotal = sum(profitlosses)
    print(f'Total: ${nettotal}')


    # changes in profit/losses for the entire period

    # average of those changes
    average = round(sum(profitlosses) / len(profitlosses))
    print("Average Change: $", average)
    



    #greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profitlosses)
    index_greatest = profitlosses.index(greatest_increase)
       
    print(f'Greatest Increase in Profits: ${greatest_increase} {date[index_greatest]}')
    
    
    #greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(profitlosses)
    index_decrease = profitlosses.index(greatest_decrease)
    print(f'Greatest Decrease in Profits: ${greatest_decrease} {date[index_decrease]}')

    #output to csv file
    pybank_final = list(zip("Date", "ProfitLosses"))
output_file = os.path.join("..", "Analysis", "pybank_final.csv")
with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        writer.writerow(["Date", "ProfitLosses"])
        writer.writerows(pybank_final)
