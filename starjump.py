from dis import dis
from turtle import *

fillcolor("black")
begin_fill()
sides = 5
distance = 10

for _ in range(15 * sides):
    distance += 5
    forward(distance)
    right(2 * 3600.0 / sides + 1)

end_fill()