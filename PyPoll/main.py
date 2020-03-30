#Pypoll
#import file
import os
import csv
#create a path to the file
#from pypoll which is the directry I am in I dont need an extensive path I changed my path to be properly accssed
csvpath = os.path.join("..","PyPoll","election_data.csv")
#here are varibles I need spaces for vote counts then areas to put the percetagas for each person
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0
khan_percentage = 0
correy_percentage = 0
li_percentage = 0
otooley_percentage = 0
winner = 0
winning_candidate = 0
with open(csvpath, newline = "") as csvfile:
    reader = csv.reader(csvfile, delimiter =",")
#skips the header when reading the file
    header = next(reader)
#each row is a vote so the total votes is the total amount of rows
    for row in reader:
        total_votes += 1
#All candidates who recieved a vote [1] need to be listed
#To get the names I will use an if function. If they recieve a vote their name from row 2 going down will be kept and tallied it's row because the reader will scan row by row and I will make it count each persons total. I will use a series of if statements to give me the total amount per person
        if (row[2] == "Khan"):
            khan += 1
        if (row[2] == "Correy"):
            correy += 1
        if (row[2] == "Li"):
            li += 1
        if (row[2] == "O'Tooley"):
            otooley += 1
#end if
#end else
#Now I need to calculate the percentage which is their votes divided by the total votes.
        khan_percentage = (khan / total_votes) * 100
        correy_percentage = (correy / total_votes) * 100
        li_percentage = (li / total_votes) * 100
        otooley_percentage = (otooley / total_votes) * 100
#the winner would be the person with the most votes out of the candidates I will use if statements again. I dont remember the function to print a certian value because the candidates names aren't listed directly so I will find them and name them manually.
        winner = max(khan,correy,li,otooley)
        if winner == khan:
            winning_candidate = "Khan"
        if winner == correy:
            winning_candidate = "Correy"
        if winner == li:
            winning_candidate = "Li"
        if winner == otooley:
            winning_candidate = "O'Tooley"
print("Results")
print("-------------------------------------------")
print("There were",total_votes,"total votes")
print("-------------------------------------------")
print("Khan had", khan_percentage,"% of the votes",khan)
print("Correy had",correy_percentage,"% of the votes",correy)
print("Li had", li_percentage,"% of the votes",correy)
print("O'Tooley had", otooley_percentage,"% of the votes",otooley)
print("-------------------------------------------")
print("Congratulations",winning_candidate,"! Serve is well!")

#Export to .txt file


