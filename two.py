import math

def doTheChallenge1(a, b, A):
    angleRadians = math.radians(A)
    B = (math.asin((math.sin(A)/a)*b))
    C = 180 - angleRadians - B
    c = math.sqrt((a**2)+(b**2)-2*a*b*(math.cos(C)))
    perimeter = a+b+c
    return perimeter

def doTheChallenge2(a,b,C):
    angleRadians = math.radians(C)
    c = math.sqrt((a**2)+(b**2)-2*a*b*(math.cos(angleRadians)))
    perimeter = a+b+c
    return perimeter

#print(cosineRule(50,60,70))

# Given in form Side Side Angle for parsing reasons
possibleSideSetsSAS = [
    (50,60,70),
    (50,70,60),
    (60,50,70),
    (60,70,50),
    (70,50,60),
    (70,60,50),
]

# Given in form Side Side Angle for parsing reasons
possibleSideSetsSSA = [
    (50,60,70),
    (50,70,60),
    (60,50,70),
    (60,70,50),
    (70,50,60),
    (70,60,50),
]

possiblePerimetersSAS = []
possiblePerimetersSSA = []

for sides in possibleSideSetsSAS:
    a, b, angle = sides
    perimeter = doTheChallenge2(a,b,angle)
    possiblePerimetersSAS.append(round(perimeter,1))

for sides in possibleSideSetsSSA:
    a, b, angle = sides
    perimeter = doTheChallenge1(a,b,angle)
    possiblePerimetersSSA.append(round(perimeter,1))
 
print(possiblePerimetersSAS)
print(round(min(possiblePerimetersSAS),1))

print(possiblePerimetersSSA)
print(round(min(possiblePerimetersSSA),1))


side_sets = [
    (50,60,70),
    (50,70,60),
    (60,50,70),
    (60,70,50),
    (70,50,60),
    (70,60,50),
]


