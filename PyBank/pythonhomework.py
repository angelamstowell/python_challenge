import os
import csv

#print("path: " + os.getcwd())
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

greatest_increase = ["",0]
greatest_decrease = ["",0]


#Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

   
#loop through the lines of the csv

    profit_loss = []
    total = 0
    

    rows = list(csvreader)
#total months/return the length of the column

    previous_net = 0

    for row in rows:
        row = row[0].split(",")
        if(len(row)>1):
            
            total = total + 1

            #print(total)

#net total amount of profit and losses
            net_change = int(row[1]) - previous_net
            previous_net = int(row[1])
            #print(net_change) 
            #profit_loss.append(row[1])

            if net_change > greatest_increase[1]:
                greatest_increase[1] = net_change
                greatest_increase[0] = row[0]
                #print(greatest_increase)

            if net_change < greatest_decrease[1]:
                greatest_decrease[1] = net_change
                greatest_decrease[0] = row[0]
                #print(greatest_decrease)
            
            #print(min(profit_loss))
            #print(max(profit_loss))

#average of changes of profit and losses
            profit_loss = profit_loss + [net_change]
    #print(sum(profit_loss)/len(profit_loss))

average_changes = sum(profit_loss)/len(profit_loss)



#Financial Analysis read-out
Readout = (
f"Financial Analysis\n"
f"------------------------------\n"
f"Total Months: {total}\n"
f"Total Amount: {profit_loss}\n"
f"Average Change: (${average_changes})\n"
f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Open the file in "read" mode ('r') and store the contents in the variable "text"

print(Readout)

with open("../pythonhomework_output.py", "w") as txt_file:
    txt_file.write(Readout)