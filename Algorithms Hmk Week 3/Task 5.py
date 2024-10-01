"""Write an algorithm which has a function which is going work out
the score of 2 dice. The function should take 2 dice throws as
parameters add the 2 numbers together. If the total is greater
than 8 then the player should score 10 points, greater than 4
then add 4 points. If the 2 dice are the same then the player
should be given an extra dice to throw. If the combined total is
greater than 15 then the player should score 12 points. The
totals from each of the dice throws should also be added
together to give the grand total.

Adapt this function so that it allows 2 players to play the game
and output which one has scored the highest score"""

import random as r
import time

# The Function
startTime = time.time()
def diceScoreCalculator(playerRoll1, playerRoll2):
    total = playerRoll1 + playerRoll2
    score = 0
    bonusRoll = 0
    if playerRoll1 == playerRoll2:
        bonusRoll = r.randint(1,6)
        total += bonusRoll
        if total > 15:
            score = 12
        else:
            score = 10
    elif total > 8:
        score = 10
    elif total > 4:
        score = 4
    else:
        score = 0
    return [score, bonusRoll]

for i in range(1,26):
    with open("scores.txt", "a") as f:
        player1Roll1 = r.randint(1,6)
        player1Roll2 = r.randint(1,6)
        player2Roll1 = r.randint(1,6)
        player2Roll2 = r.randint(1,6)
        scoreP1 = diceScoreCalculator(player1Roll1, player1Roll2)
        scoreP2 = diceScoreCalculator(player2Roll1, player2Roll2)
        if scoreP1[0] > scoreP2[0]:
            message1="Player 1 Wins"
            message2=f"""Analysis Board
          Player 1 First Roll - {player1Roll1} 
          Player 1 Second Roll - {player1Roll2}
          Player 1 Bonus Roll - {scoreP1[1]}
          Player 1 Dice Total - {player1Roll1+player1Roll2+scoreP1[1]}

          Player 2 First Roll - {player2Roll1} 
          Player 2 Second Roll - {player2Roll2}
          Player 2 Bonus Roll - {scoreP2[1]}
          Player 2 Dice Total - {player2Roll1+player2Roll2+scoreP2[1]}

          Player 1 Points Scored - {scoreP1[0]}
          Player 2 Points Scored - {scoreP2[0]}"""
        elif scoreP2 > scoreP1:
            message1=f"Player 2 Wins"
            message2=f"""Analysis Board
          Player 1 First Roll - {player1Roll1} 
          Player 1 Second Roll - {player1Roll2}
          Player 1 Bonus Roll - {scoreP1[1]}
          Player 1 Dice Total - {player1Roll1+player1Roll2+scoreP1[1]}

          Player 2 First Roll - {player2Roll1} 
          Player 2 Second Roll - {player2Roll2}
          Player 2 Bonus Roll - {scoreP2[1]}
          Player 2 Dice Total - {player2Roll1+player2Roll2+scoreP2[1]}

          Player 1 Points Scored - {scoreP1[0]}
          Player 2 Points Scored - {scoreP2[0]}"""
        elif scoreP1 == scoreP2:
            message1=f"Both Players Drew"
            message2=f"""Analysis Board
          Player 1 First Roll - {player1Roll1} 
          Player 1 Second Roll - {player1Roll2}
          Player 1 Bonus Roll - {scoreP1[1]}
          Player 1 Dice Total - {player1Roll1+player1Roll2+scoreP1[1]}

          Player 2 First Roll - {player2Roll1} 
          Player 2 Second Roll - {player2Roll2}
          Player 2 Bonus Roll - {scoreP2[1]}
          Player 2 Dice Total - {player2Roll1+player2Roll2+scoreP2[1]}

          Player 1 Points Scored - {scoreP1[0]}
          Player 2 Points Scored - {scoreP2[0]}"""
        f.write(f"Round {i}\n")
        f.write(message1+"\n")
        f.write(message2+"\n\n")
        f.close()
endTime = time.time()
totalTime = endTime-startTime
print(round(totalTime,2))