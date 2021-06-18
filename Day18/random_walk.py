from turtle import Turtle, Screen
import random

colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple"]
direction = [0, 90, 180, 270]
path_length = 40
path = Turtle()
path.speed(0)
path.pensize(5)
while True:
    current = random.choice(direction)
    color = random.choice(colors)
    path.color(color)
    path.right(current)
    path.forward(path_length)
