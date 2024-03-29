import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL_BOUNDS = 260

screen = Screen()
screen = screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake(screen)
food = Food()
scoreboard = Scoreboard()
i = 1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.2)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > WALL_BOUNDS or x_cor < -WALL_BOUNDS or y_cor > WALL_BOUNDS or y_cor < -WALL_BOUNDS:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with self
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
