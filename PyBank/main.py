import os
import csv
import numpy as np

# set csv file pointer
curDir = os.path.dirname(os.path.realpath("__file__"))
print(curDir)
budget_csv = os.path.join(curDir,'Resources','budget_data.csv') 

# set variables
monthTotal=0
netTotal=0
profitInc=""
profitIncVal=0
profitDec=""
profitDecVal=0
profitChanges=[]
lines=[]
previousProfit=0

# open and load the csv file
with open(budget_csv) as cvs_doc:
    fileReader=csv.reader(cvs_doc, delimiter=",")
    
    fileReader=next(cvs_doc)
 
    for line in csv.reader(cvs_doc):
        profit=int(line[1])
        monthTotal += 1
        netTotal += profit

        lines.append(line)
        profitChange=profit-previousProfit
        profitChanges.append(profitChange)
        previousProfit=profit

profitIncVal=max(profitChanges)
profitInc=str(lines[profitChanges.index(profitIncVal)][0])
profitDecVal=min(profitChanges)
profitDec=str(lines[profitChanges.index(profitDecVal)][0])

profits = [int(x[1]) for x in lines]

a = np.array(profits)

averageChange = "{:.2f}".format(sum(np.diff(a)) / len(np.diff(a))) 

# output the results to the terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {str(monthTotal)}")
print(f"Total: ${str(netTotal)}")
print(f"Average Change: ${str(averageChange)}")
print(f"Greatest Increase in Profits: {profitInc} (${str(profitIncVal)})")
print(f"Greatest Decrease in Profits: {profitDec} (${str(profitDecVal)})")

# output the results to a text file
with open("pybank_results.txt","w") as outputFile:
    outputFile.write("Financial Analysis\n")
    outputFile.write("------------------------------\n")
    outputFile.write(f"Total Months: {str(monthTotal)}\n")
    outputFile.write(f"Total: ${str(netTotal)}\n")
    outputFile.write(f"Average Change: ${str(averageChange)}\n")
    outputFile.write(f"Greatest Increase in Profits: {profitInc} (${str(profitIncVal)})\n")
    outputFile.write(f"Greatest Decrease in Profits: {profitDec} (${str(profitDecVal)})\n")

outputFile.close()