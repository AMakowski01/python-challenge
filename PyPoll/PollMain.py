import os
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
#print(csvpath)

#plain reading of the csv file
with open (csvpath, "r") as PyPoll_data:
  reader = csv.reader(PyPoll_data, delimiter=",")
  header = next(reader)
  first_row = next(reader)
  canidate_name = []
  votes = {}
  count = 1
  canidate_votes = 0
  #print(reader)
  print(first_row)

#for loops
  for row in reader:
    name = (row[2])
    if name in votes:
       canidate_votes = votes[name] + 1
       votes.update({name:canidate_votes})
    else:
       votes[name] = 1

    list_of_votes = list(dict.values(votes))
    
    count = count + 1

    canidate_first = (first_row[2])
    if canidate_first not in canidate_name:
      canidate_name.append(canidate_first)

c_votes = (list_of_votes[0]/(count))
c_votes_percent = "{:.3%}".format(c_votes)
d_votes = (list_of_votes[1]/(count))
d_votes_percent = "{:.3%}".format(d_votes)
r_votes = (list_of_votes[2]/(count))
r_votes_percent = "{:.3%}".format(r_votes)

popular_vote = max(votes.values())
canidate_popular_vote = list(votes.keys())[list(votes.values()).index(popular_vote)]

      
#print(canidate_name)
print("Election Results")
print("----------------------------")   
print(f"Total votes: " + str(count))
print("----------------------------")
print(f"Charles Casper Stockham: " + str(c_votes_percent) + " (" + str(list_of_votes[0]) +")")
print(f"Diana Degette: " + str(d_votes_percent) + " (" + str(list_of_votes[1]) + ")")
print(f"Raymon Anthony Doane: " + str(r_votes_percent) + " (" + str(list_of_votes[2]) + ")")
print("----------------------------") 
print(f"winner: " + str(canidate_popular_vote))
print("----------------------------")

output_file=os.path.join("PyPoll", "Resources", "Analysis.txt")

with open(output_file,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total votes: " + str(count))
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: " + str(c_votes_percent) + " (" + str(list_of_votes[0]) +")")
    file.write("\n")
    file.write(f"Diana Degette: " + str(d_votes_percent) + " (" + str(list_of_votes[1]) + ")")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: " + str(r_votes_percent) + " (" + str(list_of_votes[2]) + ")")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"winner: " + str(canidate_popular_vote))
    file.write("\n")
    file.write("----------------------------")




