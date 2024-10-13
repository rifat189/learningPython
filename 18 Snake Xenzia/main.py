# Snake Xenzia 


from snake import *
from food import Food
from scoreboard import Score
import time

X_LIMIT = 235
Y_LIMIT = 230
screen = Screen()
screen.setup(width = 500, height=500)
screen.title("Snake Xenzia")
screen.tracer(0)

food = Food()
snake = Snake()
score = Score()
is_game_on = True

screen.listen()
screen.onkey(key = "Up",fun = snake.up)
screen.onkey(key = "Down",fun = snake.down)
screen.onkey(key = "Left",fun = snake.left)
screen.onkey(key = "Right",fun = snake.right)

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.segment[0].distance(food) < 15:
        score.update_score()
        food.refresh()
        snake.extend()
    if snake.segment[0].xcor() > X_LIMIT or snake.segment[0].xcor() < -X_LIMIT or snake.segment[0].ycor() > Y_LIMIT or snake.segment[0].ycor() < -Y_LIMIT:
        score.game_over()
        is_game_on = False
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment)< 10:
            score.game_over()
            is_game_on = False



screen.exitonclick()
