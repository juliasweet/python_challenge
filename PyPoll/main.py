#Import modules
import os
import csv

#Identify path; file is in same directory as my Python file
csvpath=os.path.join('election_data.csv')

#Create a list to hold all candidate names
candidate_Name=[]

#Open sesame! Skip header.
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
#Populate list with candidate names
    for row in csvreader:
        candidate_Name.append(row[2])

votes_castTotal=len(candidate_Name)

#Fill the dictionary with unique candidate names as keys and corresponding vote
#count as values.
candidates_Dictionary = {}
for name in candidate_Name:
    if name not in candidates_Dictionary:
        candidates_Dictionary[name]=1
        
    else:
       candidates_Dictionary[name] = candidates_Dictionary[name]+1
    

 #Create a variable for the winning candidate
 #Create a variable for the highest number of votes received
 #Create a list with the outcomes (name, percent of votes rcd, # votes rcd)
winning_Candidate = ""
winning_votesReceived = 0
outcomeSummary = []
uniqueCandidates = ""
percentReceived = ""
votesReceived = "votes"
   
#Loop through dictionary. 
# Set votes as variable for loop.
# For each candidate key, find the corresponding value (number of votes recieved)
#   Divide vote by total votes to find percentage.
# Put this information into a string
# Add each candidate name, followed by the string containing their votes recieved and
#percentage of vote received into your list

#While this loop is running determine winning candidate by comparing votes recieved
#by each candidate.
for result in candidates_Dictionary:
    votes = candidates_Dictionary.get(result) 
    percent = float(votes)/float(votes_castTotal)* 100
    uniqueCandidates = (f"{result}:  {percent:.3f}% ({votes})")
    outcomeSummary.append(uniqueCandidates)
    if votes > winning_votesReceived:
        winning_votesReceived = votes
        winning_Candidate = result
    
#Convert list with outcome summary to string with line breaks 
pretty_outcomeSummary = "\n".join(outcomeSummary)

#Print results and export text file
print("Election Results:")
print("-----------------------------------------------------------")
print(f"Total votes:   {str(votes_castTotal)}")
print("------------------------------------------------------------")
print(pretty_outcomeSummary)
print("-----------------------------------------------------------")
print(f"Winner: {winning_Candidate}")

file = open("election_results_Summary.txt", "w")
file.write("Election Results:\n") 
file.write("-----------------------------------------------\n") 
file.write(f"Total votes:   {str(votes_castTotal)}\n")
file.write("------------------------------------------------\n")
file.write(f"{str(pretty_outcomeSummary)}\n")
file.write("------------------------------------------------\n")
file.write(f"Winner: {winning_Candidate}\n")
file.close()