from turtle import Screen
import time

from snake_food import Food
from snake_move import Snake
from snake_score import Score

scr = Screen()
scr.setup(width=600, height= 600)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.tracer(0)

snakes = Snake()
food = Food()
scores = Score()


scr.listen()
scr.onkey(snakes.up, "Up")
scr.onkey(snakes.down, "Down")
scr.onkey(snakes.left, "Left")
scr.onkey(snakes.right, "Right")



segments = []


game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.18)
    snakes.move()

    if snakes.head.distance(food) < 10:
        food.refresh()
        snakes.extend()
        scores.increase_score()

    if snakes.head.xcor() > 280 or snakes.head.xcor() < -280 or snakes.head.ycor() > 280 or snakes.head.ycor() < -280:
        game_is_on = False
        scores.game_over()

    for segment in snakes.segments[1:-1]:
       if snakes.head.distance(segment) < 10:
            game_is_on = False
            scores.game_over()



scr.exitonclick()
