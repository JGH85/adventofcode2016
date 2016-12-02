import turtle
wn=turtle.Screen()
frodo = turtle.Turtle()
frodo.speed(10)
#sam = turtle.Turtle()
#sam.speed(10)
#sam.up()
frodo.up()
#sam.goto(0,100)
#frodo.goto(0, 0)
#sam.down()
frodo.down()
frodo.left(90)
print(frodo.position())
print(frodo.heading())


directions = """L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"""

dList = directions.split(', ')
print(dList)
##
##
for element in dList:
    orientation = element[0]
    distance = int(element[1:])
    if orientation == 'L':
        frodo.left(90)
    elif orientation == 'R':
        frodo.right(90)
    frodo.forward(distance)
    print(frodo.position())
print("final position:", frodo.position())
x = frodo.position()
y = float(x[0]) + float(x[1])
print(y)



##wn.exitonclick()
