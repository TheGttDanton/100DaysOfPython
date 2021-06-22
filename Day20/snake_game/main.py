import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen = screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake(screen)
i = 1
#
# while i < 20:
#     print(i)
#     i += 1
#     snake.move_forward()
#     time.sleep(0.1)
#     screen.update()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    snake.move()
    time.sleep(0.3)

screen.exitonclick()
