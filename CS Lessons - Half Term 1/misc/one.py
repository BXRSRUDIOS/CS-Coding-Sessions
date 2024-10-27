# abc + ab + bc + ca + a + b + c = 2024, with a < b < c.
# Find all possible values of a, b, c, and return the sum of all distinct values of c.


# I maximised the upper boundary for each a<b<c. This is essentially brute forcing through all a, b and c values to then add to a list
# This algorithm is extremely inefficient. I think it would have a time complexity of O(n^3) but we aren't looking for efficiency merely solving the problem

# It seems that the upper limit is 45 for the two values as I do not see any other value when upper limit > 45.
# Although that seems to make sense as we would be getting some absurdly large numbers

def c(target):
    cValues = set()
    abc = list()
    for a in range(1, 45):  
        for b in range(a + 1, 45): 
            for c in range(b + 1, 2025):
                if (a * b * c) + (a * b) + (b * c) + (c * a) + a + b + c == target:
                    abc.append([a,b,c])
                    cValues.add(c)
    return(cValues, abc)


valuesOfC, abc = c(2024)
print(f"Possible Values of C are {valuesOfC}")
print(f"All combinations of a,b,c that satisfy the equation is {abc}")
print(f"The sum is {sum(valuesOfC)}")




