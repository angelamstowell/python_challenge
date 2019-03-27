import os
import csv

#print("path: " + os.getcwd())

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

#Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    Voter_ID_List = []
    eligible_candidate = []
    total_votes = 0
    rows = list(csvreader)
    final_poll = {}
    winner = []
    
    

#total number of votes
    for row in rows:

        total_votes += 1
        if row[2] in final_poll.keys():
            final_poll[row[2]] = final_poll[row[2]] + 1
        else:
            final_poll[row[2]] = 1

print(total_votes)

#Create lists for eligible_candidate and Voter_ID_List
for key, value in final_poll.items():
            eligible_candidate.append(key)
            Voter_ID_List.append(value)


#total votes each candidate won
            candidate_votes = final_poll.items().count
#print(candidate_votes)          

#percentage of votes by candidate
    
vote_percent = []
for voter_id in Voter_ID_List:
    vote_percent.append(round(voter_id/total_votes*100, 1))
#print(vote_percent)

#zip together candidate, votes and percentages
poll_data = list(zip(eligible_candidate, Voter_ID_List, vote_percent)

for rows in poll_data:
    if max(Voter_ID_List) == row[1]
        winner.append(row[0])


#winner of election by popular vote

            winner = winner[0]


Results = (
f"Election Results\n"
f"--------------------------\n"
f"Total Votes: {total_votes}\n" 
f"--------------------------"
f{clean_data} 
f"---------------------------\n"
f"Winner:{winner}\n" 
f"----------------------------\n")

print(Results)

 Open the file in "read" mode ('r') and store the contents in the variable "text"

with open("../py_poll_homework_output.py", 'w') as text:
    txt_file.write(Results)

    