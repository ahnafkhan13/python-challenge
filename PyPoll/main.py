import os
import csv

csvpath = os.path.join('election_data.csv')

Voter_id =[]
County = []
Candidate = []

with open(csvpath, newline='') as csvfile:

    # Split the data on commas
    csvfileMain = csv.reader(csvfile, delimiter=',')
    header = next(csvfileMain)
    
    for i in csvfileMain:
        Voter_id.append(i[0])
        County.append(i[1])
        Candidate.append(i[2])

votesCast = len(Voter_id) #Total numer of votes cast

#Create Candidate List
candidate_list = []
for i in range(votesCast):
    if Candidate[i] not in candidate_list:
        candidate_list.append(Candidate[i])


# number of votes per candidate
voteslist = []
for j in range(len(candidate_list)):
    voteslist.append(int(0))
for i in range(len(Candidate)):
    for j in range(len(candidate_list)):
        if Candidate[i] == candidate_list[j]:
            voteslist[j]=voteslist[j]+1

# percentage of votes
percentVotes=[]
for i in range(len(candidate_list)):
    percentVotes.append(voteslist[i]/votesCast*100)

#Winner 
winner_votes = voteslist[0]
winner_candidate = candidate_list[0]
for i in range(len(candidate_list)):
    if voteslist[i] > winner_votes:
        winner_votes = voteslist[i]
        winner_candidate=candidate_list[i]


print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {votesCast:,}")
print(f"---------------------------")
for x in range(len(candidate_list)):
    print(f"{candidate_list[x]}: {percentVotes[x]:.2f}% ({voteslist[x]:,})")
print(f"---------------------------")
print(f"Winner: {winner_candidate}")
print(f"---------------------------")


# write into txt file

#file path
text_file = os.path.join('election_results.txt')

with open(text_file, 'w') as text:
    text.write(f"Election Results\n")
    text.write(f"---------------------------\n")
    text.write(f"Total Votes: {votesCast:,}\n")
    text.write(f"---------------------------\n")
    for x in range(len(candidate_list)):
        text.write(f"{candidate_list[x]}: {percentVotes[x]:.2f}% ({voteslist[x]:,})\n")
    text.write(f"---------------------------\n")
    text.write(f"Winner: {winner_candidate}\n")
    text.write(f"---------------------------\n")
