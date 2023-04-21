import os
import csv

# function definitions
def addVote(ballot,county,candidate,candidates):
    if not candidate in candidates:
        candidates[candidate]=[(ballot)]
    else:
        candidates[candidate].append((ballot))

def getpercentage(partVal, fullVal):
    val = 100 * float(partVal)/float(fullVal)
    result="{:.3f}".format(val)
    return f"{result}%"

curDir = os.path.join(os.getcwd()) #os.path.dirname(os.path.realpath("__file__"))
print(curDir)
election_csv = os.path.join(curDir,'Resources','election_data.csv')
print(election_csv)

totalVotes=0
candidates={}
winner=""
lines=[]

with open(election_csv) as csvFile:
    fileReader=csv.reader(csvFile,delimiter=",")

    fileReader=next(csvFile)

    for line in csv.reader(csvFile, delimiter=","):
        lines.append(line)
        addVote(line[0],line[1],line[2],candidates)


totalVotes=str(len(lines))
candidateCount = str(len(candidates))

votes=0
for cand, ids in candidates.items():
    popvotes=len(ids)
    if (popvotes>votes):
        votes=popvotes
        winner=cand

# output the results to the terminal
print("Election Results")
print("------------------------------")
print(f"Total Votes: {totalVotes}")
print("------------------------------")
for voter,ids in candidates.items():
    pervotes=getpercentage(len(ids),totalVotes)
    print(f"{voter}: {pervotes} ({len(ids)})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

# output the results to a text file
with open("pypoll_results.txt","w") as outputFile:
    outputFile.write("Election Results\n")
    outputFile.write("------------------------------\n")
    outputFile.write(f"Total Votes: {totalVotes}\n")
    outputFile.write(f"------------------------------\n")
    for voter,ids in candidates.items():
        pervotes=getpercentage(len(ids),totalVotes)
        outputFile.write(f"{voter}: {pervotes} ({len(ids)})\n")
    outputFile.write(f"------------------------------\n")
    outputFile.write(f"Winner: {winner}\n")
    outputFile.write(f"------------------------------\n")

outputFile.close()


