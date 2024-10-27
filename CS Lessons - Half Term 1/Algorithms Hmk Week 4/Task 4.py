
items = 0
weight = 0
charge = 0
accepted = 0
rejected = 0

luggage = [24, 11, 32, 9, 24, 20, 6, 19, 13, 25, 5, 26, 17, 9, 13, 35]

for weight in luggage:
    if weight > 50:
        extra_weight = weight - 50
        charge += extra_weight * 10
        weight += 50
        rejected+=1
    elif weight > 35:
        extra_weight = weight - 35
        charge += extra_weight * 7.50
        weight += 35
        rejected+=1
    elif weight > 25:
        extra_weight = weight - 25
        charge += extra_weight * 5
        weight += 25
        rejected+=1
    else:
        weight += weight
        accepted+=1
    items += 1
print(f"Total number of items: {items}")
print(f"Total weight of accepted luggage: {weight}kg")
print(f"Total charge for excess luggage: £{charge}")
print(f"Total number of (hypothetically) rejected items: {rejected}")
print(f"Total number of (hypothetically) accepted items: {accepted}")
