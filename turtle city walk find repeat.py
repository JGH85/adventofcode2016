
directions = """L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"""

dList = directions.split(', ')
print(dList)
placesTraveled = []

orientation = 0
locationX = 0
locationY = 0

for element in dList:
    match = False
    turn = element[0]
    distance = int(element[1:])
    print(distance)
    orientation +=360
    if turn == 'L':
        orientation = (orientation-90)%360
        
    elif turn == 'R':
        orientation = (orientation+90)%360
    print(orientation)
    for i in range(distance):
        if orientation == 0 or orientation == 360:
            locationY +=1
        elif orientation == 90:
            locationX += 1
        elif orientation ==180:
            locationY -=1
        elif orientation ==270:
            locationX -= 1
        spot = (locationX, locationY)
        if spot in placesTraveled:
            match = True
            print("We've been here before... Current location:")
            print(spot)
            break 
        else:
            placesTraveled.append(spot)
    if match == True:
        break
    print(placesTraveled)
