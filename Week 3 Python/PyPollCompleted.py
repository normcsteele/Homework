# Dependencies
import os
import csv

# Create output file name
file_output_name = "election_results.txt"

electionpath = os.path.join("..", "PyPoll", "election_data_1.csv")

#define lists
candidates = []
unique_candidates = []
votes_list = []


#define numeric values
total_votes = 0
winning_votes = 0
winner = 0
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
cand1count = 0
cand2count = 0
cand3count = 0
cand4count = 0
cand1percent = 0
cand2percent = 0
cand3percent = 0
cand4percent = 0

with open(electionpath, newline='') as csvfile:
    election = csv.reader(csvfile, delimiter=',')
    for row in election:
    #calculate total voters
        if str(row[2]) != "Candidate":
            total_votes = total_votes + 1
            candidates.append(str(row[2]))
    #define candidates
    for x in candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)
    cand1 = unique_candidates[0]
    cand2 = unique_candidates[1]
    cand3 = unique_candidates[2]
    cand4 = unique_candidates[3]

    #count total votes per candidate
    for i in candidates:
        if i == str(cand1):
            cand1count = cand1count + 1
        if i == str(cand2):
            cand2count = cand2count + 1
        if i == str(cand3):
            cand3count = cand3count + 1
        if i == str(cand4):
            cand4count = cand4count + 1

    #determine % of votes per candidate
    cand1percent = round(100*cand1count / total_votes,2)
    cand2percent = round(100*cand2count / total_votes,2)
    cand3percent = round(100*cand3count / total_votes,2)
    cand4percent = round(100*cand4count / total_votes,2)

    #determine winner based on popular vote
    votes_list = [int(cand1count), int(cand2count), int(cand3count), int(cand4count)]
    winning_votes = max(votes_list)
    if winning_votes == cand1count:
        winner = cand1
    if winning_votes == cand2count:
        winner = cand2
    if winning_votes == cand3count:
        winner = cand3
    if winning_votes == cand4count:
        winner = cand4

print("Election Results")
print("-" * 20)
print("Total Votes: " + str(total_votes))
print("-" * 20)
print(str(cand1) + ": " + str(cand1percent) + "% (" + str(cand1count) + ")")
print(str(cand2) + ": " + str(cand2percent) + "% (" + str(cand2count) + ")")
print(str(cand3) + ": " + str(cand3percent) + "% (" + str(cand3count) + ")")
print(str(cand4) + ": " + str(cand4percent) + "% (" + str(cand4count) + ")")
print("-" * 20)
print("Winner: " + str(winner))
print("-" * 20)

 #print the financial data to text file
file = open("election_results.txt","w")

file.write("Election Results\n")
file.write("-" * 20 + "\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("-" * 20 + "\n")
file.write(str(cand1) + ": " + str(cand1percent) + "% (" + str(cand1count) + ")\n")
file.write(str(cand2) + ": " + str(cand2percent) + "% (" + str(cand2count) + ")\n")
file.write(str(cand3) + ": " + str(cand3percent) + "% (" + str(cand3count) + ")\n")
file.write(str(cand4) + ": " + str(cand4percent) + "% (" + str(cand4count) + ")\n")
file.write("-" * 20 + "\n")
file.write("Winner: " + str(winner) + "\n")
file.write("-" * 20)