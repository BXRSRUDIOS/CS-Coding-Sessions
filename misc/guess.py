import random as rtard

ans = rtard.randint(1,100)
inp = 0
while inp != ans:
    inp = int(input("Enter a number where {n: 1<n<100}"))
    if inp>ans:
        print("Ohm watt the lower Σ")
    elif inp<ans:
        print("Ohm watt the upper Σ")

for i in range(0,8):
    print("My new keyboard is amazing;")