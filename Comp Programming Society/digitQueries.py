strQ = ""
for i in range(0,1001):
    strQ += str(i)

print(strQ)

numQueries = int(input("Enter number of queries"))
queries = []
for j in range(numQueries):
    k = input("Enter number to find")
    queries.append(k)
print(queries)

for m in range(len(queries)):
    print(strQ.find(str(numQueries[m])))