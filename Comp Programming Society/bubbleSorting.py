
arrayItems = input("Enter each number adding a space in between them")
mainArray = arrayItems.split(" ")
swaps = 0

n = len(mainArray)

for i in range(n):
    mainArray[i] = int(mainArray[i])


for i in range(n-1):
    for j in range(n-i-1):
        if (mainArray[j] > mainArray[j+1]):
            temp = mainArray[j]
            mainArray[j] = mainArray[j+1]
            mainArray[j+1] = temp
            swaps+=1

print(mainArray)
print(f"Array is sorted in {swaps} swaps")
print(f"First Element {mainArray[0]}")
print(f"Last Element {mainArray[n-1]}")
