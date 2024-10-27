'''a) Write an algorithm which is going to take in a
10 digit number for example 9876543212 takes
each digit from the number and multiplies it first
by 10 then 9 , 8 etc down to 0 and produces a
total and then outputs it.

b) At the end of the iteration add some code
which is going to work out the modulus of the total
when divided by 11 and output that result'''

isbn10 = input("Enter a ten digit number")
sumISBN10 = 0
count=0
for i in range(11, 1, -1):
    sumISBN10 += i*int(isbn10[count])
    count+=1
checkdigit = 11-(sumISBN10%11)
if checkdigit == 10:
    isbn11 = isbn10+"X"
else:
    isbn11=isbn10+str(checkdigit)
print(isbn11)