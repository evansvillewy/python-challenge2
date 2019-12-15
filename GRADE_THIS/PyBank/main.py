# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# An output function to write the results to the main display and to a file
def output(output,file_name):
    print(output, file=file_name)
    print(output)

# input file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#output file path
results_file = os.path.join('Output', 'Results.txt')

#initialize the variables
month_count = 0
net_profit = 0
last_month_profit = 0
greatest_gain = 0
greatest_loss = 0
month_diff = 0
total_month_diff = 0
greatest_gain_month =''
greatest_loss_month = ''

# Open the csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #Get the total months
        month_count += 1

        #The net total amount of "Profit/Losses" over the entire period
        net_profit = net_profit + int(row[1])

        #Create a list of the change in profit/losses month over month
        if month_count > 1:

            #capture the gain/loss over the last month
            month_diff = int(row[1]) - last_month_profit 

            #capture the total month over month change for avg calc later
            total_month_diff = total_month_diff + month_diff

            if month_diff > 0:

                #capture the greatest gain/month
                if month_diff > greatest_gain:
                    greatest_gain = month_diff
                    greatest_gain_month = row[0]
            else:

                #capture the greatest loss/month
                if abs(month_diff) > abs(greatest_loss):
                    greatest_loss = month_diff
                    greatest_loss_month = row[0]

        #hold on to the months profit/loss for comparison to next month
        last_month_profit =  int(row[1])

#The average of the changes in "Profit/Losses" over the entire period
avg_change  = total_month_diff /( month_count -1)

# Opening file for results/close automatically after with
with open(results_file, 'w') as output_file:
    output('Financial Analysis', output_file)
    output('----------------------------', output_file)
    output('Total Months: '+str(month_count), output_file)
    output('Total: $'+str(net_profit), output_file)
    output("Average Change: ${0:.2f}".format(avg_change), output_file)
    output("Greatest Increase in Profits: {0:s} (${1:.0f}) ".format(greatest_gain_month,greatest_gain), output_file)
    output("Greatest Decrease in Profits: {0:s} (${1:.0f}) ".format(greatest_loss_month,greatest_loss), output_file)