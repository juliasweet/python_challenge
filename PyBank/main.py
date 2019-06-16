
#import modules
import os 
import csv
#path
csvpath = os.path.join('budget_data.csv')

#Variables; new lists
dates=[]
profitLoss=[]
monthlyChange=[]

#Open the file to read, skipping header    
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csvheader = next(csvreader)
#Fill lists
	for row in csvreader:	
		dates.append(row[0])
		profitLoss.append(row[1])
#Set as integer rather than string     
profitLoss = [int(i) for i in profitLoss]         
#Number of months
len_profitLoss=len(profitLoss)
#Net profit or loss for all months
total_profitLoss=sum(profitLoss)

#Calculate difference in profit or loss from month to month
### Need to stop one month before end of range; no i+1 after last month.
for i in range(len_profitLoss):
    if i < len_profitLoss -1:
        monthlyChange.append(profitLoss[i+1]-profitLoss[i])
        
#To correctly calculate average, divide by length of monthlyChange list, not
        #all rows (monthlyChange has one less row)
changeMonths=(len(monthlyChange))
maxIncrease=max(monthlyChange)
maxDecrease=min(monthlyChange)
totalChange=sum(monthlyChange)


averageChange=(totalChange / changeMonths)

##Assign index. Find corresponding index for month. 
monthlyChange.index(max(monthlyChange)) 
monthlyChange.index(min(monthlyChange)) 

dates.index ##Don't forget to adjust to avoid off by one error below

##Summary to display
print(f"-----------------------------------------------------")
print(f"Summary Data")
print(f"Total Months: {len(dates)}")
print(f"Total: ${(total_profitLoss)}" )
print(f"Average change: ${(averageChange)}")
print(f"Greatest increase in profits: {dates[monthlyChange.index(max(monthlyChange))+1]}  (${(maxIncrease)})")
print(f"Greatest decrease in profits: {dates[monthlyChange.index(min(monthlyChange))+1]}  (${(maxDecrease)})")
print(f"--------------------------------------------------------")
 
###Text file
file = open("budget_data_Summary.txt", "w")
file.write("Budget Summary Data\n")
file.write(f"-----------------------------------------------------\n")
file.write(f"Summary Data\n")
file.write(f"Total Months: {len(dates)}\n")
file.write(f"Total: ${(total_profitLoss)}\n" )
file.write(f"Average change: ${(averageChange)}\n")
file.write(f"Greatest increase in profits: {dates[monthlyChange.index(max(monthlyChange))+1]}  (${(maxIncrease)})\n")
file.write(f"Greatest decrease in profits: {dates[monthlyChange.index(min(monthlyChange))+1]}  (${(maxDecrease)})\n")
file.write(f"--------------------------------------------------------\n")
file.close()