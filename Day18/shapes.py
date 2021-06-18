from turtle import Turtle, Screen
import random

sides = [3, 4, 5, 6, 7, 8, 9, 10]
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple"]
shape = Turtle()
for side in sides:
    current_angle = 360 / side
    color = random.choice(colors)
    shape.color(color)
    while side > 0:
        shape.forward(100)
        shape.right(current_angle)
        side -= 1

screen = Screen()
screen.exitonclick()
