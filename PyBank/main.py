# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:38:49 2019

@author: julia
"""
import os
import csv

with open('budget_data.csv') as budget_data: #what to read
    reader = csv.DictReader(budget_data, delimiter=',') #how to read
    csvheader = next(csvreader) #ignore the header
    dates=[] #creates a list
    profitLoss=[] #creates a list
    monthlyChange=[] #creates a list
    # total=0 #was going to loop; used max instead
    for row in csvreader:
        dates.append(row[0]) #adds to the list
        profitLoss.append(row[1]) #adds to the list
        profitLoss = [int(row) for row in profitLoss]         
            for row in (profitLoss):
                monthlyChange = 1
                monthlyChange = profitLoss[row+1] + profitLoss [row]
                print(monthlyChange)
                monthlyChange.append(row[1])
        

profitLoss = [int(i) for i in profitLoss] 

######################
profitLoss.index(max(profitLoss)) 
profitLoss.index(min(profitLoss)) 

dates.index 


print(f"-----------------------------------------------------")
print(f"Summary Data")
print(f"Total months: {len(dates)}")
print(f"Total: ${sum(profitLoss)}" )
###Average goes below
print(f"Average change: ${sum(profitLoss) / len(profitLoss)}")
print(f"Greatest increase in profits: {dates[profitLoss.index(max(profitLoss))]}  (${max(profitLoss)})")
print(f"Greatest decrease in profits: {dates[profitLoss.index(min(profitLoss))]}  (${min(profitLoss)})")
print(f"--------------------------------------------------------")
 

##Create a dictionary
#budgetData={}

##How to populate dictionary with values from csv file? 
#import os
#import csv
#budget_Data = csv.DictReader(open("budget_data.csv")
#for str,int in budget_Data,budget_Data.values():
    
    
##Import necessary modules
#import os
#import csv
#import os.path

#f=open(budget_data.csv)
#csv_f=csv.reader(f)
#profitLoss=[]
#for row in csv_f:
 #   profitLoss.append(row[1])
#f.close()
#print (len(profitLoss))

#Connect to file   
#os.getcwd()
#'budget_data.csv'

# Count total_rows to determine number of months for which data exists. 
#Figured out damned f string. 
#csvpath=os.path.join('.\\budget_data.csv')
#with open(csvpath, newline='') as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=',')
  #  csv_header = next(csvfile)
   # total_rows = sum(1 for row in csvfile)
    #print (f"Months: {total_rows}")
    
#Trying to establish values based on location?
#with open(csvpath, newline='') as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=',')
  #  csv_header = next(csvfile)
   # for row in csvfile:
    #    months = row(0)
     #   profitLoss = row(1)
    
#Can probably do this all at once. 
    
    
#months = 0
#net_profitLoss = 0


#while profitLoss != 0: #as long as there is a value in 2nd index
 #   months += 1 #add to the months counter
  #  net_profitLoss +=profitLoss
    
#avg_profitLoss = net_profitLoss/months

#print(avg_profitLoss)
 

#Trying to turn into an array? 
#dates = []
#values = []

#with open('budget_data.csv') as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=',')
  #  for row in csvreader:
   #     dates.append(row[0])
    #    values.append(row[1])

#print(dates)
#print(values)

#csvpath=os.path.join('.\\budget_data.csv')
#def print_values(budget_data):
 #   month = str(budget_data[2])
  #  value = int(budget_data[1])
   # for number in numbers:
    #    print(print_values)    

#Testing path
#csvpath=os.path.join('.\\budget_data.csv')
#with open(csvpath, newline='') as csvfile:
  #  csvreader = csv.reader(csvfile, delimiter=',')
   # print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #for row in csvreader:
     #   print(row)

# Count total_rows to determine number of months for which data exists. 
#Figured out damned f string. 
#csvpath=os.path.join('.\\budget_data.csv')
#with open(csvpath, newline='') as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=',')
  #  csv_header = next(csv)
   # total_rows = sum(1 for row in csvfile)
    #print (f"Months: {total_rows}")
           

        
# Find highestProfit.
        
# Find greatestLoss.
        
#Print financialAnalysis.
        
        
#Export Text File of results.

