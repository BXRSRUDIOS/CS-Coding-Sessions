'''
Task 4
At a synchronised swimming competition each team is given a score out of 10 by each of six judges. 
The (possibly joint) highest and (possibly joint lowest) are discarded, and the teams score is then calculated by adding together 
the remaining four scores.

Using pseudocode, write an algorithm that accepts six numbers and outputs the score, calculated as described above.
'''

# Initialise teamScores & Accept team scores
teamScores = [int(input(f"Enter score number {i+1}")) for i in range(0,6)]

# Discard max and min
teamScores.remove(max(teamScores))
teamScores.remove(min(teamScores))

# Output final score
print(f"Team Final Score: {sum(teamScores)} Points")