
test1 = [44, 34, 87, 45, 98, 1, 21, 85, 82, 29, 72, 61, 15, 54]
test2 = [19, 52, 99, 51, 80, 86, 80, 22, 80, 30, 46, 17, 78, 36]
test3 = [4, 34, 78, 26, 29, 15, 95, 7, 99, 99, 24, 47, 28, 51]
highest = []
lowest = []
average = []

for i in range(len(test1)):
    tempScores = [test1[i],test2[i],test3[i]]
    highest.append(f"Boy {i} Highest: {max(tempScores)}")
    lowest.append(f"Boy {i} Lowest: {min(tempScores)}")
    average.append(f"Boy {i} Average: {round(sum(tempScores)/3, 2)}")

print(highest)
print(lowest)
print(average)