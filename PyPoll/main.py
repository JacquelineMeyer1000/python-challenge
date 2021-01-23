# import modules + set path for file
import os
import csv

electiondata_csv = os.path.join('Resources', 'election_data.csv')

# Open the File
with open(electiondata_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # Declare Variables 
    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the total of Voter ID's 
        total_votes +=1

        # If the name is found for each of the four candidates, count the times it appears and store in a list
        
        if row[2] == "Khan": 
            khan_votes +=1

        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

    # Create a dictionary out of the two lists- candidates & votes 
    candidates = ["Khan", "Correy", "Li","O'Tooley"]
    votes = [khan_votes, correy_votes, li_votes, otooley_votes]

    # Merge them together and return the winner using a max function 
    dict_candidates_and_votes = dict(zip(candidates,votes))
    key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

    # Print a the summary of the analysis
    khan_percent = (khan_votes/total_votes) *100
    correy_percent = (correy_votes/total_votes) * 100
    li_percent = (li_votes/total_votes)* 100
    otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# output statements to a text file
with open("output.txt", 'w') as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")

