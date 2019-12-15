# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#initialize variables
candidates={}
row_count = 0
highest_vote = 0
the_winner = ""
percent = ""

# An output function to write the results to the main display and to a file
def output(output,file_name):
    print(output, file=file_name)
    print(output)

# input file path
csvpath = os.path.join('Resources', 'election_data.csv')

#output file path
results_file = os.path.join('Output', 'Results.txt')

# Open the csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        in_there = False
        row_count += 1
        if row_count == 1:
            candidates.update( {row[2] : 1} )
        else:
            for (key, value) in candidates.items() :
                if row[2] == key:
                    in_there = True
                    value=value+1
                    candidates.update({key:value})
                    break

            if not in_there:
                candidates.update( {row[2] : 1} )

#Get the total votes
total_votes = row_count

# Opening file for results/close automatically after with
with open(results_file, 'w') as output_file:
    output('Election Results', output_file)
    output('-------------------------', output_file)
    output('Total Votes: '+str(total_votes), output_file)
    output('-------------------------', output_file)
    for (key, value) in candidates.items() :
        #output(key,output_file)     
        percent = "%.3f" % (value/total_votes*100) 
        output(key+": "+percent+"% ("+str(value)+")",output_file)
        if value > highest_vote:
            highest_vote = value
            the_winner = key    
    output('-------------------------', output_file)
    output('Winner: {0:s}'.format(the_winner), output_file)
    output('-------------------------', output_file)
