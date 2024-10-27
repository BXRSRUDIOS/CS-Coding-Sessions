
gtin7 = input("Enter a 7 digit number")
sumGTIN7 = 0
alternator=3
for i in range(0, len(gtin7)):
    sumGTIN7 += alternator*int(gtin7[i])
    if alternator == 3:
        alternator = 1
    elif alternator == 1:
        alternator = 3
checkdigit = 50-sumGTIN7
gtin8=gtin7+str(checkdigit)
print(gtin8)