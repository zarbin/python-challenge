# Modules
import os
import csv

# Files to load
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Initialize variables
total_vote = 0
vote_results = {}
winner = ""

# Open the CSV
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    header = next(csvreader)

    #Read each row of data after the header
    for row in csvreader:
        
        #increment vote counter
        total_vote += 1

        #Use dictionary to tally votes per candidate as we loop through  
        #check if candidate is in dictionary.  If not add new dict key, if present increment their vote count
        if row[2] not in vote_results.keys():
            vote_results[row[2]] = 1
        else:
            vote_results[row[2]] += 1

        #find the canddiate with the highest votes using max and return name of candidate
        winner = max(vote_results, key=vote_results.get)

#print results to terminal
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_vote}")
print("-------------------------------------")
#print vote results from dictionary
for x, y in vote_results.items():
    print(f'{x}:  {round((y/total_vote)*100, 3)}%  ({y})')
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

# Open a text and print results
with open("Election_Results.txt", 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------------------\n")
    file.write(f"Total Votes: {total_vote}\n")
    file.write("-------------------------------------\n")
    #print vote results from dictionary
    for x, y in vote_results.items():
        file.write(f"{x}:  {round((y/total_vote)*100, 3)}%  ({y})\n")
    file.write("-------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------------------\n")
