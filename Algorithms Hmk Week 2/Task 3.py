'''
Task 3
A memory game is played where:

Three players (A, B and C) have to choose a number between 0 and 100 if the number has already been chosen, 
a message is displayed that says "taken" if the number has not already been chosen, 
the player's letter is placed next to it the quantity of numbers that have not yet been chosen is displayed.

The winner is the player who has chosen the most unique numbers by the end of the game.
The numbers are stored in an array; numbers (). A number that has not yet been chosen is stored as an empty string''. 
The players are represented by "A", "B" and "C".

You have been asked to program part of the game.
Write an algorithm for player A's turn, which;

takes as an input the number that player A chooses
if it has not already been chosen, stores an "A" in that array element if it has already been chosen, outputs "taken"
counts and outputs the quantity of numbers left that have not been chosen.

Extra task 6 marks

1) Write an algorithm which is going to at the end of the game calculate the total number of places for each player, The player with the
highest number of spaces is the winner adapt your algorithm so the program can output the winner of the game
'''

# Initialise the Playing Board. This will contain a 2D array. Col Index 0 is the letter of the player and Col Index 1 is the number.
numbers = [["", i] for i in range(0,101)]

# Initialise other variables
notTaken = 100
currentPlayer = "A"
playerA, playerB, playerC = 0,0,0

# Player Turns
while notTaken > 0:
    choice = int(input(f"Player {currentPlayer} Choose a spot to take on the scoreboard between 0 and 100 or type -1 to END"))
    if choice == -1:
        notTaken = -1
    elif numbers[choice][0] == "":
        numbers[choice][0] = currentPlayer
        notTaken -= 1

        # Switch the Player Turn
        match currentPlayer:
            case "A":
                playerA += 1
                currentPlayer = "B"
            case "B":
                playerB += 1
                currentPlayer = "C"
            case "C":
                playerC += 1
                currentPlayer = "A"
    else:
        print(f"Taken, Spots remaining {notTaken}, Try Again or type -1 to END")
        match currentPlayer:
            case "A":
                currentPlayer = "B"
            case "B":
                currentPlayer = "C"
            case "C":
                currentPlayer = "A"

# Determine winner from all possible scenarios
# Dominant Winner Scenarios
if playerA > playerB and playerA > playerC:
    playerWin = f"Player A wins with {playerA} spots. Player B got {playerB} spots and Player C got {playerC} spots"
elif playerB > playerA and playerB > playerC:
    playerWin = f"Player B wins with {playerB} spots. Player A got {playerA} spots and Player C got {playerC} spots"
elif playerC > playerA and playerC > playerB:
    playerWin = f"Player C wins with {playerC} spots. Player A got {playerA} spots and Player B got {playerB} spots"
# Drawing but Winner is not drawn
if playerA > playerB and playerA > playerC and playerB == playerC:
    playerWin = f"Player A wins with {playerA} spots. Player B got {playerB} spots and Player C got {playerC} spots. They both drew"
elif playerB > playerA and playerB > playerC and playerA == playerC:
    playerWin = f"Player B wins with {playerB} spots. Player A got {playerA} spots and Player C got {playerC} spots. They both drew"
elif playerC > playerA and playerC > playerB and playerA == playerB:
    playerWin = f"Player C wins with {playerC} spots. Player A got {playerA} spots and Player B got {playerB} spots. They both drew"
# Drawing but two Winners drew 
if playerA == playerB and playerC < playerA and playerC < playerB:
    playerWin = f"Player A and B drew with {playerA} spots respectively. Player C got {playerC} spots"
elif playerB == playerC and playerA < playerB and playerA < playerC:
    playerWin = f"Player B and C drew with {playerB} spots respectively. Player A got {playerA} spots"
elif playerA == playerC and playerB < playerA and playerB < playerC:
    playerWin = f"Player A and C drew with {playerA} spots respectively. Player B got {playerB} spots"
# All 3 Players Drew
if playerA == playerB and playerB == playerC and playerA == playerC:
    playerWin = f"All players drew and got {playerA} spots"

# output result + board
print(playerWin)
print(numbers)
