import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# colorRGB = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colorRGB.append((r, g, b))
# print(colorRGB)

colors = [(208, 157, 107), (197, 142, 168), (231, 215, 92), (37, 109, 159), (125, 166, 196), (119, 185, 144), (38, 131, 78), (150, 79, 57), (47, 175, 110), (132, 70, 91), (180, 176, 29), (54, 19, 32), (231, 166, 197), (45, 24, 16), (227, 82, 56), (199, 83, 106), (135, 29, 50), (233, 222, 4), (10, 101, 55), (177, 184, 223), (38, 166, 194), (23, 24, 35), (144, 218, 175), (141, 30, 20), (74, 123, 204), (238, 168, 156)]

dot = Turtle()
turtle.colormode(255)
dot.hideturtle()

dot.penup()
dot.setheading(180)
dot.forward(250)
dot.setheading(270)
dot.forward(250)
dot.setheading(0)
dot.pendown()
dot.speed(0)
for j in range(10):
    for i in range(10):
        dot.dot(20, random.choice(colors))
        dot.penup()
        dot.forward(50)
        dot.pendown()
    dot.penup()
    dot.setheading(90)
    dot.forward(50)
    dot.setheading(180)
    dot.forward(500)
    dot.setheading(0)

screen = Screen()
screen.exitonclick()
