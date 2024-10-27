'''
Write an algorithm for an eager shopper who is keen to shop at the new TraviMart online store which is opening. 
Before transactions take place  the user has to input the maximum amount of money they have to spend aka their budget. 
After each transaction the program should prompt the user if they want to purchase another item. 
The program should keep a running total of Number of items purchased, total spent on all items and how much the user has left to spend. 
The user should not be allowed to go over their maximum budget. 
The program should terminate when the user no longer wishes to purchase anything else and should output 
total Number of items, total amount spent and the total amount remaining.

The owner of TraviMart Da Good Looking One is concerned products such as
Cleaning Products such as Hand Sanitizer, Tissues, Bleach and Toilet Roll
are going to run out and tinned foods and he has placed a restriction of these
of 10 products of each variety Cleaning products and tinned food. If shoppers
go over 10 items of cleaning products they are required to pay an extra 30%
and over 20 products an extra 60%. No shopper is allowed any more than 25
units of cleaning products. Adapt your algorithm to work out a new total cost
'''

budget = float(input("Enter maximum budget"))
purchase = True
noItems = 0
amountSpent = 0
receipt = list()
while purchase == True and budget > 0:
    item = input("Enter Item")
    cost = float(input("Enter cost of item"))
    if (budget-cost) < 0:
        print("Not enough money to make this purchase")
    else:
        receipt.append([item, f"£{cost}"])
        amountSpent+=cost
        budget -= cost
        noItems+=1
        print(f"Total Number of Items Purchased - {f"{noItems}"}\nTotal Amount Spent {f"£{amountSpent}"}\nTotal Budget Left {f"£{budget}"}")
        print(f"Your Receipt {receipt}")
    continuation = input("Continue? y/n")
    if continuation == "n":
        purchase = False

print(f"Total Number of Items Purchased - {f"{noItems}"}\nTotal Amount Spent {f"£{amountSpent}"}\nTotal Budget Left {f"£{budget}"}")
print(f"Your Full Receipt {receipt}")