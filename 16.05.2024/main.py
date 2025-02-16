from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Wąż rzeczny")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move

    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.ycor() > 300:
            snake.head.sety(-300)
    if snake.head.xcor() > 300:
        snake.head.setx(-300)
    if snake.head.ycor() < -300:
        snake.head.sety(300)
    if snake.head.xcor() < -300:
        snake.head.setx(300)

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick