import os

import csv

csvpath = os.path.join('Desktop','UCFLM201907DATA2','03-Python', 'Homework','Instructions','PyPoll','Resources','election_data.csv')


counter = 0
candidate_Khan = 0
candidate_Correy = 0
candidate_Li = 0
candidate_Tooley = 0


list_of_candidates = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)

    for row in csvreader:
        if str(row[2]) not in list_of_candidates:
            list_of_candidates.append(str(row[2]))
            
list_of_candidates_string = ', '.join(list_of_candidates)


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)

    for row in csvreader:
        counter += 1
        candidate_votes = str(row[2])
        if candidate_votes == "Khan":
            candidate_Khan += 1
        
        elif candidate_votes == "Correy":
            candidate_Correy +=1
            
        elif candidate_votes == "Li":
            candidate_Li += 1
            
        else:
            candidate_Tooley += 1
            
percentage_Khan = round(((candidate_Khan / counter) * 100),2)
percentage_Correy = round(((candidate_Correy / counter) * 100),2)
percentage_Li = round(((candidate_Li / counter) * 100),2)
percentage_Tooley = round(((candidate_Tooley / counter) * 100),2)

        
print("The candidates are: " + str(list_of_candidates_string))
print("Total Votes: " + str(counter))
print("Khan: " + str(percentage_Khan) + "% " + "(" + str(candidate_Khan) + ")")
print("Correy: " + str(percentage_Correy) + "% " + "(" + str(candidate_Correy) + ")")
print("Li: " + str(percentage_Li) + "% " + "(" + str(candidate_Li) + ")")
print("O'Tooley: " + str(percentage_Tooley) + "% " + "(" + str(candidate_Tooley) + ")")

if candidate_Khan > candidate_Correy and candidate_Li and candidate_Tooley:
    print("Winner: Khan")
    
elif candidate_Correy > candidate_Khan and candidate_Li and candidate_Tooley:
    print("Winner: Correy")
    
elif candidate_Li > candidate_Correy and candidate_Khan and candidate_Tooley:
    print("Winner: Li")
    
else:
    print("Winner: O'Tooley")