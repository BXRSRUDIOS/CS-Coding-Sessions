import time

def countdown(n):
    print(n)
    if n==0:
        return "Blast Off"
    else:
        return countdown(n-1)
    
# print(countdown(10))


def iterativeFactorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

#print(iterativeFactorial(3))

def recursiveFactorial(n):
    if n == 1:
        return n
    else:
        return n*recursiveFactorial(n-1)
    
#print(recursiveFactorial(4))


def fibonnaci(n):
    if n<=1:
        return n
    else:
        return (fibonnaci(n-1))+(fibonnaci(n-2))


'''for i in range(0,16):
    print(i, fibonnaci(i))'''
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

lst = prime(1, 100)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)

