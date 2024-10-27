'''
Task 2
Two players are each playing a game with a pack of cards. Each player has a hand of cards stored in an array called P1 or
P2 Hand.

Player 2 also has a hand of cards stored as a 1D array, p2Hand. Each player has a set number of moves to try to get rid of their cards. 
At the end of the game, the values of the cards in eacin hand are totalled, and the player with the smallest total wins.

Write a pseudocode algorithm that:
• adds together all the values in p1Hand
• adds together all the values in p2Hand
• compares the totals and outputs which player has the smallest number, or if there is a draw 
Make your algorithm efficient and comment your pseudocode.
'''

# Importing Random Module to Help with initialising the array decks
import random

# Initialising p1Hand & p2Hand
# Each player can have a maximum of cards if a card deck is split in half
# We will assume that there are more than 4 variants of card (would not be the case in a normal deck) for efficiency with the code
p1Hand = [random.randint(1,13) for i in range(random.randint(1,26))]
p2Hand = [random.randint(1,13) for i in range(random.randint(1,26))]

# Find the sum of each hand & declare emptry string for winner 
sumP1 = sum(p1Hand)
sumP2 = sum(p2Hand)
winner = ""

# Compare who got the smallest and store the winner text in winner to output
if sumP1 > sumP2:
    winner = f"Player 2 wins. P1 got {sumP1} and P2 got {sumP2}"
elif sumP2 > sumP1:
    winner = f"Player 1 wins. P1 got {sumP1} and P2 got {sumP2}"
else:
    winner = f"Draw. P1 got {sumP1} and P2 got {sumP2}"

print(winner)
