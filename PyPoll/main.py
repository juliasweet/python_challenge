# -*- coding: utf-8 -*-
#Import modules
import os
import csv

#Identify path; file is in same directory as my Python file
csvpath=os.path.join('election_data.csv')

#Create an empty list in which to put the candidate names (see below; 
#I am doubting this strategy)
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
    
#print(candidates_Dictionary)

 #Create a variable for the winning candidate
 #Create a variable for the highest number of votes received
 #Create a list with the outcomes (name, percent of votes rcd, # votes rcd)
winning_Candidate = ""
winning_votesReceived = 0
outcomeSummary = []
uniqueCandidates = ""
percentReceived = ""
votesReceived = "votes"
   
#Loop through  
for result in candidates_Dictionary:
    votes = candidates_Dictionary.get(result) 
    percent = float(votes)/float(votes_castTotal)* 100
    uniqueCandidates = (f"{result}:  {percent:.3f}% ({votes})")
    outcomeSummary.append(uniqueCandidates)
    if votes > winning_votesReceived:
        winning_votesReceived = votes
        winning_Candidate = result
    
print(outcomeSummary)
    #print(result)
    #print(votes)
    #print(percent)
    #print(winning_votesReceived)
print(winning_Candidate)

#Identify winner based on popular vote
#Done in for loop


#Print results and export text file
print("Election Results:")
print("-----------------------------------------------------------")
print(f"Total votes:   {str(votes_castTotal)}")
print("------------------------------------------------------------")
print(outcomeSummary)
print("-----------------------------------------------------------")
print(f"Winner: {winning_Candidate}")
