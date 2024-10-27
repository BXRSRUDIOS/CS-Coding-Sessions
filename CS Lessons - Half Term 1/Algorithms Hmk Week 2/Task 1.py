'''
Task 1
At the end of each match players upload their score to a computer. 
The computer stores the scores in the order they are received in a 2D array called player. 
The array stores the team as an integer (1 for green, 2 for red) and their score. An extract of the array called player is shown below. 
The first entry shows a green team member scored 45 points and the next shows a red team member scored 30 points.

Once all the players have uploaded their scores the computer adds up the scores for each team.
Using pseudocode write a program for a procedural language that works out and outputs the total score for each team. 
You may assume that there are always 20 players.
'''

# Importing Random Module to Help Initialise Scores
import random

# Initialising random scores to help with functionality of the program using List Comprehension
scores = []
for i in range(0,20):
    scores.append([random.randint(1,2), random.randint(0,100)])

# Creating the team point totals
team1Points = 0
team2Points = 0

# We compare in the 2D array whether the first item in the sublist is 1 or 2 to add to the right point
# Then add the 2nd value in the sublist to the teamPoint Total
for i in range(len(scores)):
    if scores[i][0] == 1:
        team1Points+=scores[i][1]
    elif scores[i][0] == 2:
        team2Points+=scores[i][1]

print(f"Team 1 earned {team1Points} points and Team 2 earned {team2Points}")