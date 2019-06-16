# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:39:18 2019

@author: julia
"""

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
print(uniqueCandidates)
