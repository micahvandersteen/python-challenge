"""
Author:
    Micah Vandersteen
Purpose: 
    The purpose of this script is to analyze election results to determine
    the number of total votes, a list of candidates, as well as the percentage
    and amount of votes each candidate received, followed by a winner statement.
"""
# import dependencies 
import os
import csv 

# reference file path
pyPoll_path = "/Users/micahvandersteen/Desktop/python-challenge/Resources/03-Python_Homework_PyPoll_Resources_election_data.csv"

# READ IN .CSV FILE ==========================================================
with open(pyPoll_path, newline = '') as pyPoll_csv:

    # CAST VARIABLE FOR CSV READER ===========================================
    pyPoll_reader = csv.reader(pyPoll_csv, delimiter = ',')

    # skip header row
    next(pyPoll_reader)

    # initialize variables 
    total_votes = 0
    candidates = []
    vote_count = {}
    winning_candidate = ""
    winning_vote_count = 0
    candidate_votes = 0 
    vote_percentage = 0
    

    # initialize loop to go through data
    for row in pyPoll_reader: 

        # tally vote count to find total votes
        total_votes += 1

        # finding unique list of candidates, and tallying their votes each
        # time their name comes up, adds 1 into vote_count dictionary key:value
        # row[2] is the candidate in the file
        if row[2] not in candidates:

            candidates.append(row[2])

            vote_count[row[2]] = 1

        vote_count[row[2]] = vote_count[row[2]] + 1

    # printing initial results to terminal
    print()
    print()
    print("-------------- ELECTION RESULTS -------------------")
    print(f"Total Election Votes: {total_votes}")
    print(f"List of Election Candidates: {candidates}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # opens file for output, writes initial results
    file = open("election_results.txt", "w")
    file.write("-------------- ELECTION RESULTS -------------------\n")
    file.write(f"Total Election Votes: {total_votes}\n")
    file.write(f"List of Election Candidates: {candidates}\n")
    file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    # for loop referencing the vote count dictionary to find
    # percentages for each candidate (row[2])
    for row[2] in vote_count:

        candidate_votes = vote_count[row[2]]

        vote_percentage = float(candidate_votes) / float(total_votes) * 100

        # conditional to determine which candidate has the most votes,
        # and proclaims them the winner
        if ( candidate_votes > winning_vote_count ):

            winning_vote_count = candidate_votes

            winning_candidate = row[2]

        # each candidate has their unique results asssigned to them 
        results = f"{row[2]}: {round(vote_percentage,2)}% with {candidate_votes} votes"

        # prints more detailed results of each candidate
        # with their percentages and vote count
        print(results)

        # writing each candidate result to .txt file
        file.write(f"{results}\n")
    
    # prints winner statement 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{winning_candidate} has won the election by popular vote!")
    print()
    print()

    # writing final winner statement to .txt file
    file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write(f"{winning_candidate} has won the election by popular vote!\n")
    file.close()

