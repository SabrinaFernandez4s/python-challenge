import csv
import os

monthcount = 0
net_total = 0
lst_total=[]
totalchange = 0
monthlychange=0
greatestincreasemonth=""
greatestprofit=0
greatestdecreasemonth=""
greatestloss=0

filepath=os.path.join('budget_data.csv')
with open(filepath, 'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    header=next(csv_reader)   
    #for line in csv_reader:
        #print(line)

    #question no 1 SOLVED
    monthcount = monthcount + 1     
    
    January_row=next(csv_reader)
    #question no 2 SOLVED
    net_total=net_total + int(January_row[1])
    
    #question no 3 SOLVED
    previous_net=int(January_row[1])
   
    for line in csv_reader:
        monthcount = monthcount + 1
        net_total=net_total+int(line[1])

        current_net=int(line[1])

        change=current_net - previous_net
        totalchange=totalchange + change
        monthlychange=monthlychange + 1
        totalaverage=float(totalchange/monthlychange)
        previous_net=int(line[1])

        if change>greatestprofit:
            greatestprofit=change
            greatestmonth = line[0]

        if change<greatestloss:
            greatestloss=change
            greatestdecreasemonth=line[0]

output=f"""
Financial Analysis
----------------------------
Total Months: {monthcount}
Total: {net_total}
Average Change: {totalaverage:.2f}
Greatest Increase in Profits: {greatestmonth} (${greatestprofit})
Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestloss})
"""

print(output)

with open(os.path.join("analysis_data.txt"), 'w') as txt:
     txt.write(output)