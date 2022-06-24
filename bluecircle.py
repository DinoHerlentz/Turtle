from turtle import *

bgcolor("black")

speed(0)
pensize(2)
pencolor("blue")

def drawcircle(radius):
    for i in range(10):
        circle(radius)
        radius = radius - 4

def drawsign():
    for i in range(10):
        drawcircle(150)
        right(36)

drawsign()
done()