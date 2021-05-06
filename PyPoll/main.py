#Modules
import os
import csv

#set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

#open the csv file
with open(csvpath) as csvfile:
    csvpoll = csv.reader(csvfile, delimiter=",")
    
    #skip the header
    header = next(csvpoll)
    
    #create lists
    voter_ID = []
    candidate = []

    #loop through the data to calulate total votes
    for row in csvpoll:
        voter_ID.append(row[0])
        candidate.append(row[2])
        total_votes = len(voter_ID)
                   
    #print result header
    print('Election Results')
    print('-------------------------')
    #calculate number of total vote 
    print('Total Votes: ' + str(total_votes))
    #print ---
    print('-------------------------')
    
    #define variables:
    vote_count_k = 0
    vote_count_c = 0
    vote_count_l = 0
    vote_count_o = 0
    
    #loop through the candidate list to calculate number of votes for each candidate
    for vote in candidate:       
        if vote == 'Khan':
           vote_count_k = vote_count_k + 1
           Khan = vote_count_k
           
        elif vote == 'Correy':
             vote_count_c += 1
             Correy = vote_count_c
                    
        elif vote == 'Li':
             vote_count_l += 1
             Li = vote_count_l
                 
        else: 
            vote_count_o += 1
            OTooley = vote_count_o
            
    # find the variable with greatest value
    var = {Khan:"Khan", Correy:"Correy", Li:"Li", OTooley:"OTooley"}        
   
    #calculate percentage of vote each candidate won        
    percentage_vote_k = "{:.3%}".format(vote_count_k / total_votes)
    percentage_vote_c = "{:.3%}".format(vote_count_c / total_votes)
    percentage_vote_l = "{:.3%}".format(vote_count_l / total_votes)
    percentage_vote_o = "{:.3%}".format(vote_count_o / total_votes)
    
    
    #print result for each candidate            
    print("Khan: " + str(percentage_vote_k) + " (" + str(vote_count_k) + ")")
    print("Correy: " + str(percentage_vote_c) + " (" + str(vote_count_c) + ")")    
    print("Li: " + str(percentage_vote_l) + " (" + str(vote_count_l) + ")") 
    print("O'Tooley: " + str(percentage_vote_o) + " (" + str(vote_count_o) + ")")   
    print("-------------------------")
    print("Winner: " + str(var.get(max(var))))
    print("-------------------------")
    
    
    

    
    
        
        
 
    
        
    
        
        
   
    