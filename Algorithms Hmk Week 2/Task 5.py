'''
Task 5
The manager of a cricket teams wants some information on the performance of the teams batting over the course of the last season. 
The team have played 15 matches and the scores of each of the 11 players in the team need to be analysed. 
The scores are stored in a 2D array called arrayscores

Write an algorithm for a program which is going to work out
1)Players total Number of runs scored in the season over the 15 matches
2) Players average, highest and lowest scores

The algorithm should output the players Number with the highest average score
'''

import random

# Initialise arrayScores & Generate random scores for 11 players over 15 matches. Each player's score across 15 matches are stored in 
# each sublist with each of the 11 players getting their own sublist to make individual total, average, highest and lowest scores
arrayScores = [[random.randint(1,100) for i in range(0,15)] for i in range(0,11)]
totalScores, highestScores, lowestScores, averageScores = [], [], [], []

# Calculate each players total, average, highest & lowest scores and store them in their respective lists
for i in range(0,11):
    tempTotal, tempHighest, tempLowest, tempAverage = 0, 0, 100, 0
    for j in range(0,15):
        tempTotal += arrayScores[i][j]
        if arrayScores[i][j] > tempHighest:
            tempHighest = arrayScores[i][j]
        elif arrayScores[i][j] < tempLowest:
            tempLowest = arrayScores[i][j]
    tempAverage = round(tempTotal/15, 1)
    totalScores.append(tempTotal)
    averageScores.append(tempAverage)
    highestScores.append(tempHighest)
    lowestScores.append(tempLowest)
    
highestScore = f"The highest score was from Player {highestScores.index(max(highestScores))+1} who achieved {max(highestScores)} points"
lowestScore = f"The lowest score was from Player {lowestScores.index(max(lowestScores))+1} who achieved {max(lowestScores)} points"
highestAverageScore = f"The highest average score was from Player {averageScores.index(max(averageScores))+1} who achieved {max(averageScores)} points on average across the 15 games"
highestTotalScore = f"The highest total score was from Player {totalScores.index(max(totalScores))+1} who achieved {max(totalScores)} points in total across the 15 games"

print(highestScore)
print(lowestScore)
print(highestAverageScore)
print(highestTotalScore)