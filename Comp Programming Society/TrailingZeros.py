'''
Your task is to calculate the number of trailing zeros in the factorial n!.
For example, 20!=2432902008176640000 and it has 4 trailing zeros.

Input
The only input line has an integer n.

Output
Print the number of trailing zeros in n!.
Constraints

1 < n < 10^9

Example
Input:
20

Output:
4
'''
def factorial(n, count):
    # Recursive method of factorial
    if count == 1:
        return n
    else:
        return factorial(n*count, count-1)

def trailingZeros(n):
    # Define variables
    factAns = 1
    trails = 0

    # Return 0 if n=1 so that None isn't returned
    if n == 1:
        return 0
    
    factAns = factorial(factAns, n)
    
    factAns = str(factAns)
    for j in range(len(factAns)-1, 0, -1):
        if factAns[j] == "0":
            trails+=1
        else:
            return trails
        
n = int(input(""))
print(trailingZeros(n))