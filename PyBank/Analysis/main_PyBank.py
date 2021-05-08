# Modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "budget_data.csv")



# open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    
    # create lists
    date=[]
    profit = []
    profit_change = []
       
    
    #define variables
    total_months = 0
    total_net = 0
     
    #loop through the data
    for row in csvreader:
        profit.append(int(row[1]))
        date.append(row[0])
        
        #calculate total number of months
        #total_months += 1
        total_months = len(date)
        #calculate total net change
        total_net += int(row[1])  
    #print header of the report
    print('Financial Analysis')
    print('---------------------------')
    #print total number of rows    
    print('Total months: ' + str(total_months))
    
    #print net total number of P/L
    print('Total net amount is $' + str(total_net))
    

    
    for i in range(1, len(profit)):
          
        
          profit_change.append(profit[i] - profit[i-1])
          
          total_profit_change = sum(profit_change)
          
          ave_profit_change = round(sum(profit_change) / len(profit_change), 2)
          
          max_profit_change = max(profit_change)
          min_profit_change = min(profit_change)
        
          max_profit_change_date = str(date[profit_change.index(max(profit_change))])
          min_profit_change_date = str(date[profit_change.index(min(profit_change))])
        
    
    print('Average Change: $' + str(ave_profit_change))
    print('Greatest Increase in profits: ' + str(max_profit_change_date) + " $" + str(max_profit_change))
    print('Greatest Decrease in Profits: ' + str(min_profit_change_date) + " $" + str(min_profit_change))
    

    
 
    
    
    
    
       
        
   
     
    
    
    
    
    
    
    
    
    
    
    
            
    
    
    
    
        
        
        
    
    
    
    
    
        
        
    
    
    
    
        
        
    
    
    
    
    