import os
import csv

#open the csv file

csvpath = os.path.join("..","Resources","election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"csv_header: {csv_header}")
    #for row in csvreader:
       #print(row)

#define the variables
    def election_results(election_data):
      ballot_Id = int(election_data[0]) 
      county = str(election_data[1])
      candidate = str(election_data[2]) 
    ballot_Id = []
    county = []
    candidate = []

    for rows in csvreader:
        ballot_Id.append(int(rows[0]))
        county.append(str(rows[1]))
        candidate.append(str(rows[2]))

    #total number of votes

    total_votes = len(ballot_Id)
    print("Election Results")
    print("___________________________________________")
    print(f'Total Votes: {total_votes}')
    print("___________________________________________")


#list of candidates and total number of votes and percentage of total vote
from collections import Counter
counter = Counter(candidate)
winner_count = 0
winner_name = ''
for value, count in counter.items():
    print(f'{value}: {count/total_votes*100:.3f}% ({count})')
    if count > winner_count:
        winner_name=value
        winner_count = count
#winner
print('____________________________________________________')
print(f'Winner:{winner_name}')
print("___________________________________________")

#create output file
pypoll_final = list(zip("BallotID", "County", "candidate"))
output_file = os.path.join("..", "Analysis", "pypoll_final.csv")
with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        writer.writerow(["BallotID", "County", "Candidate"])
        writer.writerows(pypoll_final)


    
