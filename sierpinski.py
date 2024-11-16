import turtle
import random
import math

size = 600
corners = 3
winkelDreieck = math.radians(360/corners)
winkel = math.radians(360/6)
iterations = 10000
colors = ["green", "blue", "purple", "red", "orange", "yellow"]

# p = [[0, 0],
#      [math.sin(math.radians(150))*size, math.cos(math.radians(150))*size],
#      [math.sin(math.radians(210))*size, math.cos(math.radians(210))*size]]

p = [[math.sin(math.radians(0))*size, math.cos(math.radians(0))*size]]

for i in range(1, corners):
    winkelIterator = winkelDreieck*i
    p.append([math.sin(winkelIterator)*size, math.cos(winkelIterator)*size])

# print(p)

turtle.tracer(0)
turtle.speed("fastest")
turtle.hideturtle()

turtle.bgcolor("black")
turtle.color("green")
turtle.penup()

for i in range(iterations):
    r = random.randint(0, corners-1)
    pos = turtle.pos()
    x, y = (pos[0]+p[r][0])/2, (pos[1]+p[r][1])/2
    for j in range(1, 7):
        turtle.color(colors[j-1])
        xshift = x*math.cos(winkel*j) - y*math.sin(winkel*j)
        yshift = x*math.sin(winkel*j) + y*math.cos(winkel*j)
        turtle.setpos(xshift, yshift)
        turtle.dot(1.6)

turtle.update()

print("Click to exit.")
turtle.exitonclick()
