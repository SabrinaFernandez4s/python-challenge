import csv
import os



totalno_votes=0
firstcand=0
secondcand=0
thirdcand=0

filepath=os.path.join('election_data.csv')
with open(filepath, 'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    header=next(csv_reader)
    winner=[]
    listofcandidates=[]           
    for line in csv_reader:

        currentcandidate=line[2]

        #print(line)
        totalno_votes = totalno_votes + 1

        if currentcandidate not in listofcandidates:
            listofcandidates.append(currentcandidate)

        if  currentcandidate==listofcandidates[0]:
            firstcand=firstcand+1
        elif currentcandidate==listofcandidates[1]:
            secondcand=secondcand+1
        elif currentcandidate==listofcandidates[2]:
             thirdcand=thirdcand+1
    
        firstper=(firstcand/totalno_votes)*100
        secondper=(secondcand/totalno_votes)*100
        thirdper=(thirdcand/totalno_votes)*100

        if firstcand>secondcand and thirdcand:
            winner=[listofcandidates[0]]
        elif secondcand>firstcand and thirdcand:
            winner=[listofcandidates[1]]
        elif thirdcand>firstcand and secondcand:
            winner=[listofcandidates[2]]



output=f"""
Election Results
-------------------------
Total Votes: {totalno_votes}
-------------------------
{listofcandidates[0]}: ({firstper:.2f}%) ({firstcand})
{listofcandidates[1]}: ({secondper:.2f}%) ({secondcand})
{listofcandidates[2]}: ({thirdper:.2f}%) ({thirdcand})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open(os.path.join("Pypoll_analysis.txt"), 'w') as txt:
     txt.write(output)