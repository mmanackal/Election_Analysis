# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winnder of the election based on popular vote
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time
print("The time right now is ", now)
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = r'C:\Users\mereenaf\Documents\Data Analysis Course Work\Module 3 - Python\Election_Analysis\Resources\election_results.csv'
# Create a filename variable to a direct or indirect path to the file.
file_to_save = r'C:\Users\mereenaf\Documents\Data Analysis Course Work\Module 3 - Python\Election_Analysis\analysis\election_analysis.txt'
#1 Initialize a total vote counter
total_votes =0
#Declare new list for candidate names
candidate_options = []
# Create dictionary for candidate votes
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
#Read the file object with the reader function
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
# Print each row in the CSV file.
    for row in file_reader:
       # Add to the total vote count.
       total_votes += 1
       # Print the candidate name from each row
       candidate_name = row[2]
       # If the candidate does not match any existing candidate...
       if candidate_name not in candidate_options:
         # Add the candidate name to the candidate list.
         candidate_options.append(candidate_name)
         # Begin tracking that candidate's vote count.
         candidate_votes[candidate_name] = 0
       # Add a vote to that candidate's count.
       candidate_votes[candidate_name] += 1
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Counties in the election\n\nArapahoe\nDenver\nJefferson")
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
#3 Print the candidate list
#print(candidate_votes)
# Print vote percentage
    for candidate_name in candidate_votes:
        #retrieve vote count by candidate
        votes = candidate_votes[candidate_name]
        # Calcuate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote. ")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidates name.
            winning_candidate = candidate_name
            # Print out the winning candidate, vote count and percentage to terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)












