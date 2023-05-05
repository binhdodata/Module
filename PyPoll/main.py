import csv
import os
# Step 1: Import necessary modules
election = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

# Step 2: Read CSV file
with open(election,'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # skip header row
    data = [row for row in csv_reader]

# Step 3: Calculate total votes
total_votes = len(data)

# Step 4: Create list of unique candidates and calculate votes
votes_per_candidate = {}
for row in data:
    candidate = row[2]
    if candidate in votes_per_candidate:
        votes_per_candidate[candidate] += 1
    else:
        votes_per_candidate[candidate] = 1
candidates = list(votes_per_candidate.keys())

# Step 5: Calculate percentage of votes each candidate won
for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = votes / total_votes * 100
    votes_per_candidate[candidate] = percentage

# Step 6: Determine winner of election based on popular vote
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Step 7: Print out required values
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    votes = votes_per_candidate[candidate]
    count = votes_per_candidate[candidate] / 100 * total_votes
    print(f"{candidate}: {votes:.3f}% ({count:.0f})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")